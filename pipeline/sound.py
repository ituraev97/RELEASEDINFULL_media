#!/usr/bin/env python3
"""Synthesised sound for RELEASED IN FULL — no samples, no third-party audio (copyright-free by construction).
import sound as S; S.typewriter(n_keys), S.stamp(), S.paper(), S.static(sec), S.projector(sec), S.whoosh(), S.ping()
music(total_sec, cues) -> stereo bed. All functions return float32 mono/stereo arrays at SR=48000."""
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
SR = 48000
rng = np.random.default_rng(20261029)
def lp(x, f, o=4): return sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "high", fs=SR, output="sos"), x)
def bp(x, a, b, o=2): return sosfilt(butter(o, [a, b], "band", fs=SR, output="sos"), x)
def env(n, a, d):  # attack/decay seconds, exponential decay
    t = np.arange(n) / SR; e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-np.maximum(0, t - a) / max(d, 1e-4)); return e
def norm(x, p=0.9): return (x / (np.abs(x).max() + 1e-9) * p).astype(np.float32)
def room(n=1.4, damp=4500):
    L = int(n * SR); r = rng.standard_normal(L) * np.exp(-np.arange(L) / (0.32 * SR)); r = lp(r, damp); return r / np.sqrt(np.sum(r ** 2))

# ---------------- effects ----------------
def key(strength=1.0):
    n = int(0.09 * SR); t = np.arange(n) / SR
    click = bp(rng.standard_normal(n), 1800, 7000) * env(n, 0.0005, 0.006)
    body = bp(rng.standard_normal(n), 300, 1400) * env(n, 0.001, 0.018) * 0.9
    thock = np.sin(2 * np.pi * 180 * t) * env(n, 0.0005, 0.012) * 0.5
    return (click + body + thock) * strength
def typewriter(n_keys=8, rate=11.0, bell=False):
    """n_keys strokes at ~rate keys/sec with human timing jitter; optional carriage-return bell + slide."""
    tot = int((n_keys / rate + 0.5 + (0.9 if bell else 0)) * SR); x = np.zeros(tot); pos = 0.02
    for i in range(n_keys):
        k = key(0.6 + 0.4 * rng.random()); i0 = int(pos * SR); x[i0:i0 + len(k)] += k[:max(0, min(len(k), tot - i0))]
        pos += (1 / rate) * (0.7 + 0.6 * rng.random())
        if rng.random() < 0.12: pos += 0.08  # space bar pause
    if bell:
        i0 = int((pos + 0.1) * SR); n = int(0.8 * SR); t = np.arange(n) / SR
        b = (np.sin(2 * np.pi * 2350 * t) + 0.5 * np.sin(2 * np.pi * 5870 * t)) * env(n, 0.001, 0.25) * 0.35
        x[i0:i0 + n] += b[:max(0, min(n, tot - i0))]
        s0 = i0 + int(0.15 * SR); sn = int(0.35 * SR)
        slide = bp(rng.standard_normal(sn), 600, 3000) * np.hanning(sn) * 0.3
        x[s0:s0 + sn] += slide[:max(0, min(sn, tot - s0))]
    return norm(x + fftconvolve(x, room(0.3, 3500))[:tot] * 0.1, 0.8)
def stamp():
    n = int(0.9 * SR); t = np.arange(n) / SR
    thud = np.sin(2 * np.pi * np.cumsum(70 * (1 + 1.2 * np.exp(-t * 40))) / SR) * env(n, 0.001, 0.08)
    slap = bp(rng.standard_normal(n), 500, 5000) * env(n, 0.0005, 0.02) * 0.9
    wood = sum(np.sin(2 * np.pi * f * t) * env(n, 0.0005, 0.05) * a for f, a in [(420, .25), (910, .12)])
    x = thud + slap + wood
    return norm(x + fftconvolve(x, room(0.35, 3000))[:n] * 0.12, 0.95)
def paper(sec=0.9):
    n = int(sec * SR); t = np.arange(n) / SR
    am = lp(np.abs(rng.standard_normal(n)), 18); am = am / am.max()
    crinkle = (rng.random(n) < 0.0016) * rng.standard_normal(n) * 4
    x = bp(rng.standard_normal(n) * am + crinkle, 900, 9000) * np.sin(np.pi * t / sec) ** 0.7
    return norm(x, 0.55)
