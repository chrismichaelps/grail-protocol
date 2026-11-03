---
type: module
path: "@root/src/Engine/Disguise.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Disguise

> @Engine.Disguise.Forms — the forms a secret value can take inside a message, which the custody tripwire looks for

## Purpose

The forms a secret value can take inside a message, which the custody tripwire looks for.

## Interface

### Signatures

```pudu
/// Every form a value is looked for in: as written, escaped inside JSON text, reversed, percent-encoded, in hex of either case, in base64 of both alphabets at every byte alignment, and every aligned fragment, so any contiguous piece of at least twice the fragment length less one is caught.
export fn forms(value: Str) -> Array[Str]

/// The windows of a value a fragment long, one starting at every multiple of the fragment length, the last moved back to end with the value. A value shorter than a fragment has none.
export fn fragments(value: Str) -> Array[Str]

/// The value percent-encoded, with unreserved characters kept and every other byte written as `%XX`.
export fn percentEncoded(value: Str) -> Str
```

### Linkage

- **Requires:** [[src/Constants/Custody]] · [[src/Contract/Limits]]
- **Standard library:** `Std.Bytes`, `Std.Char`, `Std.Json`, `Std.Math`
- **Consumed by:** [[src/Engine/Custody]] · [[test/Engine/DisguiseTest]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Engine/Custody]] · [[test/Engine/DisguiseTest]]
