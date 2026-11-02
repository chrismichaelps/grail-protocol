---
uid: concepts.overview
description: Understand the objects and guarantees behind Grail's collaboration model.
---

# How Grail fits together

A **fabric** accepts or refuses messages. A **scope** owns graphs and isolates them from other owners. A **graph** describes participants and their permitted relationships. An **envelope** carries information between those participants.

Participants decide what work to attempt. The fabric checks whether that attempt has a route, enough authority, the required causal evidence, and a valid lifecycle transition.

| Read next | Learn |
| --- | --- |
| [Graphs and teams](graphs.md) | Routing, dependency gates, and nested participants. |
| [Envelopes and history](envelopes.md) | Parent references, lifecycle answers, traces, and ledger verification. |
| [Delegated authority](../guides/capabilities.md) | Give each participant only the permissions it needs. |

The reference fabric is a local implementation of a draft protocol. The contract and specification define interoperable behavior; the Pudu module structure is an implementation choice.
