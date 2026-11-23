# RELEASED IN FULL — production runbook

Run notes go to RUNBOOK_NOTES.md (append there, never here). Promote a note into a rule section only if it must apply to every future run.

One LONG run = one long episode (15–20 min, English; owner 2026-11-14) + 4 TikTok cuts (62–110 s) + 4 YouTube Short candidates (20–30 s; only the best, ≤ 2 per day, go on YouTube — see the Shorts section), covering a 2-day block D and D+1 (one long video every 2 days — see "Long-video cadence" below; every other run is an OFF run), uploaded here (drop branches) and scheduled in Metricool (brand RELEASED IN FULL, blogId 7743507).
Episode 001 (`episodes/001-navy-videos/`) is the reference for structure, pacing and style. Channel bible: Claude Docs «RELEASED IN FULL — библия канала» and Projects doc `claude/released-in-full-bible.md`.

## Long-video cadence — owner decision 2026-11-23 (overrides every 'one long per run/day' line)
- One long video every 2 days. The daily run is either a LONG run or an OFF run.
- FIRST step of every run, before setup or research: Metricool `getScheduledPosts` for this brand (blogId 7743507, timezone America/New_York) covering today … today+2 (ET). Target day D = tomorrow (ET).
- OFF run: if D already has its YouTube Shorts scheduled AND today or D (the previous or the target ET day) already has a long video → do nothing else (no clone, no setup, no research); report one line to the owner, e.g. "OFF run: long on <date>, Shorts for <date> already scheduled."
- LONG run otherwise: publish the long video on D 14:00 ET AND schedule the Shorts for the 2-day block D and D+1 (max 2 YouTube Shorts per day, slots and scorecard from the Shorts section below). Cut 4 YouTube Short candidates (y1–y4) so at least 3 pass the ≥ 7/10 scorecard; a 4th passing candidate may take D+1 22:30 ET (≥ 6 h after D+1 16:30, different template). TikTok s1–s4 slots unchanged.

## Shorts: cadence + hook rules — owner decision 2026-11-23 (OVERRIDES any other YouTube Shorts count/slot in this file)
Evidence (Metricool, 2026-10-23 → 11-22): 46 YouTube Shorts here got a median of 3 views (max 35) with a median average view duration of 3 s; the same topics as 47 TikTok cuts got a median of 204 (max 1106). Across 10 channels (546 Shorts), template clones posted 3–6 times a day decayed week over week (COLD WARRANT median 633 → 107), while Shorts opening with a hard number, a famous name or a "Why…?" paradox won by 5–50x.
- **Cadence: at most 2 YouTube Shorts per day of the block (D and D+1), never more.** The run still cuts its candidates y1–y4 (`shorts.py --platform youtube`), scores each with the scorecard below, and schedules only the best ones on YouTube: D 12:30 + D 20:30, D+1 16:30 ET (at least 1 per day, ≤ 2 per day). Two Shorts on the same day are ≥ 6 h apart and use different visual templates. D is a long-video day, so the D 20:30 Short is a trailer for the long (last line "Full story on the channel."). A candidate that is not used on YouTube may be extended into one of the TikTok cuts; **TikTok stays exactly 4 cuts per block (s1–s4, slots unchanged).**
- **Scorecard — a Short goes on YouTube only if it scores ≥ 7/10:** Hook 0–4 (the first second has a hard number, a famous name/brand or a paradox question, on screen AND spoken); Payoff 0–3 (the hook's promise is paid in the last 2–3 s: a reveal, a number, a twist); Freshness 0–2 (new story/angle, not the same template as yesterday's Short); Clarity 0–1 (understandable with sound off). Below 7 → rewrite the hook/line range and re-cut (`--only yN`); write each Short's score in the owner report.
- **Hook rules:** second 0 = the most surprising sentence — no logo, no title card, no "In 1962…" slow start; on-screen hook ≤ 7 words, large, centred in the upper third. Titles ≤ 60 chars + #shorts, formulas that won: [number] + [stakes] ("638 Gang Arrests in 179 Cities…"), [famous name] + [unexpected fact] ("The Wolf of Wall Street Still Owes…"), "Why/How did…?" + paradox ("How Did a Japanese Destroyer Lead U.S. Bombers to Its Own Carriers?").
- **Banned openers/titles:** quizzes ("Name this X in 3 seconds"), plain recaps of old cases with no number or famous name, "Here's what happened…", "Did you know…".
- **Length 20–40 s, hard cap 50 s** (this channel keeps its 20–30 s rule — `shorts.py` enforces it). End on the payoff and cut; no outro card longer than 1 s; a loopable last line is a plus.
- **Template rotation:** at least 3 visual templates (footage-led, document/number-led, map/timeline-led); never the same one two days running.
- **Watch-time check:** a Short with average view duration < 5 s after 48 h = that hook style is dead; do not repeat it.
- **Weekly review every Monday:** read the last 7 days of YouTube Shorts analytics in Metricool (views + avg view duration), list top 3 / bottom 3, and add one line "what won" to "Performance rules" — repeat the winners' hook pattern, drop the losers'.

