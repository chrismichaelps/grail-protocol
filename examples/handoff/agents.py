"""The agents of the demonstration. Each runs as its own process, holds only its own token, and learns about work by pulling deliveries."""

import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fabric
from settings import DESK, LINE_WIDTH, HANDOFF_ID, QUESTION, REPLY_ID, RESULT_ID, SECTION, SOURCE, STEP_PAUSE, STUDIO, TASK_ID, WAIT_MILLIS

ROOT = Path(__file__).resolve().parents[2]


def say(who, text):
    print(f"{who:<22} {text}", flush=True)


def deliveries(side, participant, token, after):
    path = f"/v1/scopes/{side['scope']}/graphs/{side['graph']}/participants/{participant}/deliveries?after={after}&wait={WAIT_MILLIS}"
    _, page = fabric.call(side["port"], "GET", path, token)
    return page.get("deliveries", []), page.get("cursor", after)


def send(side, token, body):
    status, answer = fabric.call(side["port"], "POST", f"/v1/scopes/{side['scope']}/transfers", token, body)
    if status != 202:
        raise RuntimeError(f"{body['id']} refused: {answer.get('code')}")
    return answer


def planner(token):
    who = "studio · planner"
    say(who, f"asks the researcher: {QUESTION}")
    task = fabric.envelope(STUDIO["scope"], STUDIO["graph"], TASK_ID, "planner", "researcher", "task", {"question": QUESTION, "source": SOURCE})
    receipt = send(STUDIO, token, task)
    say(who, f"task {TASK_ID} accepted at sequence {receipt['sequence']}, state {receipt['state']}")
    while True:
        _, view = fabric.call(STUDIO["port"], "GET", f"/v1/scopes/{STUDIO['scope']}/transfers/{TASK_ID}", token)
        if view.get("state") == "completed":
            say(who, f"task {TASK_ID} completed")
            return
        time.sleep(STEP_PAUSE / 3)


def researcher(token):
    who = "studio · researcher"
    cursor = 0
    say(who, "waiting for work")
    while True:
        found, cursor = deliveries(STUDIO, "researcher", token, cursor)
        for delivered in found:
            asked = delivered["envelope"]
            if asked["kind"] != "task":
                continue
            say(who, f"received {asked['id']}: reading {asked['payload']['source']}")
            send(STUDIO, token, fabric.envelope(STUDIO["scope"], STUDIO["graph"], "progress-1", "researcher", "planner", "progress", {"reading": SOURCE}, [asked["id"]]))
            time.sleep(STEP_PAUSE)
            text = (ROOT / asked["payload"]["source"]).read_text()
            section = text.split(SECTION, 1)[1].split("\n## ", 1)[0]
            steps = [re.sub(r"\[\[[^|\]]*\|?([^\]]*)\]\]", r"\1", line.split(". ", 1)[1]) for line in section.splitlines() if re.match(r"^\d+\. ", line)]
            say(who, f"found {len(steps)} required checks in section 13.4")
            result = fabric.envelope(STUDIO["scope"], STUDIO["graph"], RESULT_ID, "researcher", "planner", "result", {"question": asked["payload"]["question"], "checks": steps}, [asked["id"]])
            receipt = send(STUDIO, token, result)
            say(who, f"result {RESULT_ID} sealed into the ledger, digest {receipt['digest'][:23]}…")
            return


def assistant(token, root):
    who = "desk · assistant"
    cursor = 0
    say(who, "pulling its deliveries")
    while True:
        found, cursor = deliveries(DESK, "assistant", token, cursor)
        for delivered in found:
            arrived = delivered["envelope"]
            if arrived["kind"] != "handoff.import":
                continue
            origin = arrived["payload"]["origin"]
            say(who, f"an agent arrived from fabric '{origin['fabric']}' ({origin['scope']}/{origin['graph']}/{origin['participant']})")
            _, bundle = fabric.call(DESK["port"], "GET", f"/v1/scopes/{DESK['scope']}/handoffs/{arrived['payload']['handoff']}", root)
            checked = check(bundle)
            say(who, f"checked {checked} entries myself: every digest and link recomputes")
            findings = next(entry["envelope"] for entry in bundle["entries"] if entry["id"] == RESULT_ID)
            for number, step in enumerate(findings["payload"]["checks"], 1):
                say(who, f"  {number}. {shortened(step)}")
            reply = fabric.envelope(DESK["scope"], DESK["graph"], REPLY_ID, "assistant", "lead", "observation", {"summary": f"{len(findings['payload']['checks'])} checks before accepting an agent", "from": origin["fabric"]}, [arrived["id"]])
            receipt = send(DESK, token, reply)
            say(who, f"briefed the lead with {REPLY_ID}, which names {HANDOFF_ID} as its parent (sequence {receipt['sequence']})")
            return


def shortened(text):
    return text if len(text) <= LINE_WIDTH else text[:LINE_WIDTH - 1].rstrip() + "…"


def check(bundle):
    assert fabric.digest(bundle, ("digest", "seal")) == bundle["digest"], "handoff digest"
    for entry in bundle["entries"]:
        if entry.get("envelope") is not None and not entry["erased"]:
            assert fabric.digest(entry["envelope"], ("sequence", "digest", "accepted")) == entry["digest"], entry["id"]
        assert fabric.link(entry["previous"], entry["digest"]) == entry["link"], entry["id"]
    return len(bundle["entries"])


if __name__ == "__main__":
    role, *tokens = sys.argv[1:]
    {"planner": planner, "researcher": researcher, "assistant": assistant}[role](*tokens)
