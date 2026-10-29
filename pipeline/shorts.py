#!/usr/bin/env python3
"""Vertical Shorts (1080x1920) cut from the finished episode, captions burned in.
usage: shorts.py <episode_dir> <out_dir>
episode.META["shorts"] = [{"id": "s1", "lines": [first, last], "hook": "TEXT<br>[GREEN WORD]"}]  (1-indexed, inclusive)
Layout: hook (top) · the 16:9 picture full-width over a blurred copy · word-group captions (lower third) · brand stamp.
Needs video_raw.mp4, overlay.ass, mix.wav, timing.json, vo/phrases.json."""
import json, os, re, subprocess, sys, importlib.util
EP = os.path.abspath(sys.argv[1]); OUT = os.path.abspath(sys.argv[2]); os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json")); ST, VD, DU = T["starts"], T["vdur"], T["durs"]; PH = json.load(open(f"{EP}/vo/phrases.json"))
SHORT = os.environ.get("RIF_SHORT", "RIF")
def disp(t):
    for a, b in E.DISPLAY: t = t.replace(a, b)
    return re.sub(r"\s+", " ", t.replace("…", "...")).strip()
def ts(x): x = max(0, x); return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,Big Shoulders Stencil Display Thin Black,118,&H00CAE0E8,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,6,8,60,60,210,1
Style: Cap,Archivo SemiBold ExtraBold,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,6,0,5,70,70,0,1
Style: Brand,Big Shoulders Stencil Display Thin Black,64,&H00C44727,&H00FFFFFF,&H00C44727,&H00000000,0,0,0,0,100,100,6,0,1,0,0,2,60,60,120,1
Style: CTA,Courier Prime,40,&H00B0F58C,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,3,0,1,3,0,5,60,60,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for sh in E.META.get("shorts", []):
    a, b = sh["lines"][0] - 1, sh["lines"][1] - 1
    t0 = max(0, ST[a] - 0.2); t1 = ST[b] + VD[b] + 0.7; D = t1 - t0
    if D > 59.5: print("WARN", sh["id"], "too long", round(D, 1)); t1 = t0 + 59.5; D = 59.5
    ev = []
    hook = sh["hook"].replace("<br>", r"\N"); hook = re.sub(r"\[(.+?)\]", r"{\\c&HB0F58C&}\1{\\c&HCAE0E8&}", hook)
    ev.append(f"Dialogue: 2,{ts(0)},{ts(D)},Hook,,0,0,0,,{{\\fad(150,0)}}{hook}")
    ev.append(f"Dialogue: 2,{ts(0)},{ts(D)},Brand,,0,0,0,,{{\\frz4\\bord4\\3c&HC44727&}} {SHORT} ")
    for i in range(a, b + 1):
        for ph in PH.get(str(i + 1), []):
            words = disp(ph["text"]).split(); groups = [" ".join(words[k:k + 3]) for k in range(0, len(words), 3)]
            tot = sum(len(g) for g in groups); s = ST[i] + ph["t0"] - t0; span = ph["t1"] - ph["t0"]
            for g in groups:
                e = s + span * len(g) / tot
                if s < D: ev.append(f"Dialogue: 1,{ts(s)},{ts(min(D, e) - 0.01)},Cap,,0,0,0,,{{\\an5\\pos(540,1400)\\fscx94\\fscy94\\t(0,80,\\fscx100\\fscy100)}}{g.upper()}")
                s = e
    ev.append(f"Dialogue: 3,{ts(D - 2.6)},{ts(D)},CTA,,0,0,0,,{{\\an5\\pos(540,1580)\\fad(200,0)}}FULL FILE ON THE CHANNEL")
    ass = f"{OUT}/{sh['id']}.ass"; open(ass, "w", encoding="utf-8").write(HEAD + "\n".join(ev) + "\n")
    vf = (f"[0:v]ass={EP}/overlay.ass,split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.18:saturation=0.7[bg];"
          f"[b]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=0:(H-h)/2-60,ass={ass},fade=t=in:st=0:d=0.25,fade=t=out:st={D - 0.45:.2f}:d=0.45[v]")
    out = f"{OUT}/{sh['id']}.mp4"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-t", f"{D:.3f}", "-i", f"{EP}/video_raw.mp4",
                    "-ss", f"{t0:.3f}", "-t", f"{D:.3f}", "-i", f"{EP}/mix.wav", "-filter_complex", vf, "-map", "[v]", "-map", "1:a",
                    "-af", f"afade=t=in:d=0.15,afade=t=out:st={D - 0.5:.2f}:d=0.5,loudnorm=I=-14:TP=-1.5", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", out], check=True)
    print(sh["id"], round(D, 1), "s", out, flush=True)
