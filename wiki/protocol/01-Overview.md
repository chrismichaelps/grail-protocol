---
type: specification
chapter: 1
tags: [protocol, specification]
---

# 1. Overview

## 1.1 Purpose

Most protocols for intelligent software describe one relationship: a client that calls a tool. Collaboration between agents, hand-offs to people, shared memory, and multi-step workflows are then rebuilt in every framework on top of that call. Grail starts from the other end. It describes a graph of participants and the information that flows along its edges, and treats a tool call as one shape of that flow rather than the only one.

Grail is designed so that:

- any participant can talk to any other participant it is connected to, using one message shape;
- the order in which work may happen is declared in the graph, not hidden in prompts;
- every result can answer the question "what information produced this?";
- one user's graphs can never observe or reach another user's graphs;
- authority is always explicit, carried in tokens that can only be narrowed when delegated;
- an agent's working context can move between fabrics run by different software and different organizations, and still prove where it came from.

## 1.2 Non-goals

- Grail does not define how a model reasons, plans, or prompts. A participant is opaque.
- Grail does not define a payload vocabulary for every domain. Payloads are typed by a schema reference; the protocol only defines the envelope and the kinds that drive its own behavior.
- Grail does not promise delivery semantics the network cannot provide. "Exactly once" is defined precisely as effectively-once processing ([[protocol/04-Transfer#4.3 Delivery guarantees]]).
- Grail does not replace transport security. Bindings run over TLS or an equivalent channel.

## 1.3 Terminology

| Term | Meaning |
| --- | --- |
| [[domain/Scope\|Scope]] | The isolation boundary owned by one principal (a user or an organization). Every other object lives inside exactly one scope. |
| [[domain/Participant\|Participant]] | Anything that sends or receives envelopes: an agent, a tool, a memory store, a person, a service, or a graph. |
| [[domain/Graph\|Graph]] | A versioned set of participants and the edges between them. A graph may itself be a participant of another graph. |
| [[domain/Edge\|Edge]] | A directed, typed link from one participant to another. Edges authorize flow and declare ordering. |
| [[domain/Envelope\|Envelope]] | The single message shape of the protocol. |
| [[domain/Transfer\|Transfer]] | One envelope moving along one or more edges, with a lifecycle the fabric tracks. |
| [[domain/Fabric\|Fabric]] | The service that hosts scopes and graphs, routes transfers, keeps the ledger, and enforces isolation. |
| [[domain/Ledger\|Ledger]] | The append-only, hash-linked record of accepted envelopes in a scope. |
| [[domain/Capability\|Capability token]] | A signed, expiring grant of abilities over a scope or a graph, which may be delegated with narrower abilities. |
| [[domain/Channel\|Channel]] | A participant that never acts: it hands each post to its subscribers and keeps every post readable in order. |
| [[domain/Handoff\|Handoff]] | A sealed, self-verifying document holding a participant's context, carried from one fabric to another. |

## 1.4 Relationship to tool protocols

Existing tool protocols built on JSON-RPC remain useful at the edge of a graph. Grail carries their messages unchanged inside envelopes of kind `bridge.rpc` ([[protocol/10-Bridge]]). A tool server reached through the bridge becomes an ordinary participant: it can be targeted by role, gated by dependencies, and traced through provenance. The bridge preserves the tool protocol's own request and response semantics; it does not claim that every feature of every tool protocol gains new meaning inside a graph.

Tool protocols describe a session between one client and one server, and their state ends with that session. Grail's unit is the graph and its ledger, which outlive any connection, and chapter 13 lets that state cross from one fabric to another. These are different layers: a tool protocol is how one participant reaches a tool; Grail is how participants, including tools reached that way, share work, order it, prove it, and take it elsewhere.

## 1.5 Design principles

1. **One mechanism.** Request and response, fire-and-forget, streaming, publish and subscribe, and workflows are all transfers of envelopes. They differ only in kind, targeting, and causal links.
2. **The graph is the program.** Topology and edge constraints express who may talk to whom and in what order.
3. **Provenance by construction.** Envelopes name their causal parents and the fabric links each accepted envelope into a hash chain. Content can be erased; the record that it existed cannot be rewritten.
4. **Isolation by construction.** Scope is part of every identifier the fabric resolves. A reference into a scope the caller does not hold behaves exactly like a reference to nothing.
5. **No ambient authority.** Every operation presents a token. A token names its scope, its audience, its abilities, and its lifetime.
6. **Portable by construction.** Because history is content-addressed, it can be moved as a document and checked by whoever receives it. No fabric has to trust another's database, and none has to call another to accept work.
7. **Keys by name.** Participants reference secrets; the fabric reveals a value only in a delivery to the executor allowed to use it, and refuses any message that carries one. A model can use a key it has never seen.

## 1.6 How systems use Grail

An owner holds the root token of a scope and rarely uses it directly. It creates a graph, gives an orchestrating agent a token bound to that graph with the abilities to change it and delegate, and steps back. The orchestrator adds participants as it needs them (a researcher, a writer, a reviewer, a tool server reached through the bridge, a person who approves) and gives each a narrower token that can do only its part. Every participant, wherever it runs, pulls its deliveries with a long wait, answers the tasks it receives, and names what it used as parents. When the orchestrator needs the writer to wait for the researcher, it adds a dependency edge instead of writing a scheduler. When it needs a person, it sends `input.request` and the task waits. When anyone asks how a result was produced, the trace answers from the ledger. When a subagent misbehaves, the orchestrator revokes its token and every token it handed on.

When the work has to continue somewhere else (a coding assistant handing a task to a support desk, or a research tool handing findings to a writing app), the orchestrator exports the agent's context as a handoff, the origin attests it, and the other fabric imports it for a participant its owner already placed. The agent picks up from the import entry, and the trace there leads back to the origin.

Agents built by others join the same way. A coding agent attaches through an adapter that holds its token and gives it tools to read its inbox, answer tasks, and post to channels ([[protocol/08-Bindings#8.6 Attaching hosted agents]]). The team talks in channels that people and dashboards can watch without being asked to answer ([[protocol/15-Channels]]).

The same shape serves one developer with three local agents over the line binding, a company running thousands of agents across regions over HTTP, and a platform hosting many customers in separate scopes on one fabric.

## Referenced by

[[protocol/_MOC]] · [[protocol/02-Model]]
