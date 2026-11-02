---
type: module
path: "@root/src/Engine/Journal.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Journal

> @Engine.Journal.Mutations — records graph changes in the ledger as fabric-written envelopes

## Purpose

Records graph changes in the ledger as fabric-written envelopes.

## Interface

### Signatures

```pudu
/// The scope with a graph stored and the change that produced it appended to the ledger.
export fn recorded(state: &Scope.State, graph: &Graph.Graph, mutation: &Mutation.Mutation, actor: Str, now: Int) -> Scope.State
```

### Linkage

- **Requires:** [[src/Constants/Fabric]] · [[src/Constants/Ledger]] · [[src/Contract/Members]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Ledger]] · [[src/Domain/Mutation]] · [[src/Domain/Scope]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Ledger]]
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/Services/Fabric]] · [[test/Support/Fixtures]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Services/Fabric]] · [[test/Support/Fixtures]]