## Real footage via relay — owner decision 2026-11-23
The cloud sandbox cannot reach youtube.com. A relay on the owner's server downloads clips from YouTube (or any yt-dlp URL: archive.org, C-SPAN, …) and hands them over through Google Drive folder "FOOTAGE RELAY". Client: `tools/footage_client.py` (stdlib only).
- Drive credentials: from Projects doc `claude/google-drive-oauth.md` → write `/tmp/drive_creds.json` (keys client_id, client_secret, refresh_token). Never into git, never into the repo folder.
- Find candidate videos with the YouTube Data API (yt_research.py / the API key the tasks use); pick exact moments by title, description, chapters or transcript.
- `clips.json` = `[{"name","src":"<youtube id or URL>","start":"M:SS","end":"M:SS"}]`, ≤ 40 clips, ≤ 90 s each. `name` = the clip name used in `C(name, …)`.
- Send the request EARLY (right after the topic is chosen), keep working on script/TTS/graphics, then collect:
  `python3 $R/tools/footage_client.py request <RUN> clips.json --creds /tmp/drive_creds.json`
  `python3 $R/tools/footage_client.py wait <RUN> $SRC --creds /tmp/drive_creds.json --timeout 1800` (clips land as `$SRC/<name>.mp4`; `<RUN>` = e.g. `rif-NNN-YYYYMMDD`).
  No answer within 30 min → continue without real footage (DVIDS/archive.org/graphics) and note it in the owner report.
