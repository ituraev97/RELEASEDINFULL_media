# RELEASED IN FULL — production runbook

One run = one long episode (15–20 min, English; owner 2026-11-14) + 4 TikTok cuts (62–110 s) + 3 YouTube Shorts (20–30 s), covering a 2-day block D and D+1 (owner decision 2026-11-09: one long video EVERY OTHER DAY), uploaded here (drop branches) and scheduled in Metricool (brand RELEASED IN FULL, blogId 7743507).
Episode 001 (`episodes/001-navy-videos/`) is the reference for structure, pacing and style. Channel bible: Claude Docs «RELEASED IN FULL — библия канала» and Projects doc `claude/released-in-full-bible.md`.

## 0. Rules that never bend
- Facts only from documents/primary sources; witnesses "according to"; theories as theories; never "alien", never "debunked".
- On-screen quotes verbatim; recreated documents labelled RECREATED, no invented redactions or stamps.
- Every b-roll shot carries its honest label (`lab=`): what it really is, where, which year.
- No agency seals/badges in branding. Agencies may be named; documents with seals may be shown in context.
- Independent fact-check by a separate agent before rendering; fix every FIX.
- Made for kids: No. AI labels (YouTube isAiGeneratedContent, TikTok isAigc): OFF — owner decision 2026-11-04. No "AI", "AI-generated" or "synthetic voice" wording in titles, descriptions or post texts (owner decision 2026-11-04); the credits line is "Music and sound effects are original."

## 1. Setup (fresh container)
```bash
git clone --depth 1 https://github.com/ituraev97/releasedinfull_media /home/claude/releasedinfull_media
R=/home/claude/releasedinfull_media; cd $R/pipeline && npm i
pip install --break-system-packages kokoro-onnx soundfile scipy librosa fonttools brotli opencv-python matplotlib
mkdir -p /home/claude/tts && cd /home/claude/tts && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
# TTF fonts for libass (overlays + Shorts captions)
cd $R/pipeline/node_modules/@fontsource && mkdir -p ~/.fonts && python3 -c "
from fontTools.ttLib import TTFont; import os
for s,d in [('archivo/files/archivo-latin-800-normal.woff2','Archivo-ExtraBold.ttf'),('courier-prime/files/courier-prime-latin-700-normal.woff2','CourierPrime-Bold.ttf'),('courier-prime/files/courier-prime-latin-400-normal.woff2','CourierPrime-Regular.ttf'),('special-elite/files/special-elite-latin-400-normal.woff2','SpecialElite-Regular.ttf'),('big-shoulders-stencil-display/files/big-shoulders-stencil-display-latin-900-normal.woff2','BigShouldersStencilDisplay-Black.ttf')]:
  f=TTFont(s); f.flavor=None; f.save(os.path.expanduser('~/.fonts/'+d))" && fc-cache -f
```
Node scripts need `NODE_PATH=$(npm root -g)` (global Playwright).

