---
type: specification
chapter: 14
tags: [protocol, specification, security, custody]
---

# 14. Custody

Agents need keys: an API token, a database password, a signing key. The usual answer puts them in environment variables or in the prompt. Then a model that reads untrusted text can be talked into repeating them. A tool that logs its input writes them down. A message to another agent carries them further. Custody gives Grail a different answer: **participants use secrets by name, and the value exists only where the work is done.**

The fabric is on every path a message can take, so it can enforce this. It is the one place that sees every envelope, knows every recipient, and decides what each delivery contains.

## 14.1 Principles

1. **Reference, never value.** Participants write `{"$secret": "<name>"}` where a value would go. The reference is what is digested, stored, traced, read, and exported.
2. **Late binding, to executors only.** The fabric replaces a reference with its value only in a delivery, at the moment the recipient pulls it, and only for recipients in the secret's audience. An audience may hold only `tool` and `service` participants. Models, people, memory, and graphs are never shown a value.
3. **Least privilege, counted.** A secret belongs to one graph. Its policy names who receives it (`audience`), who may ask for it (`senders`), which kinds may carry it (`kinds`), how often (`uses`), and until when (`expires`).
4. **Tripwire with consequences.** No envelope, bridged message, or imported handoff may contain a held value, whole, in fragments, or in a common disguise. A token that trips the wire `secretStrikes` times is revoked, with every token delegated from it.
5. **Write only.** A value is given to custody once and can never be read back through any operation.
6. **Accounted.** Every reveal is counted on the secret, with the time of the last one, so an owner sees how often a key left custody.
7. **Never portable.** Values do not travel. A handoff names the secrets its context needs, and the receiving owner binds its own.

## 14.2 Deposits

`putSecret` (`secret.manage` for the graph) gives a value to custody under a name:

| Member | Meaning |
| --- | --- |
| `value` | `secretLengthMin` to `secretBytes` characters. Write-only. |
| `graph` | The graph whose envelopes may reference it. |
| `audience` | `tool` or `service` participants of that graph whose deliveries receive the value. At least one. An audience member of any other kind is refused with `grail.forbidden`. |
| `senders` | Participants that may reference it. Empty means any participant of the graph. |
| `kinds` | Kinds that may carry a reference. Empty means any. |
| `uses` | Admitted envelopes that may reference it before it is spent. Absent means unbounded. |
| `expires` | When references stop being admitted or revealed. |
| `description` | What the secret is for, so agents can choose it by purpose. |

Putting a name again rotates it: the version grows by one and later deliveries reveal the new value. A name belongs to one graph for its whole life. A scope holds at most `secrets` names. Every audience member and sender MUST be a participant of the graph, or the deposit is refused with `grail.not-found`.

The answer, and `listSecrets`, return the name, version, graph, policy, remaining uses, creation time, how many deliveries have revealed this version (`reveals`), and when the last one did (`revealed`). Neither returns the value. `listSecrets` needs `graph.read` and lists only secrets of the graph a token is bound to, or of every graph for an unbound token. This is how agents learn which secrets exist and what they are for. `deleteSecret` destroys a secret. References to it stop resolving at once, including references already admitted and not yet delivered.

## 14.3 Admission

Custody checks every envelope before anything is appended:

1. Before any other check, so that a leak is always reported as a leak: if the envelope's body contains any form of a value the scope holds, the envelope is refused with `grail.secret-exposed`. The forms are:
   - the value as written, escaped inside JSON text, and reversed;
   - percent-encoded, and in hexadecimal of either case;
   - in standard and URL-safe base64 at every byte alignment, so a value inside a longer encoded stream is found;
   - every aligned window of `secretFragment` characters, so any contiguous piece of `2 × secretFragment − 1` characters or more is found, wherever the rest of the value went.

   A refusal is a strike against the presenting token unless its audience is the owner. The problem's `strikes` member says how many strikes the token has. At `secretStrikes` the token is revoked as by `revokeToken`, so it and every token delegated from it stop working.
2. After routing resolves the recipients, for each distinct reference in the payload, the named secret MUST belong to the envelope's graph (`grail.not-found` otherwise) and must not have expired (`grail.expired`). It MUST have uses left, the sender MUST be listed when `senders` is not empty, the kind MUST be listed when `kinds` is not empty, and every resolved recipient MUST be in the audience (each `grail.forbidden` otherwise).
3. Each reference consumes one use.

The same checks apply to messages carried by the bridge ([[protocol/10-Bridge]]). An imported handoff is refused with `grail.secret-exposed` when its document contains a held value ([[protocol/13-Portability]]).

The rule that every recipient must be in the audience is deliberately strict. A reference routed to a model must be refused, not quietly delivered unresolved, so the sender learns at once that it asked for the wrong thing.

## 14.4 Delivery

