#!/usr/bin/env python3
"""Overlays (ASS: tags, b-roll labels), SRT captions, score + effects + natural sound, final mix at -14 LUFS.
usage: finish.py <episode_dir> <src_dir>   (after build.py)  -> overlay.ass, captions_en.srt, mix.wav
Music: synthesised (sound.music), ducked under the voice, drops out on lines marked sil=True.
Effects: synthesised (sound.py), placed by graphic type — sparse by design."""
import json, os, re, subprocess, sys, importlib.util
import numpy as np, soundfile as sf
from scipy.signal import fftconvolve, butter, sosfilt
P = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, P); import sound as S
EP = os.path.abspath(sys.argv[1]); SRC = os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
LINES, DISPLAY, META = E.LINES, E.DISPLAY, getattr(E, "META", {})
os.chdir(EP); T = json.load(open("timing.json")); ST, DU, VD, TOTAL, SEGS = T["starts"], T["durs"], T["vdur"], T["total"], T["segs"]
PH = json.load(open("vo/phrases.json")); SR = S.SR
def run(c): subprocess.run(c, check=True)
def disp(t):
    for a, b in DISPLAY: t = t.replace(a, b)
    return re.sub(r"\s+", " ", t.replace("…", "...")).strip()
def ts(x): x = max(0, x); return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
def srt_t(x): return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{min(999, int(round((x % 1) * 1000))):03d}"

# ---------------- captions (SRT, for YouTube CC) ----------------
def split_chunks(text, maxc=42):
    words, out, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > maxc and cur: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    if cur: out.append(cur)
    return out
srt, n = [], 1
for i in range(len(LINES)):
    for ph in PH.get(str(i + 1), []):
        txt = disp(ph["text"]); cs = split_chunks(txt); tot = sum(len(c) for c in cs); a = ST[i] + ph["t0"]; span = ph["t1"] - ph["t0"]
        for c in cs:
            b = a + span * len(c) / tot
            srt.append(f"{n}\n{srt_t(a)} --> {srt_t(b - 0.02)}\n{c}\n"); n += 1; a = b
open("captions_en.srt", "w", encoding="utf-8").write("\n".join(srt))

# ---------------- overlay ASS: location/date tags + b-roll honesty labels ----------------
HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Tag,Archivo SemiBold ExtraBold,46,&H00CAE0E8,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,2,7,0,0,0,1
Style: TagSub,Courier Prime,26,&H00B0F58C,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,5,0,1,0,2,7,0,0,0,1
Style: Lab,Courier Prime,21,&H00CAE0E8,&H00FFFFFF,&H00000000,&H99120F0D,1,0,0,0,100,100,2,0,3,6,0,9,0,0,0,1
Style: Credit,Courier Prime,22,&H00A0A0A0,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,0,0,2,80,80,36,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
def add(a, b, st, tx, layer=0): ev.append(f"Dialogue: {layer},{ts(a)},{ts(b)},{st},,0,0,0,,{tx}")
for i, (txt, shots, o) in enumerate(LINES):
    if "tag" in o:
        t1, t2 = o["tag"]; a, b = ST[i] + 0.25, ST[i] + min(DU[i], 6.0)
        # redaction-bar reveal: a black bar sweeps off to the right, uncovering the text (signature motion)
        bar_w = 40 + 26 * max(len(t1), len(t2) * 0.7)
        add(a, b, "Tag", r"{\an7\pos(96,786)\fad(0,350)}" + t1, 2)
        add(a, b, "TagSub", r"{\an7\pos(98,842)\fad(0,350)}" + t2, 2)
        add(a, b, "Tag", r"{\an7\pos(92,782)\bord0\shad0\c&H0B0B0C&\fad(0,0)\t(0,420,0.6,\clip(%d,0,1920,1080))\clip(92,0,1920,1080)\p1}m 0 0 l %d 0 l %d 110 l 0 110{\p0}" % (92 + bar_w, bar_w, bar_w), 3)
        add(a, a + 0.45, "Tag", r"{\an7\pos(92,866)\bord0\shad0\c&HB0F58C&\t(0,420,\fscx0)\p1}m 0 0 l %d 0 l %d 4 l 0 4{\p0}" % (bar_w, bar_w), 3)
