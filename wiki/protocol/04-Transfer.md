---
type: specification
chapter: 4
tags: [protocol, specification]
---

# 4. Transfer

## 4.1 Routing

The fabric resolves an envelope's `target` against the graph named by `graph`:

- `{"participant": p}` resolves to `p` when a `flow` edge from `source` to `p` exists whose `kinds` is empty or contains the envelope's kind.
- `{"role": r}` resolves to every participant holding role `r` that `source` reaches through such an edge.
- `{"ability": a}` resolves the same way for participants advertising ability `a`.

If the selector resolves to no participant the envelope is refused with `grail.no-route`. A sender that is not a participant of the graph is refused with `grail.not-found`.

Answers travel back the way their task came. An envelope whose kind answers a lifecycle (`result`, `error`, `progress`, `input.request`, `tool.result`, and bridged responses) is routed to the task's source, needs no flow edge, and is accepted only from a recipient of the task. Its `target` MUST name the task's source participant. Authority to answer comes from having received the task, so a graph never needs a return edge for every request edge, and an answer from inside a nested graph reaches the outer participant that asked.

## 4.2 Delivery

Accepted envelopes are delivered to each resolved recipient in ledger order. Within one recipient, envelopes with a higher `priority` MAY be delivered first among those waiting; ledger order is kept within one priority. An envelope whose `deadline` has passed is not delivered and its lifecycle, if it has one, moves to `expired`.

## 4.3 Delivery guarantees

| Mode | Contract |
| --- | --- |
| `at-most-once` | The fabric delivers the envelope zero or one time. A recipient that fails mid-processing does not see it again. |
| `at-least-once` | The fabric redelivers until the recipient acknowledges. Recipients MUST tolerate duplicates. |
| `effectively-once` | Like `at-least-once`, and in addition the fabric deduplicates by `delivery.key` within the scope for at least 24 hours: a second envelope with the same key and the same digest is answered with the original acceptance; the same key with a different digest is refused with `grail.key-reused`. |

Exactly-once delivery over an unreliable network is not achievable. `effectively-once` gives the observable result callers want: one ledger entry and one lifecycle per key.

## 4.4 Lifecycle

Envelopes of kind `task` and `tool.call` open a lifecycle tracked by the fabric:

```
submitted ──► working ──► completed
    │            │  ▲
    │            ▼  │
    │       input-required
    │            │
    ├────────────┴──► failed | canceled | expired
    └──► rejected
```

| From | Event (kind) | To |
| --- | --- | --- |
| `submitted` | `progress` | `working` |
| `submitted`, `working` | `input.request` | `input-required` |
| `input-required` | `progress` | `working` |
| `submitted`, `working`, `input-required` | `result`, `tool.result` | `completed` |
| `submitted` | `error` (the recipient refuses before starting) | `rejected` |
| `working`, `input-required` | `error` | `failed` |
| `submitted`, `working`, `input-required` | `cancel` | `canceled` |
| `submitted`, `working`, `input-required` | deadline passes | `expired` |

`completed`, `failed`, `canceled`, `expired`, and `rejected` are final. An envelope that would move a final lifecycle is refused with `grail.invalid-transition`. Only a recipient of the task may complete, fail, or report progress on it; only its source may cancel it.

## 4.5 Patterns

| Pattern | How it is expressed |
| --- | --- |
| Request and response | `task` to a participant, then `result` naming it as parent. The sender waits on the lifecycle. |
| Fire and forget | Any recorded kind with `at-most-once`. |
| Streaming | `stream.open`, any number of `stream.chunk`, `stream.close`, each naming the open as parent. |
| Publish and subscribe | Role or ability targeting. |
| Workflow | Dependency edges between participants. |
| Debate, hierarchy, market | Graph shape: cycles of flow edges, trees of delegation, or many participants sharing an ability. |

## 4.6 Flow control

A recipient pulls deliveries with a cursor, a limit, and an optional wait (see [[protocol/08-Bindings]]). The fabric MUST NOT deliver more than the requested limit, so a slow recipient never receives more than it asked for. A fabric MAY refuse new envelopes for a recipient whose backlog exceeds an advertised bound with `grail.backpressure`, and SHOULD say when to retry.

## Referenced by

[[protocol/_MOC]] · [[protocol/03-Envelope]] · [[domain/Transfer]] · [[domain/Lifecycle]]
