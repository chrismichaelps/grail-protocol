---
type: moc
tags: [moc]
---

# src/App

One page per file, each with its interface and the modules it depends on.

- [[src/App/Assembly]] — the mediator built once over the runtime
- [[src/App/Commands]] — every operation as one typed call, announced when it changes something
- [[src/App/Events]] — what the fabric announces after a change, and who listens
- [[src/App/Handlers]] — each message kind bound to its use case
- [[src/App/Logging]] — the structured loggers of the fabric
- [[src/App/Messages]] — every request the fabric answers, one kind per contract operation
- [[src/App/Pipeline]] — what every message passes through
- [[src/App/Resilience]] — every message runs under a concurrency limit and a deadline; a waiting pull's deadline covers its wait

## Referenced by

[[src/_MOC]]
