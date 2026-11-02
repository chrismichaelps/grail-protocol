---
type: tool
path: "@root/tools/Recording/Record.sh"
tags: [tool, documentation]
---

# Recording

> Records a demonstration from `examples/` in a real Terminal window on macOS

## Purpose

`Record.sh team` or `Record.sh handoff` builds the fabric, moves the front Terminal window into place, starts `screencapture` on exactly that window, and types `python3 examples/<name>/demo.py build/grail` with real keystrokes through `Type.applescript`, which stops if Terminal loses focus. The recording is kept in `build/demo/<name>.mov`, converted with `avconvert` into `website/template/public/<name>-demo.mp4`, and turned into `<name>-demo.gif` by `Gif.swift`, which reads frames with AVFoundation, drops repeated frames by stretching the previous one, and writes the GIF with ImageIO.

Everything it uses ships with macOS and the Xcode tools; nothing is downloaded. The front Terminal window must be at a shell prompt, and macOS asks once for Screen Recording and Accessibility permission. `swift tools/Recording/Gif.swift frames <movie> <directory> <second>...` samples stills for review.

## Referenced by

[[tools/_MOC]] · [[decisions/ADR-0009-portable-handoffs]]
