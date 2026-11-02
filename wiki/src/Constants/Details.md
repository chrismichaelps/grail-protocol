---
type: module
path: "@root/src/Constants/Details.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Details

> @Constants.Details.Messages — what each refusal tells a person

## Purpose

What each refusal tells a person.

## Interface

### Signatures

```pudu
/// No token, or a token that does not verify.
export const UNAUTHORIZED: Str = "present a valid capability token for this scope"
/// The token lacks an ability.
export const FORBIDDEN: Str = "the token does not grant this ability"
/// Anything missing, including anything in another scope.
export const NOT_FOUND: Str = "nothing with that name exists here"
/// The envelope id was used before.
export const DUPLICATE_TRANSFER: Str = "an envelope with this id was already accepted"
/// The graph id was used before.
export const DUPLICATE_GRAPH: Str = "a graph with this id already exists"
/// A participant or edge id was used before.
export const DUPLICATE_MEMBER: Str = "an object with this id already exists in the graph"
/// The token id was used before.
export const DUPLICATE_TOKEN: Str = "a token with this id was already issued"
/// A stale revision.
export const REVISION_CONFLICT: Str = "the graph changed since the revision you read"
/// A reused delivery key.
export const KEY_REUSED: Str = "this delivery key was used for a different envelope"
/// The target resolved to nobody.
export const NO_ROUTE: Str = "no flow edge carries this kind from the source to the target"
/// The sender is not in the graph.
export const UNKNOWN_SOURCE: Str = "the source is not a participant of this graph"
/// A dependency has not produced a result among the envelope's ancestors.
export const DEPENDENCY_UNMET: Str = "a dependency has not produced a result among this task's ancestors"
/// A mutation would close a cycle.
export const CYCLE: Str = "this change would close a cycle"
/// A lifecycle would move illegally.
export const INVALID_TRANSITION: Str = "this envelope cannot move the task from its current state"
/// Only the task's recipients may answer it.
export const NOT_RECIPIENT: Str = "only a recipient of the task may answer it"
/// Only the task's source may cancel it.
export const NOT_SOURCE: Str = "only the source of the task may cancel it"
/// A parent is missing.
export const UNKNOWN_PARENT: Str = "a parent is not in the ledger"
/// A kind needs a parent of a certain kind.
export const PARENT_REQUIRED: Str = "this kind must name the envelope it answers among its parents"
/// A stream is closed.
export const STREAM_CLOSED: Str = "the stream is closed"
/// A count is too large.
export const LIMIT_EXCEEDED: Str = "a limit was exceeded"
/// A size is too large.
export const TOO_LARGE: Str = "the payload is larger than the limit"
/// The sender's clock is ahead.
export const CLOCK_SKEW: Str = "the sender's clock is too far ahead of the fabric"
/// The deadline passed.
export const EXPIRED: Str = "the deadline passed before the envelope was accepted"
/// The version is not supported.
export const UNSUPPORTED_VERSION: Str = "this protocol version is not supported"
/// A kind the fabric writes itself.
export const RESERVED_KIND: Str = "this kind is written by the fabric and cannot be sent"
/// A delegation that widens authority.
export const WIDENING: Str = "a delegated token may only narrow its parent"
/// The scope of a body differs from the path.
export const SCOPE_MISMATCH: Str = "the envelope's scope differs from the token's"
/// The source is not who the token acts for.
export const SOURCE_MISMATCH: Str = "the token does not act for this source"
/// The body is not JSON.
export const NOT_JSON: Str = "the body is not JSON"
/// A member is missing.
export const MISSING_MEMBER: Str = "is required"
/// A member is not allowed.
export const UNKNOWN_MEMBER: Str = "is not a member of this object"
/// A member has the wrong type or value.
export const WRONG_VALUE: Str = "has the wrong type or value"
/// What follows the count of refused members.
export const INVALID_MEMBERS: Str = " member(s) do not match the contract"
/// An effectively-once envelope without a key.
export const KEY_REQUIRED: Str = "effectively-once delivery needs a key"
/// A sealed payload addressed to nobody.
export const SEALED_FOR_NOBODY: Str = "a sealed payload names at least one recipient"
/// A graph participant without a graph, or a graph named by another kind.
export const GRAPH_PARTICIPANT: Str = "a graph participant names its graph, and only graph participants do"
/// An edge from a participant to itself.
export const SELF_EDGE: Str = "an edge joins two different participants"
/// A delegation window that ends before it starts.
export const EMPTY_WINDOW: Str = "a token expires after it becomes valid"
/// A delegation that grants every ability.
export const DELEGATED_ALL: Str = "only the scope owner may grant every ability"
/// The store could not be locked.
export const STORE_UNAVAILABLE: Str = "the fabric's state is unavailable"
/// Random bytes could not be read.
export const ENTROPY_UNAVAILABLE: Str = "the fabric could not draw random bytes"
/// Only a participant, or the owner, may pull its own deliveries.
export const NOT_YOUR_DELIVERIES: Str = "a token may pull only the deliveries of the participant it acts for"
/// The bridged message is not a JSON-RPC message.
export const NOT_RPC: Str = "the body is not a JSON-RPC 2.0 message"
/// An id in the range the fabric writes itself.
export const RESERVED_ID: Str = "ids beginning with mutation: are written by the fabric"
/// Only the issuer of a token, or the owner, may revoke it.
export const NOT_ISSUER: Str = "only the issuer of a token, or the scope owner, may revoke it"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Api/Bridge]] · [[src/Domain/Problem]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Erasure]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Services/Fabric]] · [[src/Services/Runtime]] · [[src/Services/Store]] · [[src/Validation/Delegation]] · [[src/Validation/Envelope]] · [[src/Validation/Graph]] · [[src/Web/Caller]] · [[src/Web/Router]]

## Referenced by

[[src/Api/Bridge]] · [[src/Constants/_MOC]] · [[src/Domain/Problem]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Erasure]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Services/Fabric]] · [[src/Services/Runtime]] · [[src/Services/Store]] · [[src/Validation/Delegation]] · [[src/Validation/Envelope]] · [[src/Validation/Graph]] · [[src/Web/Caller]] · [[src/Web/Router]]
