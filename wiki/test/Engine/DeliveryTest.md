---
type: test
path: "@root/test/Engine/DeliveryTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Engine.DeliveryTest

> @Test.Engine.Delivery.Suite — pages respect their limit, cursors acknowledge, and visibility hides

## Purpose

Pages respect their limit, cursors acknowledge, and visibility hides.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Contract/Limits]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Scope]] · [[src/Domain/Transfer]] · [[src/Engine/Delivery]]
- **Standard library:** `Std.Json`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]]
