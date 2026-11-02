---
type: module
path: "@root/src/Engine/Gating.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Gating

> @Engine.Gating.Dependencies — whether a task's dependencies produced results among its ancestors

## Purpose

Whether a task's dependencies produced results among its ancestors.

## Interface

### Signatures

```pudu
/// The dependencies of `target` in `graph` that are not among the participants whose results the task descends from.
export fn unmet(graph: &Graph.Graph, target: Str, producers: &Set[Str]) -> Array[Str]
```

### Linkage

- **Requires:** [[src/Domain/Graph]]
- **Consumed by:** [[src/Engine/Admission]]

## Referenced by

[[src/Engine/Admission]] · [[src/Engine/_MOC]]
