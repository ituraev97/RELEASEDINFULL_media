// RELEASED IN FULL graphics renderer.
// usage: NODE_PATH=$(npm root -g) node graphics.mjs <spec.json> <outdir>
// spec: [{key, name, opts}] -> <outdir>/<key>/f0001.jpg … (intro frames; the last frame is the hold frame)
// RULES: every element animates in with an eased curve, then holds perfectly still. Transforms are composited
// (will-change) so motion is sub-pixel. No zoom/drift after the intro.
import fs from "fs"; import path from "path"; import { createRequire } from "module";
import * as d3 from "d3-geo"; import * as topo from "topojson-client";
import { page, C, NAME, SHORT } from "./brand.css.mjs";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const NM = path.resolve(path.dirname(new URL(import.meta.url).pathname), "node_modules");
const W = 1920, H = 1080, FPS = 30;

const STAGE = `.stage{position:absolute;inset:0;width:${W}px;height:${H}px;overflow:hidden;background:radial-gradient(ellipse at 50% 35%,#1a2129 0%,${C.carbon} 72%)}
[data-d]{will-change:transform,opacity;backface-visibility:hidden}
.k{font-family:Courier;font-weight:700;letter-spacing:.3em;color:${C.phosphor};font-size:24px}
.h{font-family:Archivo;font-weight:800;letter-spacing:.01em;font-size:64px;color:${C.paper};text-transform:uppercase}
.src{font-family:Courier;font-size:23px;letter-spacing:.08em;color:#8a939b}
.doc{position:absolute;box-shadow:0 40px 90px rgba(0,0,0,.65),0 2px 0 rgba(0,0,0,.2)}
.doc .t{font-family:Courier;font-size:30px;line-height:1.55;color:#22201b}
.doc .hl{background:linear-gradient(transparent 12%,rgba(242,208,75,.85) 12%,rgba(242,208,75,.85) 92%,transparent 92%);padding:0 .1em}
.rbar{display:inline-block;background:#0b0b0c;height:.9em;vertical-align:-.12em;transform-origin:left center}
svg text{font-family:Archivo;font-weight:700}`;

const ANIM = `<script>
const clamp=x=>Math.max(0,Math.min(1,x));
const eo=x=>1-Math.pow(1-x,3);                 // ease-out cubic
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2; // ease-in-out cubic
window.setT=function(t){
 document.querySelectorAll('[data-d]').forEach(el=>{
  const d=+el.dataset.d, dur=+(el.dataset.dur||.5), k=el.dataset.k||'fade', r=clamp((t-d)/dur), p=eo(r), base=el.dataset.base||'';
  if(k==='fade'){el.style.opacity=p;el.style.transform=base+' translate3d(0,'+(22*(1-p)).toFixed(3)+'px,0)'}
  else if(k==='left'){el.style.opacity=p;el.style.transform=base+' translate3d('+(-40*(1-p)).toFixed(3)+'px,0,0)'}
  else if(k==='rise'){const q=eio(r);el.style.opacity=Math.min(1,r*3);el.style.transform=base+' translate3d(0,'+(160*(1-q)).toFixed(3)+'px,0)'}
  else if(k==='op'){el.style.opacity=p}
  else if(k==='bar'){el.style.transform=base+' scaleX('+eio(r).toFixed(4)+')'}
  else if(k==='unbar'){el.style.transform=base+' scaleX('+(1-eio(r)).toFixed(4)+')';el.style.transformOrigin='right center'}
  else if(k==='wipe'){el.style.clipPath='inset(0 '+(100-100*eio(r)).toFixed(3)+'% 0 0)'}
  else if(k==='type'){const s=el.dataset.full||(el.dataset.full=el.textContent);el.textContent=s.slice(0,Math.round(s.length*r));el.style.opacity=r>0?1:0}
  else if(k==='stamp'){const q=r<1?1-Math.pow(1-r,4):1;el.style.opacity=r>0?Math.min(1,r*4):0;el.style.transform=base+' scale('+(1.28-0.28*q).toFixed(4)+')'}
  else if(k==='count'){const to=+el.dataset.to;el.textContent=(el.dataset.pre||'')+Math.round(to*eio(r)).toLocaleString('en-US')+(el.dataset.suf||'')}
  else if(k==='draw'){const L=el.getTotalLength();el.style.strokeDasharray=L;el.style.strokeDashoffset=(L*(1-eio(r))).toFixed(2);el.style.opacity=r>0?1:0}
 });
};
</script>`;
const wrap = (body) => page(`<div class="stage grain">${body}</div>${ANIM}`, STAGE);
const A = (d, k = "fade", dur = 0.5, base = "") => `data-d="${d}" data-k="${k}" data-dur="${dur}"${base ? ` data-base="${base}"` : ""}`;
const esc = (s) => String(s);
// inline markup inside doc/quote text: [[x]] = redaction bar of x chars, {{x}} = highlighted, plain otherwise
function rich(s, d0, step = 0.08) {
  let i = 0;
  return esc(s).replace(/\[\[(\d+)\]\]/g, (_, n) => `<span class="rbar" style="width:${n * 0.6}em" data-d="${(d0 + step * i++).toFixed(2)}" data-k="bar" data-dur="0.35"></span>`)
    .replace(/\{\{(.+?)\}\}/g, (_, x) => `<span class="hl">${x}</span>`);
}
const stampEl = (txt, size, d, rot = -6, color = C.stamp) => `<div ${A(d, "stamp", 0.22, `rotate(${rot}deg)`)} style="display:inline-block;filter:url(#ink)">
  <div style="border:${size * .1}px solid ${color};outline:${size * .035}px solid ${color};outline-offset:${size * .07}px;padding:${size * .1}px ${size * .3}px ${size * .02}px;color:${color};font-family:Stencil;font-weight:900;font-size:${size}px;letter-spacing:.05em;line-height:1;white-space:nowrap">${txt}</div></div>`;
