---
type: test
path: "@root/test/Engine/AdmissionTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Engine.AdmissionTest

> @Test.Engine.Admission.Suite — routing, dependency gating, lifecycles, deduplication, and streams

## Purpose

Routing, dependency gating, lifecycles, deduplication, and streams.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Contract/Limits]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Problem]] · [[src/Domain/Scope]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Envelope]]
- **Standard library:** `Std.Json`, `Std.Map`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]]
