"""The executor: a tool participant that receives the key only in its delivery and uses it to call the repository service."""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fabric
from settings import FABRIC, LINE_WIDTH, RESULT_ID, SERVICE_PORT, WAIT_MILLIS

PORT, SCOPE, GRAPH = FABRIC["port"], FABRIC["scope"], FABRIC["graph"]


def say(text):
    shown = text if len(text) <= LINE_WIDTH else text[:LINE_WIDTH - 1].rstrip() + "…"
    print(f"{'executor':<10} {shown}", flush=True)


def executor(token, wanted):
    cursor = 0
    while True:
        status, page = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/graphs/{GRAPH}/participants/executor/deliveries?after={cursor}&wait={WAIT_MILLIS}", token)
        cursor = page["cursor"]
        for delivered in page["deliveries"]:
            asked = delivered["envelope"]
            if asked["id"] != wanted:
                continue
            key = asked["payload"]["auth"]
            if isinstance(key, dict):
                say(f"received {asked['id']}, but the key is no longer in custody: {json.dumps(key)}")
                return
            say(f"received {asked['id']} with a {len(key)}-character key in its delivery")
            request = urllib.request.Request(f"http://127.0.0.1:{SERVICE_PORT}{asked['payload']['path']}", headers={"Authorization": "Bearer " + key})
            try:
                with urllib.request.urlopen(request, timeout=10) as response:
                    releases = json.load(response)["releases"]
                    say(f"GET {asked['payload']['path']} -> HTTP {response.status}, {len(releases)} releases")
            except urllib.error.HTTPError as refused:
                say(f"GET {asked['payload']['path']} -> HTTP {refused.code}")
                return
            answer = fabric.envelope(SCOPE, GRAPH, RESULT_ID + "-" + asked["id"], "executor", "planner", "tool.result", {"releases": releases}, [asked["id"]])
            status, receipt = fabric.call(PORT, "POST", f"/v1/scopes/{SCOPE}/transfers", token, answer)
            say(f"returned the releases, without the key: HTTP {status}")
            return


if __name__ == "__main__":
    executor(*sys.argv[1:])
