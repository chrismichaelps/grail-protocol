---
type: module
path: "@root/src/Engine/Codec/Graph.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Codec.Graph

> @Engine.Codec.Graph — graphs, drafts, and mutations to and from JSON

## Purpose

Graphs, drafts, and mutations to and from JSON.

## Interface

### Signatures

```pudu
/// The draft a body describes, or how it departs from the contract.
export fn decodeDraft(body: &Json.Json) -> Result[Mutation.Draft, Problem.Problem]
/// The mutation a body describes, or how it departs from the contract.
export fn decodeMutation(body: &Json.Json) -> Result[Mutation.Mutation, Problem.Problem]
/// A graph as JSON.
export fn encode(graph: &Graph.Graph) -> Json.Json
/// A participant as JSON.
export fn participantJson(member: &Graph.Participant) -> Json.Json
/// An edge as JSON.
export fn edgeJson(edge: &Graph.Edge) -> Json.Json
/// A mutation as JSON, as the ledger records it.
export fn mutationJson(mutation: &Mutation.Mutation) -> Json.Json
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Members]] · [[src/Contract/Schemas]] · [[src/Contract/Vocabulary]] · [[src/Domain/Graph]] · [[src/Domain/Mutation]] · [[src/Domain/Problem]] · [[src/Engine/Codec/Shapes]] · [[src/Utils/JsonRead]] · [[src/Utils/Pointer]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Engine/Journal]] · [[src/Web/Handlers]]

## Referenced by

[[src/Engine/Codec/_MOC]] · [[src/Engine/Journal]] · [[src/Web/Handlers]]
