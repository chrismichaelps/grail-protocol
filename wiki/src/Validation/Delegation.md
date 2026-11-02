---
type: module
path: "@root/src/Validation/Delegation.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, validation]
---

# Validation.Delegation

> @Validation.Delegation.Rules — what a delegation request must hold beyond its shape

## Purpose

What a delegation request must hold beyond its shape.

## Interface

### Signatures

```pudu
/// Rules for a delegation request.
export fn rules() -> Validator.Validator[Capability.Request]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Members]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]]
- **Packages:** `PuduLangValidator`
- **Consumed by:** [[src/App/Pipeline]]

## Referenced by

[[src/App/Pipeline]] · [[src/Validation/_MOC]]
