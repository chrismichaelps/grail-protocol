---
type: test
path: "@root/test/Security/CustodyTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, security, custody]
---

# Security.CustodyTest

## Purpose

A planning agent uses a key it never sees, through the HTTP router. Deposits answer without the value, no operation reads it back, and agents can list names and policies. The stored envelope, the ledger, and traces keep only the reference; the executor's delivery holds the value. Results that repeat the value as written, in base64, or in hex are refused. References to a person, from an unlisted sender, in an unlisted kind, to an unknown name, past their last use, or after expiry are refused. Rotation reveals the new value, deletion stops pending references from resolving, a handoff names what it needs without carrying a value, and an intact handoff or a bridged message that smuggles a held value is refused.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Engine/Handoff]] · [[src/Engine/Ledger]] · [[src/Utils/JsonRead]] · [[test/Support/Fabric]] · [[test/Support/Runner]]
- **Standard library:** `Std.Bytes`, `Std.Http`, `Std.Http.Server.Route`, `Std.Json`, `Std.List`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]] · [[decisions/ADR-0010-custody]]
