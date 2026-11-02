---
type: module
path: "@root/src/App/Messages.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Messages

> @App.Messages.Vocabulary — every request the fabric answers, one kind per contract operation

## Purpose

Every request the fabric answers, one kind per contract operation.

## Interface

### Signatures

```pudu
export type Kinds = { … }
/// Every kind, named after the contract operation it serves.
export fn kinds() -> Kinds
```

### Linkage

- **Requires:** [[src/Contract/Operations]] · [[src/Domain/Capability]] · [[src/Domain/Graph]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Transfer]]
- **Packages:** `PuduLangMediator`
- **Consumed by:** [[src/App/Assembly]] · [[src/App/Handlers]] · [[src/App/Pipeline]] · [[src/App/Resilience]]

## Referenced by

[[src/App/Assembly]] · [[src/App/Handlers]] · [[src/App/Pipeline]] · [[src/App/Resilience]] · [[src/App/_MOC]]
