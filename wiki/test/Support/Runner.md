---
type: test
path: "@root/test/Support/Runner.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Support.Runner

> @Test.Support.Runner — runs a suite and names every check that did not hold

## Purpose

Runs a suite and names every check that did not hold.

## Interface

### Signatures

```pudu
/// The suite's result for the runner, with each failure written to standard error.
export fn finish(suite: &Test.Suite) -> Int
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Io`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Support/_MOC]]
