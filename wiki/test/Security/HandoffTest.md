---
type: test
path: "@root/test/Security/HandoffTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, security, portability]
---

# Security.HandoffTest

## Purpose

Two fabrics with different secrets and names, standing for two products, exchange an agent through their HTTP routers. A writer exports its result and its ancestry, with a note it cannot read withheld; the other fabric imports it for an assistant, delivers the arrival, and serves it back unchanged. Only the origin attests the seal, and only for the scope it was made for. Altered envelopes, missing parents, foreign anchors, mismatched ids, unknown participants, missing abilities, forged handoff kinds, reused ids, and expired documents are refused. Work continues from the import entry, traces back to it, and moves on again with its whole history.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Engine/Handoff]] · [[src/Engine/Ledger]] · [[src/Utils/JsonRead]] · [[test/Support/Fabric]] · [[test/Support/Runner]]
- **Standard library:** `Std.Concurrent`, `Std.Http`, `Std.Http.Server.Route`, `Std.Json`, `Std.List`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]] · [[decisions/ADR-0009-portable-handoffs]]
