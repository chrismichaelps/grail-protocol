---
type: test
path: "@root/test/Engine/CustodyTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, engine, custody]
---

# Engine.CustodyTest

## Purpose

Pins the edges of [[src/Engine/Custody]] at a fixed time: a sealed value opens only in its own scope, a secret is expired at its expiry and usable just before, the audience receives the value while others and the same participant in another graph receive the reference, an object with more than the marker is not a reference, references in lists are found once each, and screening refuses a body that holds a value.

Reveal regressions also cover empty issuer chains, foreign graph records, and stricter sender/kind policies after rotation.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Custody]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Scope]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Custody]] · [[test/Support/Fixtures]] · [[test/Support/Runner]]
- **Standard library:** `Std.Bytes`, `Std.Json`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]] · [[decisions/ADR-0010-custody]]
