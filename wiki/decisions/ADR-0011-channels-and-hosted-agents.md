---
type: adr
status: ACCEPTED
date: 2026-11-03
decision_risk: HIGH
tags: [adr, protocol, channels, agents]
---

# ADR-0011 — Channels are participants, and hosted agents attach as ordinary clients

## Context

Up to 1.1 the fabric worked when a program written for it drove the HTTP binding. The agents people actually run, coding agents run from their own command lines, do not speak Grail. They load tools over a tool protocol on standard input and output, act only when prompted, and should never see a credential. Nothing in the repository let such an agent take part in a graph, so every demonstration was a script playing the agents.

Teams of agents also had no shared place to talk. Role targeting reaches everyone holding a role when a message is sent, but leaves nothing to read back from, so an agent joining later, a person watching, or a dashboard had no way in that did not also take deliveries away from the participant doing the work.

Running real agents against a real fabric exposed three defects that the in-process suites could not see:

- A browser's preflight request was answered `405`, so no page on a listed origin could ever send a token, although `GRAIL_ALLOWED_ORIGINS` existed.
- The peer client's resilience pipeline cut each attempt at 10 seconds and the whole call at 30, so a 25-second long poll through it could never succeed.
- A model asked to name its parents mostly did not, so traces of answers produced by agents stopped at the task.

## Decision

**Channels, protocol 1.2.** A channel is a participant of kind `channel`. A post is an envelope targeting it; routing expands the channel to its subscribers, the targets of its outgoing flow edges whose kinds admit the post, leaving out the sender. A post nobody else hears yet is kept for later readers; only one that opens a lifecycle needs someone to answer it. The first subscriber to move a channel task takes it. A channel declares nothing but its id, never sends, never chains to another channel, and nothing depends on it. `readChannel` returns posts after a cursor without acknowledging anything, to the owner and current subscribers only, and returns stored bodies so a secret stays a reference. Everything else (ledger, gating, lifecycles, custody, visibility) applies unchanged, because a post is just an envelope.

**An agent layer.** `src/Agent` sits beside `App` and below `Cli`. It never reaches `Services`: it is a client that holds one participant's token and talks to a fabric through [[src/Api/Peer]], as any other program would. `grail agent` serves seven tools over the tool protocol a hosted agent already loads, so any such client attaches with one command and two variables. `grail run --exec CMD` keeps a participant attached: it starts the agent for each task, reports progress, and answers with the agent's output or failure when the agent did not answer itself. The runner supplies the provenance a model forgets: everything the agent sends for a task descends from it, and the answer names what the agent sent and read. A runner claims a task by reporting progress before it starts the agent; for a task posted to a channel, the fabric narrows the task to the first subscriber that moves it, so the claim is atomic.

**The defects fixed.** The router answers preflights from listed origins with `204` and allows private-network access. The peer sizes its attempt timeout from the contract's longest wait.

Considered and rejected:

- **Claiming as a runner convention.** Checking the task's state before starting leaves a race between two runners. The fabric already serializes every change to a scope, so it decides the claim where it decides everything else.
- **A new selector, `{"channel": c}`.** It would change the envelope shape for something a participant kind already expresses, and every binding and SDK would need to learn it. Addressing a channel like any participant keeps 1.1 clients working unchanged.
- **Channels outside the graph, with their own membership.** Membership would become a second authority system. Edges already say who may send to whom; subscription is one more flow edge, granted by whoever may change the graph.
- **Delivering posts to the channel itself, and reading its inbox.** Reading would move the channel's delivery mark, so two observers would steal posts from each other.
- **Writing the adapter as a script in another language.** It would be a second implementation of the wire to keep in step with the contract. In Pudu it reads the same generated operations, members, and vocabulary as the fabric.
- **Hosting a public fabric on the documentation site.** The site is static and the reference store is in memory; a public fabric would hold strangers' tokens and work. The channel viewer is a static page that talks to the visitor's own local fabric, with a recorded real run for visitors who have none.

## Consequences

Any coding agent that loads tools over standard input joins a graph without code of their own, and two different agents can delegate to each other through a channel with a trace that covers the whole exchange. Channel history is a scan of the ledger, linear in its length like every page; an index is a store concern for a persistent store. Claiming a channel task is decided by the fabric in the same atomic step that accepts the claiming envelope, so two runners that start at the same instant cannot both work: the second one's progress is refused and it moves on. An agent's command line must be signed in on the host that runs its runner.

## Validation

[[test/Engine/ChannelTest]] covers fan-out, kind filters, the sender's exclusion, gating through a channel, one answer per channel task, the channel rules, and history visibility. [[test/Security/ChannelTest]] drives the HTTP binding: closed history for non-members and other graphs and scopes, observers that cannot post, a channel that cannot be made to speak, held values absent from history and refused where a non-audience subscriber would hear them, and preflights. [[test/Agent/AdapterTest]] covers the handshake, the catalog, refusals, payloads, and the runner's prompt. Two separate hosted agent processes attached as builder and reviewer completed a review through `#reviews` against a running fabric, and the lead's trace of the result reached the review; that run is the recording on the channel viewer.

## Referenced by

[[decisions/_MOC]] · [[protocol/15-Channels]] · [[src/Agent/_MOC]]
