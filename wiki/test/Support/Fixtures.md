---
type: test
path: "@root/test/Support/Fixtures.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Support.Fixtures

> @Test.Support.Fixtures — scopes, graphs, envelopes, and tokens the suites share

## Purpose

Scopes, graphs, envelopes, and tokens the suites share.

## Interface

### Signatures

```pudu
/// The fabric secret every fixture signs with.
export const SECRET: Str = "fixture-secret-0123456789abcdef-0123"
/// The scope every fixture lives in.
export const SCOPE: Str = "demo"
/// The graph every fixture routes through.
export const GRAPH: Str = "team"
/// The time every fixture happens at.
export const NOW: Int = 1800000000000
/// A day in milliseconds.
export const DAY: Int = 86400000
/// A participant with roles and abilities.
export fn member(id: Str, roles: &Array[Str], abilities: &Array[Str]) -> Graph.Participant
/// An edge of a relation carrying every kind.
export fn edge(id: Str, from: Str, into: Str, relation: Str) -> Graph.Edge { Graph.Edge{id: id, from: from, to: into, relation: relation, kinds: []} }
/// A planner that reaches a writer and a reviewer, where the reviewer depends on the writer.
export fn team() -> Mutation.Draft
/// A scope holding the team graph.
export fn teamScope() -> Scope.State
/// A root token's claims for an audience with abilities.
export fn claims(id: Str, audience: Str, abilities: &Array[Str]) -> Capability.Token
/// The authority of the scope owner.
export fn owner() -> Capability.Authority
/// An envelope body in the team graph.
export fn body(id: Str, source: Str, target: Json.Json, kind: Str, parents: &Array[Str]) -> Json.Json
/// A selector naming one participant.
export fn to(id: Str) -> Json.Json { Json.object(&[("participant", Json.Text(id))]) }
/// A selector naming a role.
export fn toRole(role: Str) -> Json.Json { Json.object(&[("role", Json.Text(role))]) }
/// The scope after admitting a body as the owner, or the refusal.
export fn admitted(state: &Scope.State, sent: &Json.Json) -> Result[Scope.State, Problem.Problem]
/// The code of a refusal, or empty text for an acceptance.
export fn code[T](outcome: &Result[T, Problem.Problem]) -> Str
/// The lifecycle state of a task in a scope.
export fn stateOf(state: &Scope.State, taskId: Str) -> Str
/// The ledger vectors, computed independently of the reference implementation.
export const VECTORS: Str = "test/Fixtures/ledger-vectors.json"
/// The participants and edges of the attacked graph.
export const ATTACKED_GRAPH: Str
```

### Linkage

- **Requires:** [[src/Constants/Security]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Graph]] · [[src/Domain/Mutation]] · [[src/Domain/Problem]] · [[src/Domain/Scope]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Journal]] · [[src/Engine/Mutations]]
- **Standard library:** `Std.Json`, `Std.Map`, `Std.Result`
- **Consumed by:** the runner

## Referenced by

[[test/Support/_MOC]]
