---
type: test
path: "@root/test/Engine/HandoffTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, engine, portability]
---

# Engine.HandoffTest

## Purpose

Pins the boundaries of [[src/Engine/Handoff]] at a fixed time: the default and maximum lifetime, a handoff that would expire as it is issued, a repeated sequence, an entry with no withheld mark, the instant of expiry, and the entry limit.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Contract/Limits]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Handoff]] · [[src/Domain/Problem]] · [[src/Domain/Scope]] · [[src/Engine/Handoff]] · [[src/Utils/JsonRead]] · [[test/Support/Fixtures]] · [[test/Support/Runner]]
- **Standard library:** `Std.Json`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]] · [[decisions/ADR-0009-portable-handoffs]]
