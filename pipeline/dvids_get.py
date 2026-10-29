#!/usr/bin/env python3
"""Download DVIDS videos/images by scraping the public page (no API key). usage: dvids_get.py <outdir> video:ID|image:ID ...
Writes <outdir>/dv<ID>.mp4 (or .jpg) and appends rights info to <outdir>/rights.json"""
import sys, re, json, os, subprocess, time
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
rf = os.path.join(out, "rights.json"); rights = json.load(open(rf)) if os.path.exists(rf) else {}
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
for item in sys.argv[2:]:
    kind, vid = item.split(":")
    html = subprocess.run(["curl", "-sL", "-m", "60", "-A", UA, f"https://www.dvidshub.net/{kind}/{vid}"], capture_output=True, text=True).stdout
    title = (re.search(r"<title>(.*?)</title>", html, re.S) or [None, ""])[1].strip()
    lic = "PUBLIC DOMAIN" if re.search(r"public domain", html, re.I) else "SEE DVIDS TERMS"
    if kind == "video":
        cands = sorted(set(re.findall(r"https://[^\"' ]+?-(\d+)x(\d+)-(\d+)k\.mp4", html)), key=lambda x: (int(x[1]), int(x[2])))
        urls = {m: u for m, u in [((w, h, k), u) for u in set(re.findall(r"https://[^\"' ]+?\.mp4", html)) for (w, h, k) in [re.search(r"-(\d+)x(\d+)-(\d+)k\.mp4", u).groups() if re.search(r"-(\d+)x(\d+)-(\d+)k\.mp4", u) else ("0","0","0")]]}
        best = max(urls.items(), key=lambda kv: (int(kv[0][1]), int(kv[0][2])))[1] if urls else None
        dst = os.path.join(out, f"dv{vid}.mp4")
    else:
        best = (re.findall(r"https://d1ldvf68ux039x\.cloudfront\.net/thumbs/photos/[^\"' ]+?/1000w_q95\.jpg", html) or re.findall(r'<meta property="og:image" content="([^"]+)"', html) or [None])[0]
        dst = os.path.join(out, f"dvimg{vid}.jpg")
    if not best: print("NO FILE", item, title); continue
    if not os.path.exists(dst): subprocess.run(["curl", "-sL", "-m", "300", "-A", UA, best, "-o", dst], check=True)
    rights[os.path.basename(dst)] = dict(source=f"https://www.dvidshub.net/{kind}/{vid}", title=title, license=lic, file_url=best)
    print(item, lic, os.path.getsize(dst) // 1024, "KB", title[:80]); time.sleep(1.5)
json.dump(rights, open(rf, "w"), indent=1)
