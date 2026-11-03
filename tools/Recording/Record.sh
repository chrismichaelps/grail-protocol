#!/bin/bash
# Records one of the demonstrations in examples/ in a real Terminal window on macOS.
#
# The front Terminal window must be sitting at a shell prompt. The script moves it into place, starts a screen
# recording of exactly that window, types the demonstration command with real keystrokes, and converts the
# recording into an MP4 and a GIF for the README. Everything it uses ships with macOS and the Xcode tools.
#
#   tools/Recording/Record.sh handoff    two fabrics pass a working agent between them
#   tools/Recording/Record.sh team       a team in one fabric: gates, narrowed tokens, privacy, revocation
#   tools/Recording/Record.sh secrets    an agent uses a key it never sees
#
# macOS asks once for Screen Recording and Accessibility permission for the app that runs it.

set -euo pipefail

DEMO="${1:?name a demonstration in examples/: handoff, team, or secrets}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HERE="$ROOT/tools/Recording"
OUT="$ROOT/website/template/public"
MOVIE="$ROOT/build/demo/$DEMO.mov"
LEFT=160
TOP=60
WIDTH=900
HEIGHT=640
SECONDS_RECORDED=24
GIF_FPS=12
GIF_WIDTH=1200
COMMAND="python3 examples/$DEMO/demo.py build/grail"

if [ ! -f "$ROOT/examples/$DEMO/demo.py" ]; then
  echo "no demonstration named $DEMO in examples/" >&2
  exit 2
fi

mkdir -p "$ROOT/build/demo" "$OUT"
pudu build "$ROOT/src/Main.pudu" -o "$ROOT/build/grail" > /dev/null

osascript -e "tell application \"Terminal\"
  activate
  set bounds of front window to {$LEFT, $TOP, $((LEFT + WIDTH)), $((TOP + HEIGHT))}
  do script \"cd '$ROOT' && clear\" in selected tab of front window
end tell" > /dev/null
sleep 1.2

rm -f "$MOVIE"
screencapture -x -v -V "$SECONDS_RECORDED" -R "$LEFT,$TOP,$WIDTH,$HEIGHT" "$MOVIE" &
recording=$!
sleep 2
typed="$(osascript "$HERE/Type.applescript" "$COMMAND")"
wait "$recording"

if [ "$typed" != "typed" ]; then
  echo "recording discarded: $typed" >&2
  exit 1
fi

rm -f "$OUT/$DEMO-demo.mp4"
avconvert --source "$MOVIE" --preset PresetHighestQuality --output "$OUT/$DEMO-demo.mp4" > /dev/null
swift "$HERE/Gif.swift" gif "$MOVIE" "$OUT/$DEMO-demo.gif" "$GIF_FPS" "$GIF_WIDTH" 2> /dev/null
ls -lh "$OUT/$DEMO-demo.mp4" "$OUT/$DEMO-demo.gif"
