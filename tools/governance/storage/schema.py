"""Canonical SQLite schema definition (Programme 2.5 Phase-0, WS5
Database Consolidation).

`database_schema_freeze.json` freezes 20 tables. Prior to this module,
only 1 (`documents`) existed anywhere in the live schema (confirmed:
`SqliteStore._init_schema()` created only `documents`; the frozen
`documents/behavioural_roots/closures/.../commits` 20-table schema
existed only as this JSON name-list, never implemented). This module
defines all 20 as real, versioned DDL.

SCHEMA_VERSION is stored via SQLite's built-in `PRAGMA user_version`
(an integer stored in the database file header itself, not a
user-defined table -- this is the standard SQLite mechanism for schema
versioning and requires no extra table). `MIGRATIONS` is an ordered
list of (version, sql_statements) migration steps; `migrate()` applies
every migration with `version > current_user_version`, so upgrading an
existing (non-`fresh`) database always leaves it at `SCHEMA_VERSION`
regardless of which version it started at.
"""
from __future__ import annotations

import sqlite3

# Bump this and append a new entry to MIGRATIONS whenever the schema
# changes. Never edit an existing MIGRATIONS entry after it has shipped
# -- that would break migrate()'s "already applied" guarantee for
# databases created under an earlier version of this module.
SCHEMA_VERSION = 1

# The 20 tables frozen in
# .governance/programme_2.5/phase_0/database_schema_freeze.json, in the
# order they appear there. Every table name in this list has a
# corresponding CREATE TABLE statement in MIGRATIONS[0] below -- see
# tests/test_schema.py::test_all_20_frozen_tables_exist_after_fresh_init
# for the check that keeps these two in sync.
FROZEN_TABLE_NAMES = [
    "documents",
    "behavioural_roots",
    "closures",
    "closure_documents",
    "dimensions",
    "sections",
    "validators",
    "validator_runs",
    "repair_tasks",
    "repair_history",
    "graphs",
    "graph_nodes",
    "graph_edges",
    "metrics",
    "metric_history",
    "freeze_records",
    "freeze_history",
    "evidence",
    "reports",
    "commits",
]

MIGRATIONS: list[tuple[int, list[str]]] = [
    (1, [
        # documents: unchanged from the pre-WS5 schema (path is the
        # natural primary key; WITHOUT ROWID preserved for the
        # determinism guarantee documented in sqlite_store.py).
        """CREATE TABLE IF NOT EXISTS documents (
            path TEXT PRIMARY KEY, type TEXT, owner TEXT, status TEXT,
            version TEXT, purpose TEXT, scope TEXT, last_updated TEXT,
            canonical_source TEXT
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS behavioural_roots (
            path TEXT PRIMARY KEY, tier TEXT, signals TEXT, reason TEXT,
            lifecycle_state TEXT, owner TEXT,
            FOREIGN KEY (path) REFERENCES documents(path)
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS closures (
            root_path TEXT PRIMARY KEY, closure_hash TEXT, version INTEGER,
            closure_size INTEGER, reverse_closure_size INTEGER,
            generated_at TEXT, generated_at_commit TEXT,
            FOREIGN KEY (root_path) REFERENCES behavioural_roots(path)
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS closure_documents (
            root_path TEXT, document_path TEXT, relation TEXT,
            PRIMARY KEY (root_path, document_path),
            FOREIGN KEY (root_path) REFERENCES closures(root_path)
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS dimensions (
            root_path TEXT, dimension TEXT,
            PRIMARY KEY (root_path, dimension)
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS sections (
            document_path TEXT, dimension TEXT, section TEXT,
            PRIMARY KEY (document_path, dimension, section)
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS validators (
            validator_id TEXT PRIMARY KEY, owner TEXT, layer TEXT,
            severity TEXT, documentation TEXT
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS validator_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT, validator_id TEXT,
            status TEXT, executed_at TEXT, commit_hash TEXT,
            FOREIGN KEY (validator_id) REFERENCES validators(validator_id)
        )""",

        """CREATE TABLE IF NOT EXISTS repair_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT, document_path TEXT,
            dimension TEXT, status TEXT, created_at TEXT
        )""",

        """CREATE TABLE IF NOT EXISTS repair_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT, task_id INTEGER,
            status TEXT, changed_at TEXT,
            FOREIGN KEY (task_id) REFERENCES repair_tasks(id)
        )""",

        """CREATE TABLE IF NOT EXISTS graphs (
            graph_name TEXT PRIMARY KEY, node_count INTEGER,
            edge_count INTEGER, file_hash TEXT, generated_at TEXT
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS graph_nodes (
            graph_name TEXT, node_id TEXT,
            PRIMARY KEY (graph_name, node_id),
            FOREIGN KEY (graph_name) REFERENCES graphs(graph_name)
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS graph_edges (
            graph_name TEXT, source TEXT, target TEXT, relation TEXT,
            PRIMARY KEY (graph_name, source, target, relation),
            FOREIGN KEY (graph_name) REFERENCES graphs(graph_name)
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS metrics (
            metric_name TEXT PRIMARY KEY, value REAL, computed_at TEXT
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS metric_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT, metric_name TEXT,
            value REAL, computed_at TEXT, commit_hash TEXT,
            FOREIGN KEY (metric_name) REFERENCES metrics(metric_name)
        )""",

        """CREATE TABLE IF NOT EXISTS freeze_records (
            freeze_id TEXT PRIMARY KEY, workstream_id TEXT,
            commit_hash TEXT, repository_tree_hash TEXT, timestamp TEXT
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS freeze_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT, freeze_id TEXT,
            workstream_id TEXT, commit_hash TEXT, timestamp TEXT,
            FOREIGN KEY (freeze_id) REFERENCES freeze_records(freeze_id)
        )""",

        """CREATE TABLE IF NOT EXISTS evidence (
            record_hash TEXT PRIMARY KEY, command TEXT, commit_hash TEXT,
            timestamp TEXT
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS reports (
            report_path TEXT PRIMARY KEY, report_type TEXT,
            generated_at TEXT, commit_hash TEXT
        ) WITHOUT ROWID""",

        """CREATE TABLE IF NOT EXISTS commits (
            commit_hash TEXT PRIMARY KEY, indexed_at TEXT,
            documents_indexed INTEGER, behavioural_roots INTEGER
        ) WITHOUT ROWID""",
    ]),
]


def get_user_version(conn: sqlite3.Connection) -> int:
    cur = conn.cursor()
    cur.execute("PRAGMA user_version")
    return cur.fetchone()[0]


def set_user_version(conn: sqlite3.Connection, version: int) -> None:
    # PRAGMA does not support parameter binding; version is always an
    # int from this module's own SCHEMA_VERSION/MIGRATIONS constants,
    # never external input, so direct interpolation is safe here.
    conn.execute(f"PRAGMA user_version = {int(version)}")


def migrate(conn: sqlite3.Connection) -> int:
    """Apply every migration with version > the database's current
    user_version, in ascending order. Returns the resulting version.
    Safe to call on a brand-new (version 0) database or an existing one
    created by an earlier version of this module -- migrations already
    applied are skipped, never re-run."""
    current = get_user_version(conn)
    for version, statements in sorted(MIGRATIONS, key=lambda m: m[0]):
        if version <= current:
            continue
        for stmt in statements:
            conn.execute(stmt)
        set_user_version(conn, version)
        current = version
    conn.commit()
    return current
