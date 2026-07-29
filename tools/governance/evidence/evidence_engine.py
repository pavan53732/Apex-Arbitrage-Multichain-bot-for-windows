"""Evidence Engine — Repository Canonicality Repair, Work Item 5.

Prior to this module, "evidence" in this repository meant file hashing
performed ad hoc by `WS0VerificationLayer.collect_evidence()` (see
`.governance/programme_2.5/ws0/__init__.py`), which recorded only a
repository hash, a canonical-output hash, and a flat list of
{path, hash, type} for graph/freeze files on disk. It did not record
which command produced the evidence, what its inputs were, how long it
took, which validators ran, or the current git commit — all of which the
Repository Canonicality Repair directive (Work Item 5) requires.

This module produces a single, reproducible `EvidenceRecord` per
invocation, with every field the directive specifies:
  - engine            (which canonical engine/command produced this)
  - command           (exact command line executed)
  - inputs            (what was read: docs_globs, config path)
  - outputs           (canonical_output dict from `apex-gov run`)
  - hashes            (sha256 of every generated artefact)
  - execution_time_ms (wall-clock duration of the underlying command)
  - validator_ids     (every validator ID from the Validator Registry,
                       with PASS/FAIL, for this evidence snapshot)
  - commit            (git HEAD at the time of collection)
  - repository_hash   (git tree hash at the time of collection)
  - producer          (this module + the canonical runtime it wraps)
  - consumer          (documented list of what is expected to read this
                       evidence record: WS0 certification, integrity
                       engine, freeze framework)

Reproducibility: calling `collect()` twice against an unchanged repository
must produce byte-identical `hashes` and `outputs` (verified by the
Repository Canonicality Repair's 100-run determinism test, which now
includes evidence collection).

This module does not duplicate `WS0VerificationLayer` — WS0 remains the
verification/certification *consumer* of this evidence, exactly as ADR-0011
specifies. `WS0VerificationLayer.collect_evidence()` should be considered
superseded by this module going forward (WS0 continues to invoke the
canonical runtime and now delegates evidence collection here instead of
performing its own ad hoc hashing).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class EvidenceRecord:
    engine: str
    command: str
    inputs: dict
    outputs: dict
    hashes: dict
    execution_time_ms: float
    validator_ids: list
    validator_results: dict
    commit: str
    repository_hash: str
    producer: str
    consumer: list
    timestamp: str

    def to_dict(self) -> dict:
        return {
            "engine": self.engine,
            "command": self.command,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "hashes": self.hashes,
            "execution_time_ms": self.execution_time_ms,
            "validator_ids": self.validator_ids,
            "validator_results": self.validator_results,
            "commit": self.commit,
            "repository_hash": self.repository_hash,
            "producer": self.producer,
            "consumer": self.consumer,
            "timestamp": self.timestamp,
        }

    def record_hash(self) -> str:
        """Deterministic hash of this evidence record's substantive content
        (excludes timestamp and execution_time_ms, which are expected to
        vary between reproducible runs)."""
        stable = self.to_dict()
        stable.pop("timestamp", None)
        stable.pop("execution_time_ms", None)
        return hashlib.sha256(json.dumps(stable, sort_keys=True).encode()).hexdigest()


class EvidenceEngine:
    """Collects a reproducible EvidenceRecord for one canonical-runtime execution."""

    ARTEFACT_PATHS = [
        ".governance/exports/documents.json",
        ".governance/governance.db",
        ".governance/graphs/config_graph.graphml",
        ".governance/graphs/dependency_graph.graphml",
        ".governance/graphs/document_graph.graphml",
        ".governance/graphs/event_graph.graphml",
        ".governance/graphs/interface_graph.graphml",
        ".governance/graphs/ownership_graph.graphml",
        ".governance/graphs/schema_graph.graphml",
        ".governance/graphs/state_machine_graph.graphml",
    ]

    def __init__(self, repo_root: Path):
        self.repo_root = Path(repo_root).resolve()

    def _sha256_file(self, path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def _git(self, *args: str) -> str:
        return subprocess.run(
            ["git", *args], cwd=self.repo_root, capture_output=True, text=True
        ).stdout.strip()

    def collect(self) -> EvidenceRecord:
        from datetime import datetime, timezone

        start = time.monotonic()
        result = subprocess.run(
            ["apex-gov", "run"], cwd=self.repo_root, capture_output=True, text=True
        )
        duration_ms = (time.monotonic() - start) * 1000.0
        if result.returncode != 0:
            raise RuntimeError(f"`apex-gov run` failed: {result.stderr}")
        outputs = json.loads(result.stdout)

        hashes = {}
        for rel_path in self.ARTEFACT_PATHS:
            p = self.repo_root / rel_path
            if p.exists():
                hashes[rel_path] = self._sha256_file(p)

        # Validator results, from the single canonical Validator Registry
        # (Work Item 7) — no duplicate validator invocation logic here.
        try:
            from ..validator.registry import list_validators, run_all_validators
        except ImportError:
            from governance.validator.registry import list_validators, run_all_validators  # type: ignore
        validator_ids = [v.id for v in list_validators()]
        validator_run_results = run_all_validators(self.repo_root)
        validator_results = {r["id"]: r["status"] for r in validator_run_results}

        record = EvidenceRecord(
            engine="tools.governance.cli.main:run",
            command="apex-gov run",
            inputs={
                "config_path": "tools/governance/config/governance.yaml",
                "docs_globs": ["docs/*.md", "docs/adr/*.md", "*.md"],
            },
            outputs=outputs,
            hashes=hashes,
            execution_time_ms=round(duration_ms, 3),
            validator_ids=validator_ids,
            validator_results=validator_results,
            commit=self._git("rev-parse", "HEAD"),
            repository_hash=self._git("rev-parse", "HEAD^{tree}"),
            producer="tools.governance.evidence.evidence_engine.EvidenceEngine",
            consumer=[
                ".governance/programme_2.5/ws0/__init__.py (WS0VerificationLayer certification)",
                "tools.governance.integrity.integrity_engine.IntegrityEngine (check_evidence)",
                ".governance/freeze/freeze_WS0.json (Freeze Framework)",
            ],
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        return record

    def collect_and_save(self, output_path: Path) -> EvidenceRecord:
        record = self.collect()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(record.to_dict(), indent=2), encoding="utf-8")
        return record
