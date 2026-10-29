# RELEASED IN FULL — production runbook

One run = one long episode (~10 min, at least 10:00, English) + 4 vertical Shorts cut from it, for one US day, uploaded here (drop branches) and scheduled in Metricool (brand RELEASED IN FULL, blogId 7743507).
Episode 001 (`episodes/001-navy-videos/`) is the reference for structure, pacing and style. Channel bible: Claude Docs «RELEASED IN FULL — библия канала» and Projects doc `claude/released-in-full-bible.md`.

## 0. Rules that never bend
- Facts only from documents/primary sources; witnesses "according to"; theories as theories; never "alien", never "debunked".
- On-screen quotes verbatim; recreated documents labelled RECREATED, no invented redactions or stamps.
- Every b-roll shot carries its honest label (`lab=`): what it really is, where, which year.
- No agency seals/badges in branding. Agencies may be named; documents with seals may be shown in context.
- Independent fact-check by a separate agent before rendering; fix every FIX.
- Made for kids: No. AI disclosure (synthetic voice): Yes.

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
python3 $R/pipeline/shorts.py $EP $EP/shorts
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
- Check getScheduledPosts for the target date first: if a long YouTube video is already scheduled, stop and report.
- Long: 14:00 ET. youtubeData {title, type "video", privacy "public", madeForKids false, category "EDUCATION", isAiGeneratedContent true, tags}; text = youtube_description.txt; media [long.mp4 URL]; videoThumbnailUrl = thumb_A URL (retry once without it if rejected).
- 4 Shorts: 09:30, 12:30, 16:30, 20:30 ET. type "short", title ≤ 90 chars, text = 1–2 lines + "Full file on the channel.", same flags.
- Every Short must be 25–60 s; every b-roll label must be present; Shorts captions burned in.

## 8. Close the run
- Commit to main: episode folder (episode.py, research.md, factcheck.md, rights.json, thumb.json, youtube_description.txt, captions_en.srt), updated backlog.md. Never video files on main.
- Report to the owner in Russian: title, FILE number, publish times (ET + Tashkent), 2-line summary, plannerUrls, thumb_B/C for Test & Compare, anything skipped.
