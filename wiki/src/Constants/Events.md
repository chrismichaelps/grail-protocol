---
type: module
path: "@root/src/Constants/Events.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Events

> @Constants.Events.Lifecycle — the events that move a task lifecycle

## Purpose

The events that move a task lifecycle.

## Interface

### Signatures

```pudu
/// The recipient reports progress.
export const PROGRESS: Str = "progress"
/// The recipient needs more input.
export const INPUT: Str = "input"
/// The task finished with a result.
export const COMPLETE: Str = "complete"
/// The task finished with an error.
export const FAIL: Str = "fail"
/// The task's source withdrew it.
export const CANCEL: Str = "cancel"
/// The task's deadline passed.
export const EXPIRE: Str = "expire"
/// What separates a state from an event in a transition key.
export const ON: Str = ">"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Engine/Causality]] · [[src/Engine/Kinds]] · [[src/Engine/Lifecycle]]

## Referenced by

[[src/Constants/_MOC]] · [[src/Engine/Causality]] · [[src/Engine/Kinds]] · [[src/Engine/Lifecycle]]
