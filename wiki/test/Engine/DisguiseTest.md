---
type: test
path: "@root/test/Engine/DisguiseTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test, engine, custody]
---

# Engine.DisguiseTest

## Purpose

Pins every form [[src/Engine/Disguise]] produces, exactly. It checks the fragment windows of values shorter than, equal to, twice, and two and a half times a fragment; percent-encoding of reserved, unreserved, and multi-byte characters; the value reversed and in both cases of hex; the whole base64; and the value found inside base64 streams at every alignment.

## Interface

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Engine/Disguise]] · [[test/Support/Runner]]
- **Standard library:** `Std.Bytes`, `Std.List`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]] · [[decisions/ADR-0010-custody]]
