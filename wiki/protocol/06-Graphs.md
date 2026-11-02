---
type: specification
chapter: 6
tags: [protocol, specification]
---

# 6. Graph mutation

## 6.1 Creating a graph

A graph is created empty or with an initial set of participants and edges. Creation is checked with the same rules as a mutation; a graph that would violate them is never created. A new graph has revision 1.

## 6.2 Mutations

A mutation is a request carrying `expectedRevision` and an ordered list of operations:

| Operation | Members | Effect |
| --- | --- | --- |
| `add-participant` | `participant` | Adds the participant. Refused if the id exists. |
| `remove-participant` | `id` | Removes the participant and every edge that touches it. |
| `add-edge` | `edge` | Adds the edge. Refused if the id exists or an endpoint is missing. |
| `remove-edge` | `id` | Removes the edge. |

The fabric applies the operations in order to a copy of the graph, checks the result, and replaces the graph only if every operation applied and every check passed. A mutation therefore applies completely or not at all.

If `expectedRevision` differs from the graph's current revision the mutation is refused with `grail.revision-conflict` and the problem carries the current revision. On success the revision grows by exactly one, whatever the number of operations, and the fabric appends a `graph.mutation` entry to the ledger whose payload is the mutation and whose `source` is the participant the token acts for.

## 6.3 The acyclicity rule

After a mutation, the `dependency` edges of a graph MUST form a directed acyclic graph. A mutation that would close a cycle is refused with `grail.cycle`, and the problem lists the participants of one cycle in order. A cycle of dependencies can never be satisfied, so refusing it at mutation time is the only point where the error is cheap.

Flow edges are not subject to this rule.

## 6.4 Limits

A mutation carries at most 256 operations. The graph limits of [[protocol/02-Model#2.5 Graph]] apply to the result.

## 6.5 Graphs inside graphs

A participant of kind `graph` stands for another graph of the same scope. Envelopes sent to it are delivered to the participants of the inner graph that hold the role `entry`. Those participants answer a task as any recipient does ([[protocol/04-Transfer#4.1 Routing]]): the answer is sent in the inner graph and reaches the task's source in the outer graph. Containment forms its own graph: graph `G` contains graph `H` when `G` has a participant of kind `graph` naming `H`.

- Containment MUST be acyclic. A graph may not contain itself, directly or through other graphs (`grail.cycle`).
- Containment depth MUST NOT exceed 8 (`grail.limit-exceeded`).
- A graph participant MUST name a graph of the same scope. Naming a graph of another scope is indistinguishable from naming a graph that does not exist (`grail.not-found`).

## Referenced by

[[protocol/_MOC]] · [[protocol/02-Model]] · [[domain/Graph]] · [[domain/Mutation]]
