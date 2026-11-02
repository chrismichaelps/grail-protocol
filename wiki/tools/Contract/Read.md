---
type: tool
path: "@root/tools/Contract/Read.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Contract.Read

> @Tools.Contract.Reader — the parts of the contract the projection needs

## Purpose

The parts of the contract the projection needs.

## Interface

### Signatures

```pudu
export type Operation = { … }
export type Enumeration = { prefix: Str, collection: Str, values: Array[Str] }
export type ProblemCode = { code: Str, status: Int, title: Str }
export type Members = { schema: Str, allowed: Array[Str], required: Array[Str], closed: Bool, extensible: Bool }
export type Contract = { … }
/// The contract read from the document's text, or why it cannot be.
export fn read(source: Str) -> Result[Contract, Str]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Json`, `Std.Option`, `Std.Result`
- **Consumed by:** the runner

## Referenced by

[[tools/Contract/_MOC]]
