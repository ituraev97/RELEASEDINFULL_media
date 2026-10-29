// Shared brand tokens + CSS for RELEASED IN FULL (working name). Imported by brand, graphics and thumbnail renderers.
import path from "path"; import fs from "fs";
const NM = path.resolve(path.dirname(new URL(import.meta.url).pathname), "node_modules/@fontsource");
export const NAME = process.env.RIF_NAME || "RELEASED IN FULL";
export const SHORT = process.env.RIF_SHORT || "RIF";
export const C = { carbon: "#0D0F12", paper: "#E8E0CA", stamp: "#2747C4", phosphor: "#8CF5B0", graphite: "#5B636B", highlight: "#F2D04B", night: "#141A21" };
const F = (p) => `url(data:font/woff2;base64,${fs.readFileSync(`${NM}/${p}`).toString("base64")})`;
export const FONTS = `
@font-face{font-family:Stencil;font-weight:700;src:${F("big-shoulders-stencil-display/files/big-shoulders-stencil-display-latin-700-normal.woff2")}}
@font-face{font-family:Stencil;font-weight:800;src:${F("big-shoulders-stencil-display/files/big-shoulders-stencil-display-latin-800-normal.woff2")}}
@font-face{font-family:Stencil;font-weight:900;src:${F("big-shoulders-stencil-display/files/big-shoulders-stencil-display-latin-900-normal.woff2")}}
@font-face{font-family:Typed;src:${F("special-elite/files/special-elite-latin-400-normal.woff2")}}
@font-face{font-family:Courier;font-weight:400;src:${F("courier-prime/files/courier-prime-latin-400-normal.woff2")}}
@font-face{font-family:Courier;font-weight:700;src:${F("courier-prime/files/courier-prime-latin-700-normal.woff2")}}
@font-face{font-family:Archivo;font-weight:500;src:${F("archivo/files/archivo-latin-500-normal.woff2")}}
@font-face{font-family:Archivo;font-weight:700;src:${F("archivo/files/archivo-latin-700-normal.woff2")}}
@font-face{font-family:Archivo;font-weight:800;src:${F("archivo/files/archivo-latin-800-normal.woff2")}}`;

// Paper + ink textures (SVG filters, deterministic seeds)
export const DEFS = `<svg width="0" height="0" style="position:absolute"><defs>
 <filter id="ink" x="-10%" y="-10%" width="120%" height="120%">
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3" result="d"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="4" seed="3" result="m"/>
  <feColorMatrix in="m" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -3.2 2.75" result="mask"/>
  <feComposite in="d" in2="mask" operator="in"/>
 </filter>
 <filter id="paperf"><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="3" seed="11"/>
  <feColorMatrix values="0 0 0 0 .35  0 0 0 0 .30  0 0 0 0 .22  0 0 0 .22 0"/></filter>
</defs></svg>`;

export const CSS = `${FONTS}
:root{--carbon:${C.carbon};--paper:${C.paper};--stamp:${C.stamp};--phos:${C.phosphor};--graph:${C.graphite};--hl:${C.highlight};--night:${C.night}}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--carbon);color:var(--paper)}
.stencil{font-family:Stencil;font-weight:900;letter-spacing:.01em;line-height:.88;text-transform:uppercase}
.typed{font-family:Typed}
.courier{font-family:Courier}
.sans{font-family:Archivo}
.paper{background:var(--paper);color:#1d1b17;position:relative;overflow:hidden}
.paper::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%,rgba(255,255,255,.35),rgba(0,0,0,0) 60%),radial-gradient(ellipse at 90% 100%,rgba(120,90,40,.22),rgba(0,0,0,0) 55%)}
.paper::after{content:"";position:absolute;inset:0;pointer-events:none;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' seed='4'/><feColorMatrix values='0 0 0 0 .3  0 0 0 0 .26  0 0 0 0 .18  0 0 0 .28 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.redact{display:inline-block;background:#0b0b0c;height:.86em;vertical-align:-.08em;border-radius:1px}
.stampbox{display:inline-block;color:var(--stamp);border:.09em solid var(--stamp);outline:.035em solid var(--stamp);outline-offset:.07em;padding:.08em .32em .02em;font-family:Stencil;font-weight:800;letter-spacing:.06em;line-height:1;filter:url(#ink);mix-blend-mode:multiply}
.grain::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' seed='2'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.5 -.3'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
`;
export const page = (body, extra = "") => `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}${extra}</style></head><body>${DEFS}${body}</body></html>`;
