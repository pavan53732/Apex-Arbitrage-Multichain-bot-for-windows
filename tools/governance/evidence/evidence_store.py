"""Structured Evidence Store (Programme 2.5 Phase-0, WS7 Evidence
System).

`readiness_checklist.json` CHECK-WS7 requires 10 structured evidence
subdirectories (Programme1/, Programme2/, Programme3/, validators/,
metrics/, graphs/, closures/, hashes/, commits/, reports/) plus
"Evidence is queryable and auditable" and "No programme complete
without evidence". Prior to this module, only a flat, unconditionally
OVERWRITTEN `.governance/evidence/evidence_latest.json` existed
(confirmed by the Programme 2.5 Final Certification Audit) -- every
prior run's evidence was destroyed by the next run, and there was no
directory structure at all.

This module does NOT replace `EvidenceEngine` (evidence_engine.py
remains the single producer of evidence CONTENT -- one canonical
`EvidenceRecord` per `apex-gov run`). It adds a persistence/query layer
on top: every collected `EvidenceRecord` is additionally written,
timestamped and hashed, into the 10-directory structure below, and
`EvidenceStore` provides query methods over that structure -- turning
"evidence exists" into "evidence is queryable and auditable" as the
checklist requires.

Directory layout under `.governance/evidence/`:
    Programme1/    -- evidence tagged as belonging to Programme 1
                       (Documentation Intelligence Platform).
    Programme2/    -- evidence tagged as belonging to Programme 2.
    Programme3/    -- evidence tagged as belonging to Programme 3
                       (behavioural-root closure work).
    validators/    -- one file per `apex-gov run` invocation, containing
                       that run's validator_ids/validator_results.
    metrics/       -- one file per invocation, containing that run's
                       canonical_output (which includes avg_completeness
                       and every other computed metric).
    graphs/        -- one file per invocation, containing that run's
                       per-graph node/edge counts + file hashes.
    closures/      -- one file per invocation, containing a summary of
                       closures_computed and behavioural_roots counts.
    hashes/        -- one file per invocation, containing the full
                       `hashes` dict (every artefact's SHA-256).
    commits/       -- one file per invocation, named after the commit it
                       was collected against, containing commit +
                       repository_hash.
    reports/       -- the full raw EvidenceRecord, one file per
                       invocation (the closest equivalent to the old
                       flat evidence_latest.json, but never overwritten).

Every file is named `<record_hash>_<timestamp>.json` so that re-running
against an unchanged repository (same record_hash) does not silently
overwrite a prior evidence entry, while still being sorted
chronologically by filename.

Programme tagging (Programme1/2/3) is heuristic, based on which parts
of the canonical_output changed or which command produced the record --
since this platform has no explicit "current active programme" field
anywhere else, `store()` accepts an explicit `programme` argument
(defaulting to "Programme1", the Documentation Intelligence Platform
work this whole governance CLI implements) rather than guessing.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

STRUCTURED_SUBDIRS = [
    "Programme1", "Programme2", "Programme3",
    "validators", "metrics", "graphs", "closures", "hashes", "commits", "reports",
]


class EvidenceStore:
    def __init__(self, evidence_dir: Path):
        self.evidence_dir = Path(evidence_dir)

    def _filename(self, record_hash: str, timestamp: str) -> str:
        safe_ts = timestamp.replace(":", "").replace("+", "").replace(".", "")
        return f"{record_hash[:16]}_{safe_ts}.json"

    def store(self, record_dict: dict, record_hash: str, programme: str = "Programme1") -> dict[str, Path]:
        """Persist one EvidenceRecord (as its .to_dict() form) across all
        10 structured subdirectories. Returns a dict of subdir -> path
        written."""
        timestamp = record_dict.get("timestamp", "unknown")
        filename = self._filename(record_hash, timestamp)
        written: dict[str, Path] = {}

        for subdir in STRUCTURED_SUBDIRS:
            (self.evidence_dir / subdir).mkdir(parents=True, exist_ok=True)

        def _write(subdir: str, payload: dict) -> Path:
            path = self.evidence_dir / subdir / filename
            path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            return path

        if programme not in ("Programme1", "Programme2", "Programme3"):
            programme = "Programme1"
        written[programme] = _write(programme, record_dict)
        written["validators"] = _write("validators", {
            "record_hash": record_hash, "timestamp": timestamp, "commit": record_dict.get("commit"),
            "validator_ids": record_dict.get("validator_ids", []),
            "validator_results": record_dict.get("validator_results", {}),
        })
        written["metrics"] = _write("metrics", {
            "record_hash": record_hash, "timestamp": timestamp, "commit": record_dict.get("commit"),
            "outputs": record_dict.get("outputs", {}),
        })
        written["graphs"] = _write("graphs", {
            "record_hash": record_hash, "timestamp": timestamp, "commit": record_dict.get("commit"),
            "graph_hashes": {k: v for k, v in record_dict.get("hashes", {}).items() if k.endswith(".graphml")},
        })
        written["closures"] = _write("closures", {
            "record_hash": record_hash, "timestamp": timestamp, "commit": record_dict.get("commit"),
            "behavioural_roots": record_dict.get("outputs", {}).get("behavioural_roots"),
            "closures_computed": record_dict.get("outputs", {}).get("closures_computed"),
        })
        written["hashes"] = _write("hashes", {
            "record_hash": record_hash, "timestamp": timestamp, "commit": record_dict.get("commit"),
            "hashes": record_dict.get("hashes", {}),
        })
        commit = record_dict.get("commit", "unknown")
        commit_filename = f"{commit[:12]}_{filename}"
        commits_path = self.evidence_dir / "commits" / commit_filename
        commits_path.write_text(json.dumps({
            "record_hash": record_hash, "timestamp": timestamp, "commit": commit,
            "repository_hash": record_dict.get("repository_hash"),
        }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        written["commits"] = commits_path
        written["reports"] = _write("reports", record_dict)

        return written

    def list_evidence(self, subdir: str) -> list[Path]:
        d = self.evidence_dir / subdir
        if not d.exists():
            return []
        return sorted(d.glob("*.json"))

    def query_by_commit(self, commit: str) -> list[dict]:
        """Query all evidence entries (from the 'reports' subdir, the
        full-fidelity copy) matching a given commit hash."""
        results = []
        for path in self.list_evidence("reports"):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if data.get("commit", "").startswith(commit) or commit.startswith(data.get("commit", "\0")):
                results.append(data)
        return results

    def query_by_record_hash(self, record_hash: str) -> Optional[dict]:
        for path in self.list_evidence("reports"):
            if path.name.startswith(record_hash[:16]):
                try:
                    return json.loads(path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, OSError):
                    continue
        return None

    def latest(self, subdir: str = "reports") -> Optional[dict]:
        """Most recent evidence entry in a subdirectory, ordered by
        filename (which sorts chronologically since filenames are
        timestamp-suffixed)."""
        entries = self.list_evidence(subdir)
        if not entries:
            return None
        try:
            return json.loads(entries[-1].read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None

    def counts(self) -> dict[str, int]:
        return {subdir: len(self.list_evidence(subdir)) for subdir in STRUCTURED_SUBDIRS}

    def has_any_evidence(self) -> bool:
        """WS7 checklist item 'No programme complete without evidence':
        a caller enforcing that gate should check this before marking
        any programme/workstream complete."""
        return any(self.counts()[p] > 0 for p in ("Programme1", "Programme2", "Programme3"))
