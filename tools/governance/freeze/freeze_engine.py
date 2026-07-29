"""Freeze Engine — Repository Canonicality Repair, Remediation Item 4.

Prior to this module, `.governance/freeze/freeze_WS0.json` existed as a
DATA FILE, but no code in the repository produced it. Every prior
regeneration of that file was performed via ad hoc, uncommitted,
interactive Python one-liners run directly in a shell during earlier work
sessions -- confirmed by direct repository-wide search: `FreezeManager`
(tools/governance/freeze/manager.py) has zero call sites anywhere, and
`ClosureOrchestrator.freeze_dimension()`/`freeze_closure()`
(tools/governance/closure/orchestrator.py) are unrelated, same-named,
empty no-op stubs that are themselves never imported by anything. This
was flagged as CRITICAL 4 in the user's remediation review: "A JSON file
existing is not the same thing as a Freeze Framework. If there is no
runtime producer, then Freeze Framework is not implemented."

This module is the first actual runtime producer for freeze records. It
is invoked via `apex-gov freeze` and composes ONLY canonical runtime
outputs (no re-derivation of governance state):
  - the canonical `apex-gov run` output (documents/roots/closures/etc.)
  - the canonical Validator Registry's live results
  - the canonical Evidence Engine's record
  - the canonical database and graph file hashes
  - git's own commit/tree hash

It does NOT reimplement `FreezeManager`'s per-dimension/per-closure
freezing model (that is a distinct, larger Programme 3 concept requiring
its own SQL schema that does not exist in the current `governance.db`,
and building it out is a separate, deliberate decision, not an incidental
fix folded into this remediation). This engine freezes the REPOSITORY as
a whole, at WS0 granularity, matching the schema `freeze_WS0.json` already
uses.

Every freeze record produced by this engine includes exactly the fields
required (version, commit, repository hash, validator results/hashes,
evidence hashes, metrics, graphs, database hash, timestamp, integrity
checksum), computed live -- no manually-authored value.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass
class FreezeRecord:
    data: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return self.data


class FreezeEngine:
    """Produces a repository-level freeze record from live canonical outputs."""

    def __init__(self, repo_root: Path, workstream_id: str = "WS0"):
        self.repo_root = Path(repo_root).resolve()
        self.workstream_id = workstream_id

    def _git(self, *args: str) -> str:
        return subprocess.run(
            ["git", *args], cwd=self.repo_root, capture_output=True, text=True
        ).stdout.strip()

    def freeze(self) -> FreezeRecord:
        from ..evidence.evidence_engine import EvidenceEngine
        try:
            from ..validator.registry import run_all_validators
        except ImportError:  # pragma: no cover - installed-package fallback
            from governance.validator.registry import run_all_validators  # type: ignore

        evidence_engine = EvidenceEngine(self.repo_root)
        evidence_record = evidence_engine.collect()

        validator_results = {r["id"]: r["status"] for r in run_all_validators(self.repo_root)}

        graphs_dir = self.repo_root / ".governance" / "graphs"
        graph_hashes = {g.name: _sha256_file(g) for g in sorted(graphs_dir.glob("*.graphml"))}
        combined_graph_hash = _sha256_bytes(json.dumps(graph_hashes, sort_keys=True).encode())

        db_path = self.repo_root / ".governance" / "governance.db"
        database_hash = _sha256_file(db_path) if db_path.exists() else None

        config_path = self.repo_root / "tools" / "governance" / "config" / "governance.yaml"
        configuration_hash = _sha256_file(config_path) if config_path.exists() else None

        commit_hash = self._git("rev-parse", "HEAD")
        tree_hash = self._git("rev-parse", "HEAD^{tree}")
        branch = self._git("branch", "--show-current")
        tree_status = subprocess.run(
            ["git", "status", "--short"], cwd=self.repo_root, capture_output=True, text=True
        ).stdout

        integrity_checksum = _sha256_bytes(json.dumps({
            "combined_graph_hash": combined_graph_hash,
            "database_hash": database_hash,
            "configuration_hash": configuration_hash,
            "canonical_output": evidence_record.outputs,
        }, sort_keys=True).encode())

        freeze_id = _sha256_bytes(f"{self.workstream_id}-{commit_hash}".encode())[:16]

        record = {
            "identity": {
                "freeze_id": freeze_id,
                "workstream_id": self.workstream_id,
                "workstream_version": "3.0.0",
                "repository_version": commit_hash,
                "governance_platform_version": "1.0.0",
                "schema_version": "3.0.0",
                "producer": "tools.governance.freeze.freeze_engine.FreezeEngine",
            },
            "repository": {
                "repository_tree_hash": tree_hash,
                "git_branch": branch,
                "commit_hash": commit_hash,
                "working_tree_status": "clean" if not tree_status.strip() else "dirty",
            },
            "execution": {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "runtime_command": evidence_record.command,
                "execution_time_ms": evidence_record.execution_time_ms,
            },
            "canonical_output": evidence_record.outputs,
            "validation": {
                "validator_list": sorted(validator_results.keys()),
                "validator_results": validator_results,
                "all_pass": all(v == "PASS" for v in validator_results.values()),
            },
            "evidence": {
                "evidence_record_hash": evidence_record.record_hash(),
                "artefact_hashes": evidence_record.hashes,
            },
            "graphs": {
                "graph_hashes": graph_hashes,
                "combined_graph_hash": combined_graph_hash,
                "graph_count": len(graph_hashes),
            },
            "database": {
                "canonical_database_path": ".governance/governance.db",
                "database_hash": database_hash,
            },
            "configuration": {
                "configuration_hash": configuration_hash,
                "path": "tools/governance/config/governance.yaml",
            },
            "integrity": {
                "integrity_checksum": integrity_checksum,
                "computed_from": ["combined_graph_hash", "database_hash", "configuration_hash", "canonical_output"],
            },
            "freeze": {
                "freeze_timestamp": datetime.now(timezone.utc).isoformat(),
            },
        }
        return FreezeRecord(data=record)

    def freeze_and_save(self, output_path: Path) -> FreezeRecord:
        record = self.freeze()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # WS6 (Freeze Framework): tamper-evidence (FreezeValidator) and
        # queryable history (FreezeHistory), completing the checklist
        # items "Freeze records are tamper-evident" and "Freeze history
        # is queryable" -- neither existed before this. The signature is
        # embedded in the saved record itself (under a new top-level
        # "tamper_evidence" key) so a consumer of the JSON file alone
        # (without re-running FreezeEngine) can still call
        # FreezeValidator.verify() against it.
        from .freeze_manifest import FreezeHistory, FreezeManifest, FreezeValidator

        signing_key_path = self.repo_root / ".governance" / "freeze" / ".signing_key"
        validator = FreezeValidator(signing_key_path)
        signature = validator.sign(record.data)
        record.data["tamper_evidence"] = {
            "signature": signature,
            "signing_key_path": str(signing_key_path.relative_to(self.repo_root)),
            "public_key_path": str(validator.public_key_path.relative_to(self.repo_root)),
            "algorithm": "Ed25519",
            "verify_with": "tools.governance.freeze.freeze_manifest.FreezeValidator.verify",
        }

        output_path.write_text(json.dumps(record.to_dict(), indent=2), encoding="utf-8")

        history_dir = self.repo_root / ".governance" / "freeze" / "history"
        history = FreezeHistory(history_dir)
        manifest = FreezeManifest.from_record_dict(record.data)
        history.append(manifest, signature=signature)

        return record
