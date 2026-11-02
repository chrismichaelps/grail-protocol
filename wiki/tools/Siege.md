---
type: tool
path: "@root/tools/Siege.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Siege

> @Tools.Siege.Pressure — floods a live fabric and holds its pulls open, then judges how it held up

## Purpose

Floods a live fabric and holds its pulls open, then judges how it held up.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Concurrent`, `Std.Env`, `Std.Http`, `Std.Http.Client`, `Std.Io`, `Std.List`, `Std.Math`, `Std.Option`, `Std.Result`, `Std.Time`, `Std.Url`
- **Consumed by:** the runner

## Referenced by

[[tools/_MOC]]
