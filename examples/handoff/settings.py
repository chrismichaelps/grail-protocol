"""Names, ports, and timings of the two-fabric handoff demonstration."""

STUDIO = {"name": "studio", "port": 7430, "scope": "research", "graph": "papers"}
DESK = {"name": "desk", "port": 7431, "scope": "support", "graph": "inbox"}

STUDIO_GRAPH = {
    "participants": [{"id": "planner", "kind": "agent"}, {"id": "researcher", "kind": "agent", "roles": ["analyst"]}],
    "edges": [{"id": "ask", "from": "planner", "to": "researcher", "relation": "flow"}],
}
DESK_GRAPH = {
    "participants": [{"id": "assistant", "kind": "agent", "roles": ["support"]}, {"id": "lead", "kind": "human"}],
    "edges": [{"id": "report", "from": "assistant", "to": "lead", "relation": "flow"}],
}

SOURCE = "wiki/protocol/13-Portability.md"
SECTION = "## 13.4 Import"
QUESTION = "What must a fabric check before it accepts an agent from elsewhere?"

TASK_ID = "research-1"
RESULT_ID = "findings-1"
HANDOFF_ID = "move-1"
REPLY_ID = "brief-1"

WAIT_MILLIS = 2000
STEP_PAUSE = 0.6
TIMEOUT_SECONDS = 30
LINE_WIDTH = 74
