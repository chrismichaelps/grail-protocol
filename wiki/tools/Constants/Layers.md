---
type: tool
path: "@root/tools/Constants/Layers.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Constants.Layers

> @Tools.Constants.Layers — the folders, their ranks, and what each may import

## Purpose

The folders, their ranks, and what each may import.

## Interface

### Signatures

```pudu
/// Each folder's layer.
export const RANKS: Map[Str, Int]
/// The folders each folder may import, its own included.
export const ALLOWED: Map[Str, Set[Str]]
/// The package roots each folder may import.
export const PACKAGES: Map[Str, Set[Str]]
/// Folders that may not import effectful standard modules.
export const PURE: Set[Str]
/// Standard module prefixes that reach outside the program.
export const EFFECTFUL: Array[Str]
/// Effect-free modules under an effectful prefix.
export const PURE_EXCEPTIONS: Set[Str]
/// The entry folder, which may import anything.
export const ENTRY: Str = "Main"
/// The folder scanned when no folder is named.
export const SOURCE_ROOT: Str = "src"
/// The extension of a source file.
export const SOURCE_EXTENSION: Str = ".pudu"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Constants/_MOC]]
