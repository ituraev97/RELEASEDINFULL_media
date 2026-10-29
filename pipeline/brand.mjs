// Renders static brand assets. usage: NODE_PATH=$(npm root -g) node brand.mjs <outdir>
import fs from "fs"; import path from "path"; import { createRequire } from "module";
import { page, NAME, SHORT, C } from "./brand.css.mjs";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const out = path.resolve(process.argv[2] || "../brand"); fs.mkdirSync(out, { recursive: true });
const words = NAME.split(" ");
const line1 = words.slice(0, Math.ceil(words.length / 2)).join(" "), line2 = words.slice(Math.ceil(words.length / 2)).join(" ");
export const SLOGAN = process.env.RIF_SLOGAN || "Every secret has a release date.";

// The logo: a rubber stamp. Two lines, double border, slight tilt, ink texture.
const stamp = (size, color = C.stamp, rot = -4) => `
<div style="display:inline-block;transform:rotate(${rot}deg);filter:url(#ink)">
 <div style="border:${size * .085}px solid ${color};outline:${size * .03}px solid ${color};outline-offset:${size * .06}px;padding:${size * .1}px ${size * .28}px ${size * .04}px;color:${color};text-align:center">
  <div class="stencil" style="font-size:${size}px;font-weight:900;letter-spacing:.04em;white-space:nowrap">${line1}</div>
  <div style="display:flex;align-items:center;gap:${size * .14}px;justify-content:center;margin-top:${size * .02}px">
   <div style="height:${size * .07}px;flex:1;background:${color}"></div>
   <div class="stencil" style="font-size:${size}px;font-weight:900;letter-spacing:.04em;white-space:nowrap">${line2}</div>
   <div style="height:${size * .07}px;flex:1;background:${color}"></div>
  </div>
 </div></div>`;

const jobs = {
  logo_stamp_blue: [1600, 640, `<div style="width:1600px;height:640px;display:flex;align-items:center;justify-content:center">${stamp(170)}</div>`, true],
  logo_stamp_paper: [1600, 640, `<div style="width:1600px;height:640px;display:flex;align-items:center;justify-content:center">${stamp(170, C.paper)}</div>`, true],
  avatar_800: [800, 800, `
   <div style="width:800px;height:800px;background:${C.carbon};position:relative;overflow:hidden" class="grain">
    <div class="paper" style="position:absolute;left:100px;top:100px;width:600px;height:600px;transform:rotate(-4deg);box-shadow:0 24px 50px rgba(0,0,0,.6)">
     <div style="position:absolute;left:60px;top:62px;width:300px;height:30px;background:#0b0b0c"></div>
     <div style="position:absolute;left:60px;top:108px;width:190px;height:30px;background:#0b0b0c"></div>
     <div style="position:absolute;right:60px;bottom:62px;width:260px;height:30px;background:#0b0b0c"></div>
     <div style="position:absolute;left:0;right:0;top:190px;display:flex;justify-content:center">
      <div style="filter:url(#ink);border:16px solid ${C.stamp};outline:6px solid ${C.stamp};outline-offset:10px;padding:6px 26px 0;transform:rotate(-6deg)">
       <div class="stencil" style="font-size:215px;color:${C.stamp};letter-spacing:.05em">${SHORT}</div></div></div>
    </div></div>`],
  watermark_150: [150, 150, `<div style="width:150px;height:150px;display:flex;align-items:center;justify-content:center;transform:rotate(-6deg)">
     <div style="border:9px solid ${C.paper};outline:3px solid ${C.paper};outline-offset:5px;padding:4px 10px 0"><div class="stencil" style="font-size:62px;color:${C.paper};letter-spacing:.05em">${SHORT}</div></div></div>`, true],
  banner_2560: [2560, 1440, `
   <div style="width:2560px;height:1440px;background:${C.carbon};position:relative;overflow:hidden" class="grain">
    <div style="position:absolute;left:0;right:0;top:508px;height:424px;background:${C.night}"></div>
    ${[[-40, 470, 900], [1700, 520, 1000], [-60, 890, 760], [1880, 860, 800]].map(([x, y, w]) => `<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:40px;background:#000;opacity:.85"></div>`).join("")}
    <div style="position:absolute;left:507px;top:508px;width:1546px;height:423px;display:flex;align-items:center;justify-content:space-between;padding:0 70px 0 30px;gap:20px">
     <div style="width:600px;height:300px;flex:none;position:relative"><div style="position:absolute;left:0;top:50%;transform:translateY(-50%) scale(.52);transform-origin:left center">${stamp(150)}</div></div>
     <div style="text-align:right">
      <div class="typed" style="font-size:46px;color:${C.paper};white-space:nowrap">${SLOGAN}</div>
      <div class="courier" style="font-size:28px;font-weight:700;letter-spacing:.16em;color:${C.phosphor};margin-top:22px;white-space:nowrap">NEW FILES MON · WED · FRI · SUN · 2 PM ET</div>
      <div class="courier" style="font-size:21px;letter-spacing:.08em;color:${C.graphite};margin-top:14px;white-space:nowrap">INDEPENDENT CHANNEL · NOT AFFILIATED WITH ANY GOVERNMENT AGENCY</div>
     </div></div>
   </div>`],
};
const b = await chromium.launch();
for (const [name, [w, h, body, transparent]] of Object.entries(jobs)) {
  const pg = await b.newPage({ viewport: { width: w, height: h } });
  await pg.setContent(page(body, transparent ? "body{background:transparent}" : ""));
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(300);
  await pg.screenshot({ path: `${out}/${name}.png`, omitBackground: !!transparent });
  await pg.close(); console.log(name);
}
await b.close();