for sg in SEGS:
    if sg.get("lab"):
        add(sg["t"] + 0.15, sg["t"] + sg["d"] - 0.1, "Lab", r"{\an9\pos(1880,40)\fad(200,200)}" + sg["lab"], 1)
add(TOTAL - 5.0, TOTAL, "Credit", r"{\fad(500,0)}" + META.get("credit", ""), 4)
open("overlay.ass", "w", encoding="utf-8").write(HEAD + "\n".join(ev) + "\n")

# ---------------- audio ----------------
N = int(TOTAL * SR) + SR
voice = np.zeros(N)
for i in range(len(LINES)):
    if not LINES[i][0].strip(): continue
    x, sr = sf.read(f"vo/l_{i + 1:02d}.wav")
    if x.ndim > 1: x = x.mean(1)
    i0 = int(ST[i] * SR); voice[i0:i0 + len(x)] += x[:max(0, N - i0)]
# score sections from chapters
chap = [ST[i] for i, (_, sh, _) in enumerate(LINES) if any(s[0] == "g:chapter" for s in sh)]
kinds = ["open"] + ["tension", "calm", "reveal", "tension", "pulse", "calm", "end"][:len(chap)]
sections = [(0, "open")] + [(t, k) for t, k in zip(chap, kinds[1:])]
sections.append((ST[-1] - 2, "end"))
sil = []
for i, (_, sh, o) in enumerate(LINES):
    if o.get("sil"): sil.append((ST[i] + VD[i] + 0.1, ST[i] + DU[i] + 0.6))
music = S.music(TOTAL + 1, sections, silences=sil)
music = np.pad(music, ((0, max(0, N - len(music))), (0, 0)))[:N]
# ducking: smooth voice envelope -> gain
L = int(0.05 * SR); env = np.sqrt(np.convolve(voice ** 2, np.ones(L) / L, mode="same"))
on = (env > 0.01).astype(float)
k = int(0.35 * SR); on = np.convolve(on, np.ones(k) / k, mode="same")  # ~350 ms release/attack smoothing
duck = 1 - 0.62 * np.clip(on * 1.6, 0, 1)
music = music * duck[:, None]
# effects, placed by graphic type
fx = np.zeros(N)
def put(x, at, g=1.0):
    i0 = int(max(0, at) * SR); j = min(N, i0 + len(x)); fx[i0:j] += x[:j - i0] * g
intro_audio = None
if os.path.exists(f"{P}/../brand/intro_audio.wav"):
    intro_audio, _ = sf.read(f"{P}/../brand/intro_audio.wav"); intro_audio = intro_audio.mean(1) if intro_audio.ndim > 1 else intro_audio