def static(sec=1.2, tuned=0.0):
    """radio static; tuned>0 adds a wobbly carrier."""
    n = int(sec * SR); t = np.arange(n) / SR
    x = bp(rng.standard_normal(n), 400, 5200) * (0.6 + 0.4 * lp(rng.standard_normal(n), 3) * 3)
    cr = (rng.random(n) < 0.004) * rng.standard_normal(n) * 6; x += hp(cr, 1500)
    if tuned: x += tuned * np.sin(2 * np.pi * (900 + 60 * np.sin(2 * np.pi * 3 * t)) * t) * 0.3
    fade = np.minimum(1, np.minimum(t / 0.05, (sec - t) / 0.12))
    return norm(x * fade, 0.5)
def projector(sec=2.0):
    n = int(sec * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k in np.arange(0, sec, 1 / 24):
        c = bp(rng.standard_normal(int(0.012 * SR)), 1500, 6000) * env(int(0.012 * SR), 0.0003, 0.003)
        i0 = int(k * SR); x[i0:i0 + len(c)] += c[:max(0, min(len(c), n - i0))]
    hum = (np.sin(2 * np.pi * 120 * t) * 0.15 + np.sin(2 * np.pi * 240 * t) * 0.05)
    fade = np.minimum(1, np.minimum(t / 0.15, (sec - t) / 0.3))
    return norm((x * 0.6 + hum) * fade, 0.45)
def whoosh(sec=0.6, up=True):
    n = int(sec * SR); out = np.zeros(n); noise = rng.standard_normal(n + 4000); seg = SR // 50
    for k in range(0, n, seg):
        u = k / n; fc = (300 + 4500 * u ** 2) if up else (4800 - 4500 * u ** 0.5)
        out[k:k + seg] = bp(noise[k:k + seg + 2000], fc * .6, min(fc * 1.5, 20000))[:len(out[k:k + seg])]
    return norm(out * np.sin(np.pi * np.arange(n) / n) ** 2, 0.5)
def ping():
    n = int(2.2 * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 1180 * t) * env(n, 0.002, 0.35) + 0.3 * np.sin(2 * np.pi * 2360 * t) * env(n, 0.002, 0.15)
    return norm(x + fftconvolve(x, room(1.8, 3000))[:n] * 0.6, 0.4)
def hit(amp=1.0):
    n = int(3.5 * SR); t = np.arange(n) / SR
    f = 38 * (1 + 2.0 * np.exp(-t * 14))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.8) + lp(rng.standard_normal(n), 2500) * np.exp(-t * 20) * 0.5
    return norm(x + fftconvolve(x, room(2.4, 2500))[:n] * 0.5, amp)

