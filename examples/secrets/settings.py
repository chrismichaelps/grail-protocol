"""Names, ports, and timings of the custody demonstration."""

FABRIC = {"name": "workbench", "port": 7450, "scope": "acme", "graph": "ops"}
SERVICE_HOST = "127.0.0.1"
SERVICE_PORT = 7451

GRAPH = {
    "participants": [
        {"id": "planner", "kind": "agent", "roles": ["planning"]},
        {"id": "executor", "kind": "tool", "abilities": ["http"]},
        {"id": "reviewer", "kind": "agent"},
    ],
    "edges": [
        {"id": "call", "from": "planner", "to": "executor", "relation": "flow"},
        {"id": "share", "from": "planner", "to": "reviewer", "relation": "flow"},
    ],
}

SECRET = "repo-token"
DESCRIPTION = "read access to the release repository"
KEY_BYTES = 24
CALL_ID = "list-releases"
SECOND_CALL = "list-releases-again"
PENDING_CALL = "list-after-delete"
RESULT_ID = "releases"
WAIT_MILLIS = 2000
LINE_WIDTH = 92
