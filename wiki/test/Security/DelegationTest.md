---
type: test
path: "@root/test/Security/DelegationTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, security]
---

# Security.DelegationTest

## Purpose

A participant with `token.delegate` and `transfer.receive` cannot turn itself into the reserved owner principal. The attack first verifies that its direct inbox request is forbidden, then attempts delegation to `owner`, pulling an executor's secret-bearing delivery, and revoking the root token. Only synthetic credentials are used. Ordinary participant delegation remains available after refusal.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[test/Support/Fabric]] · [[test/Support/Runner]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Http`, `Std.Json`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]]
