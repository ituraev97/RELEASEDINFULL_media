# FILE 019 — image prep. Pages come from DOJ's released data sets (Data Sets 3, 4, 6; mirrored on archive.org, item 20251224_20251224_2055).
import subprocess, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D="/home/claude/src/doc/"; O="/home/claude/src/img/"; os.makedirs(O+"tmp",exist_ok=True)
W,H=1920,1080
def bg():
    im=Image.new("RGB",(W,H),(52,56,62)); d=ImageDraw.Draw(im)
    for y in range(H): 
        v=int(46+22*(1-abs(y-H/2)/(H/2))); d.line([(0,y),(W,y)],fill=(v,v+3,v+8))
    return im
def page(pdf,p,dpi=130):
    out=O+f"tmp/{pdf}_{p}"; subprocess.run(["pdftoppm","-r",str(dpi),"-f",str(p),"-l",str(p),"-png",D+pdf+".pdf",out],check=True)
    f=[x for x in os.listdir(O+"tmp") if x.startswith(f"{pdf}_{p}-")][0]; return Image.open(O+"tmp/"+f).convert("RGB")
def place(im,pg,h,cx,cy):
    r=h/pg.height; pg=pg.resize((int(pg.width*r),h),Image.LANCZOS)
    sh=Image.new("RGBA",(pg.width+60,pg.height+60),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([30,40,30+pg.width,40+pg.height],fill=(0,0,0,190)); sh=sh.filter(ImageFilter.GaussianBlur(14))
    x=cx-pg.width//2; y=cy-pg.height//2
    im.paste(sh,(x-30,y-30),sh); d=ImageDraw.Draw(im); d.rectangle([x-3,y-3,x+pg.width+2,y+pg.height+2],outline=(210,214,220),width=3); im.paste(pg,(x,y)); return im
def single(name,pdf,p,h=1000):
    im=place(bg(),page(pdf,p),h,W//2,H//2); im.save(O+name+".jpg",quality=93)
single("p_b1","EFTA00005586",1); single("p_b60","EFTA00005586",60)
single("t1","EFTA00008744",1); single("t2","EFTA00008744",2)
# three-document series side by side
im=bg()
for i,(n,cx) in enumerate([("EFTA00006109",340),("EFTA00006209",960),("EFTA00006309",1580)]):
    im=place(im,page(n,1,100),780,cx,H//2)
im.save(O+"p_series.jpg",quality=93)
# 119-tile grid (17 x 7), our visualization
f=lambda s,b=True: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
for fp in [os.path.expanduser("~/.fonts/Archivo-ExtraBold.ttf")]:
    if os.path.exists(fp): f=lambda s,b=True,fp=fp: ImageFont.truetype(fp,s)
im=bg(); d=ImageDraw.Draw(im)
d.text((W//2,72),"ONE DOCUMENT · 119 PAGES · EVERY PAGE BLACK",font=f(58),fill=(242,208,75),anchor="mm")
tw,th,gx,gy=80,100,14,12; cols,rows=17,7; x0=(W-(cols*tw+(cols-1)*gx))//2; y0=170
for r in range(rows):
    for c in range(cols):
        x=x0+c*(tw+gx); y=y0+r*(th+gy); d.rectangle([x,y,x+tw,y+th],fill=(0,0,0),outline=(200,204,210),width=2)
d.text((W//2,y0+rows*(th+gy)+34),"EFTA00005586 · each tile = one page · OUR VISUALIZATION of the released file",font=f(34,False),fill=(215,218,224),anchor="mm")
im.save(O+"g_119.jpg",quality=93)
print("ok")
