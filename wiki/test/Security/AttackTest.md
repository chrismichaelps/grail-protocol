---
type: test
path: "@root/test/Security/AttackTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Security.AttackTest

> @Test.Security.Attack.Suite — forgery, escalation, isolation, poisoning, abuse, and exhaustion attempts all fail safely

## Purpose

Forgery, escalation, isolation, poisoning, abuse, and exhaustion attempts all fail safely.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Ledger]] · [[src/Engine/Ledger]] · [[src/Utils/JsonRead]] · [[src/Web/Peers]]
- **Standard library:** `Std.Bytes`, `Std.Http`, `Std.Json`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]]
