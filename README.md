# Grail: A Graph-Routed Protocol for Accountable Collaboration Between Software Agents

**Grail** (Graph Routed Agent Information Lattice) · protocol version 1.0 · reference fabric 0.1.0 · Apache License 2.0

## Abstract

Software that reasons, calls tools, and delegates work to other software is increasingly assembled from many cooperating parts: orchestrating agents, specialised subagents, tool servers, memory stores, and the people who approve or correct their work. The protocols in common use describe one of these relationships at a time, most often a client invoking a tool, and leave the rest (who may hand work to whom, which work must wait for which, what authority a subagent holds, and how a result can later be explained) to ad hoc code inside each framework. We present Grail, a protocol in which every participant is a node of an explicitly declared graph and every interaction is a single kind of message, the envelope, admitted by a fabric only if it is consistent with that graph. Grail makes four properties part of the wire contract rather than conventions on top of it: ordering constraints are expressed as acyclic dependency edges and enforced by checking the causal ancestry each message declares; authority is carried in signed capability tokens that can only be attenuated when delegated; every accepted message is bound into a hash-linked ledger whose digests any reader can recompute; and each owner's graphs live in a scope that is unobservable to every other principal. We describe the model, the admission rules, and a contract-first design in which a single OpenAPI document generates every binding of the reference implementation. We evaluate the reference fabric with conformance tests, independently computed hash vectors, mutation testing, and an adversarial campaign of forty-five attacks, which exposed six weaknesses that are now fixed and permanently tested.

## 1. Introduction

A modern assistant that writes a market report may involve an orchestrator that plans the work, a researcher that searches, a writer that drafts, a reviewer who is a person, and several tools reached over a JSON-RPC interface. Each of these relationships has a shape that matters. The writer must not begin before the researcher has produced something; the reviewer's approval must precede publication; the researcher should be able to search but not to publish; and when the report contains an error, someone must be able to ask which inputs produced it. In current practice these constraints live in prompts, in the control flow of a particular framework, or nowhere at all. Authority is typically a single credential shared by every component, so a compromised subagent holds everything its orchestrator holds.

Grail starts from the observation that all of these concerns are properties of a graph. If the participants and the permitted relationships between them are declared explicitly, a neutral service can check every message against the declaration at the moment it is sent, and the record of accepted messages becomes an audit trail by construction. Grail therefore unifies what other designs keep separate. Calling a tool, assigning a task to an agent, asking a person a question, and streaming partial output are all transfers of envelopes along edges. The difference between them is the kind of the envelope and the shape of the graph, not a different API.

This document is both an introduction to the protocol and an account of the reference implementation. Section 2 places Grail among related work. Section 3 states the design goals. Section 4 gives the model, and Section 5 the mechanisms by which a fabric admits, routes, orders, and records messages. Section 6 describes how the wire format is defined by one machine-readable contract. Section 7 summarises the reference fabric, Section 8 evaluates it, and Section 9 discusses limitations. Section 10 explains how to run everything locally. The normative specification, which this document summarises, lives in [`wiki/protocol`](wiki/protocol/_MOC.md).

## 2. Background and related work

Remote procedure call protocols built on JSON-RPC 2.0 [7] have become the common way to expose tools to language-model applications. They define a request and response between one client and one server and say nothing about relationships among many parties. Grail does not replace them; it carries their messages unchanged inside envelopes of kind `bridge.rpc`, so that an existing tool server becomes one participant of a graph and gains routing, authorisation, ordering, and provenance without being modified.

Protocols for communication between agents typically introduce a task abstraction with a lifecycle and a discovery document describing what an agent can do. Grail adopts both ideas, a seven-state task lifecycle and a discovery document at `/.well-known/grail`, but places tasks inside a graph rather than between two endpoints, which is what allows ordering constraints and delegation to be checked by a third party.

