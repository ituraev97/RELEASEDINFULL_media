#!/usr/bin/env python3
"""Edit: timing from narration, then one video segment per shot, concatenated to video_raw.mp4 (no audio).
usage: build.py <episode_dir> <src_dir>
Needs: vo/raw_NN.wav (tts.py), gfx/<key>/ frames (graphics.mjs via make_gspec.py).
Motion rules: footage is retimed frame-exactly to 30 fps (29.97 -> 30 by timestamp, 59.94 -> every 2nd frame), so no frame is
ever duplicated or dropped (no stutter); no artificial zoom/pan on footage; graphics hold perfectly still after their intro;
stills move only via kb.py (sub-pixel affine)."""
import json, os, subprocess, sys, glob, hashlib, importlib.util
EP = os.path.abspath(sys.argv[1]); SRC = os.path.abspath(sys.argv[2]); P = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
LINES = E.LINES; IMGS = getattr(E, "META", {}).get("imgs", {})
W, H, FPS = 1920, 1080, 30
os.chdir(EP); os.makedirs("seg", exist_ok=True)
def run(c): subprocess.run(c, check=True)
def probe(f):
    d = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate:format=duration", "-of", "json", f]))
    n, dd = d["streams"][0]["r_frame_rate"].split("/"); return float(d["format"]["duration"]), int(n) / int(dd), d["streams"][0]["width"], d["streams"][0]["height"]
def adur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())
CLIPS = {"gofast": "navair_gofast_dvids.mp4", "gimbal": "navy_gimbal.webm", "flir1": "navy_flir1.webm"}
def clip_path(name): return os.path.join(SRC, CLIPS.get(name, f"{name}.mp4"))

# ---- narration timing ----
vd = []
for i in range(1, len(LINES) + 1):
    raw, out = f"vo/raw_{i:02d}.wav", f"vo/l_{i:02d}.wav"
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(raw):
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", raw, "-af",
             "highpass=f=70,equalizer=f=180:t=q:w=1:g=2,equalizer=f=3000:t=q:w=1.4:g=2.5,deesser=i=0.35,"
             "acompressor=threshold=-21dB:ratio=2.6:attack=5:release=120,loudnorm=I=-16:TP=-1.5:LRA=7", "-ar", "48000", "-ac", "1", out])
    vd.append(adur(out) if LINES[i - 1][0].strip() else 0.0)
MIN = {"g:intro": 4.0, "g:title": 3.6, "g:end": 6.0}
starts, durs, t = [], [], 0.6
for i, (txt, shots, o) in enumerate(LINES):
    d = vd[i] + o.get("gap", 0.55)
    for s in shots: d = max(d, MIN.get(s[0], 0))
    if any(s[0] == "g:chapter" for s in shots): d = max(d, vd[i] + 0.6)
    starts.append(t); durs.append(d); t += d
TOTAL = t + 0.4
print("TOTAL", round(TOTAL, 1), "s", flush=True)

def gkey(name, opts): return name + "_" + hashlib.md5(json.dumps(opts, sort_keys=True).encode()).hexdigest()[:6]
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), "-video_track_timescale", "15360"]
BROLL_GRADE = "eq=contrast=1.06:saturation=0.82:gamma=0.98,colorbalance=bs=0.03:bm=0.015:rh=0.01"

_CUTS = {}
def src_cuts(f):
    """scene cuts inside a source clip (seconds), cached; used to keep our shots free of the source's own edits"""
    if f not in _CUTS:
        cf = f + ".cuts.json"
        if os.path.exists(cf): _CUTS[f] = json.load(open(cf))
        else:
            # same detector as qc_report.py: big frame difference relative to the local median
            import numpy as _np
            _, r, _, _ = probe(f)
            raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", "scale=240:136,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
            x = _np.frombuffer(raw, _np.uint8).reshape(-1, 136, 240).astype(_np.int16); m = _np.abs(_np.diff(x, axis=0)).mean((1, 2))
            cuts = []
            for j in range(len(m)):
                loc = _np.median(m[max(0, j - 8):j + 8])
                if m[j] > 14 and m[j] > 5 * max(loc, 0.5): cuts.append(round((j + 1) / r, 3))
            _CUTS[f] = cuts
            json.dump(_CUTS[f], open(cf, "w"))
    return _CUTS[f]
def clean_start(f, ss, need, cd):
    """nearest start so that no source cut lands within 1 s of our shot's start or end; falls back to ss"""
    cuts = src_cuts(f)
    def ok(s): return s >= 0 and s + need <= cd - 0.3 and not any((s - 0.2 < c < s + 1.25) or (s + need - 1.25 < c < s + need + 0.2) for c in cuts)  # no flash cut near our edges; mid-shot source edits are fine
    if ok(ss): return ss
    for k in range(1, 400):
        for s in (ss + k * 0.1, ss - k * 0.1):
            if ok(s): return round(s, 2)
    return ss

