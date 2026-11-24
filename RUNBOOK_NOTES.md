# RELEASED IN FULL — run notes archive (moved out of RUNBOOK.md 2026-11-23; append new run notes at the end)

## Performance rules changelog (archived verbatim from RUNBOOK.md)
Changelog
- 2026-11-10: section created from the first weekly review (rules 1–5).
- 2026-11-16: second weekly review — rules rewritten (TikTok person/moment openings, 62–72 s, object-led UFO cuts; Shorts 20–30 s with frame-0 hook; long-video opening; bold thumbnails to verify).

## 2026-11-24 (FILE 019)
- finish.py OOM-killed under the ~4 GB cgroup; patched to float32 and freeing arrays after premix.wav.
- DOJ pages: read via the archive.org mirror (remotezip, HTTP range). justice.gov is behind a bot challenge; do not bypass.
- DVIDS clip windows: check each clip for people/overexposure; restrict start windows (dv1026930c only at 28-37 s).
- Run long jobs with plain nohup (setsid gave instant EXITED); wait with tools/waitfor.sh.
- Vertical hooks: if a hook line is wide, set hs ~150-160 in META to avoid clipping.
