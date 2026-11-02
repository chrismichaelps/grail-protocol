---
type: moc
tags: [moc]
---

# src/Web

One page per file, each with its interface and the modules it depends on.

- [[src/Web/Caller]] — what a request presents: its token, parameters, and body
- [[src/Web/Description]] — the operations described with the standard OpenAPI model, to prove the router serves exactly the contract
- [[src/Web/Handlers]] — one handler per contract operation, chosen once by operation id
- [[src/Web/Lines]] — one JSON request per input line, dispatched through the HTTP router
- [[src/Web/Peers]] — names a peer by its host, so a new connection is not a new peer
- [[src/Web/Respond]] — JSON answers and problem documents
- [[src/Web/Router]] — the HTTP routes, built from the contract's operations and nothing else

## Referenced by

[[src/_MOC]]
