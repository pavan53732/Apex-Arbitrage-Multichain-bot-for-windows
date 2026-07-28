from __future__ import annotations

import sqlite3
import json
import hashlib
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timezone


@dataclass
class FreezeRecord:
    id: str
    entity_type: str  # CLOSURE, DIMENSION, DOCUMENT, SECTION
    entity_id: str
    dimension_name: Optional[str]
    freeze_hash: str
    freeze_timestamp: str
    freeze_commit: str
    validator_results: str  # JSON
    evidence: str  # JSON
    regression_checksum: str
    reopened_at: Optional[str]
    reopened_reason: Optional[str]
    created_at: str


class FreezeManager:
    """Programme 3 Freeze Manager.

    Makes completed dimensions and closures immutable until reopened.
    Every frozen dimension gets:
    - Dimension Hash
    - Timestamp
    - Validator Results
    - Commit Hash
    - Worker
    - Evidence
    - Regression Checksum
    """

    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def freeze_dimension(
        self,
        closure_id: str,
        dimension: str,
        validator_results: List[dict],
        evidence: List[str],
        commit_hash: str,
        worker_id: str,
    ) -> FreezeRecord:
        """Freeze a dimension after all validators pass."""
        conn = self._get_conn()
        cursor = conn.cursor()
        now = datetime.now(timezone.utc).isoformat()

        # Compute freeze hash
        freeze_data = {
            "closure_id": closure_id,
            "dimension": dimension,
            "validator_results": validator_results,
            "evidence": evidence,
            "commit_hash": commit_hash,
            "worker_id": worker_id,
            "timestamp": now,
        }
        freeze_hash = hashlib.sha256(json.dumps(freeze_data, sort_keys=True).encode()).hexdigest()

        # Compute regression checksum
        regression_checksum = hashlib.sha256(json.dumps(validator_results, sort_keys=True).encode()).hexdigest()

        # Create freeze record
        freeze_id = f"FREEZE_{closure_id}_{dimension}_{now}"
        cursor.execute("""
        INSERT INTO freeze_records (
            id, entity_type, entity_id, dimension_name, freeze_hash, freeze_timestamp,
            freeze_commit, validator_results, evidence, regression_checksum,
            reopened_at, reopened_reason, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            freeze_id,
            "DIMENSION",
            closure_id,
            dimension,
            freeze_hash,
            now,
            commit_hash,
            json.dumps(validator_results),
            json.dumps(evidence),
            regression_checksum,
            None,
            None,
            now,
        ))

        # Update dimension freeze status
        cursor.execute("""
        UPDATE dimensions 
        SET freeze_status = 'FROZEN', freeze_timestamp = ?, freeze_commit = ?, updated_at = ?
        WHERE closure_id = ? AND dimension_name = ?
        """, (now, commit_hash, now, closure_id, dimension))

        conn.commit()
        conn.close()

        return FreezeRecord(
            id=freeze_id,
            entity_type="DIMENSION",
            entity_id=closure_id,
            dimension_name=dimension,
            freeze_hash=freeze_hash,
            freeze_timestamp=now,
            freeze_commit=commit_hash,
            validator_results=json.dumps(validator_results),
            evidence=json.dumps(evidence),
            regression_checksum=regression_checksum,
            reopened_at=None,
            reopened_reason=None,
            created_at=now,
        )

    def freeze_closure(
        self,
        closure_id: str,
        validator_results: List[dict],
        evidence: List[str],
        commit_hash: str,
        worker_id: str,
    ) -> FreezeRecord:
        """Freeze an entire closure after all dimensions are frozen."""
        conn = self._get_conn()
        cursor = conn.cursor()
        now = datetime.now(timezone.utc).isoformat()

        freeze_data = {
            "closure_id": closure_id,
            "validator_results": validator_results,
            "evidence": evidence,
            "commit_hash": commit_hash,
            "worker_id": worker_id,
            "timestamp": now,
        }
        freeze_hash = hashlib.sha256(json.dumps(freeze_data, sort_keys=True).encode()).hexdigest()
        regression_checksum = hashlib.sha256(json.dumps(validator_results, sort_keys=True).encode()).hexdigest()

        freeze_id = f"FREEZE_{closure_id}_CLOSURE_{now}"
        cursor.execute("""
        INSERT INTO freeze_records (
            id, entity_type, entity_id, dimension_name, freeze_hash, freeze_timestamp,
            freeze_commit, validator_results, evidence, regression_checksum,
            reopened_at, reopened_reason, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            freeze_id,
            "CLOSURE",
            closure_id,
            None,
            freeze_hash,
            now,
            commit_hash,
            json.dumps(validator_results),
            json.dumps(evidence),
            regression_checksum,
            None,
            None,
            now,
        ))

        # Update closure freeze status
        cursor.execute("""
        UPDATE closures 
        SET freeze_status = 'FROZEN', freeze_timestamp = ?, freeze_commit = ?, updated_at = ?
        WHERE id = ?
        """, (now, commit_hash, now, closure_id))

        conn.commit()
        conn.close()

        return FreezeRecord(
            id=freeze_id,
            entity_type="CLOSURE",
            entity_id=closure_id,
            dimension_name=None,
            freeze_hash=freeze_hash,
            freeze_timestamp=now,
            freeze_commit=commit_hash,
            validator_results=json.dumps(validator_results),
            evidence=json.dumps(evidence),
            regression_checksum=regression_checksum,
            reopened_at=None,
            reopened_reason=None,
            created_at=now,
        )

    def reopen_freeze(self, freeze_id: str, reason: str) -> bool:
        """Reopen a freeze record (e.g., due to regression)."""
        conn = self._get_conn()
        cursor = conn.cursor()
        now = datetime.now(timezone.utc).isoformat()
        cursor.execute("""
        UPDATE freeze_records 
        SET reopened_at = ?, reopened_reason = ?, updated_at = ?
        WHERE id = ?
        """, (now, reason, now, freeze_id))

        # Update entity freeze status
        cursor.execute("""
        SELECT entity_type, entity_id, dimension_name FROM freeze_records WHERE id = ?
        """, (freeze_id,))
        row = cursor.fetchone()
        if row:
            entity_type, entity_id, dimension_name = row
            if entity_type == "DIMENSION":
                cursor.execute("""
                UPDATE dimensions 
                SET freeze_status = 'REOPENED', updated_at = ?
                WHERE closure_id = ? AND dimension_name = ?
                """, (now, entity_id, dimension_name))
            elif entity_type == "CLOSURE":
                cursor.execute("""
                UPDATE closures 
                SET freeze_status = 'REOPENED', updated_at = ?
                WHERE id = ?
                """, (now, entity_id))

        conn.commit()
        conn.close()
        return cursor.rowcount > 0

    def get_freeze_record(self, closure_id: str, dimension: str) -> Optional[FreezeRecord]:
        """Get freeze record for a dimension."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM freeze_records 
        WHERE entity_type = 'DIMENSION' AND entity_id = ? AND dimension_name = ?
        ORDER BY created_at DESC LIMIT 1
        """, (closure_id, dimension))
        row = cursor.fetchone()
        conn.close()

        if row:
            return FreezeRecord(
                id=row["id"],
                entity_type=row["entity_type"],
                entity_id=row["entity_id"],
                dimension_name=row["dimension_name"],
                freeze_hash=row["freeze_hash"],
                freeze_timestamp=row["freeze_timestamp"],
                freeze_commit=row["freeze_commit"],
                validator_results=row["validator_results"],
                evidence=row["evidence"],
                regression_checksum=row["regression_checksum"],
                reopened_at=row["reopened_at"],
                reopened_reason=row["reopened_reason"],
                created_at=row["created_at"],
            )
        return None
