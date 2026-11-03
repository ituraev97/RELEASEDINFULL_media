#!/usr/bin/env python3
"""Vertical Shorts / TikToks (1080x1920) cut from the finished episode, captions burned in.
usage: shorts.py <episode_dir> <out_dir> [--from-long]
episode.META["shorts"] = [{"id": "s1", "lines": [first, last], "hook": "TEXT<br>[GREEN WORD]"}]  (1-indexed, inclusive)

LENGTH RULE (owner, Nov 2026): every vertical cut is 62–110 s, so it qualifies for TikTok's Creator Rewards (> 1 min)
and is still a YouTube Short (≤ 3 min). If the chosen lines run shorter than 62 s, the cut is extended line by line
(following lines first, then preceding ones) until it reaches 62 s; it never stops mid-sentence.

Layout (TikTok + Shorts safe zones: nothing important below y≈1500 or in the right 130 px):
  brand stamp + hook at the top · the 16:9 picture over a blurred copy · word-group captions at y 1330 · CTA at y 1450.
Sources: default = video_raw.mp4 + overlay.ass + mix.wav + vo/phrases.json (fresh build).
  --from-long = long.mp4 (overlays + mix already in it) + captions_en.srt, for re-cutting an already published episode."""
import json, os, re, subprocess, sys, importlib.util
EP = os.path.abspath(sys.argv[1]); OUT = os.path.abspath(sys.argv[2]); os.makedirs(OUT, exist_ok=True)
FROM_LONG = "--from-long" in sys.argv
MIN_D, MAX_D = 62.0, 110.0
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json")); ST, VD = T["starts"], T["vdur"]; TOTAL = T["total"]; NL = len(E.LINES)
SHORT = os.environ.get("RIF_SHORT", "RIF")
def disp(t):
    for a, b in E.DISPLAY: t = t.replace(a, b)
    return re.sub(r"\s+", " ", t.replace("…", "...")).strip()
def ts(x): x = max(0, x); return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
def srt_s(s): h, m, r = s.split(":"); sec, ms = r.split(","); return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000
# caption units: (start_s, end_s, text) in episode time
if not FROM_LONG and os.path.exists(f"{EP}/vo/phrases.json"):
    PH = json.load(open(f"{EP}/vo/phrases.json")); CAP = []
    for i in range(NL):
        for ph in PH.get(str(i + 1), []): CAP.append((ST[i] + ph["t0"], ST[i] + ph["t1"], disp(ph["text"])))
else:
    CAP = []
    for blk in open(f"{EP}/captions_en.srt", encoding="utf-8").read().strip().split("\n\n"):
        L = blk.strip().split("\n")
        if len(L) >= 3 and "-->" in L[1]:
            a, b = [srt_s(x.strip()) for x in L[1].split("-->")]; CAP.append((a, b, " ".join(L[2:])))
HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,Big Shoulders Stencil Display Thin Black,112,&H00CAE0E8,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,6,8,70,130,300,1
Style: Cap,Archivo SemiBold ExtraBold,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,6,0,5,90,150,0,1
Style: Brand,Big Shoulders Stencil Display Thin Black,58,&H00C44727,&H00FFFFFF,&H00C44727,&H00000000,0,0,0,0,100,100,6,0,1,0,0,8,60,130,190,1
Style: CTA,Courier Prime,40,&H00B0F58C,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,3,0,1,3,0,5,60,130,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
def span(a, b): return max(0, ST[a] - 0.2), ST[b] + VD[b] + 0.7
for sh in E.META.get("shorts", []):
    a, b = sh["lines"][0] - 1, sh["lines"][1] - 1
    t0, t1 = span(a, b)
    while t1 - t0 < MIN_D and (b + 1 < NL or a > 0):          # extend to >= 62 s, whole lines only
        nb = b + 1
        if nb < NL and not any(s[0] == "g:end" for s in E.LINES[nb][1]): b = nb  # may run through the bumper; never into the end card
        elif a > 0: a -= 1
        else: break
        t0, t1 = span(a, b)
    D = t1 - t0
    if D < MIN_D: print("WARN", sh["id"], "only", round(D, 1), "s")
    if D > MAX_D: print("WARN", sh["id"], "long", round(D, 1), "s — choose fewer lines")
    sh["lines_used"] = [a + 1, b + 1]
    ev = []
    hook = sh["hook"].replace("<br>", r"\N"); hook = re.sub(r"\[(.+?)\]", r"{\\c&HB0F58C&}\1{\\c&HCAE0E8&}", hook)
    ev.append(f"Dialogue: 2,{ts(0)},{ts(D)},Hook,,0,0,0,,{{\\fad(150,0)}}{hook}")
    ev.append(f"Dialogue: 2,{ts(0)},{ts(D)},Brand,,0,0,0,,{{\\frz4\\bord4\\3c&HC44727&}} {SHORT} ")
    for (ca, cb, txt) in CAP:
        if cb <= t0 or ca >= t1: continue
        words = txt.split(); groups = [" ".join(words[k:k + 3]) for k in range(0, len(words), 3)]
        tot = sum(len(g) for g in groups) or 1; s = ca - t0; spn = cb - ca
        for g in groups:
            e = s + spn * len(g) / tot
            if 0 <= s < D: ev.append(f"Dialogue: 1,{ts(s)},{ts(min(D, e) - 0.01)},Cap,,0,0,0,,{{\\an5\\pos(530,1330)\\fscx94\\fscy94\\t(0,80,\\fscx100\\fscy100)}}{g.upper()}")
            s = e
    ev.append(f"Dialogue: 3,{ts(D - 3.0)},{ts(D)},CTA,,0,0,0,,{{\\an5\\pos(530,1450)\\fad(200,0)}}FOLLOW FOR THE NEXT FILE")
    ass = f"{OUT}/{sh['id']}.ass"; open(ass, "w", encoding="utf-8").write(HEAD + "\n".join(ev) + "\n")
    burn = "" if FROM_LONG else f"ass={EP}/overlay.ass,"
    vf = (f"[0:v]setpts=PTS+{t0:.3f}/TB,{burn}setpts=PTS-STARTPTS,split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.42:saturation=0.7[bg];"
          f"[b]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=0:(H-h)/2-60,ass={ass},fade=t=in:st=0:d=0.25,fade=t=out:st={D - 0.45:.2f}:d=0.45[v]")
    vin = f"{EP}/long.mp4" if FROM_LONG else f"{EP}/video_raw.mp4"
    ain = ["-ss", f"{t0:.3f}", "-t", f"{D:.3f}", "-i", f"{EP}/long.mp4" if FROM_LONG else f"{EP}/mix.wav"]
    out = f"{OUT}/{sh['id']}.mp4"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-t", f"{D:.3f}", "-i", vin] + ain +
                   ["-filter_complex", vf, "-map", "[v]", "-map", "1:a",
                    "-af", f"afade=t=in:d=0.15,afade=t=out:st={D - 0.5:.2f}:d=0.5,loudnorm=I=-14:TP=-1.5", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", out], check=True)
    print(sh["id"], "lines", sh["lines_used"], round(D, 1), "s", out, flush=True)
json.dump({s["id"]: s.get("lines_used") for s in E.META.get("shorts", [])}, open(f"{OUT}/lines_used.json", "w"))
