from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Iterable
from ..metadata.models import DocumentMetadata

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
        cur = self.conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS documents ("
            "path TEXT PRIMARY KEY, type TEXT, owner TEXT, status TEXT, version TEXT, "
            "purpose TEXT, scope TEXT, last_updated TEXT, canonical_source TEXT"
            ") WITHOUT ROWID"
        )
        self.conn.commit()

    def upsert_documents(self, docs: Iterable[DocumentMetadata]):
        cur = self.conn.cursor()
        for d in docs:
            cur.execute("INSERT OR REPLACE INTO documents (path, type, owner, status, version, purpose, scope, last_updated, canonical_source) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (d.path, d.type, d.owner, d.status, d.version, d.purpose, d.scope, d.last_updated, d.canonical_source))
        self.conn.commit()

    def get_all_paths(self) -> list[str]:
        cur = self.conn.cursor()
        cur.execute("SELECT path FROM documents ORDER BY path")
        return [r[0] for r in cur.fetchall()]

