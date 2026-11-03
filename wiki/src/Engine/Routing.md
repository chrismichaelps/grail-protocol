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
/// Resolves every selected branch or refuses the whole expansion; retained paths are witnesses for later nested replies. A channel stands for its subscribers other than the sender, and one nobody else hears expands to no route at all, which the caller judges.
export fn routes(graph: &Graph.Graph, participants: &Array[Str], graphs: &Map[Str, Graph.Graph], source: Str, kind: Str) -> Result[Array[Envelope.Route], Problem.Problem]
/// The participants a channel delivers a kind to: every target of a flow edge from the channel that carries the kind, except the sender.
export fn subscribers(graph: &Graph.Graph, channel: Str, source: Str, kind: Str) -> Array[Str]
/// The participant a selector names directly, if it names one.
export fn named(selector: &Envelope.Selector) -> Option[Str]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Constants/Graphs]] · [[src/Contract/Limits]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Problem]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Engine/Admission]]

<!-- authored -->
## Algorithm

`resolverOf` turns a selector into a strategy once: one participant, every holder of a role, or every holder of an ability that the source reaches on a flow edge carrying the kind. `routes` expands graph participants through their entry participants, retaining each full path. Expansion fails atomically for an empty branch or when the projected path or containment bounds are exceeded. Shared leaf addresses retain distinct paths for causal attribution. A channel expands to its subscribers for the envelope's kind, leaving out the sender, so `routes` carries the source and kind through the expansion; a channel with no one else to hear refuses like an empty role.

## Grill Log

- **Q:** Resolve role and ability by scanning the selector at every step? **A:** No; the selector picks its strategy once. **Rationale:** the factory keeps routing free of repeated branching. **Rejected:** a conditional per rule.
<!-- /authored -->

## Referenced by

[[src/Engine/Admission]] · [[src/Engine/_MOC]]
