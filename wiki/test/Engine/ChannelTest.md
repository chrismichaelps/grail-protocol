---
type: test
path: "@root/test/Engine/ChannelTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Engine.ChannelTest

> @Test.Engine.Channel.Suite — channels fan posts out to their subscribers, keep them readable without acknowledging, and never act

## Purpose

Channels fan posts out to their subscribers, keep them readable without acknowledging, and never act.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Constants/Security]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Scope]] · [[src/Domain/Transfer]] · [[src/Engine/Delivery]] · [[src/Engine/Mutations]] · [[src/Engine/Routing]] · [[src/Validation/Graph]]
- **Standard library:** `Std.Json`, `Std.List`, `Std.Map`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]]
