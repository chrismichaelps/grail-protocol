---
type: module
path: "@root/src/Engine/Topology.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Topology

> @Engine.Topology.Acyclic — cycles and depth of dependency and containment graphs, in linear time

## Purpose

Cycles and depth of dependency and containment graphs, in linear time.

## Interface

### Signatures

```pudu
/// One cycle of a directed graph as its members in order, ending where it starts, or `None` when it has none.
export fn cycleOf(edges: &Array[(Str, Str)]) -> Option[Array[Str]]
/// The number of edges on the longest path of an acyclic graph.
export fn depthOf(edges: &Array[(Str, Str)]) -> Int
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Graph`, `Std.List`, `Std.Map`, `Std.Math`, `Std.Option`, `Std.Set`
- **Consumed by:** [[src/Engine/Mutations]]

## Referenced by

[[src/Engine/Mutations]] · [[src/Engine/_MOC]]
