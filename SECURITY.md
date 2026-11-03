# Security

Report vulnerabilities privately through GitHub's security advisories for this repository, not in public issues. Include the version, what you sent, what you expected, and what happened.

The threat model and the control each layer applies are in [`wiki/architecture/SECURITY.md`](wiki/architecture/SECURITY.md) and chapter 7 of the specification ([`wiki/protocol/07-Security.md`](wiki/protocol/07-Security.md)).

Supported: the latest release on `main`.

The [0.2.1 security review](wiki/architecture/SECURITY-REVIEW-2026-11-02.md) records reproduced custody findings, fixes, verification, and operating boundaries. Run `python3 tools/TestCustody.py` for the native localhost checks.
