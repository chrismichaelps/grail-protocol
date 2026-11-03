---
type: specification
chapter: 2
tags: [protocol, specification]
---

# 2. Model

## 2.1 Identifiers

Every identifier is a string of 1 to 128 characters drawn from `A–Z a–z 0–9 . _ : -`. Identifiers are case-sensitive and compared byte for byte.

- Scope, graph, participant, and edge identifiers are chosen by the client and MUST be unique within their container (a graph within its scope, a participant or edge within its graph).
- Transfer identifiers are chosen by the sender and MUST be unique within the scope. Senders SHOULD use time-ordered random identifiers (for example, a version 7 UUID) so that collisions are negligible and ordering by identifier approximates ordering by creation.
- An identifier is only meaningful together with its scope. Two scopes MAY use the same graph identifier; they name two unrelated graphs.

## 2.2 Scope

A scope is the unit of isolation and ownership. The fabric MUST keep every graph, participant, edge, transfer, ledger entry, and token inside exactly one scope, and MUST NOT allow any operation to read or write across scopes. A fabric MAY host many scopes; how scopes map to users and organizations is a deployment decision outside this specification.

## 2.3 Participant

A participant is declared inside a graph:

| Field | Type | Rules |
| --- | --- | --- |
| `id` | identifier | Unique in the graph. |
| `kind` | `agent` · `tool` · `memory` · `human` · `service` · `graph` · `channel` | Informational except for `graph` (see 6.5) and `channel` (see 15). |
| `roles` | array of names | Used by role targeting. At most 32 entries. |
| `abilities` | array of names | What the participant advertises it can do. Used by ability targeting. At most 64 entries. |
| `graph` | identifier | REQUIRED when `kind` is `graph`: the graph this participant stands for. Forbidden otherwise. |

A `channel` declares no `roles`, `abilities`, or `graph`; it is addressed by its id alone ([[protocol/15-Channels]]).

Names are 1 to 64 characters of `a–z 0–9 . _ -`.

There are no second-class participants. A person approving a step and a model drafting it are addressed, authorized, and traced in the same way.

## 2.4 Edge

An edge is declared inside a graph:

| Field | Type | Rules |
| --- | --- | --- |
| `id` | identifier | Unique in the graph. |
| `from` | participant id | MUST name a participant of the same graph. |
| `to` | participant id | MUST name a participant of the same graph. MUST differ from `from`. |
| `relation` | `flow` · `dependency` | See below. |
| `kinds` | array of kinds | For `flow` edges: the envelope kinds this edge carries. Empty means every kind. Ignored for `dependency` edges. |

- A **flow** edge authorizes `from` to send envelopes to `to`. Flow edges MAY form cycles; a debate between two agents is two flow edges.
- A **dependency** edge declares that work at `to` waits on `from`: a `task` sent to `to` is accepted only when a `result` produced by `from` is among its causal ancestors (see [[protocol/05-Causality#5.3 Dependency gating]]). A dependency edge does not authorize any flow by itself. Dependency edges MUST form a directed acyclic graph (see [[protocol/06-Graphs#6.3 The acyclicity rule]]).

## 2.5 Graph

| Field | Type | Rules |
| --- | --- | --- |
| `id` | identifier | Unique in the scope. |
| `revision` | integer | Starts at 1 and grows by one with every accepted mutation. |
| `participants` | array of participants | At most 1024. |
| `edges` | array of edges | At most 4096. |

## 2.6 Fabric

The fabric is the server side of the protocol. A conforming fabric:

1. validates every envelope against the envelope schema and limits;
2. authorizes it with the presented capability token;
3. resolves its target through the edges of its graph;
4. checks dependency gating and the transfer lifecycle;
5. assigns the ledger sequence and digest, and appends it to the ledger;
6. makes it available to each resolved recipient.

These steps happen in this order and atomically per envelope: an envelope either passes every step and is appended, or it is refused with one problem document and leaves no trace in the scope except, when the deployment chooses, an audit record outside the ledger.

## Referenced by

[[protocol/_MOC]] · [[protocol/01-Overview]] · [[protocol/03-Envelope]] · [[protocol/06-Graphs]]