const kick = (k, t, d = 0.1) => `<div style="position:absolute;left:120px;top:96px"><div ${A(d)}><span class="k">${k}</span></div><div ${A(d + 0.12)} style="margin-top:12px"><span class="h">${t}</span></div></div>`;
const srcLine = (s, d = 0.9) => s ? `<div ${A(d, "op")} style="position:absolute;left:120px;bottom:120px"><span class="src">${s}</span></div>` : "";

const B = {
  // 4 s channel bumper: paper rises, file number types, redaction bars sweep, stamp slams.
  intro: (o) => `
   <div ${A(0, "rise", 0.75, "rotate(-2deg)")} style="position:absolute;left:520px;top:140px;width:880px;height:800px" >
    <div class="paper doc" style="position:absolute;inset:0">
     <div style="position:absolute;left:70px;top:64px" class="courier"><span ${A(0.65, "type", 0.45)} style="font-size:34px;font-weight:700;letter-spacing:.25em;color:#22201b">FILE ${o.n || "001"}</span></div>
     ${[[0, 560], [1, 420], [2, 610], [3, 300]].map(([i, w]) => `<div style="position:absolute;left:70px;top:${160 + i * 62}px;width:${w}px;height:30px;background:#0b0b0c;transform-origin:left center" ${A(1.05 + i * 0.07, "bar", 0.35)}></div>`).join("")}
    </div></div>
   <div style="position:absolute;left:0;right:0;top:560px;display:flex;justify-content:center">${stampEl(NAME, 92, 1.75, -7)}</div>`,
  title: (o) => `
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
    <div ${A(0.1)}><span class="k" style="font-size:30px">FILE ${o.n}</span></div>
    <div ${A(0.3, "fade", 0.6)} class="stencil" style="font-size:${o.size || 150}px;margin-top:26px;color:${C.paper}">${o.t}</div>
    ${o.sub ? `<div ${A(0.6)} class="typed" style="font-size:44px;margin-top:30px;color:${C.paper};opacity:.85">${o.sub}</div>` : ""}
    <div style="margin-top:46px">${stampEl("RELEASED", 40, 1.0, -4)}</div></div>`,
  chapter: (o) => `
   <div style="position:absolute;left:0;right:0;top:330px;height:420px;background:${C.night}" ${A(0, "op", 0.4)}></div>
   <div style="position:absolute;left:160px;top:390px">
    <div ${A(0.15)}><span class="k">SECTION ${o.n}</span></div>
    <div style="position:relative;margin-top:22px">
     <div ${A(0.3, "fade", 0.5)} class="stencil" style="font-size:170px;color:${C.paper}">${o.t}</div>
     <div style="position:absolute;left:-12px;top:-6px;right:-12px;bottom:-6px;background:#000;transform-origin:right center" ${A(0.25, "unbar", 0.55)}></div>
    </div></div>`,
  // recreated document excerpt. o.lines: array of strings with [[n]] / {{hl}} markup; o.stamp optional
  doc: (o) => {
    const w = o.w || 1180, x = (W - w) / 2;
    return `<div ${A(0, "rise", 0.6, `rotate(${o.rot ?? -1.2}deg)`)} style="position:absolute;left:${x}px;top:${o.top || 110}px;width:${w}px">
     <div class="paper doc" style="padding:70px 84px 80px;position:relative">
      <div class="courier" style="font-size:24px;font-weight:700;letter-spacing:.22em;color:#3a372f">${o.header || ""}</div>
      ${o.title ? `<div class="courier" style="font-size:36px;font-weight:700;margin-top:18px;color:#1d1b17;text-transform:uppercase">${o.title}</div>` : ""}
      <div style="height:2px;background:#3a372f;opacity:.5;margin:26px 0 30px"></div>
      ${o.lines.map((l, i) => `<div class="t" ${A(0.45 + i * 0.16)} style="margin-bottom:14px">${rich(l, 0.75 + i * 0.16)}</div>`).join("")}
      ${o.stamp ? `<div style="position:absolute;right:70px;bottom:46px">${stampEl(o.stamp, 46, 1.25 + o.lines.length * 0.16, -8)}</div>` : ""}
     </div></div>${srcLine(o.source, 1.2)}`;
  },
  quote: (o) => `
   <div style="position:absolute;left:180px;right:180px;top:250px">
    <div ${A(0.05, "op")} class="stencil" style="font-size:200px;color:${C.stamp};line-height:.6;height:90px">“</div>
    <div ${A(0.2, "fade", 0.6)} class="typed" style="font-size:${o.size || 58}px;line-height:1.3;color:${C.paper}">${rich(o.q, 0.8)}</div>
    <div ${A(0.7)} style="margin-top:44px;display:flex;gap:22px;align-items:baseline">
     <span class="sans" style="font-weight:800;font-size:34px;color:${C.paper};text-transform:uppercase">${o.who}</span>
     <span class="courier" style="font-size:26px;color:${C.graphite}">${o.role || ""}</span></div>
   </div>${srcLine(o.source)}`,
  stat: (o) => `
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
    ${o.k ? `<div ${A(0.05)}><span class="k">${o.k}</span></div>` : ""}
    <div ${A(0.15, "fade", 0.6)} class="stencil" style="font-size:${o.size || 300}px;color:${C.paper};margin-top:16px">${o.to != null ? `<span data-d="0.15" data-k="count" data-dur="1.1" data-to="${o.to}" data-pre="${o.pre || ""}" data-suf="${o.suf || ""}">${o.a}</span>` : o.a}</div>
    <div ${A(0.55)} class="sans" style="font-weight:800;font-size:46px;letter-spacing:.06em;margin-top:22px;color:${C.paper};text-transform:uppercase;max-width:1400px">${o.b}</div>
    ${o.c ? `<div ${A(0.8)} class="courier" style="font-size:28px;margin-top:24px;color:${C.graphite}">${o.c}</div>` : ""}
   </div>${srcLine(o.source, 1.1)}`,
  list: (o) => `${kick(o.kicker, o.title)}
   <div style="position:absolute;left:120px;top:330px;right:120px">
    ${o.items.map((it, i) => `<div ${A(0.4 + i * 0.22, "left")} style="display:flex;gap:28px;align-items:baseline;margin-bottom:34px">
      <span class="courier" style="font-weight:700;font-size:30px;color:${C.phosphor};min-width:70px">${it.n || String(i + 1).padStart(2, "0")}</span>
      <span class="sans" style="font-weight:700;font-size:46px;color:${C.paper}">${it.t}</span>
      ${it.s ? `<span class="courier" style="font-size:26px;color:${C.graphite}">${it.s}</span>` : ""}</div>`).join("")}
   </div>${srcLine(o.source, 0.6 + o.items.length * 0.22)}`,
  timeline: (o) => {
    const n = o.events.length, x0 = 170, x1 = W - 170, y = 600;
    return `${kick(o.kicker, o.title)}
    <svg width="${W}" height="${H}" style="position:absolute;inset:0"><line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="${C.graphite}" stroke-width="4" data-d="0.3" data-k="draw" data-dur="${0.4 + n * 0.18}"/></svg>
    ${o.events.map((e, i) => {
      const x = x0 + (x1 - x0) * (n === 1 ? 0.5 : i / (n - 1)), up = i % 2 === 0, act = o.active == null || o.active === i, d = 0.45 + i * 0.18;
      return `<div ${A(d, "op", 0.3)} style="position:absolute;left:${x - 13}px;top:${y - 13}px;width:26px;height:26px;border-radius:50%;background:${act ? C.phosphor : C.graphite};box-shadow:${act ? `0 0 24px ${C.phosphor}` : "none"}"></div>
       <div ${A(d + 0.08)} style="position:absolute;left:${x - 160}px;width:320px;text-align:center;top:${up ? y - 190 : y + 46}px">
        <div class="courier" style="font-weight:700;font-size:34px;color:${act ? C.phosphor : C.graphite}">${e.y}</div>
        <div class="sans" style="font-weight:700;font-size:30px;line-height:1.2;margin-top:8px;color:${act ? C.paper : C.graphite}">${e.t}</div></div>`;
    }).join("")}${srcLine(o.source, 0.8 + n * 0.18)}`;
  },
  // still image (e.g. a frame of the released video) with callouts that point at screen regions
  annot: (o) => `${o.kicker ? kick(o.kicker, o.title) : ""}
   <div ${A(0, "op", 0.4)} style="position:absolute;left:${o.x ?? 360}px;top:${o.y ?? 250}px;width:${o.w ?? 1200}px;height:${(o.w ?? 1200) * (o.ar ?? 0.5625)}px;background:url('data:image/jpeg;base64,${fs.readFileSync(o.img).toString("base64")}') center/cover;outline:2px solid ${C.graphite}"></div>
   ${(o.marks || []).map((m, i) => `<div ${A(0.6 + i * 0.35, "op", 0.3)} style="position:absolute;left:${m.x}px;top:${m.y}px;width:${m.w}px;height:${m.h}px;border:4px solid ${C.phosphor};box-shadow:0 0 18px ${C.phosphor}"></div>
     <div ${A(0.7 + i * 0.35)} style="position:absolute;left:${m.lx}px;top:${m.ly}px;max-width:${m.lw || 420}px;background:${C.carbon};border-left:6px solid ${C.phosphor};padding:12px 18px">
      <div class="courier" style="font-weight:700;font-size:24px;color:${C.phosphor};letter-spacing:.12em">${m.k}</div>
      <div class="sans" style="font-weight:700;font-size:30px;color:${C.paper};margin-top:4px">${m.t}</div></div>`).join("")}
   ${srcLine(o.source, 0.8)}`,
  map: (o) => {
    const world = JSON.parse(fs.readFileSync(`${NM}/world-atlas/countries-50m.json`));
    const feats = topo.feature(world, world.objects.countries).features;
    const proj = d3.geoMercator().fitExtent([[120, 230], [W - 120, H - 140]], { type: "MultiPoint", coordinates: o.bounds });
    const g = d3.geoPath(proj);
    let s = `<svg width="${W}" height="${H}" style="position:absolute;inset:0"><defs><filter id="glow"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="#1f2a33" stroke-width="1"/></pattern></defs>
      <rect width="${W}" height="${H}" fill="url(#grid)" opacity=".7"/>`;
    for (const f of feats) s += `<path d="${g(f)}" fill="${(o.hl || []).includes(+f.id) ? "#22313d" : "#161c22"}" stroke="#34404b" stroke-width="1.2"/>`;
    for (const [i, a] of (o.areas || []).entries()) { const p = proj(a.ll); s += `<circle cx="${p[0]}" cy="${p[1]}" r="${a.r || 60}" fill="${C.stamp}" fill-opacity=".18" stroke="${C.stamp}" stroke-width="3" stroke-dasharray="10 8" data-d="${0.4 + i * .2}" data-k="op" data-dur=".5"/>`; }
    for (const [i, c] of (o.points || []).entries()) {
      const p = proj(c.ll), ax = c.anchor || "start", dx = ax === "end" ? -24 : 24, d = 0.5 + i * 0.25;
      s += `<g data-d="${d}" data-k="op" data-dur=".35"><circle cx="${p[0]}" cy="${p[1]}" r="11" fill="${c.color || C.phosphor}" filter="url(#glow)"/>
        <text x="${p[0] + dx}" y="${p[1] + 12}" text-anchor="${ax}" font-size="${c.size || 38}" fill="${C.paper}">${c.name}</text>
        ${c.sub ? `<text x="${p[0] + dx}" y="${p[1] + 50}" text-anchor="${ax}" font-size="24" fill="${C.graphite}" style="font-family:Courier;letter-spacing:.14em">${c.sub}</text>` : ""}</g>`;
    }
    for (const l of o.labels || []) { const p = proj(l.ll); s += `<text x="${p[0]}" y="${p[1]}" text-anchor="middle" font-size="${l.size || 28}" fill="${C.graphite}" style="letter-spacing:.3em" data-d="0.3" data-k="op">${l.t}</text>`; }
    return `${s}</svg>${kick(o.kicker, o.title)}${srcLine(o.source, 1.2)}`;
  },
  // GOFAST geometry: jet altitude + camera angle + range -> object altitude (values as read from the frame at 0:14)
  geom: (o) => {
    const x0 = 330, sea = 900, top = 300, sx = 1340 / 50000, sy = (sea - top) / 25000;
    const jx = x0, jy = sea - 25000 * sy, dh = 23280, dv = 11860;
    const ox = jx + dh * sx, oy = jy + dv * sy, ex = jx + (dh * 25000 / dv) * sx;
    const R = !!o.reveal, d0 = R ? 0 : 0.3;
    return `${kick("GOFAST · THE GEOMETRY", R ? "Where the object really was" : "Three numbers, one triangle")}
    <svg width="${W}" height="${H}" style="position:absolute;inset:0">
     <defs><linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b3346"/><stop offset="1" stop-color="#0d1a24"/></linearGradient>
      <filter id="g2"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
     <rect x="0" y="${sea}" width="${W}" height="${H - sea}" fill="url(#sea)"/>
     <line x1="0" y1="${sea}" x2="${W}" y2="${sea}" stroke="#3d6178" stroke-width="3"/>
     <text x="${W - 120}" y="${sea + 50}" text-anchor="end" font-size="26" fill="#6f8ea3" style="font-family:Courier;letter-spacing:.2em">SEA LEVEL</text>
     <line x1="${jx}" y1="${jy}" x2="${jx}" y2="${sea}" stroke="${C.graphite}" stroke-width="3" stroke-dasharray="10 10" data-d="${d0}" data-k="draw" data-dur="0.6"/>
     <g data-d="${d0 + 0.2}" data-k="op" data-dur="0.4"><text x="${jx - 24}" y="${(jy + sea) / 2}" text-anchor="end" font-size="40" fill="${C.paper}">25,000 FT</text>
      <text x="${jx - 24}" y="${(jy + sea) / 2 + 36}" text-anchor="end" font-size="24" fill="${C.graphite}" style="font-family:Courier">JET ALTITUDE</text></g>
     <g transform="translate(${jx},${jy})" data-d="${d0}" data-k="op" data-dur="0.4"><path d="M-46,0 L34,-6 L46,0 L34,6 Z M-10,0 L-30,-26 L-18,-26 L8,0 Z M-10,0 L-30,26 L-18,26 L8,0 Z M-40,0 L-50,-14 L-44,-14 L-32,0 Z" fill="${C.paper}"/></g>
     <line x1="${jx}" y1="${jy}" x2="${ex}" y2="${sea}" stroke="${C.graphite}" stroke-width="2" stroke-dasharray="4 10" opacity="${R ? 0.55 : 0}"/>
     <line x1="${jx}" y1="${jy}" x2="${ox}" y2="${oy}" stroke="${C.phosphor}" stroke-width="5" filter="url(#g2)" data-d="${d0 + 0.5}" data-k="draw" data-dur="0.9"/>
     <g data-d="${d0 + 1.1}" data-k="op" data-dur="0.4"><text x="${(jx + ox) / 2 + 30}" y="${(jy + oy) / 2 - 22}" font-size="38" fill="${C.phosphor}" transform="rotate(${Math.atan2(oy - jy, ox - jx) * 180 / Math.PI} ${(jx + ox) / 2 + 30} ${(jy + oy) / 2 - 22})">RANGE 4.3 NMI</text></g>
     <g data-d="${d0 + 1.3}" data-k="op" data-dur="0.4"><path d="M${jx + 120},${jy} A120,120 0 0,1 ${jx + 120 * Math.cos(Math.atan2(oy - jy, ox - jx))},${jy + 120 * Math.sin(Math.atan2(oy - jy, ox - jx))}" fill="none" stroke="${C.paper}" stroke-width="3"/>
      <line x1="${jx}" y1="${jy}" x2="${jx + 220}" y2="${jy}" stroke="${C.paper}" stroke-width="2" stroke-dasharray="6 6"/>
      <text x="${jx + 140}" y="${jy - 18}" font-size="34" fill="${C.paper}">−27° CAMERA ANGLE</text></g>
     ${R ? `<g data-d="0.5" data-k="op" data-dur="0.4"><circle cx="${ox}" cy="${oy}" r="16" fill="${C.highlight}" filter="url(#g2)"/></g>
     <line x1="${ox}" y1="${oy + 20}" x2="${ox}" y2="${sea}" stroke="${C.highlight}" stroke-width="3" stroke-dasharray="10 8" data-d="0.8" data-k="draw" data-dur="0.6"/>
     <g data-d="1.2" data-k="op" data-dur="0.4"><text x="${ox + 34}" y="${(oy + sea) / 2}" font-size="52" fill="${C.highlight}" style="font-family:Archivo;font-weight:800">≈ 13,000 FT</text>
      <text x="${ox + 34}" y="${(oy + sea) / 2 + 40}" font-size="26" fill="${C.paper}" style="font-family:Courier">OBJECT ALTITUDE · NOT NEAR THE WATER</text></g>
     <g data-d="1.6" data-k="op" data-dur="0.4"><text x="${ex}" y="${sea - 18}" text-anchor="middle" font-size="24" fill="${C.graphite}" style="font-family:Courier">WHERE IT "LOOKS" TO BE</text></g>` : ""}
    </svg>${srcLine(R ? "SOURCES: NASA UAP STUDY 2023; AARO GOFAST RESOLUTION 2025 · ILLUSTRATION, NOT TO SCALE" : "VALUES READ FROM THE GOFAST DISPLAY · ILLUSTRATION, NOT TO SCALE", 1.4)}`;
  },
  // altitude bands (o.bands: [{lo, hi, t, s, hl}]), feet; o.max default 70000; o.glint draws a sunlit dot at the top band
  alt: (o) => {
    const max = o.max || 70000, y0 = 890, y1 = 330, X0 = 360, X1 = W - 160, Y = (f) => y0 - (y0 - y1) * f / max;
    let s = `<svg width="${W}" height="${H}" style="position:absolute;inset:0"><defs><filter id="g3"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0f141a"/><stop offset="1" stop-color="#1c2731"/></linearGradient></defs>
      <rect x="${X0}" y="${y1}" width="${X1 - X0}" height="${y0 - y1}" fill="url(#sky)"/>
      <line x1="${X0}" y1="${y0}" x2="${X1}" y2="${y0}" stroke="${C.graphite}" stroke-width="4"/>`;
    for (let f = 0; f <= max; f += 10000) s += `<line x1="${X0 - 14}" y1="${Y(f)}" x2="${X0}" y2="${Y(f)}" stroke="${C.graphite}" stroke-width="2"/><text x="${X0 - 26}" y="${Y(f) + 10}" text-anchor="end" font-size="28" fill="${C.graphite}" style="font-family:Courier">${f ? (f / 1000) + ",000" : "0"}</text>`;
    s += `<text x="${X0 - 26}" y="${y1 - 30}" text-anchor="end" font-size="24" fill="${C.graphite}" style="font-family:Courier;letter-spacing:.2em">FEET</text>`;
    for (const [i, b] of o.bands.entries()) {
      const d = 0.4 + i * 0.35, col = b.hl ? C.highlight : C.stamp;
      s += `<g data-d="${d}" data-k="op" data-dur=".4"><rect x="${X0 + 4}" y="${Y(b.hi)}" width="${X1 - X0 - 8}" height="${Math.max(6, Y(b.lo) - Y(b.hi))}" fill="${col}" fill-opacity="${b.hl ? .22 : .2}" stroke="${col}" stroke-width="2" stroke-dasharray="${b.hl ? "0" : "10 8"}"/>
        <text x="${X0 + 40}" y="${(Y(b.hi) + Y(b.lo)) / 2 + 14}" font-size="40" fill="${C.paper}" style="font-family:Archivo;font-weight:800">${b.t}</text>
        ${b.s ? `<text x="${X1 - 40}" y="${(Y(b.hi) + Y(b.lo)) / 2 + 10}" text-anchor="end" font-size="28" fill="${C.paper}" style="font-family:Courier">${b.s}</text>` : ""}</g>`;
    }
    if (o.glint) { const gy = Y(o.glint), gx = X1 - 420, d = 0.6 + o.bands.length * 0.35;
      s += `<g data-d="${d}" data-k="op" data-dur=".5"><circle cx="${gx}" cy="${gy}" r="14" fill="${C.highlight}" filter="url(#g3)"/><circle cx="${gx}" cy="${gy}" r="34" fill="none" stroke="${C.highlight}" stroke-width="2" opacity=".5"/></g>`; }
    return `${s}</svg>${kick(o.kicker, o.title)}${srcLine(o.source, 0.8 + o.bands.length * 0.35)}`;
  },
  end: (o) => `
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
    <div ${A(0.1)}><span class="k">FILE ${o.n} · CLOSED</span></div>
    <div style="margin-top:40px">${stampEl(NAME, 110, 0.5, -5)}</div>
    <div ${A(1.0)} class="typed" style="font-size:44px;margin-top:64px;color:${C.paper}">${o.next ? `Next file: ${o.next}` : "Every secret has a release date."}</div>
    <div ${A(1.2)} class="courier" style="font-size:24px;margin-top:22px;color:${C.graphite};letter-spacing:.1em">INDEPENDENT CHANNEL · NOT AFFILIATED WITH ANY GOVERNMENT AGENCY</div></div>`,
};

