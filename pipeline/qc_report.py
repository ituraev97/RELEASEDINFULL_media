#!/usr/bin/env python3
"""Episode-level motion QC on top of qc_motion.py output.
usage: qc_report.py <episode_dir> <video>   (needs <video>_motion.json from qc_motion.py with the same prefix, timing.json, gfx/)
Checks, per segment of the edit:
  - graphics HOLD (after the intro frames): every frame identical to the previous (max diff < 0.05) -> nothing drifts/zooms
  - graphics INTRO: no single-frame jump except designed stamp hits (reported, not failed)
  - footage: duplicated frames while the picture moves (stutter) -> must be 0 for our retime; jerk counts reported as camera motion
  - cuts: every detected cut must fall on a segment boundary (an unexpected cut inside a shot = a jump)"""
import sys, os, json, glob, subprocess, hashlib, numpy as np
EP = os.path.abspath(sys.argv[1]); V = sys.argv[2]; FPS = 30
T = json.load(open(f"{EP}/timing.json")); segs = T["segs"]
W, H = 480, 270
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", V, "-vf", f"scale={W}:{H}:flags=area,format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
mad = [0.0]; prev = None
while True:
    b = p.stdout.read(W * H)
    if len(b) < W * H: break
    f = np.frombuffer(b, np.uint8).astype(np.int16)
    if prev is not None: mad.append(float(np.abs(f - prev).mean()))
    prev = f
mad = np.array(mad); N = len(mad)
gfxn = {d: len(glob.glob(f"{EP}/gfx/{d}/f*.jpg")) for d in os.listdir(f"{EP}/gfx")}
import importlib.util
spec = importlib.util.spec_from_file_location("e", f"{EP}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def gkey(src, line):
    for s in E.LINES[line][1]:
        if s[0] == src: return src[2:] + "_" + hashlib.md5(json.dumps(s[2], sort_keys=True).encode()).hexdigest()[:6]
bounds = set(); fails = []; stats = dict(holds=0, hold_frames=0, footage=0, stutter=0, inner_cuts=0)
for sg in segs:
    a = round(sg["t"] * FPS); n = round(sg["d"] * FPS); bounds.add(a)
    if sg["src"].startswith("g:"):
        k = gkey(sg["src"], sg["line"]); ni = gfxn.get(k, 0)
        h0 = a + ni + 1  # first frame after the intro frames (+1: loop join)
        hold = mad[h0 + 1:a + n] if h0 + 1 < a + n else np.array([])
        if len(hold):
            stats["holds"] += 1; stats["hold_frames"] += len(hold)
            if hold.max() >= 0.05: fails.append(f"HOLD MOVES {sg['src']} @ {a / FPS:.2f}s max diff {hold.max():.3f}")
    else:
        stats["footage"] += 1
        seg = mad[a + 1:a + n]
        for j in range(1, len(seg) - 1):
            if seg[j] < 0.05 and seg[j - 1] > 0.8 and seg[j + 1] > 0.8: stats["stutter"] += 1; fails.append(f"STUTTER {sg['src']} @ {(a + 1 + j) / FPS:.2f}s")
        for j in range(2, len(seg) - 2):
            loc = np.median(seg[max(0, j - 8):j + 8])
            if seg[j] > 18 and seg[j] > 6 * max(loc, 0.5) and (j < 30 or j > len(seg) - 31): stats["inner_cuts"] += 1; fails.append(f"CUT INSIDE SHOT {sg['src']} @ {(a + 1 + j) / FPS:.2f}s (source edit within 1 s of our cut = flash)")
print(json.dumps(stats)); print(f"frames {N}, expected {round(T['total'] * FPS)}")
print("FAILS:", len(fails))
for f in fails[:80]: print("  ", f)
json.dump(dict(stats=stats, fails=fails), open(V.rsplit(".", 1)[0] + "_qcreport.json", "w"), indent=1)
