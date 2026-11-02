---
type: architecture
status: ACTIVE
tags: [architecture, contract, openapi]
aliases: [Contract pipeline, Schema first]
---

# One schema, every binding

`schema/grail.openapi.json` is the only place the wire format is defined. Nothing else names an operation, a path, a status, a member, an enumeration value, a limit, a header, or a problem code.

## The pipeline

```
schema/grail.openapi.json
        │  pudu run tools/Contract.pudu
        ▼
src/Contract/  Operations · Members · Schemas · Vocabulary · Problems · Limits · Parameters · Version · Document
        │
        ├─► Web.Router        one route per operation: method, pattern, success status
        ├─► Web.Description   the same operations as a standard OpenAPI model; `undocumented` must be empty
        ├─► Web.Lines         the line binding dispatches through the same router
        ├─► Engine.Codec      every member name and requirement; Shapes reads allowed/required/closed lists
        ├─► Engine.Kinds, Engine.Lifecycle   every kind, state, and event by its generated name
        ├─► Domain.Problem    status and title of every code from the registry
        ├─► Engine.Codec.Views and discovery   every answer's member names and the published limits
        └─► GET /openapi.json serves the contract itself
```

## What a change looks like

| Change in the schema | What happens |
| --- | --- |
| A member renamed | Its constant in `Contract.Members` disappears; every codec using it stops compiling. |
| A new operation | The router refuses to start until a handler is bound; the router test fails. |
| An operation removed | Its constant disappears; its handler stops compiling. |
| A new kind, state, or problem code | A new constant appears; the kind table, transition table, or registry picks it up where it is referenced. |
| A limit changed | Every check and the discovery document follow on regeneration. |
| Any change not regenerated | `pudu run tools/Contract.pudu --check` and `tools/ContractTest.pudu` fail. |

## Grill Log

- **Q:** Build the document in code with the standard OpenAPI model and export it? **A:** No; the file is the source, and the standard model is used to prove the router serves it. **Rationale:** the file is what other implementations read, and the standard model cannot express every constraint the protocol needs (patterns, `x-` extensions, problem registry). **Rejected:** code-first description.
- **Q:** Interpret the schema at run time? **A:** Project it into typed constants. **Rationale:** the compiler then finds every place a change touches. **Rejected:** a run-time schema interpreter that fails only when a request arrives.

## Referenced by

[[architecture/_MOC]] · [[protocol/08-Bindings]] · [[protocol/12-Evolution]] · [[schema/grail.openapi]] · [[tools/Contract]]
