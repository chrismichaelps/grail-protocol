---
type: test
path: "@root/test/Security/CustodyMetadataTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, security]
---

# Security.CustodyMetadataTest

## Purpose

Held values cannot enter graph names, mutation payloads, exported handoff identifiers, or public secret descriptions and names. Deposits check their own incoming value and rotations check the previous value before replacing it. Refusals do not repeat the value, change revisions, append ledger entries, or store rejected metadata. Three caught graph writes revoke the presenting token. Ordinary graph and metadata writes remain available.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[test/Support/Fabric]] · [[test/Support/Runner]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Http`, `Std.Json`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]]
