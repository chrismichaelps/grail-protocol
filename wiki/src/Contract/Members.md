---
type: module
path: "@root/src/Contract/Members.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Members

> @Contract.Members.Generated — the members each object allows and requires

## Purpose

The members each object allows and requires. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
/// The `participant` member of `Selector`.
export const SELECTOR_PARTICIPANT: Str = "participant"
/// The `role` member of `Selector`.
export const SELECTOR_ROLE: Str = "role"
/// The `ability` member of `Selector`.
export const SELECTOR_ABILITY: Str = "ability"
/// Members `Selector` allows.
export const SELECTOR_ALLOWED: Array[Str]
/// Members `Selector` requires.
export const SELECTOR_REQUIRED: Array[Str] = []
/// Whether `Selector` refuses members it does not list.
export const SELECTOR_CLOSED: Bool = true
/// Whether `Selector` accepts `x-` members.
export const SELECTOR_EXTENSIBLE: Bool = false
/// The `mode` member of `Delivery`.
export const DELIVERY_MODE: Str = "mode"
/// The `key` member of `Delivery`.
export const DELIVERY_KEY: Str = "key"
/// Members `Delivery` allows.
export const DELIVERY_ALLOWED: Array[Str]
/// Members `Delivery` requires.
export const DELIVERY_REQUIRED: Array[Str]
/// Whether `Delivery` refuses members it does not list.
export const DELIVERY_CLOSED: Bool = true
/// Whether `Delivery` accepts `x-` members.
export const DELIVERY_EXTENSIBLE: Bool = false
/// The `wall` member of `Clock`.
export const CLOCK_WALL: Str = "wall"
/// The `counter` member of `Clock`.
export const CLOCK_COUNTER: Str = "counter"
/// The `node` member of `Clock`.
export const CLOCK_NODE: Str = "node"
/// Members `Clock` allows.
export const CLOCK_ALLOWED: Array[Str]
/// Members `Clock` requires.
export const CLOCK_REQUIRED: Array[Str]
/// Whether `Clock` refuses members it does not list.
export const CLOCK_CLOSED: Bool = true
/// Whether `Clock` accepts `x-` members.
export const CLOCK_EXTENSIBLE: Bool = false
/// The `scheme` member of `Encryption`.
export const ENCRYPTION_SCHEME: Str = "scheme"
/// The `recipients` member of `Encryption`.
export const ENCRYPTION_RECIPIENTS: Str = "recipients"
/// Members `Encryption` allows.
export const ENCRYPTION_ALLOWED: Array[Str]
/// Members `Encryption` requires.
export const ENCRYPTION_REQUIRED: Array[Str]
/// Whether `Encryption` refuses members it does not list.
export const ENCRYPTION_CLOSED: Bool = true
/// Whether `Encryption` accepts `x-` members.
export const ENCRYPTION_EXTENSIBLE: Bool = false
/// The `grail` member of `Envelope`.
export const ENVELOPE_GRAIL: Str = "grail"
/// The `id` member of `Envelope`.
export const ENVELOPE_ID: Str = "id"
/// The `scope` member of `Envelope`.
export const ENVELOPE_SCOPE: Str = "scope"
/// The `graph` member of `Envelope`.
export const ENVELOPE_GRAPH: Str = "graph"
/// The `source` member of `Envelope`.
export const ENVELOPE_SOURCE: Str = "source"
/// The `target` member of `Envelope`.
export const ENVELOPE_TARGET: Str = "target"
/// The `kind` member of `Envelope`.
export const ENVELOPE_KIND: Str = "kind"
/// The `parents` member of `Envelope`.
export const ENVELOPE_PARENTS: Str = "parents"
/// The `schema` member of `Envelope`.
export const ENVELOPE_SCHEMA: Str = "schema"
/// The `payload` member of `Envelope`.
export const ENVELOPE_PAYLOAD: Str = "payload"
/// The `delivery` member of `Envelope`.
export const ENVELOPE_DELIVERY: Str = "delivery"
/// The `priority` member of `Envelope`.
export const ENVELOPE_PRIORITY: Str = "priority"
/// The `deadline` member of `Envelope`.
export const ENVELOPE_DEADLINE: Str = "deadline"
/// The `clock` member of `Envelope`.
export const ENVELOPE_CLOCK: Str = "clock"
/// The `visibility` member of `Envelope`.
export const ENVELOPE_VISIBILITY: Str = "visibility"
/// The `encryption` member of `Envelope`.
export const ENVELOPE_ENCRYPTION: Str = "encryption"
/// Members `Envelope` allows.
export const ENVELOPE_ALLOWED: Array[Str]
/// Members `Envelope` requires.
export const ENVELOPE_REQUIRED: Array[Str]
/// Whether `Envelope` refuses members it does not list.
export const ENVELOPE_CLOSED: Bool = true
/// Whether `Envelope` accepts `x-` members.
export const ENVELOPE_EXTENSIBLE: Bool = true
/// The `graph` member of `Address`.
export const ADDRESS_GRAPH: Str = "graph"
/// The `participant` member of `Address`.
export const ADDRESS_PARTICIPANT: Str = "participant"
/// Members `Address` allows.
export const ADDRESS_ALLOWED: Array[Str]
/// Members `Address` requires.
export const ADDRESS_REQUIRED: Array[Str]
/// Whether `Address` refuses members it does not list.
export const ADDRESS_CLOSED: Bool = true
/// Whether `Address` accepts `x-` members.
export const ADDRESS_EXTENSIBLE: Bool = false
/// The `sequence` member of `Accepted`.
export const ACCEPTED_SEQUENCE: Str = "sequence"
/// The `digest` member of `Accepted`.
export const ACCEPTED_DIGEST: Str = "digest"
/// The `accepted` member of `Accepted`.
export const ACCEPTED_ACCEPTED: Str = "accepted"
/// Members `Accepted` allows.
export const ACCEPTED_ALLOWED: Array[Str]
/// Members `Accepted` requires.
export const ACCEPTED_REQUIRED: Array[Str]
/// Whether `Accepted` refuses members it does not list.
export const ACCEPTED_CLOSED: Bool = false
/// Whether `Accepted` accepts `x-` members.
export const ACCEPTED_EXTENSIBLE: Bool = false
/// The `id` member of `Receipt`.
export const RECEIPT_ID: Str = "id"
/// The `sequence` member of `Receipt`.
export const RECEIPT_SEQUENCE: Str = "sequence"
/// The `digest` member of `Receipt`.
export const RECEIPT_DIGEST: Str = "digest"
/// The `recipients` member of `Receipt`.
export const RECEIPT_RECIPIENTS: Str = "recipients"
/// The `state` member of `Receipt`.
export const RECEIPT_STATE: Str = "state"
/// The `duplicate` member of `Receipt`.
export const RECEIPT_DUPLICATE: Str = "duplicate"
/// Members `Receipt` allows.
export const RECEIPT_ALLOWED: Array[Str]
/// Members `Receipt` requires.
export const RECEIPT_REQUIRED: Array[Str]
/// Whether `Receipt` refuses members it does not list.
export const RECEIPT_CLOSED: Bool = false
/// Whether `Receipt` accepts `x-` members.
export const RECEIPT_EXTENSIBLE: Bool = false
/// The `envelope` member of `Transfer`.
export const TRANSFER_ENVELOPE: Str = "envelope"
/// The `recipients` member of `Transfer`.
export const TRANSFER_RECIPIENTS: Str = "recipients"
/// The `state` member of `Transfer`.
export const TRANSFER_STATE: Str = "state"
/// Members `Transfer` allows.
export const TRANSFER_ALLOWED: Array[Str]
/// Members `Transfer` requires.
export const TRANSFER_REQUIRED: Array[Str]
/// Whether `Transfer` refuses members it does not list.
export const TRANSFER_CLOSED: Bool = false
/// Whether `Transfer` accepts `x-` members.
export const TRANSFER_EXTENSIBLE: Bool = false
/// The `id` member of `TraceEntry`.
export const TRACE_ENTRY_ID: Str = "id"
/// The `sequence` member of `TraceEntry`.
export const TRACE_ENTRY_SEQUENCE: Str = "sequence"
/// The `digest` member of `TraceEntry`.
export const TRACE_ENTRY_DIGEST: Str = "digest"
/// The `erased` member of `TraceEntry`.
export const TRACE_ENTRY_ERASED: Str = "erased"
/// The `hidden` member of `TraceEntry`.
export const TRACE_ENTRY_HIDDEN: Str = "hidden"
/// The `envelope` member of `TraceEntry`.
export const TRACE_ENTRY_ENVELOPE: Str = "envelope"
/// Members `TraceEntry` allows.
export const TRACE_ENTRY_ALLOWED: Array[Str]
/// Members `TraceEntry` requires.
export const TRACE_ENTRY_REQUIRED: Array[Str]
/// Whether `TraceEntry` refuses members it does not list.
export const TRACE_ENTRY_CLOSED: Bool = false
/// Whether `TraceEntry` accepts `x-` members.
export const TRACE_ENTRY_EXTENSIBLE: Bool = false
/// The `of` member of `Trace`.
export const TRACE_OF: Str = "of"
/// The `entries` member of `Trace`.
export const TRACE_ENTRIES: Str = "entries"
/// Members `Trace` allows.
export const TRACE_ALLOWED: Array[Str]
/// Members `Trace` requires.
export const TRACE_REQUIRED: Array[Str]
/// Whether `Trace` refuses members it does not list.
export const TRACE_CLOSED: Bool = false
/// Whether `Trace` accepts `x-` members.
export const TRACE_EXTENSIBLE: Bool = false
/// The `id` member of `Participant`.
export const PARTICIPANT_ID: Str = "id"
/// The `kind` member of `Participant`.
export const PARTICIPANT_KIND: Str = "kind"
/// The `roles` member of `Participant`.
export const PARTICIPANT_ROLES: Str = "roles"
/// The `abilities` member of `Participant`.
export const PARTICIPANT_ABILITIES: Str = "abilities"
/// The `graph` member of `Participant`.
export const PARTICIPANT_GRAPH: Str = "graph"
/// Members `Participant` allows.
export const PARTICIPANT_ALLOWED: Array[Str]
/// Members `Participant` requires.
export const PARTICIPANT_REQUIRED: Array[Str]
/// Whether `Participant` refuses members it does not list.
export const PARTICIPANT_CLOSED: Bool = true
/// Whether `Participant` accepts `x-` members.
export const PARTICIPANT_EXTENSIBLE: Bool = false
/// The `id` member of `Edge`.
export const EDGE_ID: Str = "id"
/// The `from` member of `Edge`.
export const EDGE_FROM: Str = "from"
/// The `to` member of `Edge`.
export const EDGE_TO: Str = "to"
/// The `relation` member of `Edge`.
export const EDGE_RELATION: Str = "relation"
/// The `kinds` member of `Edge`.
export const EDGE_KINDS: Str = "kinds"
/// Members `Edge` allows.
export const EDGE_ALLOWED: Array[Str]
/// Members `Edge` requires.
export const EDGE_REQUIRED: Array[Str]
/// Whether `Edge` refuses members it does not list.
export const EDGE_CLOSED: Bool = true
/// Whether `Edge` accepts `x-` members.
export const EDGE_EXTENSIBLE: Bool = false
/// The `participants` member of `GraphDraft`.
export const GRAPH_DRAFT_PARTICIPANTS: Str = "participants"
/// The `edges` member of `GraphDraft`.
export const GRAPH_DRAFT_EDGES: Str = "edges"
/// Members `GraphDraft` allows.
export const GRAPH_DRAFT_ALLOWED: Array[Str]
/// Members `GraphDraft` requires.
export const GRAPH_DRAFT_REQUIRED: Array[Str] = []
/// Whether `GraphDraft` refuses members it does not list.
export const GRAPH_DRAFT_CLOSED: Bool = true
/// Whether `GraphDraft` accepts `x-` members.
export const GRAPH_DRAFT_EXTENSIBLE: Bool = false
/// The `id` member of `Graph`.
export const GRAPH_ID: Str = "id"
/// The `scope` member of `Graph`.
export const GRAPH_SCOPE: Str = "scope"
/// The `revision` member of `Graph`.
export const GRAPH_REVISION: Str = "revision"
/// The `participants` member of `Graph`.
export const GRAPH_PARTICIPANTS: Str = "participants"
/// The `edges` member of `Graph`.
export const GRAPH_EDGES: Str = "edges"
/// Members `Graph` allows.
export const GRAPH_ALLOWED: Array[Str]
/// Members `Graph` requires.
export const GRAPH_REQUIRED: Array[Str]
/// Whether `Graph` refuses members it does not list.
export const GRAPH_CLOSED: Bool = false
/// Whether `Graph` accepts `x-` members.
export const GRAPH_EXTENSIBLE: Bool = false
/// The `op` member of `MutationStep`.
export const MUTATION_STEP_OP: Str = "op"
/// The `participant` member of `MutationStep`.
export const MUTATION_STEP_PARTICIPANT: Str = "participant"
/// The `edge` member of `MutationStep`.
export const MUTATION_STEP_EDGE: Str = "edge"
/// The `id` member of `MutationStep`.
export const MUTATION_STEP_ID: Str = "id"
/// Members `MutationStep` allows.
export const MUTATION_STEP_ALLOWED: Array[Str]
/// Members `MutationStep` requires.
export const MUTATION_STEP_REQUIRED: Array[Str]
/// Whether `MutationStep` refuses members it does not list.
export const MUTATION_STEP_CLOSED: Bool = true
/// Whether `MutationStep` accepts `x-` members.
export const MUTATION_STEP_EXTENSIBLE: Bool = false
/// The `expectedRevision` member of `Mutation`.
export const MUTATION_EXPECTED_REVISION: Str = "expectedRevision"
/// The `operations` member of `Mutation`.
export const MUTATION_OPERATIONS: Str = "operations"
/// Members `Mutation` allows.
export const MUTATION_ALLOWED: Array[Str]
/// Members `Mutation` requires.
export const MUTATION_REQUIRED: Array[Str]
/// Whether `Mutation` refuses members it does not list.
export const MUTATION_CLOSED: Bool = true
/// Whether `Mutation` accepts `x-` members.
export const MUTATION_EXTENSIBLE: Bool = false
/// The `sequence` member of `Delivered`.
export const DELIVERED_SEQUENCE: Str = "sequence"
/// The `envelope` member of `Delivered`.
export const DELIVERED_ENVELOPE: Str = "envelope"
/// Members `Delivered` allows.
export const DELIVERED_ALLOWED: Array[Str]
/// Members `Delivered` requires.
export const DELIVERED_REQUIRED: Array[Str]
/// Whether `Delivered` refuses members it does not list.
export const DELIVERED_CLOSED: Bool = false
/// Whether `Delivered` accepts `x-` members.
export const DELIVERED_EXTENSIBLE: Bool = false
/// The `deliveries` member of `DeliveryPage`.
export const DELIVERY_PAGE_DELIVERIES: Str = "deliveries"
/// The `cursor` member of `DeliveryPage`.
export const DELIVERY_PAGE_CURSOR: Str = "cursor"
/// Members `DeliveryPage` allows.
export const DELIVERY_PAGE_ALLOWED: Array[Str]
/// Members `DeliveryPage` requires.
export const DELIVERY_PAGE_REQUIRED: Array[Str]
/// Whether `DeliveryPage` refuses members it does not list.
export const DELIVERY_PAGE_CLOSED: Bool = false
/// Whether `DeliveryPage` accepts `x-` members.
export const DELIVERY_PAGE_EXTENSIBLE: Bool = false
/// The `sequence` member of `LedgerEntry`.
export const LEDGER_ENTRY_SEQUENCE: Str = "sequence"
/// The `id` member of `LedgerEntry`.
export const LEDGER_ENTRY_ID: Str = "id"
/// The `digest` member of `LedgerEntry`.
export const LEDGER_ENTRY_DIGEST: Str = "digest"
/// The `link` member of `LedgerEntry`.
export const LEDGER_ENTRY_LINK: Str = "link"
/// Members `LedgerEntry` allows.
export const LEDGER_ENTRY_ALLOWED: Array[Str]
/// Members `LedgerEntry` requires.
export const LEDGER_ENTRY_REQUIRED: Array[Str]
/// Whether `LedgerEntry` refuses members it does not list.
export const LEDGER_ENTRY_CLOSED: Bool = false
/// Whether `LedgerEntry` accepts `x-` members.
export const LEDGER_ENTRY_EXTENSIBLE: Bool = false
/// The `entries` member of `LedgerPage`.
export const LEDGER_PAGE_ENTRIES: Str = "entries"
/// The `cursor` member of `LedgerPage`.
export const LEDGER_PAGE_CURSOR: Str = "cursor"
/// Members `LedgerPage` allows.
export const LEDGER_PAGE_ALLOWED: Array[Str]
/// Members `LedgerPage` requires.
export const LEDGER_PAGE_REQUIRED: Array[Str]
/// Whether `LedgerPage` refuses members it does not list.
export const LEDGER_PAGE_CLOSED: Bool = false
/// Whether `LedgerPage` accepts `x-` members.
export const LEDGER_PAGE_EXTENSIBLE: Bool = false
/// The `id` member of `Delegation`.
export const DELEGATION_ID: Str = "id"
/// The `audience` member of `Delegation`.
export const DELEGATION_AUDIENCE: Str = "audience"
/// The `graph` member of `Delegation`.
export const DELEGATION_GRAPH: Str = "graph"
/// The `abilities` member of `Delegation`.
export const DELEGATION_ABILITIES: Str = "abilities"
/// The `notBefore` member of `Delegation`.
export const DELEGATION_NOT_BEFORE: Str = "notBefore"
/// The `expires` member of `Delegation`.
export const DELEGATION_EXPIRES: Str = "expires"
/// Members `Delegation` allows.
export const DELEGATION_ALLOWED: Array[Str]
/// Members `Delegation` requires.
export const DELEGATION_REQUIRED: Array[Str]
/// Whether `Delegation` refuses members it does not list.
export const DELEGATION_CLOSED: Bool = true
/// Whether `Delegation` accepts `x-` members.
export const DELEGATION_EXTENSIBLE: Bool = false
/// The `token` member of `Grant`.
export const GRANT_TOKEN: Str = "token"
/// The `expires` member of `Grant`.
export const GRANT_EXPIRES: Str = "expires"
/// Members `Grant` allows.
export const GRANT_ALLOWED: Array[Str]
/// Members `Grant` requires.
export const GRANT_REQUIRED: Array[Str]
/// Whether `Grant` refuses members it does not list.
export const GRANT_CLOSED: Bool = false
/// Whether `Grant` accepts `x-` members.
export const GRANT_EXTENSIBLE: Bool = false
/// The `jsonrpc` member of `RpcMessage`.
export const RPC_MESSAGE_JSONRPC: Str = "jsonrpc"
/// The `id` member of `RpcMessage`.
export const RPC_MESSAGE_ID: Str = "id"
/// The `method` member of `RpcMessage`.
export const RPC_MESSAGE_METHOD: Str = "method"
/// The `params` member of `RpcMessage`.
export const RPC_MESSAGE_PARAMS: Str = "params"
/// The `result` member of `RpcMessage`.
export const RPC_MESSAGE_RESULT: Str = "result"
/// The `error` member of `RpcMessage`.
export const RPC_MESSAGE_ERROR: Str = "error"
/// Members `RpcMessage` allows.
export const RPC_MESSAGE_ALLOWED: Array[Str]
/// Members `RpcMessage` requires.
export const RPC_MESSAGE_REQUIRED: Array[Str]
/// Whether `RpcMessage` refuses members it does not list.
export const RPC_MESSAGE_CLOSED: Bool = false
/// Whether `RpcMessage` accepts `x-` members.
export const RPC_MESSAGE_EXTENSIBLE: Bool = false
/// The `grail` member of `Discovery`.
export const DISCOVERY_GRAIL: Str = "grail"
/// The `fabric` member of `Discovery`.
export const DISCOVERY_FABRIC: Str = "fabric"
/// The `bindings` member of `Discovery`.
export const DISCOVERY_BINDINGS: Str = "bindings"
/// The `limits` member of `Discovery`.
export const DISCOVERY_LIMITS: Str = "limits"
/// The `kinds` member of `Discovery`.
export const DISCOVERY_KINDS: Str = "kinds"
/// The `abilities` member of `Discovery`.
export const DISCOVERY_ABILITIES: Str = "abilities"
/// The `extensions` member of `Discovery`.
export const DISCOVERY_EXTENSIONS: Str = "extensions"
/// Members `Discovery` allows.
export const DISCOVERY_ALLOWED: Array[Str]
/// Members `Discovery` requires.
export const DISCOVERY_REQUIRED: Array[Str]
/// Whether `Discovery` refuses members it does not list.
export const DISCOVERY_CLOSED: Bool = false
/// Whether `Discovery` accepts `x-` members.
export const DISCOVERY_EXTENSIBLE: Bool = false
/// The `status` member of `Health`.
export const HEALTH_STATUS: Str = "status"
/// Members `Health` allows.
export const HEALTH_ALLOWED: Array[Str]
/// Members `Health` requires.
export const HEALTH_REQUIRED: Array[Str]
/// Whether `Health` refuses members it does not list.
export const HEALTH_CLOSED: Bool = false
/// Whether `Health` accepts `x-` members.
export const HEALTH_EXTENSIBLE: Bool = false
/// The `type` member of `Problem`.
export const PROBLEM_TYPE: Str = "type"
/// The `title` member of `Problem`.
export const PROBLEM_TITLE: Str = "title"
/// The `status` member of `Problem`.
export const PROBLEM_STATUS: Str = "status"
/// The `code` member of `Problem`.
export const PROBLEM_CODE: Str = "code"
/// The `detail` member of `Problem`.
export const PROBLEM_DETAIL: Str = "detail"
/// The `instance` member of `Problem`.
export const PROBLEM_INSTANCE: Str = "instance"
/// Members `Problem` allows.
export const PROBLEM_ALLOWED: Array[Str]
/// Members `Problem` requires.
export const PROBLEM_REQUIRED: Array[Str]
/// Whether `Problem` refuses members it does not list.
export const PROBLEM_CLOSED: Bool = false
/// Whether `Problem` accepts `x-` members.
export const PROBLEM_EXTENSIBLE: Bool = false
/// The `id` member of `Token`.
export const TOKEN_ID: Str = "id"
/// The `scope` member of `Token`.
export const TOKEN_SCOPE: Str = "scope"
/// The `graph` member of `Token`.
export const TOKEN_GRAPH: Str = "graph"
/// The `issuer` member of `Token`.
export const TOKEN_ISSUER: Str = "issuer"
/// The `audience` member of `Token`.
export const TOKEN_AUDIENCE: Str = "audience"
/// The `abilities` member of `Token`.
export const TOKEN_ABILITIES: Str = "abilities"
/// The `notBefore` member of `Token`.
export const TOKEN_NOT_BEFORE: Str = "notBefore"
/// The `expires` member of `Token`.
export const TOKEN_EXPIRES: Str = "expires"
/// The `parent` member of `Token`.
export const TOKEN_PARENT: Str = "parent"
/// The `chain` member of `Token`.
export const TOKEN_CHAIN: Str = "chain"
/// Members `Token` allows.
export const TOKEN_ALLOWED: Array[Str]
/// Members `Token` requires.
export const TOKEN_REQUIRED: Array[Str]
/// Whether `Token` refuses members it does not list.
export const TOKEN_CLOSED: Bool = true
/// Whether `Token` accepts `x-` members.
export const TOKEN_EXTENSIBLE: Bool = false
/// The `id` member of `TokenView`.
export const TOKEN_VIEW_ID: Str = "id"
/// The `scope` member of `TokenView`.
export const TOKEN_VIEW_SCOPE: Str = "scope"
/// The `graph` member of `TokenView`.
export const TOKEN_VIEW_GRAPH: Str = "graph"
/// The `issuer` member of `TokenView`.
export const TOKEN_VIEW_ISSUER: Str = "issuer"
/// The `audience` member of `TokenView`.
export const TOKEN_VIEW_AUDIENCE: Str = "audience"
/// The `abilities` member of `TokenView`.
export const TOKEN_VIEW_ABILITIES: Str = "abilities"
/// The `notBefore` member of `TokenView`.
export const TOKEN_VIEW_NOT_BEFORE: Str = "notBefore"
/// The `expires` member of `TokenView`.
export const TOKEN_VIEW_EXPIRES: Str = "expires"
/// The `depth` member of `TokenView`.
export const TOKEN_VIEW_DEPTH: Str = "depth"
/// Members `TokenView` allows.
export const TOKEN_VIEW_ALLOWED: Array[Str]
/// Members `TokenView` requires.
export const TOKEN_VIEW_REQUIRED: Array[Str]
/// Whether `TokenView` refuses members it does not list.
export const TOKEN_VIEW_CLOSED: Bool = false
/// Whether `TokenView` accepts `x-` members.
export const TOKEN_VIEW_EXTENSIBLE: Bool = false
/// The `token` member of `Revocation`.
export const REVOCATION_TOKEN: Str = "token"
/// The `revoked` member of `Revocation`.
export const REVOCATION_REVOKED: Str = "revoked"
/// Members `Revocation` allows.
export const REVOCATION_ALLOWED: Array[Str]
/// Members `Revocation` requires.
export const REVOCATION_REQUIRED: Array[Str]
/// Whether `Revocation` refuses members it does not list.
export const REVOCATION_CLOSED: Bool = false
/// Whether `Revocation` accepts `x-` members.
export const REVOCATION_EXTENSIBLE: Bool = false
/// The `id` member of `Erasure`.
export const ERASURE_ID: Str = "id"
/// The `sequence` member of `Erasure`.
export const ERASURE_SEQUENCE: Str = "sequence"
/// The `digest` member of `Erasure`.
export const ERASURE_DIGEST: Str = "digest"
/// The `erased` member of `Erasure`.
export const ERASURE_ERASED: Str = "erased"
/// Members `Erasure` allows.
export const ERASURE_ALLOWED: Array[Str]
/// Members `Erasure` requires.
export const ERASURE_REQUIRED: Array[Str]
/// Whether `Erasure` refuses members it does not list.
export const ERASURE_CLOSED: Bool = false
/// Whether `Erasure` accepts `x-` members.
export const ERASURE_EXTENSIBLE: Bool = false
/// The `fabric` member of `Origin`.
export const ORIGIN_FABRIC: Str = "fabric"
/// The `scope` member of `Origin`.
export const ORIGIN_SCOPE: Str = "scope"
/// The `graph` member of `Origin`.
export const ORIGIN_GRAPH: Str = "graph"
/// The `participant` member of `Origin`.
export const ORIGIN_PARTICIPANT: Str = "participant"
/// Members `Origin` allows.
export const ORIGIN_ALLOWED: Array[Str]
/// Members `Origin` requires.
export const ORIGIN_REQUIRED: Array[Str]
/// Whether `Origin` refuses members it does not list.
export const ORIGIN_CLOSED: Bool = true
/// Whether `Origin` accepts `x-` members.
export const ORIGIN_EXTENSIBLE: Bool = false
/// The `id` member of `HandoffRequest`.
export const HANDOFF_REQUEST_ID: Str = "id"
/// The `transfers` member of `HandoffRequest`.
export const HANDOFF_REQUEST_TRANSFERS: Str = "transfers"
/// The `expires` member of `HandoffRequest`.
export const HANDOFF_REQUEST_EXPIRES: Str = "expires"
/// Members `HandoffRequest` allows.
export const HANDOFF_REQUEST_ALLOWED: Array[Str]
/// Members `HandoffRequest` requires.
export const HANDOFF_REQUEST_REQUIRED: Array[Str]
/// Whether `HandoffRequest` refuses members it does not list.
export const HANDOFF_REQUEST_CLOSED: Bool = true
/// Whether `HandoffRequest` accepts `x-` members.
export const HANDOFF_REQUEST_EXTENSIBLE: Bool = false
/// The `sequence` member of `HandoffEntry`.
export const HANDOFF_ENTRY_SEQUENCE: Str = "sequence"
/// The `id` member of `HandoffEntry`.
export const HANDOFF_ENTRY_ID: Str = "id"
/// The `previous` member of `HandoffEntry`.
export const HANDOFF_ENTRY_PREVIOUS: Str = "previous"
/// The `digest` member of `HandoffEntry`.
export const HANDOFF_ENTRY_DIGEST: Str = "digest"
/// The `link` member of `HandoffEntry`.
export const HANDOFF_ENTRY_LINK: Str = "link"
/// The `erased` member of `HandoffEntry`.
export const HANDOFF_ENTRY_ERASED: Str = "erased"
/// The `withheld` member of `HandoffEntry`.
export const HANDOFF_ENTRY_WITHHELD: Str = "withheld"
/// The `envelope` member of `HandoffEntry`.
export const HANDOFF_ENTRY_ENVELOPE: Str = "envelope"
/// Members `HandoffEntry` allows.
export const HANDOFF_ENTRY_ALLOWED: Array[Str]
/// Members `HandoffEntry` requires.
export const HANDOFF_ENTRY_REQUIRED: Array[Str]
/// Whether `HandoffEntry` refuses members it does not list.
export const HANDOFF_ENTRY_CLOSED: Bool = true
/// Whether `HandoffEntry` accepts `x-` members.
export const HANDOFF_ENTRY_EXTENSIBLE: Bool = false
/// The `grail` member of `Handoff`.
export const HANDOFF_GRAIL: Str = "grail"
/// The `handoff` member of `Handoff`.
export const HANDOFF_HANDOFF: Str = "handoff"
/// The `origin` member of `Handoff`.
export const HANDOFF_ORIGIN: Str = "origin"
/// The `participant` member of `Handoff`.
export const HANDOFF_PARTICIPANT: Str = "participant"
/// The `anchors` member of `Handoff`.
export const HANDOFF_ANCHORS: Str = "anchors"
/// The `entries` member of `Handoff`.
export const HANDOFF_ENTRIES: Str = "entries"
/// The `issued` member of `Handoff`.
export const HANDOFF_ISSUED: Str = "issued"
/// The `expires` member of `Handoff`.
export const HANDOFF_EXPIRES: Str = "expires"
/// The `digest` member of `Handoff`.
export const HANDOFF_DIGEST: Str = "digest"
/// The `seal` member of `Handoff`.
export const HANDOFF_SEAL: Str = "seal"
/// The `needs` member of `Handoff`.
export const HANDOFF_NEEDS: Str = "needs"
/// Members `Handoff` allows.
export const HANDOFF_ALLOWED: Array[Str]
/// Members `Handoff` requires.
export const HANDOFF_REQUIRED: Array[Str]
/// Whether `Handoff` refuses members it does not list.
export const HANDOFF_CLOSED: Bool = true
/// Whether `Handoff` accepts `x-` members.
export const HANDOFF_EXTENSIBLE: Bool = false
/// The `handoff` member of `HandoffReceipt`.
export const HANDOFF_RECEIPT_HANDOFF: Str = "handoff"
/// The `id` member of `HandoffReceipt`.
export const HANDOFF_RECEIPT_ID: Str = "id"
/// The `sequence` member of `HandoffReceipt`.
export const HANDOFF_RECEIPT_SEQUENCE: Str = "sequence"
/// The `digest` member of `HandoffReceipt`.
export const HANDOFF_RECEIPT_DIGEST: Str = "digest"
/// The `entries` member of `HandoffReceipt`.
export const HANDOFF_RECEIPT_ENTRIES: Str = "entries"
/// The `duplicate` member of `HandoffReceipt`.
export const HANDOFF_RECEIPT_DUPLICATE: Str = "duplicate"
/// Members `HandoffReceipt` allows.
export const HANDOFF_RECEIPT_ALLOWED: Array[Str]
/// Members `HandoffReceipt` requires.
export const HANDOFF_RECEIPT_REQUIRED: Array[Str]
/// Whether `HandoffReceipt` refuses members it does not list.
export const HANDOFF_RECEIPT_CLOSED: Bool = false
/// Whether `HandoffReceipt` accepts `x-` members.
export const HANDOFF_RECEIPT_EXTENSIBLE: Bool = false
/// The `handoff` member of `HandoffCheck`.
export const HANDOFF_CHECK_HANDOFF: Str = "handoff"
/// The `digest` member of `HandoffCheck`.
export const HANDOFF_CHECK_DIGEST: Str = "digest"
/// The `intact` member of `HandoffCheck`.
export const HANDOFF_CHECK_INTACT: Str = "intact"
/// The `attested` member of `HandoffCheck`.
export const HANDOFF_CHECK_ATTESTED: Str = "attested"
/// The `expired` member of `HandoffCheck`.
export const HANDOFF_CHECK_EXPIRED: Str = "expired"
/// Members `HandoffCheck` allows.
export const HANDOFF_CHECK_ALLOWED: Array[Str]
/// Members `HandoffCheck` requires.
export const HANDOFF_CHECK_REQUIRED: Array[Str]
/// Whether `HandoffCheck` refuses members it does not list.
export const HANDOFF_CHECK_CLOSED: Bool = false
/// Whether `HandoffCheck` accepts `x-` members.
export const HANDOFF_CHECK_EXTENSIBLE: Bool = false
/// The `$secret` member of `SecretReference`.
export const SECRET_REFERENCE_SECRET: Str = "$secret"
/// Members `SecretReference` allows.
export const SECRET_REFERENCE_ALLOWED: Array[Str]
/// Members `SecretReference` requires.
export const SECRET_REFERENCE_REQUIRED: Array[Str]
/// Whether `SecretReference` refuses members it does not list.
export const SECRET_REFERENCE_CLOSED: Bool = true
/// Whether `SecretReference` accepts `x-` members.
export const SECRET_REFERENCE_EXTENSIBLE: Bool = false
/// The `value` member of `SecretDeposit`.
export const SECRET_DEPOSIT_VALUE: Str = "value"
/// The `graph` member of `SecretDeposit`.
export const SECRET_DEPOSIT_GRAPH: Str = "graph"
/// The `audience` member of `SecretDeposit`.
export const SECRET_DEPOSIT_AUDIENCE: Str = "audience"
/// The `senders` member of `SecretDeposit`.
export const SECRET_DEPOSIT_SENDERS: Str = "senders"
/// The `kinds` member of `SecretDeposit`.
export const SECRET_DEPOSIT_KINDS: Str = "kinds"
/// The `uses` member of `SecretDeposit`.
export const SECRET_DEPOSIT_USES: Str = "uses"
/// The `expires` member of `SecretDeposit`.
export const SECRET_DEPOSIT_EXPIRES: Str = "expires"
/// The `description` member of `SecretDeposit`.
export const SECRET_DEPOSIT_DESCRIPTION: Str = "description"
/// Members `SecretDeposit` allows.
export const SECRET_DEPOSIT_ALLOWED: Array[Str]
/// Members `SecretDeposit` requires.
export const SECRET_DEPOSIT_REQUIRED: Array[Str]
/// Whether `SecretDeposit` refuses members it does not list.
export const SECRET_DEPOSIT_CLOSED: Bool = true
/// Whether `SecretDeposit` accepts `x-` members.
export const SECRET_DEPOSIT_EXTENSIBLE: Bool = false
/// The `name` member of `SecretView`.
export const SECRET_VIEW_NAME: Str = "name"
/// The `version` member of `SecretView`.
export const SECRET_VIEW_VERSION: Str = "version"
/// The `graph` member of `SecretView`.
export const SECRET_VIEW_GRAPH: Str = "graph"
/// The `audience` member of `SecretView`.
export const SECRET_VIEW_AUDIENCE: Str = "audience"
/// The `senders` member of `SecretView`.
export const SECRET_VIEW_SENDERS: Str = "senders"
/// The `kinds` member of `SecretView`.
export const SECRET_VIEW_KINDS: Str = "kinds"
/// The `uses` member of `SecretView`.
export const SECRET_VIEW_USES: Str = "uses"
/// The `expires` member of `SecretView`.
export const SECRET_VIEW_EXPIRES: Str = "expires"
/// The `description` member of `SecretView`.
export const SECRET_VIEW_DESCRIPTION: Str = "description"
/// The `created` member of `SecretView`.
export const SECRET_VIEW_CREATED: Str = "created"
/// The `reveals` member of `SecretView`.
export const SECRET_VIEW_REVEALS: Str = "reveals"
/// The `revealed` member of `SecretView`.
export const SECRET_VIEW_REVEALED: Str = "revealed"
/// Members `SecretView` allows.
export const SECRET_VIEW_ALLOWED: Array[Str]
/// Members `SecretView` requires.
export const SECRET_VIEW_REQUIRED: Array[Str]
/// Whether `SecretView` refuses members it does not list.
export const SECRET_VIEW_CLOSED: Bool = false
/// Whether `SecretView` accepts `x-` members.
export const SECRET_VIEW_EXTENSIBLE: Bool = false
/// The `secrets` member of `SecretList`.
export const SECRET_LIST_SECRETS: Str = "secrets"
/// Members `SecretList` allows.
export const SECRET_LIST_ALLOWED: Array[Str]
/// Members `SecretList` requires.
export const SECRET_LIST_REQUIRED: Array[Str]
/// Whether `SecretList` refuses members it does not list.
export const SECRET_LIST_CLOSED: Bool = false
/// Whether `SecretList` accepts `x-` members.
export const SECRET_LIST_EXTENSIBLE: Bool = false
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Token]] · [[src/Engine/Codec/Views]] · [[src/Engine/Custody]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Ledger]] · [[src/Services/Bridge]] · [[src/Validation/Delegation]] · [[src/Validation/Envelope]] · [[src/Validation/Graph]]

## Referenced by

[[src/Contract/_MOC]] · [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Token]] · [[src/Engine/Codec/Views]] · [[src/Engine/Custody]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Ledger]] · [[src/Services/Bridge]] · [[src/Validation/Delegation]] · [[src/Validation/Envelope]] · [[src/Validation/Graph]]
