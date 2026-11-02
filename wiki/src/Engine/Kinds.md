---
type: module
path: "@root/src/Engine/Kinds.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Kinds

> @Engine.Kinds.Factory — the behavior of every kind, chosen once by name

## Purpose

The behavior of every kind, chosen once by name.

## Interface

### Signatures

```pudu
export type Effect
export type Actor
export type Stream
export type Behavior = { effect: Effect, actor: Actor, stream: Stream }
/// The behavior of an envelope's kind. A bridged JSON-RPC message behaves as the request or response it carries.
export fn behaviorOf(kind: Str, payload: &Option[Json.Json]) -> Behavior
/// Whether a kind answers a lifecycle, and so is routed back to the task's source.
export fn answers(behavior: &Behavior) -> Bool { behavior.actor == Recipient }
```

### Linkage

- **Requires:** [[src/Constants/Events]] · [[src/Constants/Rpc]] · [[src/Contract/Vocabulary]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Engine/Admission]] · [[src/Engine/Causality]]

<!-- authored -->
## Algorithm

The behavior of a reserved kind is a row of a constant table: its effect on lifecycles (records, opens, or moves with an event), who may send it, its part in a stream, and whether dependency gating applies. A bridged JSON-RPC message behaves as the request, notification, or response it carries. Any other kind only leaves a record.

## Negative Logic

- ❌ Never compare kind names anywhere else; every rule asks for the behavior.

## Grill Log

- **Q:** A switch on the kind in each engine, or one table? **A:** One table, read once per envelope. **Rationale:** adding a kind is one row, and no engine grows a ladder of name comparisons. **Rejected:** per-engine matching on names.
<!-- /authored -->

## Referenced by

[[src/Engine/Admission]] · [[src/Engine/Causality]] · [[src/Engine/_MOC]]
