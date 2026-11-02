---
type: tool
path: "@root/tools/Spacing/Rules.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Spacing.Rules

> @Tools.Spacing.Rules — finds statements spaced against the code style

## Purpose

Finds statements spaced against the code style.

## Interface

### Signatures

```pudu
export type Finding = { line: Int, reason: Str }
/// Every spacing finding in one file's text.
export fn check(text: Str) -> Array[Finding]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Spacing/_MOC]]
