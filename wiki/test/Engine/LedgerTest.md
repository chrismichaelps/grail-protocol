---
type: test
path: "@root/test/Engine/LedgerTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Engine.LedgerTest

> @Test.Engine.Ledger.Suite — canonical form, digests, and links match vectors computed elsewhere

## Purpose

Canonical form, digests, and links match vectors computed elsewhere.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Ledger]] · [[src/Utils/Canonical]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Io`, `Std.Json`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]]
