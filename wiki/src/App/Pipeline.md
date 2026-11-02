---
type: module
path: "@root/src/App/Pipeline.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Pipeline

> @App.Pipeline.Behaviors — what every message passes through

## Purpose

What every message passes through.

## Interface

### Signatures

```pudu
/// The registrations every mediator starts with: the recorder outermost, the alarm, and validation of every input with rules beyond its shape.
export fn registrations(kinds: &Messages.Kinds, messages: &Logger.Logger) -> Array[Registration.Registration]
/// The problem a mediator failure stands for.
export fn problemOf(failure: &Messaging.Failure[Problem.Problem]) -> Problem.Problem
```

### Linkage

- **Requires:** [[src/App/Messages]] · [[src/Constants/Extras]] · [[src/Constants/Logging]] · [[src/Constants/Server]] · [[src/Constants/Text]] · [[src/Contract/Problems]] · [[src/Domain/Capability]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Utils/Pointer]] · [[src/Validation/Delegation]] · [[src/Validation/Envelope]] · [[src/Validation/Graph]]
- **Packages:** `PuduLangLog`, `PuduLangMediator`, `PuduLangValidator`
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/App/Assembly]]

## Referenced by

[[src/App/Assembly]] · [[src/App/_MOC]]
