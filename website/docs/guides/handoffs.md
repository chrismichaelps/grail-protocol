---
uid: guides.handoffs
description: Move an agent's working context from one fabric to another, with its history intact and its origin attested.
---

# Move an agent between fabrics

A handoff lets work started in one product continue in another. The agent's results and everything they depend on travel as one document. The receiving fabric checks every digest and link itself, and asks the origin whether it sealed the document. Neither side has to trust the other's database, and neither fabric ever calls the other.

## See it first

```bash
python3 examples/handoff/demo.py
```

The demonstration builds the fabric, starts two copies with different secrets (`studio` on port 7430 and `desk` on 7431), and runs three agent processes. In the studio, a planner asks a researcher a question; the researcher reads chapter 13 of the specification and returns its findings. The researcher's context then moves to the desk, where an assistant checks the handoff independently, summarizes the findings, and briefs a person. Last, a forged handoff is refused.

## Prepare both sides

The origin needs a participant with `handoff.export` for its graph. The destination owner places the arriving participant in a graph first; import never creates participants or grants abilities. Give each fabric its own name so receivers can tell where work came from:

```text
GRAIL_FABRIC_NAME=studio   # on the origin
GRAIL_FABRIC_NAME=desk     # on the destination
```

## Carry the handoff

`grail handoff` runs the three steps and stops if the origin does not attest the document:

```text
grail handoff \
  --from http://127.0.0.1:7430 --from-token "$RESEARCHER_TOKEN" \
  --scope research --graph papers --participant researcher \
  --to http://127.0.0.1:7431 --to-token "$DESK_OWNER_TOKEN" \
  --to-scope support --to-graph inbox --to-participant assistant \
  --id move-1 --transfers findings-1
```

It prints one line per step: the sealed handoff from `exportHandoff`, the origin's answer from `verifyHandoff`, and the receipt from `importHandoff`. The same calls are available over HTTP if you would rather carry the document yourself.

## Continue the work

The arriving participant receives a `handoff.import` delivery. It reads the carried entries with `GET /v1/scopes/{scope}/handoffs/{handoff}` and names the import entry as a parent of whatever it sends next. A trace in the destination then leads to the import entry, the stored handoff holds the origin's entries, and the origin's ledger holds a matching `handoff.export` entry.

## What the receiver can rely on

- Every carried envelope hashes to its digest, every link follows from the one before it, the ancestry is closed, and the anchors are present. Anything else is refused with `grail.integrity`.
- Entries the exporter could not read travel withheld, and erased payloads stay erased.
- Only the origin can attest a seal, and only for the scope it was made for.
- The same handoff imported twice returns the first receipt. A handoff expires at most a day after it is sealed.

The [portability chapter](../protocol/13-Portability.md) is the normative text.
