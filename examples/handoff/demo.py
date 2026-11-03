"""Two fabrics, standing for two products, pass a working agent from one to the other.

The studio runs a planner and a researcher. The researcher answers a question by reading the specification, then its context is exported, attested by the studio, and imported into the desk, where an assistant picks it up, checks it independently, and briefs a person.
"""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fabric
import stage
from settings import DESK, DESK_GRAPH, HANDOFF_ID, REPLY_ID, RESULT_ID, STUDIO, STUDIO_GRAPH, TIMEOUT_SECONDS

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def delegate(side, owner, audience, abilities):
    return stage.delegate(side["port"], side["scope"], owner, audience, audience, side["graph"], abilities)[1]["token"]


def agent(role, *tokens):
    return subprocess.Popen([sys.executable, str(HERE / "agents.py"), role, *tokens], cwd=HERE)


def main():
    with tempfile.TemporaryDirectory(prefix="grail-demo-") as directory:
        work = Path(directory)
        executable = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else work / "grail"
        if len(sys.argv) == 1:
            subprocess.run(["pudu", "build", "src/Main.pudu", "-o", str(executable)], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
        stage.heading("Two fabrics, two products, no shared secret")
        studio, studio_owner = stage.start(executable, STUDIO["name"], STUDIO["port"], STUDIO["scope"], work)
        desk, desk_owner = stage.start(executable, DESK["name"], DESK["port"], DESK["scope"], work)
        try:
            for side, graph, owner in ((STUDIO, STUDIO_GRAPH, studio_owner), (DESK, DESK_GRAPH, desk_owner)):
                status, created = fabric.call(side["port"], "PUT", f"/v1/scopes/{side['scope']}/graphs/{side['graph']}", owner, graph)
                members = ", ".join(member["id"] for member in created["participants"])
                stage.note(f"{side['name']:<7} :{side['port']}  graph {side['scope']}/{side['graph']} ({members})  HTTP {status}")
            planner_token = delegate(STUDIO, studio_owner, "planner", ["transfer.send", "transfer.read"])
            researcher_token = delegate(STUDIO, studio_owner, "researcher", ["transfer.send", "transfer.receive", "handoff.export"])
            assistant_token = delegate(DESK, desk_owner, "assistant", ["transfer.send", "transfer.receive"])
            stage.note("each agent holds a token for its own graph and nothing more")

            stage.heading("In the studio, a planner asks and a researcher works")
            researcher = agent("researcher", researcher_token)
            agent("planner", planner_token).wait(TIMEOUT_SECONDS)
            researcher.wait(TIMEOUT_SECONDS)

            stage.heading("The researcher's context moves to the desk")
            carried = subprocess.run([
                str(executable), "handoff",
                "--from", fabric.base(STUDIO["port"]), "--from-token", researcher_token,
                "--scope", STUDIO["scope"], "--graph", STUDIO["graph"], "--participant", "researcher",
                "--to", fabric.base(DESK["port"]), "--to-token", desk_owner,
                "--to-scope", DESK["scope"], "--to-graph", DESK["graph"], "--to-participant", "assistant",
                "--id", HANDOFF_ID, "--transfers", RESULT_ID,
            ], cwd=work, capture_output=True, text=True, check=True)
            steps = [json.loads(line) for line in carried.stdout.splitlines()]
            exported, verified, imported = (step["answer"] for step in steps)
            stage.note(f"export   HTTP {steps[0]['status']}  {len(exported['entries'])} entries, digest {exported['digest'][:23]}…, sealed by '{exported['origin']['fabric']}'")
            stage.note(f"verify   HTTP {steps[1]['status']}  intact {verified['intact']}, attested by origin {verified['attested']}")
            stage.note(f"import   HTTP {steps[2]['status']}  recorded at desk sequence {imported['sequence']}, duplicate {imported['duplicate']}")

            stage.heading("At the desk, the assistant comes online and finds the work waiting")
            agent("assistant", assistant_token, desk_owner).wait(TIMEOUT_SECONDS)

            stage.heading("One trace across both fabrics")
            _, trace = fabric.call(DESK["port"], "GET", f"/v1/scopes/{DESK['scope']}/transfers/{REPLY_ID}/trace", desk_owner)
            for entry in trace["entries"]:
                payload = entry["envelope"]["payload"]
                stage.note(f"desk     {entry['id']:<12} {entry['envelope']['kind']:<15} from {payload['origin']['fabric']}, handoff digest {payload['digest'][:23]}…")
            _, held = fabric.call(DESK["port"], "GET", f"/v1/scopes/{DESK['scope']}/handoffs/{HANDOFF_ID}", desk_owner)
            for entry in held["entries"]:
                shown = entry.get("envelope") or {}
                stage.note(f"studio   {entry['id']:<12} {shown.get('kind', 'withheld'):<15} sequence {entry['sequence']}, link {entry['link'][:16]}…")
            _, departure = fabric.call(STUDIO["port"], "GET", f"/v1/scopes/{STUDIO['scope']}/transfers/{HANDOFF_ID}", studio_owner)
            stage.note(f"studio   {HANDOFF_ID:<12} {departure['envelope']['kind']:<15} the origin's own record that the agent left")

            stage.heading("A forged handoff does not get in")
            forged = copy.deepcopy(exported)
            forged["handoff"] = "move-2"
            for entry in forged["entries"]:
                if entry["id"] == RESULT_ID:
                    entry["envelope"]["payload"]["checks"][0] = "skip every check"
            forged["digest"] = fabric.digest(forged, ("digest", "seal"))
            status, refused = fabric.call(DESK["port"], "PUT", f"/v1/scopes/{DESK['scope']}/graphs/{DESK['graph']}/participants/assistant/handoffs/move-2", desk_owner, forged)
            stage.refused(f"import   HTTP {status}  {refused['code']}: {refused['detail']}")
            status, checked = fabric.call(STUDIO["port"], "POST", f"/v1/scopes/{STUDIO['scope']}/handoffs/move-2/verification", "", forged)
            stage.refused(f"verify   HTTP {status}  intact {checked['intact']}, attested by origin {checked['attested']}")
            stage.finished()
        finally:
            for server in (studio, desk):
                server.terminate()
                server.wait(TIMEOUT_SECONDS)


if __name__ == "__main__":
    main()
