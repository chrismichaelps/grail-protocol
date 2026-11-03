---
type: specification
chapter: 15
tags: [protocol, specification, channels]
---

# 15. Channels

A team of agents needs a place to talk that is not one inbox. A reviewer joins halfway through and has to see what was said before. A person wants to watch the work without being asked to answer it. A dashboard wants the stream without acknowledging anything. Role targeting (4.5) reaches everyone holding a role at the moment of sending, but it leaves no place to read back from, and it makes membership a property of the participant rather than of the conversation.

A channel is that place. It is a participant of kind `channel` that never acts: it receives envelopes, hands each one to its subscribers, and keeps them readable in order. Membership, posting rights, and what a subscriber hears are all edges, so the orchestrator that owns the graph decides them the same way it decides everything else.

## 15.1 Declaring a channel

A channel is declared like any participant, with `kind` set to `channel`. It is addressed by its id alone: a channel MUST NOT declare `roles`, `abilities`, or `graph`, and a draft or mutation that gives it any is refused with `grail.invalid`.

| Edge | Meaning |
| --- | --- |
| flow from `p` to the channel | `p` may post to the channel, with the kinds the edge carries. |
| flow from the channel to `p` | `p` subscribes to the channel and hears the kinds the edge carries. |
| dependency from `p` to the channel | Tasks posted to the channel wait for a result from `p` (5.3). |

A flow edge between two channels, and a dependency edge from a channel, are refused with `grail.invalid`. Channels do not chain, and a channel never produces a result for anything to wait on.

## 15.2 Posting

An envelope whose target is `{"participant": c}`, where `c` is a channel the sender may post to, resolves to every subscriber of `c` whose subscription carries the envelope's kind, except the sender itself. A subscriber that is a graph participant expands to its entry participants as in 6.5, and the channel counts toward the containment depth. When nobody but the sender would hear it yet, the post is still accepted with no recipients and kept for whoever reads the channel later. An envelope that opens a lifecycle (a `task`, a `tool.call`, or a bridged request) is the exception: nobody could answer it, so it is refused with `grail.no-route` and nothing is appended.

Each delivery's route starts at the channel, so a trace and every lifecycle record which channel carried the work. Everything else is unchanged: ids, digests, the ledger, visibility, delivery modes, deadlines, custody, and dependency gating apply to channel posts as they apply to any envelope. Gating checks the channel and every subscriber it reaches.

A `task` posted to a channel opens one lifecycle whose recipients are the subscribers it reached. The first of them to report `progress`, ask with `input.request`, or answer takes the task: the fabric narrows the lifecycle's recipients to that subscriber in the same atomic step that accepts its envelope, and from then on only it may move the task. Any other subscriber is refused with `grail.forbidden`. This is how a team asks "who can take this?" without naming anyone, and why two agents never both do the work. A task sent to one participant is never narrowed.

A channel never sends. An envelope whose `source` is a channel is refused with `grail.forbidden`. A channel never receives deliveries of its own, and answers to a task posted to a channel go to the task's source, as every answer does (4.1).

## 15.3 Reading a channel

`readChannel` (`transfer.receive`) returns the envelopes posted to a channel after a cursor, oldest first, with the same page shape and the same `after`, `limit`, and `wait` parameters as `pullDeliveries`. It differs in three ways:

1. **Nothing is acknowledged.** Reading a channel never moves a delivery mark, so a participant can watch a channel and pull its own deliveries independently, and an observer cannot cause anyone to miss anything.
2. **Late subscribers see the past.** A subscriber reads every post since the channel began whose kind its subscription carries, including posts made before it subscribed, except posts with `recipients` visibility that it did not receive.
3. **Values stay in custody.** Posts are returned as stored. A secret reference stays a reference; only a delivery to an audience member reveals a value (14.1).

When a page holds no post, its cursor is the end of the ledger as the fabric saw it, so a reader that keeps passing it back does not rescan history.

Only the scope owner and the channel's current subscribers may read it. For any other token, and for a participant that is not a channel, the answer is `grail.not-found`, so a non-member learns nothing about the channel. A token bound to another graph is refused with `grail.forbidden`, as everywhere else (7.2).

## 15.4 Observers

An observer is a participant that subscribes to a channel and holds a token with `transfer.receive` alone. It can read the channel and pull its own deliveries, but it cannot post, answer, or delegate. People watching a team, dashboards, audit tools, and test harnesses are observers. Because reading never acknowledges, any number of observers can watch the same channel without affecting delivery to the participants that do the work.

## 15.5 Limits

Channels add no limits of their own. A channel counts as a participant toward `participants`, its edges count toward `edges`, and the recipients of one post count toward `routingPaths`.

## Referenced by

[[protocol/_MOC]] · [[protocol/04-Transfer]] · [[protocol/08-Bindings]] · [[protocol/11-Conformance]] · [[decisions/ADR-0011-channels-and-hosted-agents]]
