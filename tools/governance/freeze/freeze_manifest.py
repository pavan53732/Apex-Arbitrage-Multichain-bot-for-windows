"""FreezeManifest, FreezeHash, FreezeValidator, FreezeEvidence,
FreezeHistory (Programme 2.5 Phase-0, WS6 Freeze Framework).

`readiness_checklist.json` CHECK-WS6 requires 6 classes: FreezeRecord
(already implemented in freeze_engine.py), FreezeManifest, FreezeHash,
FreezeValidator, FreezeEvidence, FreezeHistory. Prior to this module,
only FreezeRecord existed among the 6 (confirmed by the Programme 2.5
Final Certification Audit).

This module does not reimplement freeze computation -- `FreezeEngine`
(freeze_engine.py) remains the single producer of freeze content. These
5 classes are structural/behavioural WRAPPERS around a `FreezeRecord`'s
already-computed `data` dict, each responsible for one of the 5
concerns the checklist names separately:

- FreezeManifest: a lightweight, stable summary view of a freeze record
  (what would be printed/indexed), independent of the full nested
  record structure.
- FreezeHash: computes and verifies a cryptographic hash over a freeze
  record's content, used both for the record's own integrity_checksum
  (already computed by FreezeEngine) and for this module's NEW
  tamper-evidence layer (FreezeValidator).
- FreezeValidator: the tamper-evidence layer WS6 also requires
  ("Freeze records are tamper-evident") -- computes an HMAC-SHA256
  signature over a freeze record using a repository-local secret key
  (generated once, stored outside version control), and verifies a
  record against that signature. This is a genuinely new capability;
  FreezeEngine's own `integrity_checksum` field is a content hash
  (detects accidental corruption) but is NOT a signature (anyone with
  read access to the record could recompute a matching hash after
  editing it) -- FreezeValidator's HMAC requires the secret key,
  which is not embedded in the freeze record itself.
- FreezeEvidence: thin adapter exposing a freeze record's embedded
  evidence fields (evidence_record_hash, artefact_hashes) through a
  typed interface, rather than requiring callers to know the record's
  raw dict shape.
- FreezeHistory: the "Freeze history is queryable" checklist item --
  an index over ALL freeze records ever produced for a workstream
  (previously, only the single latest freeze_<workstream_id>.json was
  kept, with no history at all). Appends every `freeze_and_save()` call
  to a per-workstream history log
  (.governance/freeze/history/<workstream_id>_history.jsonl) and
  provides query methods (list all, get by freeze_id, get by commit).
"""
from __future__ import annotations

import hashlib
import hmac
import json
import secrets
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional


@dataclass(frozen=True)
class FreezeManifest:
    """Stable, flat summary of a freeze record -- what you'd want to
    print or index without traversing the full nested structure."""
    freeze_id: str
    workstream_id: str
    commit_hash: str
    repository_tree_hash: str
    timestamp: str
    all_validators_pass: bool
    integrity_checksum: str

    @classmethod
    def from_record_dict(cls, data: dict[str, Any]) -> "FreezeManifest":
        return cls(
            freeze_id=data["identity"]["freeze_id"],
            workstream_id=data["identity"]["workstream_id"],
            commit_hash=data["repository"]["commit_hash"],
            repository_tree_hash=data["repository"]["repository_tree_hash"],
            timestamp=data["execution"]["timestamp"],
            all_validators_pass=data["validation"]["all_pass"],
            integrity_checksum=data["integrity"]["integrity_checksum"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "freeze_id": self.freeze_id,
            "workstream_id": self.workstream_id,
            "commit_hash": self.commit_hash,
            "repository_tree_hash": self.repository_tree_hash,
            "timestamp": self.timestamp,
            "all_validators_pass": self.all_validators_pass,
            "integrity_checksum": self.integrity_checksum,
        }


class FreezeHash:
    """Computes and verifies a deterministic content hash over a freeze
    record, excluding fields expected to vary between reproductions of
    the SAME logical freeze (execution timestamp, execution duration) --
    mirroring the pattern already established by
    EvidenceRecord.record_hash()."""

    _VOLATILE_KEYS = [("execution", "timestamp"), ("execution", "execution_time_ms"), ("freeze", "freeze_timestamp")]
    # Top-level keys excluded entirely from the hash: "tamper_evidence"
    # is added to a freeze record's saved JSON AFTER FreezeValidator.sign()
    # computes the signature (the signature necessarily cannot include
    # itself), so it must also be excluded here -- otherwise loading the
    # saved JSON file back (which now has this key present) and calling
    # FreezeValidator.verify() against it would always fail, since the
    # hash computed at verify-time would differ from the hash computed
    # at sign-time purely because of this key's presence/absence.
    _EXCLUDED_TOP_LEVEL_KEYS = ["tamper_evidence"]

    @classmethod
    def compute(cls, record_data: dict[str, Any]) -> str:
        stable = json.loads(json.dumps(record_data))  # deep copy
        for outer, inner in cls._VOLATILE_KEYS:
            if outer in stable and isinstance(stable[outer], dict):
                stable[outer].pop(inner, None)
        for key in cls._EXCLUDED_TOP_LEVEL_KEYS:
            stable.pop(key, None)
        return hashlib.sha256(json.dumps(stable, sort_keys=True).encode()).hexdigest()

    @classmethod
    def verify(cls, record_data: dict[str, Any], expected_hash: str) -> bool:
        return cls.compute(record_data) == expected_hash


class FreezeValidator:
    """Tamper-evidence layer for freeze records: HMAC-SHA256 signatures
    keyed by a repository-local secret, generated on first use and
    stored outside version control (`.governance/freeze/.signing_key`,
    listed in .gitignore-equivalent handling -- callers are responsible
    for ensuring this path is git-ignored; this class does not modify
    .gitignore itself).

    A `FreezeHash` content hash alone is NOT tamper-evident: anyone who
    can edit a freeze record can also recompute a matching content hash
    from the edited content and paste it back in. An HMAC signature
    requires possession of the secret key to produce a signature that
    verifies -- editing the record without the key invalidates the
    signature, which IS what "tamper-evident" means.
    """

    def __init__(self, key_path: Path):
        self.key_path = Path(key_path)

    def _load_or_create_key(self) -> bytes:
        if self.key_path.exists():
            return self.key_path.read_bytes()
        self.key_path.parent.mkdir(parents=True, exist_ok=True)
        key = secrets.token_bytes(32)
        self.key_path.write_bytes(key)
        return key

    def sign(self, record_data: dict[str, Any]) -> str:
        key = self._load_or_create_key()
        content_hash = FreezeHash.compute(record_data)
        return hmac.new(key, content_hash.encode(), hashlib.sha256).hexdigest()

    def verify(self, record_data: dict[str, Any], signature: str) -> bool:
        if not self.key_path.exists():
            return False
        key = self.key_path.read_bytes()
        content_hash = FreezeHash.compute(record_data)
        expected = hmac.new(key, content_hash.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)


@dataclass(frozen=True)
class FreezeEvidence:
    """Typed view over a freeze record's embedded evidence fields."""
    evidence_record_hash: str
    artefact_hashes: dict[str, str]

    @classmethod
    def from_record_dict(cls, data: dict[str, Any]) -> "FreezeEvidence":
        return cls(
            evidence_record_hash=data["evidence"]["evidence_record_hash"],
            artefact_hashes=data["evidence"]["artefact_hashes"],
        )


class FreezeHistory:
    """Queryable history of every freeze record ever produced for a
    workstream, appended to on every `freeze_and_save()` call (see
    freeze_engine.py's integration). Previously, only the single latest
    freeze_<workstream_id>.json was kept -- no history existed at all.

    Stored as JSON Lines (one manifest per line) rather than a single
    growing JSON array, so appending never requires rewriting the whole
    file.
    """

    def __init__(self, history_dir: Path):
        self.history_dir = Path(history_dir)

    def _history_path(self, workstream_id: str) -> Path:
        return self.history_dir / f"{workstream_id}_history.jsonl"

    def append(self, manifest: FreezeManifest, signature: Optional[str] = None) -> Path:
        path = self._history_path(manifest.workstream_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        entry = manifest.to_dict()
        if signature is not None:
            entry["signature"] = signature
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, sort_keys=True) + "\n")
        return path

    def list_all(self, workstream_id: str) -> list[dict]:
        path = self._history_path(workstream_id)
        if not path.exists():
            return []
        entries = []
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                entries.append(json.loads(line))
        return entries

    def get_by_freeze_id(self, workstream_id: str, freeze_id: str) -> Optional[dict]:
        for entry in self.list_all(workstream_id):
            if entry.get("freeze_id") == freeze_id:
                return entry
        return None

    def get_by_commit(self, workstream_id: str, commit_hash: str) -> list[dict]:
        return [e for e in self.list_all(workstream_id) if e.get("commit_hash") == commit_hash]
