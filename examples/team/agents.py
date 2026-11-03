"""The writer and the reviewer. Each runs as its own process, holds only the token it was given, and learns about work by pulling deliveries."""

import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fabric
import stage
from settings import DRAFT, FABRIC, LINE_WIDTH, NOTE_WORDS_MAX, RELEASE, SECTION, SOURCE, VERDICT, WAIT_MILLIS, WORK_PAUSE

ROOT = Path(__file__).resolve().parents[2]
PORT, SCOPE, GRAPH = FABRIC["port"], FABRIC["scope"], FABRIC["graph"]


def say(who, text):
    shown = text if len(text) <= LINE_WIDTH else text[:LINE_WIDTH - 1].rstrip() + "…"
    print(f"{who:<11} {shown}", flush=True)


def next_task(participant, token):
    cursor = 0
    while True:
        status, page = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/graphs/{GRAPH}/participants/{participant}/deliveries?after={cursor}&wait={WAIT_MILLIS}", token)
        if status != 200:
            raise RuntimeError(f"{participant} could not pull: {page.get('code')}")
        cursor = page["cursor"]
        for delivered in page["deliveries"]:
            yield delivered["envelope"]


def send(token, body):
    status, answer = fabric.call(PORT, "POST", f"/v1/scopes/{SCOPE}/transfers", token, body)
    if status != 202:
        raise RuntimeError(f"{body['id']} refused: {answer.get('code')}")
    return answer


def writer(token, handed):
    who = "writer"
    say(who, "waiting for work")
    for asked in next_task("writer", token):
        if asked["kind"] != "task":
            continue
        say(who, f"received {asked['id']}: {asked['payload']['brief']}")
        status, answer = stage.delegate(PORT, SCOPE, token, "helper-wide", "helper", GRAPH, ["transfer.receive", "ledger.erase"], 3)
        say(who, f"tries to give a helper ledger.erase: HTTP {status} {answer.get('code')}")
        status, answer = stage.delegate(PORT, SCOPE, token, "helper", "helper", GRAPH, ["transfer.receive"], 3)
        say(who, f"gives the helper transfer.receive only: HTTP {status}")
        Path(handed).write_text(answer["token"])
        Path(handed).chmod(0o600)
        time.sleep(WORK_PAUSE)
        release = (ROOT / SOURCE).read_text().split(RELEASE, 1)[1].split("\n## ", 1)[0]
        added = release.split(SECTION, 1)[1].split("\n### ", 1)[0]
        items = [re.sub(r"`|\*\*", "", line[2:]) for line in added.splitlines() if line.startswith("- ")]
        headline = items[0].split(". ")[0].split(": ", 1)[-1]
        note = f"Grail 0.2.0 brings {headline}, with {len(items) - 1} more additions in the changelog."
        say(who, f"read {SOURCE} and wrote a {len(note.split())}-word release note")
        receipt = send(token, fabric.envelope(SCOPE, GRAPH, DRAFT, "writer", "coordinator", "result", {"note": note}, [asked["id"]]))
        say(who, f"result {DRAFT} accepted at sequence {receipt['sequence']}")
        return


def reviewer(token):
    who = "reviewer"
    say(who, "waiting for work")
    for asked in next_task("reviewer", token):
        if asked["kind"] == "memory":
            say(who, f"received a private note: {asked['payload']['text']}")
            continue
        if asked["kind"] != "task":
            continue
        _, draft = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{asked['parents'][0]}", token)
        words = len(draft["envelope"]["payload"]["note"].split())
        approved = words <= NOTE_WORDS_MAX
        say(who, f"reviewing {asked['parents'][0]}: {words} words, limit {NOTE_WORDS_MAX}")
        time.sleep(WORK_PAUSE)
        receipt = send(token, fabric.envelope(SCOPE, GRAPH, VERDICT, "reviewer", "coordinator", "result", {"approved": approved, "words": words}, [asked["id"]]))
        say(who, f"{'approved' if approved else 'sent back'} as {VERDICT} at sequence {receipt['sequence']}")
        return


if __name__ == "__main__":
    role, *given = sys.argv[1:]
    {"writer": writer, "reviewer": reviewer}[role](*given)
