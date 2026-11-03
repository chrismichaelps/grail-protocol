---
type: module
path: "@root/src/Domain/Graph.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Graph

> @Domain.Graph.Topology — participants, edges, and their lookups

## Purpose

Participants, edges, and their lookups.

## Interface

### Signatures

```pudu
export type Participant = { id: Str, kind: Str, roles: Array[Str], abilities: Array[Str], graph: Option[Str] }
export type Edge = { id: Str, from: Str, to: Str, relation: Str, kinds: Array[Str] }
export type Graph = { id: Str, scopeId: Str, revision: Int, participants: Array[Participant], edges: Array[Edge] }
/// The participant with an id.
export fn participant(graph: &Graph, id: Str) -> Option[Participant]
/// Whether the graph has a participant with an id.
export fn hasParticipant(graph: &Graph, id: Str) -> Bool { Option.isSome(&participant(graph, id)) }
/// Whether the graph has an edge with an id.
export fn hasEdge(graph: &Graph, id: Str) -> Bool { List.any(&graph.edges, |edge: Edge| edge.id == id) }
/// The edges of one relation.
export fn edgesOf(graph: &Graph, relation: Str) -> Array[Edge] { graph.edges.filter(|edge: Edge| edge.relation == relation) }
/// The participants a dependency edge says `to` waits on.
export fn dependenciesOf(graph: &Graph, to: Str) -> Array[Str]
/// Whether a flow edge from one participant to another carries a kind.
export fn carries(graph: &Graph, from: Str, to: Str, kind: Str) -> Bool
/// The graphs this graph's graph participants stand for.
export fn contained(graph: &Graph) -> Array[Str] { Option.present(&graph.participants.map(|member: Participant| member.graph)) }
```

### Linkage

- **Requires:** [[src/Contract/Vocabulary]]
- **Standard library:** `Std.List`, `Std.Option`
- **Consumed by:** [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Messages]] · [[src/Domain/Mutation]] · [[src/Domain/Scope]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Custody]] · [[src/Engine/Gating]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Mutations]] · [[src/Engine/Routing]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Validation/Graph]] · [[src/Web/Handlers]] · [[test/Engine/MutationsTest]] · [[test/Support/Fixtures]]

## Referenced by

[[src/Domain/_MOC]] · [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Messages]] · [[src/Domain/Mutation]] · [[src/Domain/Scope]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Custody]] · [[src/Engine/Gating]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Mutations]] · [[src/Engine/Routing]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Validation/Graph]] · [[src/Web/Handlers]] · [[test/Engine/MutationsTest]] · [[test/Support/Fixtures]]
