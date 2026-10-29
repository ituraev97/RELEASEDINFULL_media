#!/usr/bin/env python3
"""Phrase-by-phrase Kokoro narration (livelier than one-shot synthesis: measured F0 spread ~4.5 st vs ~3.0 st).
usage: tts.py <episode_dir> [voice] [base_speed]
Each LINES text is split into phrases at sentence ends and at "|" marks; each phrase is synthesised separately,
trimmed, and joined with pauses: "." 0.32 s, "?" 0.5 s, "!" 0.4 s, "|" 0.45 s, "..." 0.75 s.
opts.slow=True reads the line ~7% slower (reveals). Questions get +3% speed (natural lift).
Writes <ep>/vo/raw_NN.wav (24 kHz) and vo/phrases.json (phrase timings, used for subtitles)."""
import sys, os, re, json, importlib.util, numpy as np, soundfile as sf, librosa
from kokoro_onnx import Kokoro
ep = os.path.abspath(sys.argv[1]); voice = sys.argv[2] if len(sys.argv) > 2 else "am_fenrir"
base = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
spec = importlib.util.spec_from_file_location("episode", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
K = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
def vstyle(v):
    if ":" not in v: return v
    acc = None
    for part in v.split("+"):
        n, w = part.split(":"); x = K.get_voice_style(n) * float(w); acc = x if acc is None else acc + x
    return acc
STY = vstyle(voice)
PAUSE = {".": 0.32, "?": 0.5, "!": 0.4, "|": 0.45, "…": 0.75, ",": 0.0}
PRON = getattr(E, "PRON", [])
def say(p):
    for a, b in PRON: p = p.replace(a, b)
    return p
def phrases(text):
    t = text.replace("...", "…")
    parts = re.split(r"(\||…|(?<=[.?!])\s)", t)
    out, cur = [], ""
    for p in parts:
        if p is None: continue
        if p in ("|", "…"):
            if cur.strip(): out.append((cur.strip(), p)); cur = ""
            elif out: out[-1] = (out[-1][0], p)
        elif p.strip() == "" and cur.strip():
            out.append((cur.strip(), cur.strip()[-1] if cur.strip()[-1] in ".?!" else ".")); cur = ""
        else: cur += p
    if cur.strip(): out.append((cur.strip(), cur.strip()[-1] if cur.strip()[-1] in ".?!" else "."))
    return out
def trim(a, sr):
    _, (s, e) = librosa.effects.trim(a, top_db=42, frame_length=512, hop_length=128)
    s = max(0, s - int(0.015 * sr)); e = min(len(a), e + int(0.03 * sr)); return a[s:e]
os.makedirs(f"{ep}/vo", exist_ok=True); meta = {}; tot = 0
PJ = f"{ep}/vo/phrases.json"; OLD = json.load(open(PJ)) if os.path.exists(PJ) and not os.environ.get("TTS_FRESH") else {}
for i, (text, shots, o) in enumerate(E.LINES, 1):
    f = f"{ep}/vo/raw_{i:02d}.wav"
    if not text.strip():
        sf.write(f, np.zeros(int(0.05 * 24000), np.float32), 24000); meta[i] = []; continue
    if os.path.exists(f) and str(i) in OLD and OLD[str(i)] and " ".join(p["text"] for p in OLD[str(i)]) == " ".join(p for p, _ in phrases(text)):
        meta[i] = OLD[str(i)]; tot += len(sf.read(f)[0]) / 24000; continue
    chunks, t, pm = [], 0.0, []
    ph = phrases(text)
    for j, (p, end) in enumerate(ph):
        sp = base * (0.93 if o.get("slow") else 1.0) * (1.03 if end == "?" else 1.0)
        a, sr = K.create(say(p), voice=STY, speed=sp, lang="en-us"); a = trim(a, sr)
        pm.append(dict(text=p, t0=round(t, 3), t1=round(t + len(a) / sr, 3)))
        chunks.append(a); t += len(a) / sr
        if j < len(ph) - 1:
            g = PAUSE.get(end, 0.32) * (1.25 if o.get("slow") else 1.0)
            chunks.append(np.zeros(int(g * sr), np.float32)); t += g
    a = np.concatenate(chunks).astype(np.float32); sf.write(f, a, sr); meta[i] = pm; tot += len(a) / sr
json.dump({str(k): v for k, v in meta.items()}, open(f"{ep}/vo/phrases.json", "w"), indent=1)
print("speech seconds:", round(tot, 1))
