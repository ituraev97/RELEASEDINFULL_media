#!/usr/bin/env bash
# usage: encode.sh <episode_dir> [max_MB=95]  -> <ep>/long.mp4
# Burns overlay.ass (tags, b-roll labels, credit), fades, muxes mix.wav; two-pass x265 sized under GitHub's 100 MB limit.
set -euo pipefail
EP="$1"; MAXMB="${2:-95}"; cd "$EP"
D=$(python3 -c "import json;print(json.load(open('timing.json'))['total'])")
VBR=$(python3 -c "print(int(($MAXMB*8*1024*0.97)/$D - 160))")
VF="fade=t=in:st=0:d=0.5,fade=t=out:st=$(python3 -c "print($D-0.8)"):d=0.8,ass=overlay.ass"
X="keyint=300:min-keyint=30:aq-mode=3:log-level=error"
ffmpeg -nostdin -v error -y -i video_raw.mp4 -vf "$VF" -c:v libx265 -preset fast -b:v ${VBR}k -x265-params pass=1:$X -an -f null /dev/null
ffmpeg -nostdin -v error -y -i video_raw.mp4 -i mix.wav -vf "$VF" -c:v libx265 -preset fast -b:v ${VBR}k -x265-params pass=2:$X \
  -tag:v hvc1 -pix_fmt yuv420p -r 30 -c:a aac -b:a 160k -ar 48000 -t "$D" -movflags +faststart long.mp4
rm -f x265_2pass.log*; ls -la long.mp4
