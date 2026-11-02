---
type: module
path: "@root/src/Validation/Graph.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, validation]
---

# Validation.Graph

> @Validation.Graph.Rules — what drafts and mutations must hold beyond their shape

## Purpose

What drafts and mutations must hold beyond their shape.

## Interface

### Signatures

```pudu
/// Rules for a graph about to be created.
export fn draft() -> Validator.Validator[Mutation.Draft]
/// Rules for a mutation.
export fn mutation() -> Validator.Validator[Mutation.Mutation]
/// Whether a participant names a graph exactly when it is a graph participant.
export fn participantHolds(member: &Graph.Participant) -> Bool { (member.kind == Vocabulary.PARTICIPANT_GRAPH) == Option.isSome(&member.graph) }
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Members]] · [[src/Contract/Vocabulary]] · [[src/Domain/Graph]] · [[src/Domain/Mutation]]
- **Packages:** `PuduLangValidator`
- **Standard library:** `Std.List`, `Std.Option`
- **Consumed by:** [[src/App/Pipeline]]

## Referenced by

[[src/App/Pipeline]] · [[src/Validation/_MOC]]
