---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: HIGH
tags: [adr, protocol, security, custody]
---

# ADR-0010 — Participants use secrets by name; the fabric reveals values only to their executors

## Context

Agents work with keys, and the common practice is to hand them over: environment variables in the agent's process, keys pasted into prompts, tokens passed from one tool to the next. Each of these puts the value where a model can read it. A model that also reads untrusted text can then be steered into repeating it. Private data, untrusted instructions, and a way out, all in one place, is the combination prompt-injection attacks need. Tool protocols forbid passing tokens through for this reason, and broker designs that inject credentials at execution time keep them out of prompts. A broker in front of one tool, though, does not see the rest of the conversation. It cannot stop a key from reaching another agent, a log, or a ledger.

A Grail fabric sees every envelope and decides what every delivery contains, so it can be the broker for the whole graph.

## Decision

Add chapter 14. A secret is deposited once, sealed, and never readable again. Participants reference it as `{"$secret": name}`. Admission refuses any envelope, bridged message, or imported handoff holding a held value, and checks each reference against the secret's graph, expiry, uses, senders, kinds, and audience, counting a use. Delivery is the only place a reference becomes a value, and only for audience members. Handoffs list the names they need and never carry values. `listSecrets` tells agents what exists and what it is for.

Considered and rejected:

- **Revealing to any recipient and trusting the graph.** A reference routed to a model would deliver the key to the model. Every recipient must be in the audience.
- **Delivering a reference unresolved to recipients outside the audience.** This fails silently. Refusing at admission tells the sender at once.
- **Resolving at admission and storing the value.** The ledger, traces, and handoffs would hold it. Resolving at pull time keeps the stored record clean and makes rotation and deletion take effect immediately.
- **The fabric calling external services with the key.** That makes the fabric a general proxy for arbitrary addresses. Executors make the calls; the fabric decides what they receive.
- **Keyed fingerprints instead of values for the tripwire.** Matching a value inside arbitrary text needs the value. It is opened in memory only for the check, under the same sealing.

## Consequences

A model can use a key it has never seen, and a leaked key cannot travel through Grail undetected in its common forms. The executor still holds the value, so audiences must stay small and trusted. The tripwire is a narrowing control, not a proof: split, re-encoded, or paraphrased values are out of its reach, and the chapter says so. Probing by guessing full values is possible only at the cost of guessing the secret. Each admission opens every held value of the scope, which is bounded by `secrets`.

## Validation

[[test/Security/CustodyTest]] runs through the HTTP router. It covers deposit answers without values, the missing read operation, references in stored envelopes, ledgers, and traces, reveal for the executor only, the tripwire in plain text, base64, and hex, and refusals by audience, sender, kind, spent uses, expiry, and unknown name. It also covers rotation, deletion of pending references, handoff `needs`, an intact handoff smuggling a value, and the bridge. Mutation testing covers [[src/Engine/Custody]], [[src/Engine/Codec/Custody]], and [[src/Services/Custody]].

## Referenced by

[[decisions/_MOC]] · [[protocol/14-Custody]]
