---
type: tool
path: "@root/tools/Site.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Site

> @Tools.Site.Builder — assembles the documentation site's sources from the paper, the vault, and the contract

## Purpose

Assembles the documentation site's sources from the paper, the vault, and the contract into `build/site`. This command neither renders nor serves the site. Rendering requires a compatible docgen CLI with `build build/site --serve`; docgen 0.1.0 needs the `Serve.pudu` compatibility patch described in the repository README before it can run on Pudu 0.1.3.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Fs`, `Std.Io`, `Std.Json`, `Std.Result`
- **Consumed by:** the runner

## Referenced by

[[tools/_MOC]]
