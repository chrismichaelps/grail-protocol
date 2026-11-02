---
type: module
path: "@root/src/Engine/Lifecycle.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Lifecycle

> @Engine.Lifecycle.Machine — the legal moves of a task lifecycle

## Purpose

The legal moves of a task lifecycle.

## Interface

### Signatures

```pudu
/// The state a lifecycle moves to on an event, or the refusal naming where it stands.
export fn advance(state: Str, event: Str) -> Result[Str, Problem.Problem]
/// Whether a state never changes again.
export fn isFinal(state: Str) -> Bool { Vocabulary.FINAL_STATES.contains(state) }
/// The state a new lifecycle starts in.
export fn initial() -> Str { Vocabulary.STATE_SUBMITTED }
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Events]] · [[src/Constants/Extras]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Problem]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Engine/Admission]] · [[src/Engine/Bridge]]

## Referenced by

[[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/_MOC]]
