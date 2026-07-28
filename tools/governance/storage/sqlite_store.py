from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Iterable
from ..metadata.models import DocumentMetadata

class SqliteStore:
    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self._init_schema()

    def _init_schema(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS documents (path TEXT PRIMARY KEY, type TEXT, owner TEXT, status TEXT, version TEXT, purpose TEXT, scope TEXT, last_updated TEXT, canonical_source TEXT)")
        self.conn.commit()

    def upsert_documents(self, docs: Iterable[DocumentMetadata]):
        cur = self.conn.cursor()
        for d in docs:
            cur.execute("INSERT OR REPLACE INTO documents (path, type, owner, status, version, purpose, scope, last_updated, canonical_source) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (d.path, d.type, d.owner, d.status, d.version, d.purpose, d.scope, d.last_updated, d.canonical_source))
        self.conn.commit()

    def get_all_paths(self) -> list[str]:
        cur = self.conn.cursor()
        cur.execute("SELECT path FROM documents")
        return [r[0] for r in cur.fetchall()]
