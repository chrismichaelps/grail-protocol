"""A team inside one fabric: a coordinator, a writer, and a reviewer.

The graph says the review depends on the draft, so a review asked for too early is refused. Each agent holds a token
the coordinator narrowed for it, and cannot hand out more than it holds. A note sent only to the reviewer stays out of
the writer's sight. When the work is done, the writer's token is revoked, and every token it issued falls with it.
"""

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fabric
import stage
from settings import DRAFT, DRAFT_TASK, EARLY_REVIEW, FABRIC, GRAPH, PRIVATE_NOTE, REVIEW_TASK, VERDICT

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PORT, SCOPE, NAME = FABRIC["port"], FABRIC["scope"], FABRIC["graph"]
TIMEOUT_SECONDS = 30


def agent(role, *given):
    return subprocess.Popen([sys.executable, str(HERE / "agents.py"), role, *given], cwd=HERE)


def sent(token, body):
    return fabric.call(PORT, "POST", f"/v1/scopes/{SCOPE}/transfers", token, body)


def token(issuer, audience, abilities, depth):
    return stage.delegate(PORT, SCOPE, issuer, audience, audience, NAME, abilities, depth)[1]["token"]


def main():
    with tempfile.TemporaryDirectory(prefix="grail-team-") as directory:
        work = Path(directory)
        executable = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else work / "grail"
        if len(sys.argv) == 1:
            subprocess.run(["pudu", "build", "src/Main.pudu", "-o", str(executable)], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
        server, owner = stage.start(executable, FABRIC["name"], PORT, SCOPE, work)
        try:
            stage.heading("One graph says who works with whom, and in what order")
            status, created = fabric.call(PORT, "PUT", f"/v1/scopes/{SCOPE}/graphs/{NAME}", owner, GRAPH)
            stage.note(f"graph {SCOPE}/{NAME} revision {created['revision']}  HTTP {status}")
            for edge in created["edges"]:
                stage.note(f"  {edge['from']:<11} → {edge['to']:<9} {edge['relation']}")
            coordinator = token(owner, "coordinator", ["transfer.send", "transfer.receive", "transfer.read", "token.delegate", "ledger.read"], 1)
            writer = token(coordinator, "writer", ["transfer.send", "transfer.receive", "transfer.read", "token.delegate"], 2)
            reviewer = token(coordinator, "reviewer", ["transfer.send", "transfer.receive", "transfer.read"], 2)
            for held in (coordinator, writer, reviewer):
                _, seen = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/tokens/self", held)
                stage.note(f"token for {seen['audience']:<11} depth {seen['depth']}  {', '.join(seen['abilities'])}")

            stage.heading("A review asked for before the draft exists is refused")
            status, answer = sent(coordinator, fabric.envelope(SCOPE, NAME, EARLY_REVIEW, "coordinator", "reviewer", "task", {"brief": "Review the release note"}))
            stage.refused(f"{EARLY_REVIEW:<18} HTTP {status}  {answer['code']}: waiting on {', '.join(answer.get('unmet', []))}")

            stage.heading("The writer drafts, and cannot hand out more than it holds")
            handed = work / "helper.token"
            workers = [agent("writer", writer, str(handed)), agent("reviewer", reviewer)]
            status, answer = sent(coordinator, {**fabric.envelope(SCOPE, NAME, DRAFT_TASK, "coordinator", "writer", "task", {"brief": "Write the 0.2.0 release note"}), "target": {"role": "author"}})
            stage.note(f"{DRAFT_TASK:<18} HTTP {status}  routed by role to {', '.join(address['participant'] for address in answer['recipients'])}")
            workers[0].wait(TIMEOUT_SECONDS)

            stage.heading("A note meant only for the reviewer")
            status, _ = sent(coordinator, fabric.envelope(SCOPE, NAME, PRIVATE_NOTE, "coordinator", "reviewer", "memory", {"text": "keep it under 120 words"}, visibility="recipients"))
            stage.note(f"{PRIVATE_NOTE:<18} HTTP {status}  visibility recipients")
            status, _ = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{PRIVATE_NOTE}", reviewer)
            stage.note(f"reviewer reads it      HTTP {status}")
            status, answer = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{PRIVATE_NOTE}", writer)
            stage.refused(f"writer reads it        HTTP {status}  {answer['code']}")

            stage.heading("With the draft among its causes, the review goes through")
            status, answer = sent(coordinator, fabric.envelope(SCOPE, NAME, REVIEW_TASK, "coordinator", "reviewer", "task", {"brief": "Review the release note"}, [DRAFT]))
            stage.note(f"{REVIEW_TASK:<18} HTTP {status}  state {answer['state']}")
            workers[1].wait(TIMEOUT_SECONDS)
            _, verdict = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{REVIEW_TASK}", coordinator)
            _, draft = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{DRAFT}", coordinator)
            stage.note(f"{REVIEW_TASK:<18} {verdict['state']}")
            stage.note(f"release note: {draft['envelope']['payload']['note']}")

            stage.heading("The writer is done, so its authority goes")
            status, _ = fabric.call(PORT, "POST", f"/v1/scopes/{SCOPE}/tokens/writer/revocation", coordinator)
            stage.note(f"revoke writer           HTTP {status}")
            status, answer = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/tokens/self", writer)
            stage.refused(f"writer's token          HTTP {status}  {answer['code']}")
            status, answer = stage.delegate(PORT, SCOPE, writer, "late", "helper", NAME, ["transfer.receive"], 3)
            stage.refused(f"writer delegates        HTTP {status}  {answer['code']}")
            status, answer = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/tokens/self", handed.read_text())
            stage.refused(f"helper's token          HTTP {status}  {answer['code']}, it fell with its issuer")

            stage.heading("How the verdict was produced")
            _, trace = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{VERDICT}/trace", coordinator)
            for entry in trace["entries"]:
                stage.note(f"  {entry['sequence']:>2}  {entry['id']:<14} {entry['envelope']['kind']:<7} from {entry['envelope']['source']}")
            _, ledger = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/ledger", coordinator)
            previous = ""
            for entry in ledger["entries"]:
                material = "grail-ledger:" + entry["digest"] if not previous else previous + ":" + entry["digest"]
                assert hashlib.sha256(material.encode()).hexdigest() == entry["link"], entry["id"]
                previous = entry["link"]
            stage.note(f"all {len(ledger['entries'])} ledger links recomputed here, head {previous[:16]}…")
            stage.finished()
        finally:
            server.terminate()
            server.wait(TIMEOUT_SECONDS)


if __name__ == "__main__":
    main()
