---
type: tool
path: "@root/tools/Constants/Mutate.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Constants.Mutate

> @Tools.Constants.Mutate — what the mutation harness changes and how long it waits

## Purpose

What the mutation harness changes and how long it waits.

## Interface

### Signatures

```pudu
/// Operator replacements, tried at every code position in this order.
export const OPERATORS: Array[(Str, Str)]
/// Longest a mutant's check or test run may take before it counts as killed.
export const MUTANT_TIMEOUT_MS: Int = 60000
/// The pure layers, mutated alone by `--pure`.
export const PURE: Array[Str] = ["src/Domain", "src/Engine", "src/Utils", "src/Validation"]
/// The folder mutated when no file or layer is named.
export const SOURCE_ROOT: Str = "src"
/// The folder of tests run against each mutant.
export const TEST_ROOT: Str = "test"
/// The extension of a source file.
export const SOURCE_EXTENSION: Str = ".pudu"
/// Folders never mutated: the projected contract is regenerated, not written.
export const EXCLUDED: Array[Str] = ["src/Contract"]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Constants/_MOC]]
