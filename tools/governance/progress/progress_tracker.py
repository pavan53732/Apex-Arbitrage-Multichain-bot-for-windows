from __future__ import annotations
import json
from pathlib import Path

class ProgressTracker:
    def __init__(self, json_path: Path):
        self.json_path = json_path
        self.data: list[dict] = []
        if self.json_path.exists():
            self.data = json.loads(self.json_path.read_text(encoding="utf-8"))

    def update_programme(self, programme: str, phase: str, completed: bool, last_commit: str | None = None, notes: list[str] | None = None):
        entry = {"programme": programme, "phase": phase, "completed": completed, "last_commit": last_commit, "notes": notes or []}
        self.data = [e for e in self.data if not (e["programme"] == programme and e["phase"] == phase)]
        self.data.append(entry)
        self.json_path.parent.mkdir(parents=True, exist_ok=True)
        self.json_path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")
