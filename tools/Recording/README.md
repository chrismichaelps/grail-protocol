# Record demonstrations

`Record.sh` captures the existing Terminal demonstrations on macOS. `Frames.swift` encodes selected real application captures as an edited MP4 and a compact GIF preview, using macOS frameworks without third-party encoders.

For a capture-based walkthrough, collect authorized screenshots without changing their contents. Keep credentials, unrelated workspaces, and personal contact details out of the frames. Browser captures are JPEG. A manifest supplies the order, captions, and display duration:

```json
{
  "width": 1280,
  "height": 976,
  "scenes": [
    {
      "image": "frames/request.jpg",
      "seconds": 7,
      "title": "A real Slack task starts the exchange",
      "note": "Grail Lab / session-operated gateway",
      "preview": true
    }
  ]
}
```

```bash
swift tools/Recording/Frames.swift manifest.json output.mp4 preview.gif
```

Images resolve relative to the manifest. Output paths must not already exist. The MP4 contains every scene; the GIF includes only scenes marked `preview`, held for four seconds each. Captions and letterboxing are added without altering the underlying captures. Label edited captures and live/replayed data honestly.

The Slack/Codex recording uses seven captured states over 51 seconds. Slack footage is the real desktop app; Codex footage displays actual CLI output in a read-only local console because direct capture of the Codex and Terminal apps was unavailable. The Slack gateway is operated by the recording session. The worker itself is a real `codex exec` process supervised by `grail run`, with no MCP connection to Grail.
