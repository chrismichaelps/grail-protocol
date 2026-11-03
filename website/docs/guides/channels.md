---
uid: guides.channels
description: Give a team shared channels that agents, people, and observers can post to and read back, and watch them live in your browser.
---

# Use channels

A channel is a participant of kind `channel`. It never acts. It hands each post to its subscribers and keeps every post readable in order, so a reviewer who joins late can read what was said, and a person or a dashboard can watch without being asked to answer.

[Open the channel viewer](../live/channels.html) to replay a recorded run of two agents, or to watch your own fabric.

## Declare one

Edges decide everything. A flow edge into the channel lets a participant post. A flow edge out of it subscribes a participant, and its `kinds` limit what that subscriber hears.

```json
{
  "participants": [
    {"id": "lead", "kind": "human"},
    {"id": "builder", "kind": "agent"},
    {"id": "reviewer", "kind": "agent"},
    {"id": "watcher", "kind": "service"},
    {"id": "general", "kind": "channel"}
  ],
  "edges": [
    {"id": "lead-posts", "from": "lead", "to": "general", "relation": "flow"},
    {"id": "builder-posts", "from": "builder", "to": "general", "relation": "flow"},
    {"id": "to-lead", "from": "general", "to": "lead", "relation": "flow"},
    {"id": "to-builder", "from": "general", "to": "builder", "relation": "flow"},
    {"id": "to-reviewer", "from": "general", "to": "reviewer", "relation": "flow", "kinds": ["task"]},
    {"id": "to-watcher", "from": "general", "to": "watcher", "relation": "flow"}
  ]
}
```

A channel declares no roles, abilities, or graph. Channels do not subscribe to channels, and nothing may depend on a channel.

## Post

Address the channel like any participant:

```bash
curl -sS -X POST http://127.0.0.1:7420/v1/scopes/studio/transfers \
  -H "Authorization: Bearer $(cat build/channels/lead.token)" -H 'Content-Type: application/json' \
  -d '{"grail":"1.2","id":"hello","scope":"studio","graph":"studio","source":"lead","target":{"participant":"general"},"kind":"observation","payload":{"text":"Morning, team."}}'
```

The receipt lists every subscriber that received it. The sender never receives its own post. A post nobody else hears yet is still kept for later readers; a task nobody could answer is refused with `grail.no-route`.

A `task` posted to a channel reaches every subscriber. The first one to report progress or answer takes it, and the fabric refuses everyone else from then on, so two agents never both do the work. The answer goes to whoever asked, not to the channel.

## Read back

```bash
curl -sS 'http://127.0.0.1:7420/v1/scopes/studio/graphs/studio/channels/general?after=0&wait=25000' \
  -H "Authorization: Bearer $(cat build/channels/watcher.token)"
```

The answer has the same shape as a page of deliveries. Pass `cursor` back as `after` to continue; with `wait`, the fabric holds the request until a post arrives. Reading a channel never acknowledges anything, so watching it does not change what any participant receives.

Only the owner and the channel's subscribers may read it; anyone else is told it does not exist. A subscriber reads only the kinds its edge carries, including posts made before it subscribed, except posts with `recipients` visibility that it did not receive. A secret reference stays a reference.

## Run the showcase

`examples/channels/showcase.sh` walks the studio graph through every part of the protocol in 15 steps and stops on the first answer it did not expect. The lead narrates each step in `#general` while `#reviews` carries the review and `#builds` carries a streamed build log, so the viewer below tells the story as it runs. With `AGENTS=1`, the review is done by whatever agent you attached as the reviewer.

```bash
examples/channels/up.sh
examples/channels/showcase.sh
```

## Watch from the browser

The [channel viewer](../live/channels.html) is a page on this site that connects to a fabric on your own machine. It sends your token only to the fabric address you enter and keeps it in the tab's memory.

1. Start the example. Its `up.sh` lists this site's origin in `GRAIL_ALLOWED_ORIGINS`, so the browser may call the fabric:

   ```bash
   examples/channels/up.sh
   ```

2. Open the viewer, choose **Your fabric**, and paste the contents of `build/channels/watcher.token`. The watcher holds `transfer.receive` alone: it can watch, never post.
3. Attach agents with `examples/channels/attach.sh builder <agent>` and `examples/channels/attach.sh reviewer <agent>`, and give the builder a task. See [Attach hosted agents](agents.md).

Your browser may ask whether this page may reach devices on your local network; allow it for the viewer to connect. To use another origin, start the fabric with `GRAIL_ALLOWED_ORIGINS` set to it.

See the [channels specification](../protocol/15-Channels.md) for the normative rules.
