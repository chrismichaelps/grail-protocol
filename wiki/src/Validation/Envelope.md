---
type: module
path: "@root/src/Validation/Envelope.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, validation]
---

# Validation.Envelope

> @Validation.Envelope.Rules — what an envelope must hold beyond its shape

## Purpose

What an envelope must hold beyond its shape.

## Interface

### Signatures

```pudu
/// Rules every envelope meets before admission.
export fn rules() -> Validator.Validator[Envelope.Envelope]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Members]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]]
- **Packages:** `PuduLangValidator`
- **Standard library:** `Std.Option`
- **Consumed by:** [[src/App/Pipeline]]

## Referenced by

[[src/App/Pipeline]] · [[src/Validation/_MOC]]