- Priority 1 = public-domain government video: congressional hearings (C-SPAN, House/Senate committee channels), official agency releases (CIA/FBI/NARA/DoD/NASA), archival government films and newsreels (archive.org can also be downloaded directly). Priority 2 = news reports about the exact case: short excerpts used for commentary (fair use). Never movies/TV dramas, other YouTubers, private people's faces, gore.
- Real footage 30–50 % of the runtime; at most ~12 s of one external clip at a time; mostly muted under narration (finish.py mixes clip sound under the voice), original audio only for short key quotes (≤ 15 s, speaker named on screen and in narration).
- Every relay clip carries an on-screen source label (`lab=`, e.g. "SENATE ARMED SERVICES HEARING · C-SPAN · 2023", "NBC NEWS REPORT · 1997") and an entry in rights.json (source URL, title, license "PUBLIC DOMAIN" or "FAIR USE — NEWS EXCERPT"); list all footage sources in youtube_description.txt.
- All relay clips go through the same checks as DVIDS clips (gore, pull-down/duplicated frames, flash cuts).

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
- Footage: first the relay clips (see "Real footage via relay" above — request them now); then DVIDS pages are scraped (no API key needed; an API key also works: https://api.dvidshub.net/search?api_key=key-6ae3182ef3840&q=...&type[]=video): `python3 pipeline/dvids_get.py <src_dir> video:ID image:ID …` → writes rights.json. Check every frame used for gore/injury (never use).
- Skip source clips with a 25→30 pull-down pattern or many duplicated frames (they judder): check with mpdecimate.
- Relay clips (`$SRC/<name>.mp4`), DVIDS and archive.org clips are all used the same way: `C(name, start, lab=…)`; together real footage = 30–50 % of runtime.

## 3. Script → `episodes/NNN-slug/episode.py`
- `LINES = [(spoken, shots, opts)]`; `C(clip, start, lab=…)`, `G(graphic, …)`; opts: `slow`, `gap`, `sil`, `tag`.
- `PRON` (how TTS says it) and `DISPLAY` (subtitle spelling). Write numbers as words.
- 2,300–2,900 words → 15–20 min (owner 2026-11-14; default pause 0.55 s between lines). Length comes from more real material, never padding. Graphics: intro, title, chapter, doc, quote, stat, list, timeline, map, annot, geom, end (see pipeline/graphics.mjs).
- Lines with more than ~7 s of footage get 2–3 shots from different clips.

## 4. Build
```bash
R=/home/claude/releasedinfull_media; EP=$R/episodes/NNN-slug; SRC=/home/claude/src
python3 $R/pipeline/tts.py $EP "am_puck" 1.0      # voice C, owner choice 2026-11-17 (was am_eric:0.6+am_fenrir:0.4)
python3 $R/pipeline/make_gspec.py $EP && (cd $R/pipeline && NODE_PATH=$(npm root -g) node graphics.mjs $EP/gspec.json $EP/gfx)
python3 $R/pipeline/build.py $EP $SRC          # frame-exact 30 fps, cached segments
python3 $R/pipeline/finish.py $EP $SRC         # overlays, SRT, music, SFX, -14 LUFS
python3 $R/pipeline/qc_report.py $EP $EP/video_raw.mp4   # must say FAILS: 0
# encode (≤ 450 MB, hosted on Google Drive), Shorts, thumbnails
python3 $R/pipeline/shorts.py $EP $EP/shorts      # 4 cuts, 62–110 s each (--from-long re-cuts a published long.mp4)
python3 $R/pipeline/shorts.py $EP $EP/shorts --platform youtube   # YouTube Short candidates y1–y4, 20–30 s, from META["yshorts"] (owner rule 2026-11-06); score them, schedule ≤ 2/day (2026-11-23)
(cd $R/pipeline && NODE_PATH=$(npm root -g) node thumb_bold.cjs $EP/thumb_bold.json $EP $EP)   # thumbnails A/B/C (thumb.mjs is retired, see Growth playbook)
bash $R/pipeline/encode.sh $EP 450      # -> long.mp4 (two-pass x265, overlay burned in, <= 450 MB; Metricool YouTube limit 500 MB) — owner 2026-11-23
```

Document crops (2026-11-16): `pipeline/doc_crop.py <pdf> <page> "<first-line phrase>" "<last-line phrase>" out.jpg` crops whole lines tightly (no slivers of neighbouring lines), pads to 16:9 and black-bars personal names in its NAMES list (Epstein series rule: only Epstein, Acosta and other public officials stay visible) with the note "BLACK BARS: NAMES WITHHELD BY RELEASED IN FULL". `pipeline/phrase_crop.py` makes the tight phrase crop + box JSON used by the bold thumbnail. After replacing images, delete seg/*.sig of img segments before build.py. (2026-11-20) doc_crop.py options: `COL=left|right` crops one column of a two-column page (e.g. executive summaries); `NAMES_EXTRA=name1,name2` adds per-episode names to black-bar. Check the credit line of every report photo: photos credited to a city/state agency (e.g. NYC OCME) are NOT public domain — use only federal (DOJ/BOP/FBI) images.
Memory (2026-11-16): finish.py synthesises the score in 4-minute chunks and uses overlap-add convolution so 15-20 min episodes fit in 8 GB RAM. Long steps (tts ~45 min, build ~35 min, encode ~40 min on 2 cores) run in the background:

**Waiting for long steps (token rule, 2026-11-23):** start with nohup + log + pid file, then wait ONLY with `tools/waitfor.sh` (one call waits up to 9 min, prints DONE / EXITED / WAITING + 3 log lines). Repeat the same waitfor call while it prints WAITING. Never `cat`/`tail`/`grep` big logs to poll, never sleep-loop yourself; on EXITED or an error match, read only the last ~20 lines once.
```bash
L=/home/claude/logs; mkdir -p $L
nohup bash -c "python3 $R/pipeline/tts.py $EP am_puck 1.0; echo EXIT \$?" > $L/tts.log 2>&1 & echo $! > $L/tts.pid
bash $R/tools/waitfor.sh $L/tts.log "^EXIT |^speech seconds:|Traceback|Error" 540 $(cat $L/tts.pid)
```
Same pattern for each long step (always append `; echo EXIT \$?` inside the nohup command); done/error regexes (tts.py: as above):
- build.py: `"^EXIT |^done [0-9]|Traceback|Error"`
- finish.py: `"^EXIT |mix done|Traceback|Error"`
- encode.sh: `"^EXIT |long\.mp4$|Error|Invalid"`
- shorts.py (both platforms in one nohup): `"^EXIT |Traceback|Error"`
After DONE/EXITED check that the EXIT code is 0.

## 5. QC (blockers)
- qc_report: graphic holds perfectly still, 0 stutters, 0 flash cuts (source edits within 1 s of our cut).
- Contact sheets every 8 s: no gore, no overlap of tags with graphic headers, labels on every b-roll.
- Loudness −14 LUFS integrated.

## 6. Upload (public raw URLs for Metricool)
- Long video (owner 2026-11-23): Google Drive folder "RELEASED IN FULL", not GitHub: `python3 $R/tools/drive_upload.py $EP/long.mp4 --folder "RELEASED IN FULL" --creds /tmp/drive_creds.json` → its `direct` URL is the Metricool media for the long video. If Metricool rejects it: re-encode `encode.sh $EP 300`, upload again; if still rejected, fall back to `encode.sh $EP 95` + the drop branch below.
- Shorts, TikTok cuts and thumbnails (and the ≤ 95 MB fallback long video) stay on GitHub drop branches:
- Branch = ET weekday of publish: drop-mon … drop-sun. Orphan commit with that day's files only, force-push. Never commit video to main.
- URL: `https://raw.githubusercontent.com/ituraev97/releasedinfull_media/drop-<day>/<file>`

## 7. Schedule in Metricool (blogId 7743507, timezone America/New_York)
- Cadence: see "Long-video cadence — owner decision 2026-11-23" at the top (LONG run vs OFF run, D = tomorrow ET).
- Long: D 14:00 ET. youtubeData {title, type "video", privacy "public", madeForKids false, category "EDUCATION", isAiGeneratedContent false, tags}; text = youtube_description.txt; media [Drive `direct` URL of long.mp4]; videoThumbnailUrl = thumb_A URL (retry once without it if rejected).
- YouTube Shorts (20–30 s, YouTube only; owner 2026-11-23): only candidates scoring ≥ 7/10, at most 2 per day — D 12:30 + D 20:30 (trailer for the long), D+1 16:30 ET; ≥ 6 h apart, different templates. type "short", isAiGeneratedContent false, title ≤ 60 chars = question or surprising claim, never a document quote, memo name or a leading year.
- TikTok s1–s4 (62–110 s, TikTok only): D 12:30, D 20:30, D+1 12:30, D+1 20:30 ET. tiktokData {title ≤ 90 chars, privacyOption "PUBLIC_TO_EVERYONE", isAigc false}; text = 1–2 lines with search keywords + 4–5 hashtags.
- Language: narration, titles and descriptions are English. Metricool cannot set the YouTube video language; the channel's upload default must be English (YouTube Studio → Settings → Upload defaults → Advanced → Video language).
- Every vertical cut must be 62–110 s (TikTok Creator Rewards needs > 1 min; shorts.py auto-extends whole lines to ≥ 62 s), captions burned in, b-roll labels present, nothing important below y≈1500 or in the right 130 px (TikTok UI). Pick line ranges that make a complete mini-story (hook → reveal) of ~65–90 s.

## 8. Close the run
- After everything is scheduled: `python3 $R/tools/drive_upload.py --cleanup-days 7 --folder "RELEASED IN FULL" --creds /tmp/drive_creds.json` (deletes our Drive files older than 7 days).
- Commit to main: episode folder (episode.py, research.md, factcheck.md, rights.json, thumb.json, youtube_description.txt, captions_en.srt), updated backlog.md. Never video files on main.
- Report to the owner in Russian: title, FILE number, publish times (ET + Tashkent), 2-line summary, plannerUrls, thumb_B/C for Test & Compare, real-footage share (or "relay did not answer"), anything skipped.

## Pre-publish gate (blocker — nothing is scheduled until every line passes)
- long.mp4 duration 15:00–20:00 (ffprobe).
- Title ≤ 70 chars, does not start with a date, a year, an agency code, an operation/program name or "FILE"; it is a question or curiosity gap containing the searched keyword.
- thumb_A uses the bold template (huge subject, red circle/arrow, 2–3 huge words); look at it at 320 px wide — the words must be readable.
- First 5 s of narration = the most shocking verified fact + the question.
- Every YouTube Short 20–30 s, every TikTok cut 62–110 s; frame at 0.3 s is bright with the hook text.
- Narration voice is "am_puck" (Kokoro), speed 1.0.
- factcheck.md applied; legal_review.md all PASS where required.
If any line fails: fix and rebuild; if it cannot be fixed, do not publish and report why.

## Growth playbook (owner 2026-11-14 — grow aggressively, never look like a farm)
- Studio baseline (28 days to 2026-11-13): long CTR 3.4 %, avg view duration 2:01 (~19 %), 206 impressions; Shorts 43.6 % stayed to watch, 91.8 % of Shorts views from search, 8.2 % from the feed. Targets: CTR ≥ 6 %, retention ≥ 35 %, Shorts stayed ≥ 60 %.
- Freshness first: scan official releases of the last 14 days every run; at least every other episode is fresh (or has a fresh hook stated in the first 30 s). Epstein series: 3–4 episodes from official records only, interleaved with other topics.
- Titles: curiosity gap about an object/person/question with the searched keyword ("Where Is the Lost H-Bomb Now?", "What the Epstein Files Actually Show"). Never start with a date, agency code, operation name or FILE number. Strong but true.
- Thumbnails (owner 2026-11-17: "same as SWORN — bright and eye-catching; ours were unreadable") = `pipeline/thumb_bold.cjs` with `<ep>/thumb_bold.json` (`NODE_PATH=$(npm root -g) node pipeline/thumb_bold.cjs <ep>/thumb_bold.json <ep> <ep>`), port of SWORN thumb2.js v3. The old thumb.mjs is retired.
  - A = real photo left (aircraft, ship, place, archival photo of a historical/convicted/public-official person) + document right with the key lines highlighted yellow and a stamp (NEVER RECOVERED / DECLASSIFIED / REDACTED / CLASSIFIED), tag top-left, line1 white + line2 red.
  - B = question panel `{"q": ["STILL","IN THE","GROUND?"]}` left + strongest photo right, no bottom lines.
  - C = document left + photo right, line1 white + line2 yellow.
  - ≤ 5 words per line, every word true to the documents; photos bright and colourful (sunset, night lights, blue sky) — never grey/backlit; documents highlighted with a yellow band on the exact sentence (draw it in PIL before rendering).
  - Legal: never a photo of a living person who is not convicted, charged or acting as a public official; never victims; no news/TV frames.
  - QA: look at all three at full size AND at 168×94 — the big words must read.
  - Reference: `reference/thumb_bold_demo/thumb_bold.json` (Goldsboro).
- Opening: the most shocking verified fact + the question in the first 5 s; no bumper before 0:10; a new turn every 60–90 s; open loops; payoff in the last act.
- Verticals: frame 0 bright + huge hook text, voice on the hook word at 0.0 s; YouTube Shorts 20–30 s, TikTok 62–110 s; QA a frame at 0.3 s.
- Anti-farm: rotate opening types and structures, vary chapters and thumbnail compositions, a different template per Short, a description written for the episode, a genuine question for viewers.

## Legal safety (absolute — the channel belongs to the owner's sister in the USA)
- Facts only from official records (DOJ/FBI, court filings, IG reports, congressional reports, transcripts) or major outlets quoting them; every claim → opened URL in research.md.
- A living person is named only if convicted/charged/acting as a public official, or if named in an official record — then say exactly what the record says, plus "Appearing in these records is not evidence of wrongdoing." No guilt by association, sequencing, music or rhetorical questions. No photos of living non-convicted people. When in doubt, leave the name out.
- "Alleged", "accused", "according to …" for anything unproven; mention acquittals, dropped charges, denials, settlements without admission.
- Victims/minors: never named or shown; no description of sexual acts; court-summary level only.
- Politics: neutral, both parties' statements and votes.
- Copyright: public-domain government material and our own RECREATED graphics only; never third-party photos. News footage only as short fair-use excerpts about the exact case, labelled and credited (owner 2026-11-23, see "Real footage via relay").
- Mandatory legal review (separate agent, legal_review.md, PASS/FIX per named person and claim) for any episode naming a living person or touching a criminal case; apply every FIX, cut anything doubtful.
- Description line for such episodes: "This video reports on official public records. Inclusion of a name in released records does not imply wrongdoing. Allegations are unproven unless stated otherwise."

## Performance rules
Weekly review 2026-11-16 (Metricool, 28 days; YouTube rows only up to 2026-11-09 because of analytics lag; 33 TikTok cuts, 38 YouTube items). Targets: long CTR ≥ 6 %, retention ≥ 35 %, Shorts stayed ≥ 60 % (Studio baseline 3.4 % / 19 % / 43.6 %). Each rule is backed by ≥ 3 videos. Never changes cadence, slots, AI-label settings, legal or content rules.
1. TikTok topic: Cold War confrontation and spy stories keep winning (Azorian ship 962, Stevenson 1106, K-129 605, RFK on Oct 16 391, Hunt's wig 380); median of all 33 cuts is 192. UFO cuts now do well only when built on one object or person (CIA saucer memo 372, Tremonton film 347) and stay low as report counts (18 incidents 86, 510 reports 129, 43 reports 163).
2. TikTok opening: start on a person doing or saying something. Person/moment openings (Stevenson 1106, Soviet ship radio 962, RFK 391, Hunt 380, Theodore Hall 320) beat openings on a programme name or a memo (NSAM 181 / "Course B" 125, 1973 directive 123, Rosenbergs code names 138).
3. TikTok length: 62–72 s cuts (n=22) median 222 views vs 73 s+ (n=11) median 189. Default to 63–72 s.
4. YouTube Shorts titles (see also "Shorts: cadence + hook rules" 2026-11-23): a plain intriguing statement or a question with the object in it ("Two Navy UFO Videos Are Still Unidentified" 35, "Roswell's 'Bodies'? … Test Dummies" 19, "11 Near Misses…" 15); quote-led or memo-named titles get 0–2. From 2026-11-16 Shorts are 20–30 s with a huge boxed hook on frame 0 (watch "stayed to watch").
5. YouTube long: the only long video with real watch time (FILE 009 Goldsboro, avg 248 s on 4 views) opened on the event itself; FILE 001–005 averaged 7–79 s. Open on the most striking verified fact + the question; no logo before 0:10 (done from FILE 015).
6. Packaging (from the 2026-11-14 owner brief, to verify next review): bold thumbnail template (`thumb_bold.cjs`), curiosity titles about an object/person; compare FILE 015+ CTR with the 3.4 % baseline.


## Thumbnails v5 — illustrated cut-out from REAL images (owner decision 2026-11-23)
Owner: "bright and illustrated-looking, like the top drama channels — but faces must not be distorted". This section overrides the **thumb_A** part of the earlier thumbnail rules; thumb_B and thumb_C keep the current generator, so YouTube Studio → Test & Compare measures the new style against the old one. All earlier content rules stay in force: lawful image sources, every word true and sourced, fact-check of the thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

- Tool: `tools/thumbkit/thumbkit.py` (header = full spec). Setup once per run: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"` (downloads a 176 MB cut-out model on first use; if that fails the tool still works with a soft oval mask — say so in the report).
- It cuts the subject out of a real photo or video frame, adds a white sticker outline, a coloured glow and a rim light, washes the background in colour and sets 2–3 huge Anton words + an optional yellow sticker. Only pixel filters — no AI redraw, faces stay exactly as photographed. NEVER feed it an AI-generated image of a real person.
- Spec (`<ep>/thumbkit.json`, a list → thumb.jpg, thumb_B.jpg… — for this channel set "out":"thumb_A.jpg"):
  `[{"out":"thumb_A.jpg","layout":"solo","people":[{"src":"photo_or_clip","t":12.4,"crop":[x,y,w,h],"tint":"warm","kind":"person"}],"line1":"$250M","line2":"VANISHED","sticker":"SMALL FACT","brand":{"accent":"<channel colour>","sticker":"#FFD400","border":false}}]`
  - `layout`: "solo" (subject right, words left) or "versus" (two REAL sides of the same dispute, words centre — never pair people who are not part of the same story).
  - `kind`: "person" or "object" (boat, drug bundle, document, product, building, aircraft…).
  - `crop`: generous box around head + shoulders (face ≈ 35–50 % of its height) in source pixels; the subject must be ≥ 360 px tall in the source (the tool warns otherwise — find a bigger image).
  - `tint`: warm | cold | toxic | gold. `brand.accent` = the channel's main colour from the current generator.
- After rendering, LOOK at thumb_A at 320 px wide: words readable, face not covered, outline clean (no chunks of background). If the cut-out is bad (busy background, hands lost), use the current generator for A and say so in the report.

## Thumbnails v6 — YouTube-AI style: AI picture + real text/documents (owner decision 2026-11-23)
Owner: "make them like the thumbnails YouTube Studio's AI draws — bright, illustrated, with brands". This section overrides the **thumb_A and thumb_B** parts of the earlier thumbnail rules; thumb_C keeps the current generator, so YouTube Studio → Test & Compare measures the new style. Earlier content rules stay: lawful image sources, every word true and sourced, fact-check of thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

0. **EMOTION FIRST (owner 2026-11-24):** every thumbnail must show a strong emotion at first glance (rage, shock, fear, disbelief) — never a calm or smiling face. Pick the PEAK real frame/photo, let the AI dramatize light/smoke/contrast while keeping the exact face and expression; if no emotional real frame exists, put the emotion into the scene (fire, sirens, red stamp). Details: STYLE.md "EMOTION FIRST".
1. Read `tools/thumbkit/STYLE.md` — templates learned from YouTube's own AI thumbnails: doc (documentary split), evidence/fraud (object + real document + stamp), ntsb (full-bleed reconstruction + telemetry HUD + red circle), mugshot (real face + seized items, soft seam), versus, solo. Pick the template that fits this channel's examples.
2. AI pictures (free, FLUX.2 klein on the owner's office PC) via Drive "IMG RELAY" — request EARLY in the run (≈ 12 min per picture, longer while the PC voices — at most 3 pictures per run):
   `python3 tools/img_client.py request <ID> plates.json --creds /tmp/drive_creds.json` then later `python3 tools/img_client.py wait <ID> <ep>/plates --creds /tmp/drive_creds.json --timeout 2400`.
   plates.json = `[{"name":"plate_A.png","prompt":"cinematic photo of ..., dramatic side light, dark background, high detail","w":1280,"h":720,"seed":1}, ...]` (max 6). The AI paints ONLY pictures — NEVER ask it for text, documents, logos-as-evidence. Real people: send their REAL lawful photo as `"ref"` (edit mode: "same person, same expression, re-lit with red and blue police lights, sharp, cinematic") — never generate a real person from text.
   No answer in time → build A/B with real frames (thumbkit solo/versus) and say so in the report.
3. Compose with `tools/thumbkit/thumbkit.py <ep>/thumbkit.json` (setup: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"`; header lists every layout and overlay: tag, ribbon, hud, circle, path, stamp, bignum, pill, label, band). Text, numbers, stamps and the REAL document crop are drawn by thumbkit — documents come only from the real source (PDF page → `doc`, `highlights` boxes in its pixels).
4. LOOK at every thumb at full size and at 320 px: AI picture has no garbage text/extra fingers/melted objects, faces unchanged, words readable. Bad picture → new seed/prompt (one retry), otherwise fall back to the real-frame layout.

## Promise, clips & subtitles (owner decision 2026-11-24 — lesson from HOTFIX comments: "baited by title, talks about it for 2 seconds", "censors so much you can't tell what he's saying", "ai slop")
- **Promise rule:** the moment the title + thumbnail promise (the arrest, the verdict, the crash, the confession, the number) must appear IN FULL within the first 60 s — the real clip/document/audio, not a 2-second tease — and that story takes ≥ 25 % of the runtime. The title describes what the video is mostly about; never sell one moment that only pays off near the end. Shorts: the hook's promise is paid by the last 3 s.
- **Original audio is always subtitled:** every bodycam/court/interview/stream clip gets burned-in subtitles (word-timed from faster-whisper or the official transcript), big and high-contrast, so viewers understand it on a phone with bad speakers.
- **Bleep only the f-word, c-word and slurs**, exactly the word length (±0.03 s); milder swearing stays audible; the subtitle shows the bleeped word as f***. No swearing at all in the first 15 s (advertiser rules). Gore/violence rules of this runbook stay as they are.
- **Against the "AI slop" impression:** open on real footage/real voices, not narration over stock; real material (clips, documents, photos) ≥ 30 % of the runtime; the narrator states clear judgements ("this is where it went wrong"), no filler or repeated recaps; length follows the story — a tight 12-minute video beats a padded 25.
- Check before publishing: watch the first 60 s — is the promise delivered? Read 3 random subtitled clips with the sound off — are they understandable?
