---
type: moc
tags: [moc]
---

# src/Agent

One page per file, each with its interface and the modules it depends on. This layer is a client of a fabric: it reaches one only through [[src/Api/Peer]], with a participant's token, exactly as any other software would.

- [[src/Agent/Mcp]] — serves the participant's tools to a hosted model over a tool protocol on standard input and output
- [[src/Agent/Runner]] — keeps a participant attached: pulls its deliveries, starts a hosted agent for each task, and makes sure every task it starts ends answered
- [[src/Agent/Session]] — one participant attached to one fabric: who it acts for, how it reaches the fabric, and where its delivery cursor stands
- [[src/Agent/Tools]] — what an attached participant can do, as tools a hosted model calls, each chosen once by name
- [[src/Agent/Wire]] — the envelopes an attached participant writes, and the compact form a model reads them in

## Referenced by

[[src/_MOC]] · [[decisions/ADR-0011-channels-and-hosted-agents]]