# ---------------- music ----------------
def music(total, sections, silences=(), seed=7):
    """total sec. sections: list of (start, kind) where kind in {'open','tension','pulse','reveal','calm','end'}.
    silences: list of (t0, t1) where the bed fades out (for dramatic pauses).
    Palette: D minor with a flat-2 (Eb) colour; slow pads, sub drone, sparse FM-bell motifs, soft clock pulse."""
    r = np.random.default_rng(seed); N = int(total * SR) + SR; t = np.arange(N) / SR
    def kind_at(x):
        k = sections[0][1]
        for s, kk in sections:
            if x >= s: k = kk
        return k
    level = {'open': .8, 'tension': .9, 'pulse': 1.0, 'reveal': .7, 'calm': .55, 'end': .8}
    # control curves (smoothed step functions)
    def curve(fn, smooth=2.0):
        raw = np.array([fn(kind_at(x)) for x in np.arange(0, total + 1, 0.05)])
        k = int(smooth / 0.05); ker = np.hanning(2 * k + 1); ker /= ker.sum()
        sm = np.convolve(np.pad(raw, k, mode="edge"), ker, mode="valid")
        return np.interp(t, np.arange(len(sm)) * 0.05, sm)
    lvl = curve(lambda k: level[k]); pul = curve(lambda k: 1.0 if k == 'pulse' else (0.45 if k == 'tension' else 0.0), 1.5)
    bright = curve(lambda k: 1.0 if k in ('reveal', 'end') else 0.3)
    # sub drone D1/A1
    drone = 0.55 * np.sin(2 * np.pi * 36.71 * t) + 0.25 * np.sin(2 * np.pi * 55.0 * t + 0.4 * np.sin(2 * np.pi * 0.05 * t))
    # pads: detuned saw-ish stacks, chord changes every ~16 s: Dm(add9) -> Bb(maj7) -> Gm -> Eb(lyd) colour
    chords = [[146.83, 174.61, 220.0, 329.63], [116.54, 146.83, 174.61, 220.0], [98.0, 146.83, 196.0, 233.08], [155.56, 196.0, 233.08, 293.66]]
    pad = np.zeros(N); L = 16.0
    for ci in range(int(total // L) + 2):
        ch = chords[ci % len(chords)]; s0, s1 = int(ci * L * SR), int(min(N, (ci + 1) * L * SR + 4 * SR))
        if s0 >= N: break
        tt = np.arange(s1 - s0) / SR; seg = np.zeros(s1 - s0)
        for f in ch:
            for det in (-0.12, 0.0, 0.11):
                ph = r.random() * 6.28
                seg += sum(np.sin(2 * np.pi * f * (1 + det / 100) * h * tt + ph * h) / h ** 1.6 for h in (1, 2, 3))
        w = np.minimum(1, tt / 4.0) * np.minimum(1, (tt[-1] - tt) / 4.0)  # 4 s crossfades
        pad[s0:s1] += seg * w
    pad = lp(pad, 900) * 0.06 + lp(pad, 2600) * 0.025 * bright
    # bell motif (FM), sparse: every 5–9 s, notes from D minor pentatonic + Eb
    bells = np.zeros(N); x0 = 3.0
    notes = [587.33, 698.46, 880.0, 622.25, 783.99, 1174.66]
    while x0 < total - 4:
        f = notes[r.integers(len(notes))]; n = int(3.0 * SR); tt = np.arange(n) / SR
        b = np.sin(2 * np.pi * f * tt + 1.4 * np.exp(-tt * 3) * np.sin(2 * np.pi * f * 1.41 * tt)) * np.exp(-tt * 1.6)
        i0 = int(x0 * SR); bells[i0:i0 + n] += b[:max(0, min(n, N - i0))] * 0.12
        x0 += 5 + r.random() * 4
    # clock-like pulse (soft ticks, 84 bpm)
    tick = np.zeros(N); per = 60 / 84
    for k, x in enumerate(np.arange(0.5, total, per)):
        n = int(0.06 * SR); c = bp(r.standard_normal(n), 2000, 6000) * env(n, 0.0005, 0.008) * (0.8 if k % 2 == 0 else 0.5)
        th = np.sin(2 * np.pi * 55 * np.arange(int(.25 * SR)) / SR) * env(int(.25 * SR), 0.002, 0.07) * (0.9 if k % 4 == 0 else 0)
        i0 = int(x * SR); tick[i0:i0 + n] += c[:max(0, min(n, N - i0))]; tick[i0:i0 + len(th)] += th[:max(0, min(len(th), N - i0))]
    mono = drone * 0.35 * lvl + pad * lvl + bells * lvl * (0.6 + 0.4 * bright) + tick * 0.08 * pul
    # silences: fade the whole bed out and back in
    g = np.ones(N)
    for a, b_ in silences:
        ia, ib = int(a * SR), int(b_ * SR); fo = int(0.6 * SR); fi = int(1.2 * SR)
        g[max(0, ia - fo):ia] = np.minimum(g[max(0, ia - fo):ia], np.linspace(1, 0, ia - max(0, ia - fo)))
        g[ia:ib] = 0; g[ib:ib + fi] = np.minimum(g[ib:ib + fi], np.linspace(0, 1, len(g[ib:ib + fi])))
    fade = np.minimum(1, np.minimum(t / 3.0, np.maximum(0, total - t) / 5.0))
    mono = mono * g * fade
    rv = fftconvolve(mono, room(3.0, 3500))[:N]
    L_ = mono + rv * 0.35; R_ = np.roll(mono, int(0.011 * SR)) + np.roll(rv, int(0.023 * SR)) * 0.35  # slight width
    return np.stack([L_, R_], 1)[:int(total * SR)].astype(np.float32)

if __name__ == "__main__":
    import soundfile as sf, os, sys
    d = sys.argv[1] if len(sys.argv) > 1 else "sfx_demo"; os.makedirs(d, exist_ok=True)
    for name, x in [("typewriter", typewriter(14, bell=True)), ("stamp", stamp()), ("paper", paper()), ("static", static(1.5, 0.6)),
                    ("projector", projector(2.5)), ("whoosh", whoosh()), ("ping", ping()), ("hit", hit())]:
        sf.write(f"{d}/{name}.wav", x, SR)
    m = music(60, [(0, 'open'), (12, 'tension'), (28, 'pulse'), (44, 'reveal')], silences=[(40.5, 43.5)])
    sf.write(f"{d}/music60.wav", m / np.abs(m).max() * 0.8, SR)
    print("ok")
