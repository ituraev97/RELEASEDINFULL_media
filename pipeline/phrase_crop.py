#!/usr/bin/env python3
"""phrase_crop.py <pdf> <page> "<phrase>" <out.jpg> [ctx_lines=1] -> tight high-dpi crop around a phrase (for thumbnails).
Writes <out>.json with the phrase box in output pixel coords (x,y,w,h)."""
import sys, re, subprocess, html, json, tempfile, os
from PIL import Image
pdf, page, phrase, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]; ctx = int(sys.argv[5]) if len(sys.argv) > 5 else 1
x = subprocess.check_output(["pdftotext", "-f", str(page), "-l", str(page), "-bbox", pdf, "-"]).decode()
pw = float(re.search(r'<page width="([\d.]+)"', x).group(1))
W = [(float(a), float(b), float(c), float(d), html.unescape(t)) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
toks = phrase.lower().split(); n = len(toks)
norm = lambda s: re.sub(r"[^a-z0-9-]", "", s.lower())
for i in range(len(W) - n + 1):
    if all(norm(W[i + k][4]) == norm(toks[k]) for k in range(n)): seq = W[i:i + n]; break
else: sys.exit("phrase not found")
x0, y0, x1, y1 = min(w[0] for w in seq), min(w[1] for w in seq), max(w[2] for w in seq), max(w[3] for w in seq)
lh = (y1 - y0) if len({round(w[1]) for w in seq}) == 1 else 12
cx0, cx1 = x0 - 90, x1 + 90; cy0, cy1 = y0 - lh * (1.6 * ctx + 0.5), y1 + lh * (1.6 * ctx + 0.5)
tmp = tempfile.mkdtemp(); subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "400", "-jpeg", pdf, tmp + "/p"], check=True)
im = Image.open([os.path.join(tmp, f) for f in os.listdir(tmp)][0]).convert("RGB"); s = im.width / pw
c = im.crop((int(cx0 * s), int(cy0 * s), int(cx1 * s), int(cy1 * s))); c.save(out, quality=94)
json.dump(dict(x=(x0 - cx0) * s, y=(y0 - cy0) * s, w=(x1 - x0) * s, h=(y1 - y0) * s, W=c.width, H=c.height), open(out + ".json", "w"))
print(out, c.size, [w[4] for w in seq])
