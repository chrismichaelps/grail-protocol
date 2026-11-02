---
type: module
path: "@root/src/Domain/Lifecycle.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Lifecycle

> @Domain.Lifecycle.Task — where a task stands

## Purpose

Where a task stands. Each task retains the resolved routing paths from admission, independently of later graph changes. Replies preserve those paths when the lifecycle moves.

## Interface

### Signatures

```pudu
export type Lifecycle = { … }
```

### Linkage

- **Requires:** [[src/Domain/Envelope]]
- **Consumed by:** [[src/Domain/Scope]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[test/Engine/AdmissionTest]]

## Referenced by

[[src/Domain/Scope]] · [[src/Domain/_MOC]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[test/Engine/AdmissionTest]]
