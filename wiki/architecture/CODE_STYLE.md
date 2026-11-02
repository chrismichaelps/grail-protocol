---
type: architecture
status: ACTIVE
tags: [architecture, readability, code]
---

# Code style

## Statement spacing

A blank line goes before an `if`, `for`, or `while` that follows a variable declaration, including a declaration that spans several lines. Consecutive declarations stay together with no blank line between them, and consecutive `if` checks stay together too. Separate phases of a function with one blank line; never open or close a body with one. [[tools/Spacing]] enforces this on `src/`, `test/`, and `tools/`, and refuses files over 500 lines.

```pudu
let state = Store.read(&runtime.store, call.scopeId) ?
let authority = authorized(&state, call, runtime.secret, Runtime.now()) ?

if !Delivery.visible(&record, &authority) { return Err(notFound()) }
```

## Constants

Values live in `Constants/` (hand-written) or `Contract/` (projected). A module never spells a name, limit, message, separator, or member literally. A table that binds names to behavior — a factory of handlers, step readers, kind behaviors, shapes, transitions — lives beside the behavior it selects, keyed by those constants.

## Factories

A choice made by name is made once, in a table, and the rest of the code asks the table: [[src/Engine/Kinds]], [[src/Engine/Routing]], [[src/Engine/Mutations]], [[src/Engine/Codec/Graph]], [[src/Engine/Codec/Shapes]], [[src/Engine/Lifecycle]], [[src/Web/Handlers]].

## Comments

Every file, exported type, and service anchor carries `/** @Layer.Entity.Role — intent */`; every exported function and constant carries one `///` line. Rationale lives in the mirrored page.

## Referenced by

[[architecture/_MOC]] · [[grammar/pudu]] · [[tools/Spacing]]
