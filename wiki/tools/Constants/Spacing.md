---
type: tool
path: "@root/tools/Constants/Spacing.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Constants.Spacing

> @Tools.Constants.Spacing — the statement spacing rules and the files they cover

## Purpose

The statement spacing rules and the files they cover.

## Interface

### Signatures

```pudu
/// Words that open a declaration statement.
export const DECLARATIONS: Array[Str] = ["let ", "var ", "const ", "export const "]
/// Words that open a statement which needs a blank line after a declaration.
export const GUARDED: Array[Str] = ["if ", "for ", "while "]
/// The folders checked when none is named.
export const ROOTS: Array[Str] = ["src", "test", "tools"]
/// The longest a source file may grow.
export const LINES_MAX: Int = 500
/// The extension of a source file.
export const SOURCE_EXTENSION: Str = ".pudu"
/// Folders whose files are generated and judged by their generator instead.
export const EXCLUDED: Array[Str] = ["src/Contract"]
/// Why a guard right after a declaration is refused.
export const NEEDS_BREAK: Str = "add a blank line between the declaration and this statement"
/// Why a blank line between two declarations is refused.
export const SPLIT_DECLARATIONS: Str = "keep consecutive declarations together"
/// Why a long file is refused.
export const TOO_LONG: Str = "split this file; it is longer than the limit"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Constants/_MOC]]
