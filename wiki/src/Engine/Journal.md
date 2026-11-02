---
type: module
path: "@root/src/Engine/Journal.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Journal

> @Engine.Journal.Written — records the fabric's own changes, graph mutations and handoffs, in the ledger as fabric-written envelopes

## Purpose

Records the fabric's own changes in the ledger as fabric-written envelopes: graph mutations, and the export and import entries of handoffs. Both share one writer, so every fabric-written entry has the same shape and digest rules.

## Interface

### Signatures

```pudu
export type Entry = { id: Str, graph: Str, actor: Str, kind: Str, parents: Array[Str], payload: Json.Json, recipients: Array[Envelope.Address] }

/// The scope with a graph stored and the change that produced it appended to the ledger.
export fn recorded(state: &Scope.State, graph: &Graph.Graph, mutation: &Mutation.Mutation, actor: Str, now: Int) -> Scope.State

/// The record of a fabric-written entry and the scope with it appended to the ledger.
export fn written(state: &Scope.State, entry: &Entry, now: Int) -> (Ledger.Record, Scope.State)
```

### Linkage

- **Requires:** [[src/Constants/Fabric]] · [[src/Constants/Ledger]] · [[src/Contract/Members]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Ledger]] · [[src/Domain/Mutation]] · [[src/Domain/Scope]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Ledger]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Support/Fixtures]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Support/Fixtures]]
