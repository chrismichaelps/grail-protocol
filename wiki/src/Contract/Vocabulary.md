---
type: module
path: "@root/src/Contract/Vocabulary.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Vocabulary

> @Contract.Vocabulary.Generated — every closed set of names in the contract

## Purpose

Every closed set of names in the contract. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
/// `task`.
export const KIND_TASK: Str = "task"
/// `result`.
export const KIND_RESULT: Str = "result"
/// `error`.
export const KIND_ERROR: Str = "error"
/// `progress`.
export const KIND_PROGRESS: Str = "progress"
/// `input.request`.
export const KIND_INPUT_REQUEST: Str = "input.request"
/// `cancel`.
export const KIND_CANCEL: Str = "cancel"
/// `thought`.
export const KIND_THOUGHT: Str = "thought"
/// `observation`.
export const KIND_OBSERVATION: Str = "observation"
/// `memory`.
export const KIND_MEMORY: Str = "memory"
/// `tool.call`.
export const KIND_TOOL_CALL: Str = "tool.call"
/// `tool.result`.
export const KIND_TOOL_RESULT: Str = "tool.result"
/// `stream.open`.
export const KIND_STREAM_OPEN: Str = "stream.open"
/// `stream.chunk`.
export const KIND_STREAM_CHUNK: Str = "stream.chunk"
/// `stream.close`.
export const KIND_STREAM_CLOSE: Str = "stream.close"
/// `ability.advert`.
export const KIND_ABILITY_ADVERT: Str = "ability.advert"
/// `graph.mutation`.
export const KIND_GRAPH_MUTATION: Str = "graph.mutation"
/// `bridge.rpc`.
export const KIND_BRIDGE_RPC: Str = "bridge.rpc"
/// `handoff.export`.
export const KIND_HANDOFF_EXPORT: Str = "handoff.export"
/// `handoff.import`.
export const KIND_HANDOFF_IMPORT: Str = "handoff.import"
/// Every value of the set.
export const KINDS: Array[Str]
/// `*`.
export const ABILITY_ALL: Str = "*"
/// `graph.read`.
export const ABILITY_GRAPH_READ: Str = "graph.read"
/// `graph.write`.
export const ABILITY_GRAPH_WRITE: Str = "graph.write"
/// `transfer.send`.
export const ABILITY_TRANSFER_SEND: Str = "transfer.send"
/// `transfer.receive`.
export const ABILITY_TRANSFER_RECEIVE: Str = "transfer.receive"
/// `transfer.read`.
export const ABILITY_TRANSFER_READ: Str = "transfer.read"
/// `ledger.read`.
export const ABILITY_LEDGER_READ: Str = "ledger.read"
/// `ledger.erase`.
export const ABILITY_LEDGER_ERASE: Str = "ledger.erase"
/// `token.delegate`.
export const ABILITY_TOKEN_DELEGATE: Str = "token.delegate"
/// `handoff.export`.
export const ABILITY_HANDOFF_EXPORT: Str = "handoff.export"
/// `handoff.import`.
export const ABILITY_HANDOFF_IMPORT: Str = "handoff.import"
/// Every value of the set.
export const ABILITIES: Array[Str]
/// `agent`.
export const PARTICIPANT_AGENT: Str = "agent"
/// `tool`.
export const PARTICIPANT_TOOL: Str = "tool"
/// `memory`.
export const PARTICIPANT_MEMORY: Str = "memory"
/// `human`.
export const PARTICIPANT_HUMAN: Str = "human"
/// `service`.
export const PARTICIPANT_SERVICE: Str = "service"
/// `graph`.
export const PARTICIPANT_GRAPH: Str = "graph"
/// Every value of the set.
export const PARTICIPANT_KINDS: Array[Str]
/// `flow`.
export const RELATION_FLOW: Str = "flow"
/// `dependency`.
export const RELATION_DEPENDENCY: Str = "dependency"
/// Every value of the set.
export const RELATIONS: Array[Str]
/// `at-most-once`.
export const DELIVERY_AT_MOST_ONCE: Str = "at-most-once"
/// `at-least-once`.
export const DELIVERY_AT_LEAST_ONCE: Str = "at-least-once"
/// `effectively-once`.
export const DELIVERY_EFFECTIVELY_ONCE: Str = "effectively-once"
/// Every value of the set.
export const DELIVERY_MODES: Array[Str]
/// `scope`.
export const VISIBILITY_SCOPE: Str = "scope"
/// `graph`.
export const VISIBILITY_GRAPH: Str = "graph"
/// `recipients`.
export const VISIBILITY_RECIPIENTS: Str = "recipients"
/// Every value of the set.
export const VISIBILITIES: Array[Str]
/// `submitted`.
export const STATE_SUBMITTED: Str = "submitted"
/// `working`.
export const STATE_WORKING: Str = "working"
/// `input-required`.
export const STATE_INPUT_REQUIRED: Str = "input-required"
/// `completed`.
export const STATE_COMPLETED: Str = "completed"
/// `failed`.
export const STATE_FAILED: Str = "failed"
/// `canceled`.
export const STATE_CANCELED: Str = "canceled"
/// `expired`.
export const STATE_EXPIRED: Str = "expired"
/// `rejected`.
export const STATE_REJECTED: Str = "rejected"
/// Every value of the set.
export const STATES: Array[Str]
/// `add-participant`.
export const OP_ADD_PARTICIPANT: Str = "add-participant"
/// `remove-participant`.
export const OP_REMOVE_PARTICIPANT: Str = "remove-participant"
/// `add-edge`.
export const OP_ADD_EDGE: Str = "add-edge"
/// `remove-edge`.
export const OP_REMOVE_EDGE: Str = "remove-edge"
/// Every value of the set.
export const MUTATION_OPS: Array[Str]
/// The lifecycle states that never change again.
export const FINAL_STATES: Array[Str]
/// The kinds that open a lifecycle.
export const OPENING_KINDS: Array[Str]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Cli/Commands]] · [[src/Domain/Graph]] · [[src/Domain/Identifier]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Bridge]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Journal]] · [[src/Engine/Kinds]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Engine/Routing]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Validation/Delegation]] · [[src/Validation/Envelope]] · [[src/Validation/Graph]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/MutationsTest]] · [[test/Engine/ShapesTest]] · [[test/Security/AttackTest]] · [[test/Security/HandoffTest]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Contract/_MOC]] · [[src/Cli/Commands]] · [[src/Domain/Graph]] · [[src/Domain/Identifier]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Bridge]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Journal]] · [[src/Engine/Kinds]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Engine/Routing]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Validation/Delegation]] · [[src/Validation/Envelope]] · [[src/Validation/Graph]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/MutationsTest]] · [[test/Engine/ShapesTest]] · [[test/Security/AttackTest]] · [[test/Security/HandoffTest]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Web/RouterTest]]
