"""Names, ports, and timings of the team demonstration."""

FABRIC = {"name": "workshop", "port": 7440, "scope": "acme", "graph": "release"}

GRAPH = {
    "participants": [
        {"id": "coordinator", "kind": "agent", "roles": ["lead"]},
        {"id": "writer", "kind": "agent", "roles": ["author"]},
        {"id": "reviewer", "kind": "agent", "roles": ["review"]},
    ],
    "edges": [
        {"id": "assign", "from": "coordinator", "to": "writer", "relation": "flow"},
        {"id": "ask-review", "from": "coordinator", "to": "reviewer", "relation": "flow"},
        {"id": "review-needs-draft", "from": "writer", "to": "reviewer", "relation": "dependency"},
    ],
}

SOURCE = "CHANGELOG.md"
RELEASE = "## 0.2.0"
SECTION = "### Added"
NOTE_WORDS_MAX = 120

EARLY_REVIEW = "review-early"
DRAFT_TASK = "draft-task"
DRAFT = "draft-1"
REVIEW_TASK = "review-task"
VERDICT = "verdict-1"
PRIVATE_NOTE = "note-for-reviewer"

WAIT_MILLIS = 2000
WORK_PAUSE = 0.6
LINE_WIDTH = 78
