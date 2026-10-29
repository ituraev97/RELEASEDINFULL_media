// Thumbnails, 3 variants for YouTube Test & Compare. usage: NODE_PATH=$(npm root -g) node thumb.mjs <thumb.json> <outdir>
// thumb.json: {"image":"/abs/frame.jpg","pos":"60% 40%","zoom":110,"hud":true,
//  "A":{"big":"NAVY<br>UFO <b>TAPES</b>","stamp":"RELEASED 2020"},           // big stencil words + stamp
//  "B":{"header":"DEPT. OF DEFENSE · 2020","lines":["[[9]] [[6]] remain","{{UNIDENTIFIED}}"]},  // document excerpt
//  "C":{"q":"WHAT DID THE <b>PILOTS</b> SEE?","tag":"OFFICIAL VIDEO · FLIR1"}}  // question over full-bleed frame
// Rules: ≤ 5 words of big text, nothing in bottom-right (duration badge), no seals/badges, no gore, honest promise.
import fs from "fs"; import path from "path"; import { createRequire } from "module";
import { page, C, NAME, SHORT } from "./brand.css.mjs";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const cfg = JSON.parse(fs.readFileSync(process.argv[2])); const out = process.argv[3]; fs.mkdirSync(out, { recursive: true });
const img = `data:image/jpeg;base64,${fs.readFileSync(cfg.image).toString("base64")}`;
const b_ = (s) => s.replace(/<b>/g, `<span style="color:${C.phosphor}">`).replace(/<\/b>/g, "</span>");
const rich = (s) => s.replace(/\[\[(\d+)\]\]/g, (_, n) => `<span style="display:inline-block;width:${n * .55}em;height:.8em;background:#0b0b0c;vertical-align:-.05em"></span>`)
  .replace(/\{\{(.+?)\}\}/g, (_, x) => `<span style="background:${C.highlight};padding:0 .12em">${x}</span>`);
const X = `.t{position:relative;width:1280px;height:720px;overflow:hidden;background:${C.carbon}}
.ph{position:absolute;background-image:url(${img});background-size:${cfg.zoom || 110}%;background-position:${cfg.pos || "50% 50%"};filter:contrast(1.08) saturate(.9)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 160px rgba(0,0,0,.8)}
.logo{position:absolute;left:34px;bottom:28px;transform:rotate(-4deg);filter:url(#ink)}
.logo div{border:5px solid ${C.paper};outline:2px solid ${C.paper};outline-offset:3px;padding:3px 9px 0;font-family:Stencil;font-weight:900;font-size:34px;color:${C.paper};letter-spacing:.05em;line-height:1}
.hud{position:absolute;border:3px solid ${C.phosphor};opacity:.9}
.hud::before,.hud::after{content:"";position:absolute;background:${C.phosphor}}
.hud::before{left:50%;top:-22px;bottom:-22px;width:3px;margin-left:-1.5px;clip-path:polygon(0 0,100% 0,100% 18%,0 18%,0 82%,100% 82%,100% 100%,0 100%)}
.hud::after{top:50%;left:-22px;right:-22px;height:3px;margin-top:-1.5px;clip-path:polygon(0 0,12% 0,12% 100%,0 100%,88% 0,100% 0,100% 100%,88% 100%)}`;
const logo = `<div class="logo"><div>${SHORT}</div></div>`;
const stamp = (txt, size, rot) => `<div style="display:inline-block;transform:rotate(${rot}deg);filter:url(#ink)"><div style="border:${size * .1}px solid ${C.stamp};outline:${size * .035}px solid ${C.stamp};outline-offset:${size * .07}px;background:rgba(232,224,202,.92);padding:${size * .1}px ${size * .3}px ${size * .02}px;color:${C.stamp};font-family:Stencil;font-weight:900;font-size:${size}px;letter-spacing:.05em;line-height:1;white-space:nowrap">${txt}</div></div>`;
const hud = cfg.hud ? (x, y, s) => `<div class="hud" style="left:${x}px;top:${y}px;width:${s}px;height:${s}px"></div>` : () => "";
const V = {
  A: (o) => `<div class="t"><div class="ph" style="left:470px;top:0;right:0;bottom:0"></div>
     <div style="position:absolute;inset:0;background:linear-gradient(90deg,${C.carbon} 0%,${C.carbon} 37%,rgba(13,15,18,.55) 48%,rgba(13,15,18,0) 62%)"></div><div class="vig"></div>
     ${hud(o.hx ?? 820, o.hy ?? 210, o.hs ?? 230)}
     <div style="position:absolute;left:40px;top:${o.top ?? 70}px" class="stencil"><div style="font-size:${o.size || 168}px;color:${C.paper};text-shadow:0 6px 0 rgba(0,0,0,.5)">${b_(o.big)}</div></div>
     ${o.stamp ? `<div style="position:absolute;left:${o.sx ?? 60}px;top:${o.sy ?? 500}px">${stamp(o.stamp, o.ss || 52, -6)}</div>` : ""}${logo}</div>`,
  B: (o) => `<div class="t"><div class="ph" style="left:520px;top:0;right:0;bottom:0"></div><div class="vig"></div>
     ${hud(o.hx ?? 860, o.hy ?? 200, o.hs ?? 220)}
     <div class="paper" style="position:absolute;left:36px;top:60px;width:640px;padding:40px 44px 50px;transform:rotate(-3deg);box-shadow:0 30px 60px rgba(0,0,0,.7)">
      <div class="courier" style="font-weight:700;font-size:22px;letter-spacing:.2em;color:#3a372f">${o.header}</div>
      <div style="height:2px;background:#3a372f;opacity:.5;margin:16px 0 20px"></div>
      ${o.lines.map((l, i) => `<div class="courier" style="font-weight:700;font-size:${i === o.lines.length - 1 ? (o.size || 86) : 40}px;line-height:1.15;color:#1d1b17;margin-top:${i ? 14 : 0}px">${rich(l)}</div>`).join("")}
     </div>${logo}</div>`,
  C: (o) => `<div class="t"><div class="ph" style="inset:0"></div>
     <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,15,18,.85) 0%,rgba(13,15,18,.35) 55%,rgba(13,15,18,.6) 100%)"></div><div class="vig"></div>
     ${hud(o.hx ?? 900, o.hy ?? 300, o.hs ?? 200)}
     <div style="position:absolute;left:40px;top:40px;width:${o.w || 900}px">
      ${o.tag ? `<div class="courier" style="display:inline-block;font-weight:700;font-size:28px;letter-spacing:.18em;color:${C.carbon};background:${C.phosphor};padding:6px 14px 4px">${o.tag}</div>` : ""}
      <div class="stencil" style="font-size:${o.size || 132}px;color:${C.paper};margin-top:16px;text-shadow:0 6px 0 rgba(0,0,0,.5)">${b_(o.q)}</div></div>${logo}</div>`,
};
const br = await chromium.launch(); const pg = await br.newPage({ viewport: { width: 1280, height: 720 } });
for (const k of ["A", "B", "C"]) {
  if (!cfg[k]) continue;
  await pg.setContent(page(V[k](cfg[k]), X)); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(150);
  await pg.screenshot({ path: path.join(out, `thumb_${k}.jpg`), type: "jpeg", quality: 92 }); console.log("thumb", k);
}
await br.close();
