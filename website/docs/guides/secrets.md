---
uid: guides.secrets
description: Let agents use API keys and passwords by name, without any model ever seeing the value.
---

# Use keys without showing them to agents

An agent that holds a key can be talked into repeating it. With custody, the agent never holds it. You give the key to the fabric once, and agents refer to it by name. The fabric hands the value only to the executor you name, at the moment it pulls its work, and refuses any message that tries to carry the value anywhere else.

## Give a key to custody

Only a token with `secret.manage` for the graph can deposit. Name the participant that will actually call the external service as the `audience`; it must be a `tool` or `service` participant, never an agent. Name the agents allowed to ask for it as `senders`:

```text
PUT /v1/scopes/demo/secrets/github
{
  "value": "<the key>",
  "graph": "workflow",
  "audience": ["executor"],
  "senders": ["planner"],
  "kinds": ["tool.call"],
  "uses": 50,
  "expires": 1798761600000,
  "description": "repository access for release automation"
}
```

The answer describes the secret, with its version, policy, remaining uses, and how many deliveries have revealed it, but never the value. No operation reads a value back. Putting the same name again rotates it to a new version.

## Let agents discover what exists

`GET /v1/scopes/demo/secrets` lists names, descriptions, and policies for the graph a token is bound to. This is how an agent knows that `github` exists and what it is for, without ever learning what it is.

## Use it by name

The agent puts a reference wherever the value would go:

```json
{"kind": "tool.call", "source": "planner", "target": {"participant": "executor"},
 "payload": {"url": "https://api.example.test/repos", "auth": {"$secret": "github"}}}
```

The ledger, traces, reads, and handoffs keep `{"$secret": "github"}`. When `executor` pulls its deliveries, it receives `"auth": "<the key>"`, and nobody else ever does.

## What the fabric refuses

| Attempt | Answer |
| --- | --- |
| Any message holding the value: whole, any piece of 31 characters or more, reversed, JSON-escaped, percent-encoded, hex, or base64 at any alignment | `grail.secret-exposed`, and a strike against the sender's token |
| A third strike | the token and every token delegated from it are revoked |
| An agent, person, memory, or graph as the audience | `grail.forbidden` |
| A reference to a participant outside the audience | `grail.forbidden` |
| A reference from an agent not in `senders`, or in a kind not in `kinds` | `grail.forbidden` |
| A reference after the last use | `grail.forbidden` |
| A reference after `expires` | `grail.expired` |
| A name the graph does not hold | `grail.not-found` |

`DELETE /v1/scopes/demo/secrets/github` destroys the key. Calls already waiting for delivery stop resolving at once.

## Moving agents between fabrics

A [handoff](handoffs.md) lists the secrets its context `needs` and never carries a value. The receiving owner deposits its own key under the same name.

## Good practice

- Keep models out of every audience. The audience is for executors that make the external call.
- Let the executor, not the request, decide where a key goes. Pin the destination host and accept only a plain path; see `pinned` in `examples/secrets/agents.py`.
- Prefer `uses` and `expires` over long-lived keys, and rotate by putting the name again.
- Store only high-entropy values. Custody refuses values shorter than 12 characters.
- Deposit only the secret part of a credential, such as the password rather than the whole connection URL, so shared text like a host name never matches the tripwire.
- Watch `reveals` in the listing. A count that grows faster than your executor's work is worth a look.

The [custody chapter](../protocol/14-Custody.md) is the normative text, including what the tripwire does not catch.
