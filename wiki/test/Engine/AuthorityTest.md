---
type: test
path: "@root/test/Engine/AuthorityTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Engine.AuthorityTest

> @Test.Engine.Authority.Suite — tokens verify only in their scope, expire, and only ever narrow when delegated

## Purpose

Tokens verify only in their scope, expire, and only ever narrow when delegated.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Constants/Security]] · [[src/Contract/Limits]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Problem]] · [[src/Engine/Authority]]
- **Standard library:** `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]]
