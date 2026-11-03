---
type: module
path: "@root/src/Engine/Mutations.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Mutations

> @Engine.Mutations.Steps — applies mutation steps chosen once by operation, then checks the whole graph

## Purpose

Applies mutation steps chosen once by operation, then checks the whole graph.

## Interface

### Signatures

```pudu
export type Apply = fn(Graph.Graph) -> Result[Graph.Graph, Problem.Problem]
/// The effect of one step.
export fn stepOf(step: &Mutation.Step) -> Apply
/// The graph after a mutation, checked against every other graph of its scope; the revision grows by one.
export fn apply(graph: &Graph.Graph, mutation: &Mutation.Mutation, others: &Map[Str, Graph.Graph]) -> Result[Graph.Graph, Problem.Problem]
/// A new graph from a draft, checked the same way a mutation is.
export fn create(id: Str, scopeId: Str, draft: &Mutation.Draft, others: &Map[Str, Graph.Graph]) -> Result[Graph.Graph, Problem.Problem]
/// Whether a graph is well formed within its scope: unique ids, existing endpoints, limits, acyclic dependencies, and acyclic, shallow containment.
export fn check(graph: &Graph.Graph, others: &Map[Str, Graph.Graph]) -> Result[(), Problem.Problem]
/// Whether an edge respects what a channel is: no channel subscribes to another, and no dependency waits on a channel, which never produces a result.
export fn channelEdgeHolds(graph: &Graph.Graph, edge: &Graph.Edge) -> Bool
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Graph]] · [[src/Domain/Mutation]] · [[src/Domain/Problem]] · [[src/Engine/Topology]] · [[src/Utils/JsonRead]] · [[src/Utils/Pointer]]
- **Standard library:** `Std.Json`, `Std.List`, `Std.Map`
- **Consumed by:** [[src/Services/Fabric]]

<!-- authored -->
## Algorithm

1. Refuse a stale revision and more operations than the contract allows.
2. Apply each step through the effect [[src/Engine/Mutations]] chooses for it once (`stepOf`); the first failing step aborts the whole mutation.
3. Check the result: limits, unique ids, edges between existing participants, acyclic dependency edges, contained graphs that exist, acyclic containment across the scope, and containment depth.
4. Raise the revision by exactly one.

## Negative Logic

- ❌ Never check flow edges for cycles; debates and loops are legal.
- ❌ Never keep a partially applied mutation.

## Grill Log

- **Q:** Check cycles incrementally or on the whole graph? **A:** On the whole graph after the steps. **Rationale:** a mutation may remove an edge and add another; only the end state matters. **Rejected:** per-step checks, which refuse valid reorderings.
- **Q:** How is a cycle reported? **A:** As its members in order, found from a strongly connected component and a shortest path back to its start. **Rationale:** a caller can see exactly which edge to drop. **Rejected:** a bare boolean.
<!-- /authored -->

## Referenced by

[[src/Engine/_MOC]] · [[src/Services/Fabric]] · [[test/Engine/MutationsTest]] · [[test/Support/Fixtures]]
