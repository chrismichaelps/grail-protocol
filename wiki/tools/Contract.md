---
type: tool
path: "@root/tools/Contract.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Contract

> @Tools.Contract.Projector — writes or checks the modules projected from the contract

## Purpose

Writes or checks the modules projected from the contract.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Env`, `Std.Io`, `Std.Option`, `Std.Result`
- **Consumed by:** the runner

<!-- authored -->
## Algorithm

1. Read the contract with [[tools/Contract/Read]]: operations with their path and query parameters, enumerations, problem registry, limits, headers, and every object schema's members.
2. Render nine modules with [[tools/Contract/Emit]].
3. Write them, or with `--check` compare them with what is on disk and fail on any difference.

## Grill Log

- **Q:** Generate the contract from code, or code from the contract? **A:** Code from the contract. **Rationale:** the contract is what other implementations read; it must be the single place a change happens. **Rejected:** describing routes in code and exporting a document.
- **Q:** How does a change in the schema reach the code? **A:** Through named constants. Renaming a member, operation, kind, or problem code removes a constant, and every use stops compiling. **Rejected:** string lookups that fail at run time.
<!-- /authored -->

## Referenced by

[[tools/_MOC]]
