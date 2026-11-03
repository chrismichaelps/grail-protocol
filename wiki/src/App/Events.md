---
type: module
path: "@root/src/App/Events.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Events

> @App.Events.Notifications — what the fabric announces after a change, and who listens

## Purpose

What the fabric announces after a change, and who listens.

## Interface

### Signatures

```pudu
export type Kinds = { … }
/// Every notification kind.
export fn kinds() -> Kinds
/// The listeners: each notification is written to the server log.
export fn registrations(events: &Kinds, server: &Logger.Logger) -> Array[Registration.Registration]
```

### Linkage

- **Requires:** [[src/Constants/Logging]] · [[src/Domain/Custody]] · [[src/Domain/Graph]] · [[src/Domain/Handoff]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Transfer]]
- **Packages:** `PuduLangLog`, `PuduLangMediator`
- **Consumed by:** [[src/App/Assembly]]

## Referenced by

[[src/App/Assembly]] · [[src/App/_MOC]]