Workflow engines express ordering as a directed acyclic graph executed by a central scheduler. Grail keeps the acyclic graph and removes the scheduler. A dependency edge is not an instruction to run something; it is a precondition that the fabric checks against the causal ancestry a task declares, so participants remain autonomous and the fabric remains a referee rather than a conductor. Detecting a cycle when a graph changes uses linear-time topological ordering [10].

Capability-based security grants authority through unforgeable references rather than identities. Macaroons [4] showed how bearer credentials can be attenuated by their holders, and later delegation-chain designs carry the full chain of grants with each token [5]. Grail's tokens follow this line: each delegated token embeds its ancestry, and verification requires every link to narrow its parent in abilities, graph, and lifetime.

Provenance has been modelled formally by the W3C PROV family [6], and tamper-evident append-only logs are deployed at scale in Certificate Transparency [8]. Grail combines a lighter version of both. Every envelope names the envelopes it was derived from, and every accepted envelope is bound into a hash chain over a canonical JSON form [9], so the question "what produced this result?" has a verifiable answer. Ordering for human readers uses hybrid logical clocks [3], while causality itself is carried only by explicit parent references, following the distinction between physical time and causal order drawn by Lamport [2].

Errors follow RFC 9457 problem details [11], and normative language follows RFC 2119 and RFC 8174 [1].

## 3. Design goals

Grail was designed to satisfy six goals, each of which shaped a specific mechanism. The first is that collaboration must be expressible without a privileged coordinator: any participant may send to any other it is connected to, and the fabric only judges. The second is that ordering must be declarative and checkable, so that "the writer waits for the researcher" is a fact the fabric can refuse to violate rather than an intention buried in a prompt. The third is least authority: a component should hold exactly the abilities its task requires, and delegation must never be able to widen them. The fourth is accountability: any result must be traceable to its inputs, and the record must be tamper-evident while still allowing personal data to be erased. The fifth is isolation strong enough that one principal cannot learn whether another principal's objects exist. The sixth is reach: a participant must be able to take part from any network position that permits an outgoing HTTPS request, including laptops, private networks, and serverless functions, without the fabric ever needing to call it.

## 4. Model

A **scope** is the unit of ownership and isolation; every other object belongs to exactly one scope. Within a scope, a **graph** is a triple $G = (P, F, D)$ where $P$ is a set of participants, $F \subseteq P \times P$ is a set of flow edges each optionally restricted to a set of envelope kinds, and $D \subseteq P \times P$ is a set of dependency edges. The protocol requires that $(P, D)$ be acyclic at all times; flow edges may form cycles, which is how two agents can argue with each other. A participant may itself stand for another graph of the same scope, and the containment relation between graphs must also be acyclic and at most eight levels deep. Every graph carries a revision number, and a change is accepted only if it names the revision it was computed against, which gives concurrent editors optimistic concurrency without locks.

An **envelope** $e$ carries an identifier, its scope and graph, a source participant, a target (a participant, every holder of a role, or every holder of an ability), a kind, an optional payload with a schema reference, delivery requirements, an optional deadline, and a set of **parents** $\pi(e)$ naming earlier envelopes of the same scope from which it was derived. The causal ancestry $\mathrm{anc}(e)$ is the transitive closure of $\pi$. Because a parent must already be in the ledger when its child arrives, the causal graph of a scope is acyclic by construction.

A **fabric** hosts scopes. Its central operation is admission: given the state of a scope, an envelope, a verified capability token, and the current time, it either refuses the envelope with exactly one problem and leaves the scope unchanged, or accepts it, appends it to the scope's ledger, updates any lifecycle the envelope affects, and makes it available to its resolved recipients. Admission is a pure function of its inputs in the reference implementation, which is what makes its behaviour exhaustively testable.

## 5. Mechanisms

### 5.1 Routing and answers