// intro length = when the last element finishes animating (+ small settle)
async function introLen(pg) {
  return await pg.evaluate(() => { let m = 0; document.querySelectorAll('[data-d]').forEach(el => { m = Math.max(m, +el.dataset.d + +(el.dataset.dur || .5)); }); return m; });
}
const spec = JSON.parse(fs.readFileSync(process.argv[2])); const out = process.argv[3];
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: W, height: H } });
for (const g of spec) {
  const dir = path.join(out, g.key);
  if (fs.existsSync(path.join(dir, "done"))) { console.log("skip", g.key); continue; }
  fs.mkdirSync(dir, { recursive: true });
  await pg.setContent(wrap(B[g.name](g.opts || {})), { waitUntil: "load" });
  await pg.evaluate(() => document.fonts.ready);
  const L = g.name === "intro" ? 4.0 : (await introLen(pg)) + 0.15;
  const n = Math.ceil(L * FPS);
  for (let i = 0; i < n; i++) {
    await pg.evaluate((t) => window.setT(t), i / FPS);
    await pg.screenshot({ path: path.join(dir, `f${String(i + 1).padStart(4, "0")}.jpg`), type: "jpeg", quality: 93 });
  }
  fs.writeFileSync(path.join(dir, "done"), String(n));
  console.log(g.key, n, "frames");
}
await b.close();
