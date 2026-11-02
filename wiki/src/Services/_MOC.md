---
type: moc
tags: [moc]
---

# src/Services

One page per file, each with its interface and the modules it depends on.

- [[src/Services/Bridge]] — carries one JSON-RPC message through a graph as an envelope
- [[src/Services/Fabric]] — every operation of the protocol over one scope at a time
- [[src/Services/Handoffs]] — exporting, importing, reading, and verifying portable handoffs
- [[src/Services/Runtime]] — the settings, the store, and the clock every use case shares
- [[src/Services/Store]] — every scope's state, changed one scope at a time under a lock

## Referenced by

[[src/_MOC]]