prev_src = None
for sg in SEGS:
    src, t0 = sg["src"], sg["t"]; o = next((s[2] for s in LINES[sg["line"]][1] if s[0] == src), {})
    if src == "g:intro" and intro_audio is not None: put(intro_audio, t0, 0.9)
    elif src == "g:title": put(S.ping(), t0 + 0.3, 0.35); put(S.hit(0.6), t0 + 0.05, 0.5); put(S.stamp(), t0 + 1.2, 0.35)
    elif src == "g:chapter": put(S.whoosh(0.5), t0 - 0.25, 0.5); put(S.paper(0.6), t0 + 0.2, 0.5); put(S.hit(0.5), t0 + 0.3, 0.35)
    elif src == "g:doc":
        put(S.paper(0.9), t0, 0.6)
        nl = len(o.get("lines", [])); put(S.typewriter(10 + 4 * nl, rate=14), t0 + 0.45, 0.22)
        if o.get("stamp"): put(S.stamp(), t0 + 1.25 + nl * 0.16 + 0.15, 0.75)
    elif src == "g:quote": put(S.typewriter(12, rate=15), t0 + 0.2, 0.18)
    elif src == "g:stat": put(S.hit(0.5), t0 + 0.15, 0.4)
    elif src in ("g:list", "g:timeline"): put(S.whoosh(0.4), t0, 0.22)
    elif src == "g:annot": put(S.static(0.6, 0.3), t0, 0.35); put(S.ping(), t0 + 0.6, 0.18)
    elif src == "g:geom": put(S.ping(), t0 + 0.5, 0.2)
    elif src == "g:end": put(S.stamp(), t0 + 0.5 + 0.2, 0.8); put(S.hit(0.6), t0 + 0.7, 0.4)
    elif src in ("gofast", "gimbal", "flir1") and prev_src != src: put(S.static(0.35), t0, 0.25)
    elif not src.startswith("g:") and prev_src and prev_src.startswith("g:"): put(S.projector(0.5), t0, 0.15)
    prev_src = src
# natural sound from footage (jets on deck, crew audio in the Navy videos), side-chained under the voice
os.makedirs("nat", exist_ok=True); lst = open("nat/list.txt", "w")
def clip_path(name): return os.path.join(SRC, {"gofast": "navair_gofast_dvids.mp4", "gimbal": "navy_gimbal.webm", "flir1": "navy_flir1.webm"}.get(name, f"{name}.mp4"))
for k_, sg in enumerate(SEGS):
    out = f"nat/{k_:03d}.wav"; src = sg["src"]
    has_a = (not src.startswith(("g:", "img:"))) and os.path.exists(clip_path(src)) and subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", clip_path(src)], capture_output=True, text=True).stdout.strip()
    if not has_a:
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", f"anullsrc=r={SR}:cl=mono", "-t", f"{sg['d']:.3f}", out])
    else:
        g = 1.0 if src in ("gimbal",) else 0.55  # GIMBAL cockpit audio is part of the evidence: keep it audible
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(sg["ss"]), "-i", clip_path(src), "-t", f"{sg['d']:.3f}", "-af",
             f"aresample={SR},pan=mono|c0=0.5*c0+0.5*c1,highpass=f=120,lowpass=f=7000,volume={g},apad,afade=t=in:d=0.08,afade=t=out:st={max(0, sg['d'] - 0.12):.3f}:d=0.12", "-ac", "1", "-t", f"{sg['d']:.3f}", out])
    lst.write(f"file '{k_:03d}.wav'\n")
lst.close()
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "nat/list.txt", "-af", "dynaudnorm=f=250:g=15:m=6", "nat.wav"])
nat, _ = sf.read("nat.wav"); nat = np.pad(nat, (0, max(0, N - len(nat))))[:N]
depth = np.full(N, 0.75)
for sg in SEGS:
    if sg["src"] == "gimbal": depth[int(sg["t"] * SR):int((sg["t"] + sg["d"]) * SR)] = 0.35  # cockpit voices stay audible
nat = nat * (1 - depth * np.clip(on * 1.6, 0, 1))  # under the voice
# room tone on voice (tiny), assemble
rv = S.room(0.5, 4000); voice_w = voice + fftconvolve(voice, rv)[:N] * 0.05
mixL = voice_w + music[:, 0] * 0.42 + fx * 0.8 + nat * 0.30
mixR = voice_w + music[:, 1] * 0.42 + fx * 0.8 + nat * 0.30
mix = np.stack([mixL, mixR], 1)[:int(TOTAL * SR)]
mix = mix / (np.abs(mix).max() + 1e-9) * 0.7
sf.write("premix.wav", mix.astype(np.float32), SR)
# two-pass loudness normalisation to -14 LUFS, true peak -1.5 dBTP
m = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", "premix.wav", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
js = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", "premix.wav", "-af",
     f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true",
     "-ar", str(SR), "mix.wav"])
print("overlay, captions, mix done")
