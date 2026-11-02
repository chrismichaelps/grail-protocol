---
type: tool
path: "@root/tools/Layers/Graph.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Layers.Graph

> @Tools.Layers.Graph — imports, cycles, depth, and violations of a module graph

## Purpose

Imports, cycles, depth, and violations of a module graph.

## Interface

### Signatures

```pudu
export type Unit = { name: Str, imports: Array[Str] }
export type Violation = { from: Str, target: Str, reason: Str }
export type Report = { … }
/// A module's name and imports, read from its source; `None` without exactly one module line.
export fn parse(source: Str) -> Option[Unit]
/// The report of a graph judged by a catalog.
export fn analyze(units: &Array[Unit], judge: fn(Str, Str, &Set[Str]) -> Option[Str]) -> Report
/// The report as lines of text.
export fn render(report: &Report) -> Array[Str]
/// Whether the graph has no violations and no cycles.
export fn passed(report: &Report) -> Bool
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Map`
- **Consumed by:** the runner

## Referenced by

[[tools/Layers/_MOC]]
