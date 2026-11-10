# RELEASED IN FULL — production runbook

One run = one long episode (~10 min, at least 10:00, English) + 4 TikTok cuts (62–110 s) + 3 YouTube Shorts (30–45 s), covering a 2-day block D and D+1 (owner decision 2026-11-09: one long video EVERY OTHER DAY), uploaded here (drop branches) and scheduled in Metricool (brand RELEASED IN FULL, blogId 7743507).
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
- 1,650–1,750 words → 10:00–10:45 (default pause 0.55 s between lines). Must stay ≥ 10:00. Graphics: intro, title, chapter, doc, quote, stat, list, timeline, map, annot, geom, end (see pipeline/graphics.mjs).
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
python3 $R/pipeline/shorts.py $EP $EP/shorts --platform youtube   # YouTube Shorts y1–y3, 30–45 s, from META["yshorts"] (owner rule 2026-11-06)
(cd $R/pipeline && NODE_PATH=$(npm root -g) node thumb.mjs $EP/thumb.json $EP)
```
bash $R/pipeline/encode.sh $EP 95       # -> long.mp4 (two-pass x265, overlay burned in, <= 95 MB)

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
- YouTube Shorts y1–y3 (30–45 s, YouTube only): D 12:30, D 20:30, D+1 16:30 ET. type "short", isAiGeneratedContent false, title ≤ 60 chars = question or surprising claim, never a document quote, memo name or a leading year.
- TikTok s1–s4 (62–110 s, TikTok only): D 12:30, D 20:30, D+1 12:30, D+1 20:30 ET. tiktokData {title ≤ 90 chars, privacyOption "PUBLIC_TO_EVERYONE", isAigc false}; text = 1–2 lines with search keywords + 4–5 hashtags.
- Language: narration, titles and descriptions are English. Metricool cannot set the YouTube video language; the channel's upload default must be English (YouTube Studio → Settings → Upload defaults → Advanced → Video language).
- Every vertical cut must be 62–110 s (TikTok Creator Rewards needs > 1 min; shorts.py auto-extends whole lines to ≥ 62 s), captions burned in, b-roll labels present, nothing important below y≈1500 or in the right 130 px (TikTok UI). Pick line ranges that make a complete mini-story (hook → reveal) of ~65–90 s.

## 8. Close the run
- Commit to main: episode folder (episode.py, research.md, factcheck.md, rights.json, thumb.json, youtube_description.txt, captions_en.srt), updated backlog.md. Never video files on main.
- Report to the owner in Russian: title, FILE number, publish times (ET + Tashkent), 2-line summary, plannerUrls, thumb_B/C for Test & Compare, anything skipped.

## Performance rules
Weekly review (Metricool, last 28 days; YouTube rows only up to 2026-11-04 because of analytics lag; 22 TikTok cuts, 19 YouTube items). Each rule is backed by ≥ 3 videos. Never changes cadence, slots, AI-label settings or content rules.
1. TikTok topic: US-vs-Soviet Cold War confrontation stories win. Cuba 1962 + Azorian cuts (n=8) median 319 views; CIA Family Jewels (n=4) 221; Goldsboro (n=4) 162; UAP/UFO cuts (n=6) median 130. When choosing between candidates, prefer a Cold War spy/confrontation story; for UAP topics, cut around a person and a moment, not a report.
2. TikTok opening: start on a scene with a person acting or speaking (a Soviet ship radios "What are you doing here?" 957; Stevenson's yes-or-no question 1103; CIA wiretaps two reporters 278; CIA gives Hunt a wig 259). Openings on a report or a count (144 reports 185, 18 incidents 85, 43 reports 102, the 1973 directive 121) stay low.
3. TikTok length: cuts of 62–72 s (n=13) median 185 views vs 73–95 s (n=9) median 137. Aim for 63–72 s; go longer only when the story needs it.
4. YouTube Shorts titles: a plain intriguing statement ("Two Navy UFO Videos Are Still Unidentified" 35, "The CIA Blacked Out This Page. The Name Underneath: Area 51" 9, "The CIA Destroyed Its MKUltra Files in 1973. Seven Boxes Survived" 6); quote-led or memo-named titles get 0–2.
5. YouTube long: average view duration is 7–46 s (FILE 001 46 s, 002 39 s, 003 7 s) — viewers decide in the first half-minute. The first 30 s must answer the searched question and show the most striking document/footage, no slow logo or setup.

Changelog
- 2026-11-10: section created from the first weekly review (rules 1–5).
