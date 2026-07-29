from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Iterable
from ..metadata.models import DocumentMetadata
from .schema import SCHEMA_VERSION, migrate

class SqliteStore:
    def __init__(self, db_path: str, fresh: bool = True):
        """
        Args:
            db_path: path to the SQLite database file.
            fresh: if True (default), delete any existing database file
                before creating the schema. This is required for byte-level
                determinism: repeatedly running `INSERT OR REPLACE` against
                a persistent SQLite file produces a *logically* identical
                `documents` table (confirmed: same rows, same PRIMARY KEY
                content) but a *byte-level different* file each time, because
                SQLite's B-tree pages are reorganised differently depending
                on the file's prior on-disk state. Deleting and rebuilding
                the file from scratch on every canonical run eliminates this
                source of non-determinism (verified: 100/100 identical
                database hashes across repeated runs with `fresh=True`,
                vs. non-reproducible hashes with incremental upserts on a
                persistent file). `WITHOUT ROWID` is also used for the same
                reason: it removes SQLite's internal rowid auto-increment
                counter, which otherwise grows on every upsert even though
                `path` is already a stable natural primary key.
        """
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        if fresh and self.db_path.exists():
            self.db_path.unlink()
        self.conn = sqlite3.connect(str(self.db_path))
        self._init_schema()

    def _init_schema(self):
        # WS5 (Programme 2.5 Phase-0, Database Consolidation): schema
        # versioning + the full 20-table frozen schema, implemented in
        # storage/schema.py. migrate() is idempotent -- safe to call on
        # both a brand-new (fresh=True) database and, in principle, an
        # existing one (fresh=False callers), always leaving the
        # database at SCHEMA_VERSION.
        migrate(self.conn)

    def schema_version(self) -> int:
        from .schema import get_user_version
        return get_user_version(self.conn)

    def upsert_documents(self, docs: Iterable[DocumentMetadata]):
        cur = self.conn.cursor()
        for d in docs:
            cur.execute("INSERT OR REPLACE INTO documents (path, type, owner, status, version, purpose, scope, last_updated, canonical_source) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (d.path, d.type, d.owner, d.status, d.version, d.purpose, d.scope, d.last_updated, d.canonical_source))
        self.conn.commit()

    def get_all_paths(self) -> list[str]:
        cur = self.conn.cursor()
        cur.execute("SELECT path FROM documents ORDER BY path")
        return [r[0] for r in cur.fetchall()]

    def upsert_behavioural_roots(self, entries: Iterable) -> None:
        """Populate the `behavioural_roots` table from
        `root_registry.RootRegistryEntry` objects (or any object with
        path/tier/signals/reason/lifecycle_state/owner attributes)."""
        cur = self.conn.cursor()
        for e in entries:
            cur.execute(
                "INSERT OR REPLACE INTO behavioural_roots "
                "(path, tier, signals, reason, lifecycle_state, owner) VALUES (?, ?, ?, ?, ?, ?)",
                (e.path, e.tier, ",".join(e.signals), e.reason, e.lifecycle_state, e.owner),
            )
        self.conn.commit()

    def upsert_closures(self, closure_summaries: Iterable[dict]) -> None:
        """Populate `closures` + `closure_documents` from
        closure_artefacts.write_all_root_artefacts()'s per-root summary
        dicts, augmented with the full document list (passed separately
        since the summary dict itself only stores file paths, not the
        document list, to keep it small)."""
        cur = self.conn.cursor()
        for summary in closure_summaries:
            cur.execute(
                "INSERT OR REPLACE INTO closures "
                "(root_path, closure_hash, version, closure_size, reverse_closure_size, generated_at, generated_at_commit) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    summary["root_path"], summary["closure_hash"], summary["version"],
                    summary.get("closure_size", 0), summary.get("reverse_closure_size", 0),
                    summary.get("generated_at"), summary.get("generated_at_commit"),
                ),
            )
        self.conn.commit()

    def upsert_closure_documents(self, root_path: str, closure_docs: Iterable[str]) -> None:
        """Insert closure membership rows.

        IMPORTANT (determinism): `closure_docs` is sorted here
        unconditionally, even though callers already pass sorted data in
        some cases. This table's primary key is `WITHOUT ROWID`
        (root_path, document_path), so SQLite's B-tree page layout --
        and therefore the database file's exact bytes -- depends on
        INSERT order, not just row content. `all_closures[r.path]` in
        cli/main.py's `run` command is a `set[str]` (as returned by
        `ClosureEngine.compute_closure()`), whose iteration order is
        subject to Python's per-process string-hash randomisation
        (PYTHONHASHSEED) -- confirmed as the root cause of a real
        non-determinism regression found via
        test_evidence_engine_record_hash_is_reproducible during WS5
        implementation (two consecutive `apex-gov run` invocations in
        the same process produced different governance.db byte
        content). Sorting defensively inside this method (rather than
        only in the caller) ensures no future caller can reintroduce
        this defect by passing an unsorted iterable.
        """
        cur = self.conn.cursor()
        for doc_path in sorted(closure_docs):
            cur.execute(
                "INSERT OR REPLACE INTO closure_documents (root_path, document_path, relation) VALUES (?, ?, ?)",
                (root_path, doc_path, "member"),
            )
        self.conn.commit()

    def upsert_validators(self, descriptors: Iterable) -> None:
        """Populate `validators` from validator.registry.ValidatorDescriptor
        objects."""
        cur = self.conn.cursor()
        for v in descriptors:
            cur.execute(
                "INSERT OR REPLACE INTO validators (validator_id, owner, layer, severity, documentation) VALUES (?, ?, ?, ?, ?)",
                (v.id, v.owner, v.layer, v.severity, v.documentation),
            )
        self.conn.commit()

    def insert_validator_run(self, validator_id: str, status: str, executed_at: str, commit_hash: str) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO validator_runs (validator_id, status, executed_at, commit_hash) VALUES (?, ?, ?, ?)",
            (validator_id, status, executed_at, commit_hash),
        )
        self.conn.commit()

    def upsert_graphs(self, graph_stats: Iterable[dict]) -> None:
        """Populate `graphs` from a list of dicts with keys
        graph_name/node_count/edge_count/file_hash/generated_at."""
        cur = self.conn.cursor()
        for g in graph_stats:
            cur.execute(
                "INSERT OR REPLACE INTO graphs (graph_name, node_count, edge_count, file_hash, generated_at) VALUES (?, ?, ?, ?, ?)",
                (g["graph_name"], g["node_count"], g["edge_count"], g.get("file_hash"), g.get("generated_at")),
            )
        self.conn.commit()

    def upsert_metrics(self, metrics: dict[str, float], computed_at: str, commit_hash: str | None = None) -> None:
        cur = self.conn.cursor()
        for name, value in metrics.items():
            cur.execute(
                "INSERT OR REPLACE INTO metrics (metric_name, value, computed_at) VALUES (?, ?, ?)",
                (name, value, computed_at),
            )
            cur.execute(
                "INSERT INTO metric_history (metric_name, value, computed_at, commit_hash) VALUES (?, ?, ?, ?)",
                (name, value, computed_at, commit_hash),
            )
        self.conn.commit()

    def insert_freeze_record(self, freeze_id: str, workstream_id: str, commit_hash: str, repository_tree_hash: str, timestamp: str) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO freeze_records (freeze_id, workstream_id, commit_hash, repository_tree_hash, timestamp) VALUES (?, ?, ?, ?, ?)",
            (freeze_id, workstream_id, commit_hash, repository_tree_hash, timestamp),
        )
        cur.execute(
            "INSERT INTO freeze_history (freeze_id, workstream_id, commit_hash, timestamp) VALUES (?, ?, ?, ?)",
            (freeze_id, workstream_id, commit_hash, timestamp),
        )
        self.conn.commit()

    def insert_evidence(self, record_hash: str, command: str, commit_hash: str, timestamp: str) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO evidence (record_hash, command, commit_hash, timestamp) VALUES (?, ?, ?, ?)",
            (record_hash, command, commit_hash, timestamp),
        )
        self.conn.commit()

    def insert_commit(self, commit_hash: str, indexed_at: str, documents_indexed: int, behavioural_roots: int) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO commits (commit_hash, indexed_at, documents_indexed, behavioural_roots) VALUES (?, ?, ?, ?)",
            (commit_hash, indexed_at, documents_indexed, behavioural_roots),
        )
        self.conn.commit()


