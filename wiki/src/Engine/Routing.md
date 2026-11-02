---
type: module
path: "@root/src/Engine/Routing.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Routing

> @Engine.Routing.Resolvers — the strategy that turns a selector into recipients, chosen once

## Purpose

The strategy that turns a selector into recipients, chosen once.

## Interface

### Signatures

```pudu
export type Resolve = fn(Graph.Graph, Str, Str) -> Array[Str]
/// The resolver for a selector.
export fn resolverOf(selector: &Envelope.Selector) -> Resolve
/// Every address an envelope reaches: resolved participants, with graph participants replaced by the entry participants of the graph they stand for.
export fn addresses(graph: &Graph.Graph, participants: &Array[Str], graphs: &Map[Str, Graph.Graph]) -> Array[Envelope.Address]
/// The participant a selector names directly, if it names one.
export fn named(selector: &Envelope.Selector) -> Option[Str]
```

### Linkage

- **Requires:** [[src/Constants/Graphs]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]]
- **Standard library:** `Std.List`, `Std.Option`
- **Consumed by:** [[src/Engine/Admission]]

<!-- authored -->
## Algorithm

`resolverOf` turns a selector into a strategy once: one participant, every holder of a role, or every holder of an ability that the source reaches on a flow edge carrying the kind. `addresses` replaces a graph participant with the entry participants of the graph it stands for, recursively and bounded by the number of graphs.

## Grill Log

- **Q:** Resolve role and ability by scanning the selector at every step? **A:** No; the selector picks its strategy once. **Rationale:** the factory keeps routing free of repeated branching. **Rejected:** a conditional per rule.
<!-- /authored -->

## Referenced by

[[src/Engine/Admission]] · [[src/Engine/_MOC]]
