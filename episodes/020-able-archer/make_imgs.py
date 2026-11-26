# FILE 020 — image prep. Pages come from declassified scans mirrored on archive.org (PFIAB 1990 report via NSArchive EBB 533; SACEUR After Action Report; DCI memo; SNIE; CIA memo).
import subprocess, os, re, json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D="/home/claude/src/doc/"; O="/home/claude/src/img/"; os.makedirs(O+"tmp",exist_ok=True)
W,H=1920,1080
def bg():
    im=Image.new("RGB",(W,H),(52,56,62)); d=ImageDraw.Draw(im)
    for y in range(H):
        v=int(46+22*(1-abs(y-H/2)/(H/2))); d.line([(0,y),(W,y)],fill=(v,v+3,v+8))
    return im
def render(pdf,p,dpi=170):
    out=O+f"tmp/{pdf}_{p}"
    if not any(x.startswith(f"{pdf}_{p}-") for x in os.listdir(O+"tmp")):
        subprocess.run(["pdftoppm","-r",str(dpi),"-f",str(p),"-l",str(p),"-png",D+pdf+".pdf",out],check=True)
    f=[x for x in os.listdir(O+"tmp") if x.startswith(f"{pdf}_{p}-") and x.endswith(".png")][0]; return Image.open(O+"tmp/"+f).convert("RGB")
def words(img):
    img.save(O+"tmp/_t.png"); r=subprocess.run(["tesseract",O+"tmp/_t.png","-","--psm","6","tsv"],capture_output=True,text=True).stdout.splitlines()[1:]
    out=[]
    for l in r:
        c=l.split("\t")
        if len(c)>=12 and c[11].strip() and float(c[10])>20: out.append((int(c[6]),int(c[7]),int(c[8]),int(c[9]),re.sub(r"[^a-z0-9]","",c[11].lower()),int(c[2]),int(c[3]),int(c[4])))
    return out
def find(ws,phrase):
    toks=[re.sub(r"[^a-z0-9]","",t.lower()) for t in phrase.split()]; toks=[t for t in toks if t]
    best=None
    for i in range(len(ws)):
        if ws[i][4]==toks[0] or (len(toks[0])>3 and toks[0][:4]==ws[i][4][:4]):
            # walk forward matching loosely within the next 3*len words
            j=i; k=0; last=i
            while j<len(ws) and k<len(toks) and j<i+len(toks)*3:
                a=ws[j][4]; b=toks[k]
                if a==b or (len(b)>3 and a[:4]==b[:4]): k+=1; last=j
                j+=1
            if k>=max(2,int(len(toks)*0.7)): best=(i,last); break
    return best
def hl(img,phrases):
    ws=words(img); ov=Image.new("RGBA",img.size,(0,0,0,0)); d=ImageDraw.Draw(ov); box=None
    for ph in phrases:
        m=find(ws,ph)
        if not m: print("  NOT FOUND:",ph[:50]); continue
        i,j=m; seg=ws[i:j+1]
        # group by line (block,par,line)
        lines={}
        for w in seg: lines.setdefault((w[5],w[6],w[7]),[]).append(w)
        for ln in lines.values():
            x0=min(w[0] for w in ln)-6; x1=max(w[0]+w[2] for w in ln)+6; y0=min(w[1] for w in ln)-3; y1=max(w[1]+w[3] for w in ln)+3
            d.rectangle([x0,y0,x1,y1],fill=(255,222,40,120))
            box=(x0,y0,x1,y1) if box is None else (min(box[0],x0),min(box[1],y0),max(box[2],x1),max(box[3],y1))
    out=Image.alpha_composite(img.convert("RGBA"),ov).convert("RGB")
    # multiply-ish: darken text under highlight is preserved since overlay is translucent
    return out,box
def place(im,pg,h,cx,cy):
    r=h/pg.height; pg=pg.resize((int(pg.width*r),h),Image.LANCZOS)
    sh=Image.new("RGBA",(pg.width+60,pg.height+60),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([30,40,30+pg.width,40+pg.height],fill=(0,0,0,190)); sh=sh.filter(ImageFilter.GaussianBlur(14))
    x=cx-pg.width//2; y=cy-pg.height//2
    im.paste(sh,(x-30,y-30),sh); d=ImageDraw.Draw(im); d.rectangle([x-3,y-3,x+pg.width+2,y+pg.height+2],outline=(210,214,220),width=3); im.paste(pg,(x,y)); return im,(x,y,r)
FOC={}
def single(key,pdf,p,phrases=(),h=1010,dpi=170):
    pg=render(pdf,p,dpi); box=None
    if phrases: pg,box=hl(pg,phrases)
    im,(x,y,r)=place(bg(),pg,h,W//2,H//2); im.save(O+key+".jpg",quality=93)
    if box: FOC[key]=[round((x+(box[0]+box[2])/2*r)/W,3),round((y+(box[1]+box[3])/2*r)/H,3)]
    else: FOC[key]=[0.5,0.5]
    print(key,FOC[key])
SPEC=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"imgspec.json")))
only=sys.argv[1:]
for s in SPEC:
    if only and s["key"] not in only: continue
    single(s["key"],s["pdf"],s["p"],s.get("hl",[]),s.get("h",1010),s.get("dpi",170))
fp=os.path.join(os.path.dirname(os.path.abspath(__file__)),"focus.json")
old=json.load(open(fp)) if os.path.exists(fp) else {}; old.update(FOC); json.dump(old,open(fp,"w"),indent=1)
