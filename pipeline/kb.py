#!/usr/bin/env python3
"""Sub-pixel Ken Burns for stills/documents (replaces ffmpeg zoompan, which rounds crop offsets and wobbles).
usage: kb.py <image> <out.mp4> <seconds> [mode] [focus_x focus_y]
mode: in | out | left | right | up | down | hold     focus: 0..1 point the move centres on (default .5 .5)
Each frame is an exact float affine warp (Lanczos) of the original image, so motion is continuous to 1/256 px.
Motion is a slow constant-velocity move in log-zoom space with a short ease at both ends (no visible start/stop jolt).
Background behind the image: blurred, darkened copy (for portrait documents)."""
import sys, subprocess, numpy as np, cv2
img_p, out, secs = sys.argv[1], sys.argv[2], float(sys.argv[3])
mode = sys.argv[4] if len(sys.argv) > 4 else "in"
fx, fy = (float(sys.argv[5]), float(sys.argv[6])) if len(sys.argv) > 6 else (0.5, 0.5)
W, H, FPS = 1920, 1080, 30
src = cv2.imread(img_p, cv2.IMREAD_COLOR); h0, w0 = src.shape[:2]
n = max(1, round(secs * FPS))
# cover vs contain: documents (portrait-ish) are contained on a blurred backdrop; photos cover the frame
contain = (w0 / h0) < 1.25
if contain:
    bg = cv2.resize(src, (W, int(W * h0 / w0)) if w0 / h0 < W / H else (int(H * w0 / h0), H))
    by, bx = (bg.shape[0] - H) // 2, (bg.shape[1] - W) // 2
    bg = bg[max(0, by):max(0, by) + H, max(0, bx):max(0, bx) + W]
    bg = cv2.resize(bg, (W, H)); bg = cv2.GaussianBlur(bg, (0, 0), 40); bg = (bg * 0.32).astype(np.uint8)
    base = min(W * 0.86 / w0, H * 0.94 / h0)
else:
    base = max(W / w0, H / h0)
Z = {"in": (1.0, 1.10), "out": (1.10, 1.0), "left": (1.08, 1.08), "right": (1.08, 1.08), "up": (1.08, 1.08), "down": (1.08, 1.08), "hold": (1.0, 1.0)}[mode]
def ease(u):  # constant speed with 12% smooth ramps at each end (C1-continuous)
    a = 0.12
    if u < a: return (u * u) / (2 * a * (1 - a))
    if u > 1 - a: return 1 - ((1 - u) ** 2) / (2 * a * (1 - a))
    return (u - a / 2) / (1 - a)
ff = subprocess.Popen(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                       "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), out], stdin=subprocess.PIPE)
for i in range(n):
    u = ease(i / max(1, n - 1))
    z = base * np.exp(np.log(Z[0]) + (np.log(Z[1]) - np.log(Z[0])) * u)
    # focus point in source px; the visible window is centred on it, panning shifts it
    cxs, cys = fx * w0, fy * h0
    # pan amplitude limited to the margin the zoom leaves, so the window never hits the image edge (no clamp kink)
    if contain: mx, my = 0.04 * W, 0.04 * H
    else:
        tcx, tcy = W / 2 - cxs * z, H / 2 - cys * z
        mx = 0.9 * max(0.0, min(tcx - (W - w0 * z), -tcx)); my = 0.9 * max(0.0, min(tcy - (H - h0 * z), -tcy))
    s_ = (u - 0.5) * 2
    dx = {"left": -s_, "right": s_}.get(mode, 0.0) * min(0.06 * W, mx)
    dy = {"up": -s_, "down": s_}.get(mode, 0.0) * min(0.06 * H, my)
    # keep the window inside the image for cover mode
    tx = W / 2 - cxs * z + dx; ty = H / 2 - cys * z + dy
    if not contain:
        tx = min(0, max(W - w0 * z, tx)); ty = min(0, max(H - h0 * z, ty))
    M = np.float32([[z, 0, tx], [0, z, ty]])
    if contain:
        fr = cv2.warpAffine(src, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
        mask = cv2.warpAffine(np.full((h0, w0), 255, np.uint8), M, (W, H), flags=cv2.INTER_LINEAR)
        m = (mask.astype(np.float32) / 255)[..., None]
        fr = (fr * m + bg * (1 - m)).astype(np.uint8)
    else:
        fr = cv2.warpAffine(src, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
    ff.stdin.write(fr.tobytes())
ff.stdin.close(); ff.wait()
