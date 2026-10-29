#!/usr/bin/env python3
"""Motion QC: finds jumps, stutters and jerks in a rendered video.
usage: qc_motion.py <video.mp4> [out_prefix]   -> prints a report, writes <prefix>_motion.png and <prefix>_motion.json
Per frame (downscaled 480x270 gray):
  mad   = mean abs difference to previous frame
  flow  = dense optical flow (Farneback) median vector + its magnitude
Detection (cuts are excluded and reported separately):
  CUT     mad > CUT_T and histogram correlation drop  (expected at edits)
  JUMP    inside a shot, mad > 4x local median and > 2.0 (a sudden visual leap)
  STUTTER inside a moving stretch, a frame identical to its predecessor (mad < 0.05) while neighbours move (> 0.6)
  JERK    inside a shot, global flow changes by > 1.5 px/frame (at 480p) from one frame to the next while the
          camera/graphic is moving smoothly before and after (velocity discontinuity)
  FPS     non-constant frame timing in the container
"""
import sys, json, subprocess, numpy as np, cv2
VID = sys.argv[1]; PRE = sys.argv[2] if len(sys.argv) > 2 else VID.rsplit(".", 1)[0]
w, h = 480, 270
W2, H2 = 960, 540
probe = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                            "stream=r_frame_rate,avg_frame_rate,nb_frames", "-of", "json", VID]))["streams"][0]
pts = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "packet=pts_time",
                               "-of", "csv=p=0", VID]).decode().split()
pts = np.sort(np.array([float(x) for x in pts if x.strip() and x != "N/A"]))
dts = np.diff(pts)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", VID, "-vf", f"scale={W2}:{H2}:flags=area,format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
def affine(a, b):
    pts0 = cv2.goodFeaturesToTrack(a, 400, 0.01, 8)
    if pts0 is None or len(pts0) < 12: return None
    pts1, st, _ = cv2.calcOpticalFlowPyrLK(a, b, pts0, None, winSize=(21, 21), maxLevel=3)
    ok = st.ravel() == 1
    if ok.sum() < 12: return None
    M, inl = cv2.estimateAffinePartial2D(pts0[ok], pts1[ok], method=cv2.RANSAC, ransacReprojThreshold=1.0)
    if M is None or inl.sum() < 10: return None
    sc = float(np.hypot(M[0, 0], M[1, 0]))
    # translation of the frame centre, in 1080p pixels
    cx, cy = W2 / 2, H2 / 2
    tx = (M[0, 0] * cx + M[0, 1] * cy + M[0, 2] - cx) * 2; ty = (M[1, 0] * cx + M[1, 1] * cy + M[1, 2] - cy) * 2
    return tx, ty, sc
prev = None; prevh = None; mad, mag, vec, hc = [], [], [], []
while True:
    buf = p.stdout.read(W2 * H2)
    if len(buf) < W2 * H2: break
    full = np.frombuffer(buf, np.uint8).reshape(H2, W2); f = cv2.resize(full, (w, h), interpolation=cv2.INTER_AREA)
    hist = cv2.calcHist([f], [0], None, [32], [0, 256]); cv2.normalize(hist, hist)
    if prev is None: mad.append(0); vec.append((np.nan, np.nan, np.nan)); hc.append(1)
    else:
        mad.append(float(np.mean(cv2.absdiff(f, prev))))
        r = affine(prevfull, full); vec.append(r if r else (np.nan, np.nan, np.nan))
        hc.append(float(cv2.compareHist(hist, prevh, cv2.HISTCMP_CORREL)))
    prev, prevh, prevfull = f, hist, full
