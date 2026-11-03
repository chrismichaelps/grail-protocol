---
type: module
path: "@root/src/Domain/Problem.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Problem

> @Domain.Problem.Refusal — why the fabric refused an operation

## Purpose

Why the fabric refused an operation.

## Interface

### Signatures

```pudu
export type Problem = { code: Str, detail: Str, extras: Array[(Str, Json.Json)] }
export type Violation = { path: Str, message: Str }
/// A problem with a code from the registry and a detail for people.
export fn of(code: Str, detail: Str) -> Problem { Problem{code: code, detail: detail, extras: []} }
/// The problem with one more member.
export fn withMember(problem: &Problem, name: Str, value: Json.Json) -> Problem
/// A refusal of a request that does not match the contract.
export fn invalid(violations: &Array[Violation]) -> Problem
/// A violation at a path.
export fn violation(path: Str, message: Str) -> Violation { Violation{path: path, message: message} }
/// The registry entry of a problem's code; unregistered codes are reported as unavailable.
export fn entryOf(problem: &Problem) -> Codes.Entry
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Contract/Problems]]
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/Api/Bridge]] · [[src/App/Assembly]] · [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Messages]] · [[src/App/Pipeline]] · [[src/App/Resilience]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Token]] · [[src/Engine/Custody]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Runtime]] · [[src/Services/Store]] · [[src/Web/Caller]] · [[src/Web/Handlers]] · [[src/Web/Lines]] · [[src/Web/Respond]] · [[src/Web/Router]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/MutationsTest]] · [[test/Engine/ShapesTest]] · [[test/Support/Fixtures]]

## Referenced by

[[src/Domain/_MOC]] · [[src/Api/Bridge]] · [[src/App/Assembly]] · [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Messages]] · [[src/App/Pipeline]] · [[src/App/Resilience]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Token]] · [[src/Engine/Custody]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Runtime]] · [[src/Services/Store]] · [[src/Web/Caller]] · [[src/Web/Handlers]] · [[src/Web/Lines]] · [[src/Web/Respond]] · [[src/Web/Router]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/MutationsTest]] · [[test/Engine/ShapesTest]] · [[test/Support/Fixtures]]
