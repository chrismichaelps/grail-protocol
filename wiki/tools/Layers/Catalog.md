---
type: tool
path: "@root/tools/Layers/Catalog.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Layers.Catalog

> @Tools.Layers.Catalog — judges one import against the layer table

## Purpose

Judges one import against the layer table.

## Interface

### Signatures

```pudu
/// The folder a module belongs to: its first segment.
export fn folderOf(name: Str) -> Str
/// Why an import is refused, or `None` when the catalog allows it.
export fn judge(from: Str, target: Str, known: &Set[Str]) -> Option[Str]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Layers/_MOC]]
