---
type: test
path: "@root/test/Security/CustodyDelegationTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, security]
---

# Security.CustodyDelegationTest

## Purpose

A child token named after an executor cannot reveal a value its parent was not authorized to receive. Refused revelation leaves at-most-once deliveries available to a legitimate executor and does not increment reveal counters. Authorized executor delegation still works with a spent admission budget. Rotation rechecks the original sender, so queued calls do not inherit a replacement key under a stricter policy; new compliant calls work.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[test/Support/Fabric]] · [[test/Support/Runner]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Http`, `Std.Json`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]]
