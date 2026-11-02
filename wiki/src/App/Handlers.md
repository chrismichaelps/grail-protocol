---
type: module
path: "@root/src/App/Handlers.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Handlers

> @App.Handlers.Registrations — each message kind bound to its use case

## Purpose

Each message kind bound to its use case.

## Interface

### Signatures

```pudu
/// The handler of every kind.
export fn registrations(kinds: &Messages.Kinds, runtime: &Runtime.Runtime) -> Array[Registration.Registration]
```

### Linkage

- **Requires:** [[src/App/Messages]] · [[src/Domain/Capability]] · [[src/Domain/Request]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/Runtime]]
- **Packages:** `PuduLangMediator`
- **Consumed by:** [[src/App/Assembly]]

## Referenced by

[[src/App/Assembly]] · [[src/App/_MOC]]
