---
type: domain
tags: [domain, security, custody]
aliases: [Custody, Secret reference]
---

# Custody

- **Definition:** The fabric holding a scope's secrets sealed, with a policy each, and revealing a value only in a delivery to the participants named as its audience.
- **Canonical name:** Custody; a held value is a *secret*, and `{"$secret": name}` in a payload is a *secret reference*.
- **Not:** An environment variable, a vault the agent reads from, or a key the fabric uses itself.
- **Example:** Secret `github` in graph `g`, audience `executor`, senders `planner`, kinds `tool.call`. The planner sends a `tool.call` with `{"$secret": "github"}`; only the executor's delivery holds the token.

## Referenced by

[[protocol/14-Custody]] · [[src/Domain/Custody]] · [[domain/_MOC]]
