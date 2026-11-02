---
uid: guides.contributing
description: Change the proposal, validate the implementation, and build the documentation.
---

# Contribute to the proposal

The repository is private for invited testers. Report reproducible behavior with the request, expected result, actual result, and reference fabric version. Follow the repository's security policy for sensitive findings.

## Change the right source

| Change | Source |
| --- | --- |
| Wire fields, operations, errors, limits | `schema/grail.openapi.json`, then run `pudu run tools/Contract.pudu`. |
| Protocol semantics | `wiki/protocol/` and an appropriate decision record. |
| Runtime behavior | `src/`, with regressions under `test/`. |
| Practical documentation | `website/docs/`. |
| Site configuration and appearance | `website/docgen.json` and `website/template/`. |

Run the complete checks in `CONTRIBUTING.md`. `pudu run tools/Layers.pudu` enforces the dependency catalog and rejects cycles. Test changed engines with meaningful mutation cases.

## Build the documentation

With Pudu 0.1.3 and Python 3.12 or later, run `python3 tools/BuildDocs.py`. Add `--serve --port 8080` for a preview. The build treats warnings as errors and generates the HTTP reference from the same contract used by the fabric.

Feature PRs target `dev`. Promote a reviewed release to `main` through a release branch, verify the local API workflow, and publish only static documentation to the existing free Worker. Record merge commits in their issues and remove completed feature branches. The API is not deployed.