A target is resolved against the flow edges leaving the sender. A participant target resolves only if a flow edge from the source reaches it and carries the envelope's kind; a role or ability target resolves to every such participant holding that role or ability, which gives publish and subscribe without a separate mechanism. Answers are treated differently, and deliberately so. An envelope whose kind answers a task (a result, an error, progress, or a request for input) needs no edge of its own: it is accepted only from a recipient of the task and is routed back to the task's source. Authority to answer is therefore a consequence of having been asked, graphs do not need a return edge for every request edge, and an answer produced inside a nested graph reaches the outer participant that asked.

### 5.2 Dependency gating

For a task $e$ addressed to participant $t$, let $\mathrm{deps}(t) = \{ d \mid (d, t) \in D \}$. The fabric accepts $e$ only if, for every $d \in \mathrm{deps}(t)$, some envelope $a \in \mathrm{anc}(e)$ is a result produced by $d$. The sender proves that the precondition holds by naming the result among its parents; the fabric verifies the claim against its own ledger. No scheduler is involved, ordering cannot be violated by a participant that ignores it, and the check is bounded: if the walk of ancestry reaches the bound published in the contract without finding a required result, the task is refused, so the bound fails closed. An approval gate is simply a dependency edge from a person to the step that must wait for them.

### 5.3 Lifecycles and delivery

Tasks, tool calls, and bridged JSON-RPC requests open a lifecycle with the states submitted, working, input-required, completed, failed, canceled, expired, and rejected, and an explicit transition table that the fabric enforces; only a recipient may advance a task and only its source may cancel it. Delivery is pull-based and cursor-acknowledged. A participant asks for the envelopes addressed to it after a sequence number, optionally waiting up to thirty seconds for one to arrive, and the cursor it passes back acknowledges everything up to it. This choice is what gives the protocol its reach: any participant that can make an outgoing request can take part in real time, and the fabric never needs an address or credentials for its participants. Grail defines three delivery guarantees and declines to promise a fourth. At-most-once envelopes are never served twice, at-least-once envelopes are served until acknowledged, and effectively-once envelopes carry a key such that a repeated send with the same content returns the original receipt while a reused key with different content is refused. Exactly-once delivery over an unreliable network is not achievable, and the protocol does not pretend otherwise.

### 5.4 Provenance

Each accepted envelope receives a sequence number and a digest $\delta = H(\mathrm{canon}(e))$, where $\mathrm{canon}$ sorts object members by key at every depth and removes insignificant whitespace, and $H$ is SHA-256. The ledger binds the digests in order with links $\ell_1 = H(\texttt{grail-ledger:} \Vert \delta_1)$ and $\ell_n = H(\ell_{n-1} \Vert \texttt{:} \Vert \delta_n)$, so altering or removing any entry changes every later link. A trace of an envelope returns its ancestry in ledger order; ancestors the reader may not see are reduced to their digest and position so that the chain remains verifiable. Erasure removes a payload from storage while keeping its digest and link, which reconciles a permanent record with the obligation to delete personal data.

### 5.5 Authority and isolation

A token is a set of claims (scope, optional graph, issuer, audience, abilities, validity window, and the chain of tokens it was delegated from) serialised canonically and signed with HMAC-SHA-256 under a key derived from the fabric's secret and the scope's name. Verification always uses the key of the scope the request names, so a token of another scope fails before any lookup takes place, and the refusal is identical whether the requested object exists or not; scopes cannot be enumerated by status codes, and in our measurements not by timing either. A delegation chain $\tau_0, \ldots, \tau_n$ is accepted only if $\tau_0$ was issued by the scope owner, each $\tau_i$ was issued by the audience of $\tau_{i-1}$, its abilities are a subset of its parent's, its graph restriction is preserved, its validity window lies within its parent's, no token in the chain is revoked, and $n < 8$. Revoking any token therefore revokes everything delegated from it.

## 6. One contract for every binding