def render(idx, shot, n):
    src, ss, o = shot; out = f"seg/{idx:03d}.mp4"
    sig = json.dumps(dict(v=2, src=src, ss=ss, n=n, o=o, have=os.path.exists(clip_path(src)) if not src.startswith(("g:", "img:")) else True), sort_keys=True)
    if os.path.exists(out) and os.path.exists(out + ".sig") and open(out + ".sig").read() == sig: return out
    _render(idx, shot, n, out); open(out + ".sig", "w").write(sig); return out

def _render(idx, shot, n, out):
    src, ss, o = shot
    if src.startswith("g:"):
        key = gkey(src[2:], o); frames = sorted(glob.glob(f"gfx/{key}/f*.jpg")); nint = len(frames)
        vf = (f"[0:v]fps={FPS},trim=end_frame={min(n, nint)},setpts=PTS-STARTPTS[a];"
              f"[1:v]loop=loop=-1:size=1,fps={FPS},trim=end_frame={max(0, n - nint) + 1},setsar=1,setpts=PTS-STARTPTS[b];"
              f"[a][b]concat=n=2:v=1,trim=end_frame={n},format=yuv420p[v]")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"gfx/{key}/f%04d.jpg",
             "-loop", "1", "-i", frames[-1], "-filter_complex", vf, "-map", "[v]", "-frames:v", str(n), "-an"] + ENC + ["-g", "100000", out])
    elif src.startswith("img:"):
        run(["python3", f"{P}/kb.py", IMGS[src[4:]], out, f"{n / FPS:.4f}", o.get("kb", "in")] + [str(x) for x in o.get("focus", [])])
    elif not os.path.exists(clip_path(src)):
        print(f"PLACEHOLDER: {src} missing", flush=True)
        txt = f"{src.upper()} FOOTAGE PENDING"
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0x0D0F12:s={W}x{H}:r={FPS}", "-vf",
             f"drawtext=text='{txt}':fontcolor=0x5B636B:fontsize=48:x=(w-tw)/2:y=(h-th)/2", "-frames:v", str(n), "-an"] + ENC + [out])
    else:
        f = clip_path(src); cd, rate, cw, ch = probe(f)
        need = n / FPS * (rate / FPS if rate > 40 else 1.0) * 1.002
        if ss + need > cd - 0.3:
            print(f"WARN {src} @{ss}: need {need:.1f}s, clip {cd:.1f}s -> clamped", flush=True); ss = max(0.0, cd - need - 0.3)
        if not src in ("gofast", "gimbal", "flir1"): ss = clean_start(f, ss, need, cd)
        sel = "select='not(mod(n\\,2))'," if rate > 40 else ""
        navy = src in ("gofast", "gimbal", "flir1")
        fit = (f"scale={W}:{H}:force_original_aspect_ratio=decrease:flags=lanczos,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black" if navy or cw / ch < 1.7
               else f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H}")
        grade = "" if navy else "," + BROLL_GRADE
        # frame-exact retime: every decoded (or every 2nd) frame becomes exactly one output frame at 30 fps
        vf = f"{sel}setpts=N/{FPS}/TB,{fit},setsar=1{grade},format=yuv420p"
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{ss}", "-i", f, "-vf", vf, "-frames:v", str(n), "-an"] + ENC + [out])
    got = int(subprocess.check_output(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", out]).decode())
    if got != n: print(f"WARN seg {idx} {src}: {got} frames != {n}", flush=True)

segs, files, acc_f, idx = [], [], 0, 0
for i, (txt, shots, o) in enumerate(LINES):
    a = starts[i] if i else 0.0; b = starts[i + 1] if i + 1 < len(LINES) else TOTAL
    for j, shot in enumerate(shots):
        end_f = round((a + (b - a) * (j + 1) / len(shots)) * FPS); n = end_f - acc_f
        files.append(render(idx, shot, n))
        segs.append(dict(t=acc_f / FPS, d=n / FPS, src=shot[0], ss=shot[1], line=i, lab=shot[2].get("lab", "")))
        acc_f = end_f; idx += 1
    print(f"line {i + 1}/{len(LINES)}", flush=True)
with open("seg/list.txt", "w") as fh:
    for f in files: fh.write(f"file '{os.path.basename(f)}'\n")
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "seg/list.txt", "-c", "copy", "video_raw.mp4"])
json.dump(dict(starts=starts, durs=durs, vdur=vd, total=acc_f / FPS, segs=segs), open("timing.json", "w"), indent=1)
print("done", acc_f / FPS)
