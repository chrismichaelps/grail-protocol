---
type: tool
path: "@root/tools/Contract/Emit.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Contract.Emit

> @Tools.Contract.Emitter — renders the projected contract modules

## Purpose

Renders the projected contract modules.

## Interface

### Signatures

```pudu
/// Every projected file: its path and its text.
export fn files(contract: &Read.Contract) -> Array[(Str, Str)]
/// A name in constant case: `envelopeBytes` is `ENVELOPE_BYTES`, `tool.call` is `TOOL_CALL`, `*` is `ALL`.
export fn constantName(name: Str) -> Str
/// Text as a source string literal.
export fn literal(text: Str) -> Str
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Char`
- **Consumed by:** the runner

## Referenced by

[[tools/Contract/_MOC]]