mad = np.array(mad); vec = np.array(vec, dtype=float); hc = np.array(hc); N = len(mad)
FPS = 30.0
JT, JS = 0.6, 6e-4   # 1080p px/frame^2 and scale/frame^2 thresholds for a visible jerk
cut = (mad > 18) | ((mad > 6) & (hc < 0.85))
cut_i = set(np.where(cut)[0])
def near_cut(i, r=2): return any(j in cut_i for j in range(i - r, i + r + 1))
issues = []
for i in range(3, N - 3):
    if near_cut(i): continue
    loc = np.median(mad[max(0, i - 8):i + 8])
    if mad[i] > 2.0 and mad[i] > 4 * max(loc, 0.3):
        issues.append(("JUMP", i, round(mad[i], 2), round(loc, 2)))
    if mad[i] < 0.05 and mad[i - 1] > 0.6 and mad[i + 1] > 0.6:
        issues.append(("STUTTER", i, round(mad[i], 3), None))
    if near_cut(i, 3) or np.isnan(vec[i - 1:i + 2]).any(): continue
    acc = vec[i + 1] - 2 * vec[i] + vec[i - 1]          # velocity change per frame
    moving = np.hypot(vec[i, 0], vec[i, 1]) > 0.15 or abs(vec[i, 2] - 1) > 2e-4
    if moving and (np.hypot(acc[0], acc[1]) > JT or abs(acc[2]) > JS):
        issues.append(("JERK", i, round(float(np.hypot(acc[0], acc[1])), 3), dict(tx=round(vec[i, 0], 3), ty=round(vec[i, 1], 3), ds=round((vec[i, 2] - 1) * 1e4, 2))))
valid = ~np.isnan(vec).any(1)
acc_all = np.full((N, 3), np.nan); acc_all[1:-1] = vec[2:] - 2 * vec[1:-1] + vec[:-2]
mv = valid & ((np.hypot(vec[:, 0], vec[:, 1]) > 0.15) | (np.abs(vec[:, 2] - 1) > 2e-4))
jit = float(np.sqrt(np.nanmean(np.hypot(acc_all[mv, 0], acc_all[mv, 1]) ** 2))) if mv.sum() > 5 else 0.0
fps_bad = int(np.sum(np.abs(dts - 1 / FPS) > 0.002)) if len(dts) else 0
rep = dict(video=VID, frames=N, jitter_rms_px=round(jit, 3), moving_frames=int(mv.sum()), r_frame_rate=probe.get("r_frame_rate"), avg_frame_rate=probe.get("avg_frame_rate"),
           irregular_frame_intervals=fps_bad, cuts=[round(i / FPS, 2) for i in sorted(cut_i)],
           issues=[dict(type=t, t=round(i / FPS, 2), frame=i, value=v, ctx=c) for t, i, v, c in issues])
json.dump(rep, open(PRE + "_motion.json", "w"), indent=1)
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 1, figsize=(18, 6), sharex=True)
tt = np.arange(N) / FPS
ax[0].plot(tt, mad, lw=.6); ax[0].set_ylabel("frame diff"); ax[0].set_ylim(0, min(30, mad.max() + 1))
ax[1].plot(tt, vec[:, 0], lw=.6, label="tx"); ax[1].plot(tt, vec[:, 1], lw=.6, label="ty"); ax[1].plot(tt, (vec[:, 2] - 1) * 1000, lw=.6, label="scale-1 (x1000)"); ax[1].legend(); ax[1].set_ylabel("px/frame @1080p")
for t, i, *_ in issues: ax[0].axvline(i / FPS, color="r", lw=.8)
for i in cut_i: ax[1].axvline(i / FPS, color="#bbb", lw=.4)
plt.tight_layout(); plt.savefig(PRE + "_motion.png", dpi=80)
print(f"jitter_rms {jit:.3f} px/frame^2 over {int(mv.sum())} moving frames")
print(f"frames {N}  fps {probe.get('r_frame_rate')}/{probe.get('avg_frame_rate')}  irregular intervals {fps_bad}  cuts {len(cut_i)}  issues {len(issues)}")
for t, i, v, c in issues[:12]: print(f"  {t:8s} t={i / FPS:8.2f}s frame={i} value={v} ctx={c}")
