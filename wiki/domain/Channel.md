---
type: domain
tags: [domain, channels]
aliases: [Channel]
---

# Channel

- **Definition:** A participant of kind `channel` that never acts. It hands each post to its subscribers, the targets of its outgoing flow edges whose kinds admit the post, leaving out the sender, and keeps every post readable in ledger order.
- **Canonical name:** Channel; a post is an envelope whose target names the channel; a subscriber is a participant a flow edge leads to from the channel; an observer is a subscriber whose token holds only `transfer.receive`.
- **Not:** A role, a queue, a topic outside the graph, or a participant that can answer, send, or produce a result. Not a separate store either: its history is the ledger, read through `readChannel`.
- **Example:** In graph `studio`, `builder` posts a review task to `reviews`; the flow edge `reviews → reviewer` carries only `task`, so the reviewer hears it, while `reviews → watcher` carries every kind and the watcher reads it back from the start.

## Referenced by

[[protocol/15-Channels]] · [[protocol/01-Overview]] · [[domain/_MOC]]