When a recipient pulls its deliveries, each reference is replaced by the value, as a JSON string, when its secret still exists, has not expired, lists that recipient in its audience, and the recipient is still a `tool` or `service` participant. The last condition is checked again at every pull, so a graph mutated after the deposit cannot turn a model into an audience member. Each reveal adds one to the secret's `reveals`. Nothing else ever reveals a value. That includes `readTransfer`, `traceTransfer`, `readLedger`, `readHandoff`, `exportHandoff`, discovery, and logs. Because the stored body keeps the reference, the ledger proves which secret, at which point in the conversation, was handed to which executor, without holding the secret itself.

Revealing a value also requires the whole presenting token's verified delegation chain to hold that authority. Every non-owner audience in the chain MUST currently be a tool or service participant in the secret's audience. An agent cannot obtain a key by delegating `transfer.receive` to an executor identity. An owner may issue an executor token directly; an authorized executor may narrow it further. An empty chain is not authority.

The stored envelope's graph, sender, and kind MUST still satisfy the current secret policy at reveal time, including after rotation. `uses` counts admission rather than redelivery and is not decremented again. A refusal answers `grail.forbidden` and MUST commit neither delivery acknowledgment marks nor any reveal counters from the batch.

## 14.5 Storage

The reference fabric seals each value with an authenticated cipher. The key is derived from the fabric secret and the scope, a fresh nonce is drawn for every version, and the scope, name, and version are bound as associated data. A sealed value moved to another scope, name, or version does not open. Values are opened only to reveal them in a delivery and to check admissions. They never appear in log lines; notifications name a secret and its version only.

## 14.6 Across fabrics

A handoff's `needs` lists the secret names its readable entries reference. The receiving owner deposits its own values under those names in the destination graph, with its own policy. The two fabrics never exchange a value, and a stolen handoff contains nothing to steal.

## 14.7 Residual risks and how they are bounded

Custody removes the common ways a key escapes. Four risks cannot be removed by a message fabric alone. Each is bounded here, and the bound is part of the protocol.

- **The executor holds the value.** Whoever is revealed a key can misuse it; no protocol can stop that. Custody bounds it in four ways. Only `tool` and `service` participants can receive values, which is checked at deposit and again at every reveal. Every reveal is counted and timestamped. `uses` and `expires` limit how long and how often a value goes out. The tripwire stops an executor from passing the key on through Grail. An executor MUST decide for itself where a key may be sent. It pins the destination host and accepts only plain paths or arguments from the request, because a sender that can choose the address, for example with `@other.host` in a path, can make the executor carry the key anywhere.
- **Leaks the tripwire cannot see.** The forms of 14.3 cover the value whole, in fragments of `2 × secretFragment − 1` characters, and in the encodings most often used to smuggle text. A value cut into pieces shorter than that, transformed by a cipher or an unlisted encoding, or described rather than written is out of reach. Such leaks need a sender that already holds the value. Under 14.2 only executors do, and each attempt that is caught costs a strike. Deposit only the secret part of a credential, not a whole connection string, so that fragments of shared text such as a host name never match.
- **Probing.** A sender can test a guess by sending it and watching for a refusal. Every refusal is a strike, and `secretStrikes` refusals revoke the token and its delegates. A guess must also be a full value or a whole fragment of at least `secretFragment` characters. Guessing a high-entropy secret within three attempts is not a practical attack. Short or low-entropy secrets do not belong in custody, and values shorter than `secretLengthMin` are refused.
- **Durability.** The reference store is in memory, so custody empties when the fabric stops, like everything else it holds. That is the safe failure. A fabric that persists custody MUST store only sealed values, keep the sealing key outside the stored data, and bind every sealed value to its scope, name, and version as 14.5 requires.

## 14.8 Threats

An executor's destination policy MUST cover redirects and proxies as well as the initial URL. The reference example refuses every redirect and ignores environment proxy configuration for credential-bearing requests. Its tests exercise separate local service and collector authorities without using provider credentials.

| Threat | Control |
| --- | --- |
| A model repeats a key it was shown | Models are never shown keys; only tool and service participants can be an audience. |
| Prompt injection asks an agent to post a key elsewhere | The agent never held the key, and the tripwire refuses any envelope that does. |
| An executor echoes a key in its result | `grail.secret-exposed`. |
| A reference routed to the wrong participant | Every recipient must be in the audience. |
| A compromised participant asks for a key it should not use | `senders`, `kinds`, and `uses`. |
| A key leaks through a trace, ledger read, or handoff | Only references are stored, traced, or exported. |
| A key leaks in pieces or encoded | Fragments, alignments, and encodings of 14.3. |
| Repeated probing for a value | Strikes, then revocation of the token and its delegates. |
| A model added to an audience by a later graph change | The executor kind is checked again at every reveal. |
| A key outlives its purpose | `expires`, `uses`, rotation, and deletion. |
| A stored value is copied | It is sealed and bound to its scope, name, and version. |

## Referenced by

[[protocol/_MOC]] · [[protocol/07-Security]] · [[protocol/13-Portability]] · [[decisions/ADR-0010-custody]] · [[src/Engine/Custody]] · [[src/Services/Custody]]