The wire format of Grail is defined in exactly one place, the OpenAPI 3.1 document [`schema/grail.openapi.json`](schema/grail.openapi.json). It declares every operation with its path, method, success status, and required ability, every object with its permitted and required members, every enumeration, every limit, every header, and the registry of problem codes with their statuses and titles. The reference implementation never restates any of these. A projector, `tools/Contract.pudu`, reads the contract and generates typed modules of constants from which the router, the request codecs, the validators, the lifecycle tables, and the discovery document are all built. Renaming a member in the contract therefore removes a constant and stops the build at every place that used it; adding an operation stops the server from starting until a handler is bound to it; and the served router is compared at start-up with a description built from the same contract using the standard library's OpenAPI model, so that the routes served and the operations documented cannot diverge. Two bindings are generated from the one contract: an HTTP binding, and a line binding that carries the same operations as one JSON object per line over standard input and output for participants started as local processes.

## 7. Reference implementation

The reference fabric is written in Pudu [12] and organised as thirteen dependency layers, from generated contract constants and pure domain records at the bottom, through pure engines for authority, admission, routing, gating, lifecycles, graph mutation, provenance, and delivery, to services, a mediator-based message pipeline, and the HTTP and line bindings at the top. A gate run on every change reads every import and refuses any edge that points up the table, any cycle among modules, any effect (clock, network, file, randomness) in the pure layers, and any package used outside the layers allowed to use it. Every operation is a message sent through a mediator whose pipeline records it, validates it against rules beyond its shape, guards it with a concurrency limit and a deadline, and publishes a notification after a successful change; outbound calls to other fabrics use a resilience pipeline with retries, a circuit breaker, and timeouts. The design of every module is recorded in the vault under [`wiki/`](wiki/00-INDEX.md).

## 8. Evaluation

**Conformance.** The specification lists ten checks a fabric must pass. The reference suites contain 186 assertions across eleven suites, organised by those checks, covering contract validation, cross-scope isolation, delegation, acyclicity, revisions, dependency gating, lifecycle transitions, deduplication, hash-chain recomputation, and delivery bounds. The canonical form, digests, and links are additionally checked against vectors computed with an independent implementation in a different language, so the tests do not merely restate the code.

**Mutation testing.** To test the tests, the engines were mutated one operator at a time and every mutant was required to make some test fail. Surviving mutants pointed at untested boundaries, such as a deadline exactly equal to the current time or a delegation chain exactly at its depth limit, and at dead code, which was removed. The authority engine kills all of its mutants.

**Adversarial campaign.** We attacked a live fabric as an outsider holding no secret and only narrow tokens, with forty-five attacks spanning token forgery, cross-scope probing, privilege escalation through delegation, ledger poisoning, lifecycle abuse, malformed and oversized input, cross-origin access, algorithmic complexity, request floods, and exhaustion of long-polling workers. Forgery, isolation, and escalation held from the start. Six weaknesses were found and fixed, and the attacks now run on every change in an in-process security suite and against a live server with a stress tool.

| Finding | Before | After |
| --- | --- | --- |
| Creating the largest legal graph (1024 participants) held the store lock | 22.1 s | 0.69 s |
| Refusing a cycle through 1024 participants | 2.84 s | 0.07 s |
| A flood of 800 requests in under one second | all answered | cut at the per-host limit |
| Discovery latency while 40–48 pulls wait | 15.25 s | 7 ms |
| Envelope ids reserved for the fabric's own records | could be claimed by a sender, corrupting the ledger | refused |
| Deduplication keys and ledger size per scope | unbounded | bounded and expiring |

Two of these weaknesses were not in Grail's own code. The standard rate-limiting guard keyed its windows by address and port, so every new connection started a fresh window, and the fix was to identify peers by host; the quadratic cost came from computing reachability per node and was replaced by linear-time topological ordering. Scope enumeration by timing was measured directly: the median time to refuse a request for an existing and a non-existent scope differed by less than one millisecond.

## 9. Limitations and future work

