---
type: module
path: "@root/src/Domain/Mutation.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Mutation

> @Domain.Mutation.Change — an atomic, revision-checked change to a graph

## Purpose

An atomic, revision-checked change to a graph.

## Interface

### Signatures

```pudu
export type Step
export type Mutation = { expectedRevision: Int, steps: Array[Step] }
export type Draft = { participants: Array[Graph.Participant], edges: Array[Graph.Edge] }
```

### Linkage

- **Requires:** [[src/Domain/Graph]]
- **Consumed by:** [[src/Domain/Request]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Journal]] · [[src/Engine/Mutations]] · [[src/Services/Fabric]] · [[src/Validation/Graph]] · [[src/Web/Handlers]] · [[test/Engine/MutationsTest]] · [[test/Support/Fixtures]]

## Referenced by

[[src/Domain/Request]] · [[src/Domain/_MOC]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Journal]] · [[src/Engine/Mutations]] · [[src/Services/Fabric]] · [[src/Validation/Graph]] · [[src/Web/Handlers]] · [[test/Engine/MutationsTest]] · [[test/Support/Fixtures]]
