---
type: module
path: "@root/src/Services/Handoffs.pudu"
layer: 5
grammar: "[[grammar/pudu]]"
tags: [module, services]
---

# Services.Handoffs

> @Services.Handoffs.UseCases — exporting, importing, reading, and verifying portable handoffs

## Purpose

Exporting, importing, reading, and verifying portable handoffs.

## Interface

### Signatures

```pudu
/// Seals a participant's anchors and their ancestry into a handoff, and records that it left.
export fn exportHandoff(runtime: &Runtime.Runtime, call: &Request.Call[Handoff.Asked]) -> Result[Handoff.Stored, Problem.Problem]

/// Admits a handoff from another fabric once its integrity holds, and delivers its arrival to the participant it is for. The same handoff imported again answers the original receipt.
export fn importHandoff(runtime: &Runtime.Runtime, call: &Request.Call[Handoff.Arriving]) -> Result[Handoff.Receipt, Problem.Problem]

/// Reads a handoff this scope exported or imported, when the token may read the entry that records it.
export fn readHandoff(runtime: &Runtime.Runtime, call: &Request.Call[Str]) -> Result[Handoff.Stored, Problem.Problem]

/// Says whether a handoff is intact, whether this fabric sealed it for the scope in the path, and whether it expired. It reads no scope, so it tells nothing about what the scope holds.
export fn verifyHandoff(runtime: &Runtime.Runtime, call: &Request.Call[Handoff.Presented]) -> Result[Handoff.Check, Problem.Problem]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Handoff]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Handoff]] · [[src/Domain/Ledger]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Scope]] · [[src/Engine/Authority]] · [[src/Engine/Delivery]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Services/Fabric]] · [[src/Services/Runtime]] · [[src/Services/Store]]
- **Standard library:** `Std.Json`, `Std.Map`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/App/Handlers]]

## Referenced by

[[src/Services/_MOC]] · [[src/App/Handlers]]