The reference store keeps scopes in memory, so a restart loses them; a durable adapter that replays and verifies the ledger on start is the next step, and the storage boundary was designed as a seam for it. Delivery is pull-only; push delivery to reachable participants is reserved for a minor version and does not change the pull contract. Tokens are signed symmetrically by the fabric, which suffices because the fabric is their only verifier, but asymmetric signatures would allow third parties to verify grants and are left to an extension. The adversarial campaign ran from a single host, so it measures per-host limiting and worker exhaustion rather than a distributed attack, and a fabric exposed to the open internet belongs behind network-level protection. Finally, Grail standardises the envelope and the graph, not the payloads; interoperability of content still depends on shared schemas, which the envelope references but does not define.

## 10. Running Grail locally

The reference fabric needs Pudu 0.1.3. Install the pinned packages, choose a secret, issue the owner's token for a scope, and start the server, which listens on port 7420.

```bash
pudu install --locked
export GRAIL_SECRET="$(openssl rand -hex 32)"
pudu run src/Main.pudu token --scope demo --id root > root.token
pudu run src/Main.pudu serve
```

The running fabric describes itself at `http://127.0.0.1:7420/.well-known/grail` and serves its contract at `http://127.0.0.1:7420/openapi.json`, which any OpenAPI tool can load to generate a client or explore the operations. A complete session, from creating a graph to tracing a result, is walked through in [Appendix A](#appendix-a-a-worked-session).

The documentation is published as a static site built with `pudu-lang-docgen`, which renders Markdown articles and renders the OpenAPI contract as a browsable HTTP API reference with every operation, parameter, schema, and response. The site is assembled from the vault and the contract at build time, so nothing in it is written twice:

```bash
pudu run tools/Site.pudu --serve
```

This builds the site into `build/site/_site` and serves it at `http://localhost:8080`. The same output is what is deployed to Cloudflare as static assets, which the free plan serves without limit. The fabric itself is a native program and runs anywhere a daemon can, on a server, a container platform, or a workstation; it can be published through Cloudflare Tunnel, which places Cloudflare's network in front of it without opening an inbound port.

The protocol's own checks, from the contract projection to the dependency layers, the attack suite, and the live stress tool, are described in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 11. Conclusion

Grail treats the collaboration between software agents as a graph that can be declared, checked, and audited, and it moves ordering, authority, provenance, and isolation from framework code into the protocol itself. The result is that a fabric can refuse an out-of-order step, a widened delegation, a forged token, or a probe into another owner's data with the same mechanism it uses to deliver ordinary work, and can explain any result after the fact. The reference implementation shows that these guarantees can be delivered by a small, layered, contract-driven program and that they survive deliberate attack.

## Appendix A. A worked session

The following exchange shows the protocol end to end with the HTTP binding. The owner creates a graph containing a single orchestrating agent.

```bash
curl -X PUT http://127.0.0.1:7420/v1/scopes/demo/graphs/launch \
  -H "Authorization: Bearer $(cat root.token)" -H 'content-type: application/json' \
  -d '{"participants":[{"id":"orchestrator","kind":"agent"}],"edges":[]}'
```

The owner then delegates to the orchestrator a token bound to that graph, with the abilities it needs to grow the team and run the work. Any holder can later ask what its token allows with a `GET` on `/v1/scopes/demo/tokens/self`.

```bash
curl -X POST http://127.0.0.1:7420/v1/scopes/demo/tokens \
  -H "Authorization: Bearer $(cat root.token)" -H 'content-type: application/json' \
  -d '{"id":"orch-1","audience":"orchestrator","graph":"launch","abilities":["graph.read","graph.write","transfer.send","transfer.receive","transfer.read","ledger.read","token.delegate"],"expires":1830000000000}'
```

The orchestrator spawns a researcher and a writer by mutating the graph against the revision it last read, adding flow edges to each and a dependency edge that makes the writer wait for the researcher. It then delegates to each subagent a token that can only send and receive in this graph.

```bash
curl -X POST http://127.0.0.1:7420/v1/scopes/demo/graphs/launch/mutations \
  -H "Authorization: Bearer $ORCH_TOKEN" -H 'content-type: application/json' \
  -d '{"expectedRevision":1,"operations":[
        {"op":"add-participant","participant":{"id":"researcher","kind":"agent","abilities":["search"]}},
        {"op":"add-participant","participant":{"id":"writer","kind":"agent","roles":["author"]}},
        {"op":"add-edge","edge":{"id":"o-r","from":"orchestrator","to":"researcher","relation":"flow"}},
        {"op":"add-edge","edge":{"id":"o-w","from":"orchestrator","to":"writer","relation":"flow"}},
        {"op":"add-edge","edge":{"id":"r-w","from":"researcher","to":"writer","relation":"dependency"}}]}'
```

The orchestrator sends a task to whoever can search. The researcher, wherever it runs, holds a pull open until the task arrives, and answers with a result naming the task as its parent; the answer returns to the orchestrator without any edge of its own.

```bash
curl -X POST http://127.0.0.1:7420/v1/scopes/demo/transfers \
  -H "Authorization: Bearer $ORCH_TOKEN" -H 'content-type: application/json' \
  -d '{"grail":"1.0","id":"t-1","scope":"demo","graph":"launch","source":"orchestrator","target":{"ability":"search"},"kind":"task","payload":{"question":"Who are the competitors?"}}'

curl "http://127.0.0.1:7420/v1/scopes/demo/graphs/launch/participants/researcher/deliveries?after=0&wait=30000" \
  -H "Authorization: Bearer $RESEARCHER_TOKEN"
```

A task to the writer is accepted only if it names the researcher's result among its parents; otherwise the fabric answers `grail.dependency-unmet` and names the researcher. Afterwards, `/v1/scopes/demo/transfers/{id}/trace` returns the ancestry of any result, `/v1/scopes/demo/ledger` returns the hash-linked record for independent verification, `/v1/scopes/demo/tokens/{id}/revocation` withdraws a misbehaving subagent's authority together with everything it delegated, and `/v1/scopes/demo/transfers/{id}/erasure` removes a payload while the chain still verifies. Tool servers that speak JSON-RPC join through `/v1/scopes/demo/graphs/launch/bridge/{tool}`, and the same operations are available over standard input and output with `pudu run src/Main.pudu lines`.

## References

[1] S. Bradner, "Key words for use in RFCs to Indicate Requirement Levels," RFC 2119, 1997; B. Leiba, "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words," RFC 8174, 2017.

[2] L. Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System," Communications of the ACM 21(7), 1978.

[3] S. Kulkarni, M. Demirbas, D. Madappa, B. Avva, M. Leone, "Logical Physical Clocks," Principles of Distributed Systems (OPODIS), 2014.

[4] A. Birgisson, J. G. Politz, Ú. Erlingsson, A. Taly, M. Vrable, M. Lentczner, "Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud," NDSS, 2014.

[5] User Controlled Authorization Networks (UCAN) specification, UCAN Working Group.

[6] L. Moreau, P. Missier (eds.), "PROV-DM: The PROV Data Model," W3C Recommendation, 2013.

[7] JSON-RPC Working Group, "JSON-RPC 2.0 Specification," 2010.

[8] B. Laurie, E. Messeri, R. Stradling, "Certificate Transparency Version 2.0," RFC 9162, 2021.

[9] A. Rundgren, B. Jordan, S. Erdtman, "JSON Canonicalization Scheme (JCS)," RFC 8785, 2020.

[10] A. B. Kahn, "Topological Sorting of Large Networks," Communications of the ACM 5(11), 1962.

[11] M. Nottingham, E. Wilde, S. Dalal, "Problem Details for HTTP APIs," RFC 9457, 2023.

[12] The Pudu programming language, version 0.1.3.

## License

Grail is released under the Apache License 2.0, whose explicit patent grant allows the many parties a protocol invites to implement it without fear of later claims ([decision record](wiki/decisions/ADR-0006-license.md)).
