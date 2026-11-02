---
type: test
path: "@root/test/Security/AttackTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Security.AttackTest

> @Test.Security.Attack.Suite — forgery, escalation, isolation, poisoning, abuse, and exhaustion attempts all fail safely

## Purpose

Forgery, escalation, isolation, poisoning, abuse, and exhaustion attempts all fail safely. Proxy identity checks cover disabled forwarding, case-insensitive header lookup, trimming, IPv6, and fallback to the connection host for missing or blank headers.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Ledger]] · [[src/Engine/Ledger]] · [[src/Utils/JsonRead]] · [[src/Web/Peers]]
- **Standard library:** `Std.Bytes`, `Std.Http`, `Std.Http.Server.Route`, `Std.Map`, `Std.Json`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]]