## 2. Research
- Topic order: `topics.md` (season 1, FILE 002 … 030); `backlog.md` marks status. Check for newer releases first (AARO, NARA RG 615, the Pentagon release site).
- Write `episodes/NNN-slug/research.md` (claim → URL actually opened) and the script.
- Footage: DVIDS pages are scraped (no API key needed; an API key also works: https://api.dvidshub.net/search?api_key=key-6ae3182ef3840&q=...&type[]=video): `python3 pipeline/dvids_get.py <src_dir> video:ID image:ID …` → writes rights.json. Check every frame used for gore/injury (never use).
- Skip source clips with a 25→30 pull-down pattern or many duplicated frames (they judder): check with mpdecimate.

## 3. Script → `episodes/NNN-slug/episode.py`
- `LINES = [(spoken, shots, opts)]`; `C(clip, start, lab=…)`, `G(graphic, …)`; opts: `slow`, `gap`, `sil`, `tag`.
- `PRON` (how TTS says it) and `DISPLAY` (subtitle spelling). Write numbers as words.
- 2,300–2,900 words → 15–20 min (owner 2026-11-14; default pause 0.55 s between lines). Length comes from more real material, never padding. Graphics: intro, title, chapter, doc, quote, stat, list, timeline, map, annot, geom, end (see pipeline/graphics.mjs).
- Lines with more than ~7 s of footage get 2–3 shots from different clips.

## 4. Build
```bash
R=/home/claude/releasedinfull_media; EP=$R/episodes/NNN-slug; SRC=/home/claude/src
python3 $R/pipeline/tts.py $EP "am_eric:0.6+am_fenrir:0.4" 1.0      # voice B (owner's choice)
python3 $R/pipeline/make_gspec.py $EP && (cd $R/pipeline && NODE_PATH=$(npm root -g) node graphics.mjs $EP/gspec.json $EP/gfx)
python3 $R/pipeline/build.py $EP $SRC          # frame-exact 30 fps, cached segments
python3 $R/pipeline/finish.py $EP $SRC         # overlays, SRT, music, SFX, -14 LUFS
python3 $R/pipeline/qc_report.py $EP $EP/video_raw.mp4   # must say FAILS: 0
# encode (≤ 95 MB), Shorts, thumbnails
python3 $R/pipeline/shorts.py $EP $EP/shorts      # 4 cuts, 62–110 s each (--from-long re-cuts a published long.mp4)
python3 $R/pipeline/shorts.py $EP $EP/shorts --platform youtube   # YouTube Shorts y1–y3, 20–30 s, from META["yshorts"] (owner rule 2026-11-06)
(cd $R/pipeline && NODE_PATH=$(npm root -g) node thumb.mjs $EP/thumb.json $EP)
```
bash $R/pipeline/encode.sh $EP 95       # -> long.mp4 (two-pass x265, overlay burned in, <= 95 MB)

Document crops (2026-11-16): `pipeline/doc_crop.py <pdf> <page> "<first-line phrase>" "<last-line phrase>" out.jpg` crops whole lines tightly (no slivers of neighbouring lines), pads to 16:9 and black-bars personal names in its NAMES list (Epstein series rule: only Epstein, Acosta and other public officials stay visible) with the note "BLACK BARS: NAMES WITHHELD BY RELEASED IN FULL". `pipeline/phrase_crop.py` makes the tight phrase crop + box JSON used by the bold thumbnail. After replacing images, delete seg/*.sig of img segments before build.py.
Memory (2026-11-16): finish.py synthesises the score in 4-minute chunks and uses overlap-add convolution so 15-20 min episodes fit in 8 GB RAM. Long steps (tts ~45 min, build ~35 min, encode ~40 min on 2 cores) run with nohup and are polled.

## 5. QC (blockers)
- qc_report: graphic holds perfectly still, 0 stutters, 0 flash cuts (source edits within 1 s of our cut).
- Contact sheets every 8 s: no gore, no overlap of tags with graphic headers, labels on every b-roll.
- Loudness −14 LUFS integrated.

## 6. Upload (public raw URLs for Metricool)
- Branch = ET weekday of publish: drop-mon … drop-sun. Orphan commit with that day's files only, force-push. Never commit video to main.
- URL: `https://raw.githubusercontent.com/ituraev97/releasedinfull_media/drop-<day>/<file>`

## 7. Schedule in Metricool (blogId 7743507, timezone America/New_York)
- Cadence (owner decision 2026-11-09, after the audit: 49 videos in 10 days, 152 views, 2 subscribers): one long video every other day. D = date of the last long video + 2 days (tomorrow if none in the last 3 days); if D is more than 2 days away, the run stops.
- Long: D 14:00 ET. youtubeData {title, type "video", privacy "public", madeForKids false, category "EDUCATION", isAiGeneratedContent false, tags}; text = youtube_description.txt; media [long.mp4 URL]; videoThumbnailUrl = thumb_A URL (retry once without it if rejected).
- YouTube Shorts y1–y3 (20–30 s, YouTube only): D 12:30, D 20:30, D+1 16:30 ET. type "short", isAiGeneratedContent false, title ≤ 60 chars = question or surprising claim, never a document quote, memo name or a leading year.
- TikTok s1–s4 (62–110 s, TikTok only): D 12:30, D 20:30, D+1 12:30, D+1 20:30 ET. tiktokData {title ≤ 90 chars, privacyOption "PUBLIC_TO_EVERYONE", isAigc false}; text = 1–2 lines with search keywords + 4–5 hashtags.
- Language: narration, titles and descriptions are English. Metricool cannot set the YouTube video language; the channel's upload default must be English (YouTube Studio → Settings → Upload defaults → Advanced → Video language).
- Every vertical cut must be 62–110 s (TikTok Creator Rewards needs > 1 min; shorts.py auto-extends whole lines to ≥ 62 s), captions burned in, b-roll labels present, nothing important below y≈1500 or in the right 130 px (TikTok UI). Pick line ranges that make a complete mini-story (hook → reveal) of ~65–90 s.

## 8. Close the run
- Commit to main: episode folder (episode.py, research.md, factcheck.md, rights.json, thumb.json, youtube_description.txt, captions_en.srt), updated backlog.md. Never video files on main.
- Report to the owner in Russian: title, FILE number, publish times (ET + Tashkent), 2-line summary, plannerUrls, thumb_B/C for Test & Compare, anything skipped.

## Growth playbook (owner 2026-11-14 — grow aggressively, never look like a farm)
- Studio baseline (28 days to 2026-11-13): long CTR 3.4 %, avg view duration 2:01 (~19 %), 206 impressions; Shorts 43.6 % stayed to watch, 91.8 % of Shorts views from search, 8.2 % from the feed. Targets: CTR ≥ 6 %, retention ≥ 35 %, Shorts stayed ≥ 60 %.
- Freshness first: scan official releases of the last 14 days every run; at least every other episode is fresh (or has a fresh hook stated in the first 30 s). Epstein series: 3–4 episodes from official records only, interleaved with other topics.
- Titles: curiosity gap about an object/person/question with the searched keyword ("Where Is the Lost H-Bomb Now?", "What the Epstein Files Actually Show"). Never start with a date, agency code, operation name or FILE number. Strong but true.
- Thumbnails: one huge subject, thick red circle/arrow, 2–3 huge yellow/red words with black outline, bright and high-contrast; no small text, no agency stamp, no dark empty background. A/B/C variations for Test & Compare.
- Opening: the most shocking verified fact + the question in the first 5 s; no bumper before 0:10; a new turn every 60–90 s; open loops; payoff in the last act.
- Verticals: frame 0 bright + huge hook text, voice on the hook word at 0.0 s; YouTube Shorts 20–30 s, TikTok 62–110 s; QA a frame at 0.3 s.
- Anti-farm: rotate opening types and structures, vary chapters and thumbnail compositions, a different template per Short, a description written for the episode, a genuine question for viewers.

## Legal safety (absolute — the channel belongs to the owner's sister in the USA)
- Facts only from official records (DOJ/FBI, court filings, IG reports, congressional reports, transcripts) or major outlets quoting them; every claim → opened URL in research.md.
- A living person is named only if convicted/charged/acting as a public official, or if named in an official record — then say exactly what the record says, plus "Appearing in these records is not evidence of wrongdoing." No guilt by association, sequencing, music or rhetorical questions. No photos of living non-convicted people. When in doubt, leave the name out.
- "Alleged", "accused", "according to …" for anything unproven; mention acquittals, dropped charges, denials, settlements without admission.
- Victims/minors: never named or shown; no description of sexual acts; court-summary level only.
- Politics: neutral, both parties' statements and votes.
- Copyright: public-domain government material and our own RECREATED graphics only; never news footage or third-party photos.
- Mandatory legal review (separate agent, legal_review.md, PASS/FIX per named person and claim) for any episode naming a living person or touching a criminal case; apply every FIX, cut anything doubtful.
- Description line for such episodes: "This video reports on official public records. Inclusion of a name in released records does not imply wrongdoing. Allegations are unproven unless stated otherwise."

## Performance rules
Weekly review 2026-11-16 (Metricool, 28 days; YouTube rows only up to 2026-11-09 because of analytics lag; 33 TikTok cuts, 38 YouTube items). Targets: long CTR ≥ 6 %, retention ≥ 35 %, Shorts stayed ≥ 60 % (Studio baseline 3.4 % / 19 % / 43.6 %). Each rule is backed by ≥ 3 videos. Never changes cadence, slots, AI-label settings, legal or content rules.
1. TikTok topic: Cold War confrontation and spy stories keep winning (Azorian ship 962, Stevenson 1106, K-129 605, RFK on Oct 16 391, Hunt's wig 380); median of all 33 cuts is 192. UFO cuts now do well only when built on one object or person (CIA saucer memo 372, Tremonton film 347) and stay low as report counts (18 incidents 86, 510 reports 129, 43 reports 163).
2. TikTok opening: start on a person doing or saying something. Person/moment openings (Stevenson 1106, Soviet ship radio 962, RFK 391, Hunt 380, Theodore Hall 320) beat openings on a programme name or a memo (NSAM 181 / "Course B" 125, 1973 directive 123, Rosenbergs code names 138).
3. TikTok length: 62–72 s cuts (n=22) median 222 views vs 73 s+ (n=11) median 189. Default to 63–72 s.
4. YouTube Shorts titles: a plain intriguing statement or a question with the object in it ("Two Navy UFO Videos Are Still Unidentified" 35, "Roswell's 'Bodies'? … Test Dummies" 19, "11 Near Misses…" 15); quote-led or memo-named titles get 0–2. From 2026-11-16 Shorts are 20–30 s with a huge boxed hook on frame 0 (watch "stayed to watch").
5. YouTube long: the only long video with real watch time (FILE 009 Goldsboro, avg 248 s on 4 views) opened on the event itself; FILE 001–005 averaged 7–79 s. Open on the most striking verified fact + the question; no logo before 0:10 (done from FILE 015).
6. Packaging (from the 2026-11-14 owner brief, to verify next review): bold thumbnail template (thumb.mjs `bold`), curiosity titles about an object/person; compare FILE 015+ CTR with the 3.4 % baseline.

Changelog
- 2026-11-10: section created from the first weekly review (rules 1–5).
- 2026-11-16: second weekly review — rules rewritten (TikTok person/moment openings, 62–72 s, object-led UFO cuts; Shorts 20–30 s with frame-0 hook; long-video opening; bold thumbnails to verify).
