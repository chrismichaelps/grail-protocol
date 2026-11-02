---
type: test
path: "@root/test/Security/ErasureTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, security]
---

# Security.ErasureTest

## Purpose

Graph restrictions constrain payload erasure through the HTTP router. A graph-bound caller cannot erase another graph's payload, including when its audience is `owner`. Refused erasure leaves the transfer unchanged. Same-graph erasure succeeds; an unbound owner can erase either graph. Missing abilities remain forbidden, and ledger digests and links survive erasure.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Support/Runner]]
- **Standard library:** `Std.Http`, `Std.Json`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]]
