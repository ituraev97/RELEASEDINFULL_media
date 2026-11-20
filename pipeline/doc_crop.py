#!/usr/bin/env python3
"""crop.py <pdf> <page> <start-phrase> <end-phrase> <out.jpg> [margin]
Crops whole lines from the first line containing start-phrase through the first later line containing end-phrase,
renders at 200 dpi, pads to 16:9 with white (>=10% margins)."""
import sys, subprocess, re, os, tempfile, html
from PIL import Image
pdf, page, a, b, out = sys.argv[1], int(sys.argv[2]), sys.argv[3].lower(), sys.argv[4].lower(), sys.argv[5]
x = subprocess.check_output(["pdftotext", "-f", str(page), "-l", str(page), "-bbox-layout", pdf, "-"]).decode("utf-8", "replace")
pw, ph = map(float, re.search(r'<page width="([\d.]+)" height="([\d.]+)"', x).groups())
lines = []
for m in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', x, re.S):
    words = re.findall(r'>([^<]*)</word>', m.group(5)); t = html.unescape(" ".join(words))
    lines.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), t))
COL = os.environ.get("COL")  # 2026-11-20: two-column pages (left/right half only)
if COL: lines = [l for l in lines if (l[0] < pw / 2) == (COL == "left")]
lines.sort(key=lambda l: (round(l[1]), l[0]))
NAMES = ["villafa", "lourie", "sloman", "menchel", "lefkowitz", "[j]ay", "jay", "krischer", "krisher", "belohlavek", "reiter", "goldberger",
         "starr", "whitley", "roth", "filip", "sanchez", "[m]arie", "marie", "andy", "dershowitz", "lefcourt", "senior", "black", "jack", "lanna", "michael"]
NAMES += [n for n in os.environ.get("NAMES_EXTRA", "").lower().split(",") if n]  # 2026-11-20: per-episode names to bar
words_all = [(float(a), float(b), float(c), float(d), html.unescape(t)) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
norm = lambda s: re.sub(r"\s+", "", s.lower().replace("’", "'").replace("“", '"').replace("”", '"'))
i0 = next(i for i, l in enumerate(lines) if norm(a) in norm(l[4]))
i1 = next(i for i, l in enumerate(lines) if i >= i0 and norm(b) in norm(l[4]))
sel = lines[i0:i1 + 1]
# full text-column width for whole lines
x0 = min(l[0] for l in lines if l[1] > ph * 0.06 and l[3] < ph * 0.94); x1 = max(l[2] for l in lines if l[1] > ph * 0.06 and l[3] < ph * 0.94)
y0 = min(l[1] for l in sel) - 1.2; y1 = max(l[3] for l in sel) + 2.2  # tight: no slivers of neighbouring lines
tmp = tempfile.mkdtemp(); subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "200", "-jpeg", pdf, tmp + "/p"], check=True)
im = Image.open([os.path.join(tmp, f) for f in os.listdir(tmp)][0]).convert("RGB"); s = im.width / pw
from PIL import ImageDraw, ImageFont
dr = ImageDraw.Draw(im); nred = 0
# 2026-11-18: blank words of neighbouring lines that poke into the crop (no slivers)
for l in lines:
    if l in sel: continue
    ys0 = min(q[1] for q in sel); ys1 = max(q[3] for q in sel)
    if l[1] >= ys1 - 4 and l[1] < y1 + 3:   # line below: blank only what lies below the selected text
        dr.rectangle([l[0] * s - 2, (ys1 + 0.4) * s, l[2] * s + 2, (y1 + 3) * s], fill=(255, 255, 255))
    elif l[1] < ys0 - 2 and l[3] > y0 - 3:  # line above
        dr.rectangle([l[0] * s - 2, (y0 - 3) * s, l[2] * s + 2, (ys0 + float(os.environ.get("TOPCUT", "0.9"))) * s], fill=(255, 255, 255))
for (wa, wb, wc, wd, t) in words_all:
    if COL and ((wa < pw / 2) != (COL == "left")): continue
    tl = t.lower().strip(".,;:’'\"“”()")
    if wb >= y0 - 2 and wd <= y1 + 2 and any((tl.startswith(n) if n in ('black','roth','andy','senior','jay','marie','jack','alex','michael','starr') else n in tl) for n in NAMES) and not tl.startswith('[a]lex') and not (tl == "black" and os.environ.get("KEEPBLACK")) and not (tl == "senior" and not os.environ.get("REDSENIOR")):
        dr.rectangle([wa * s - 3, wb * s - 2, wc * s + 3, wd * s + 2], fill=(10, 10, 10)); nred += 1
c = im.crop((int(x0 * s) - 10, int(y0 * s), int(x1 * s) + 10, int(y1 * s)))
cw, chh = c.size; W = int(cw * 1.22); H = int(chh * 1.3)
if W / H > 16 / 9: H = int(W * 9 / 16)
else: W = int(H * 16 / 9)
bg = Image.new("RGB", (W, H), (250, 250, 247)); bg.paste(c, ((W - cw) // 2, (H - chh) // 2))
if nred:
    d2 = ImageDraw.Draw(bg); fs = max(16, W // 70)
    f = ImageFont.truetype(os.path.expanduser("~/.fonts/CourierPrime-Bold.ttf"), fs)
    d2.text((W // 2, H - (H - chh) // 4), "BLACK BARS: NAMES WITHHELD BY RELEASED IN FULL", font=f, fill=(90, 90, 90), anchor="mm")
if bg.width < 1920: bg = bg.resize((1920, int(1920 * bg.height / bg.width)), Image.LANCZOS)
bg.save(out, quality=93); print(out, bg.size, "red", nred, "|", " / ".join(l[4] for l in sel)[:300])
