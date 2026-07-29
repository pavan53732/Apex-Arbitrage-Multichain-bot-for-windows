"""Regression tests for the determinism fixes made during Repository
Canonicality Repair, Work Item 1.

These tests specifically guard against reintroducing the two confirmed
non-determinism sources: `list(set(...))` in ReferenceParser, and
SQLite file-content instability from incremental upserts on a persistent
database file.
"""
import subprocess
import sys
from pathlib import Path

from governance.references.reference_parser import ReferenceParser, _dedupe_preserve_order
from governance.storage.sqlite_store import SqliteStore
from governance.metadata.models import DocumentMetadata


def test_dedupe_preserve_order_is_deterministic_and_order_preserving():
    items = ["c.md", "a.md", "b.md", "a.md", "c.md"]
    result = _dedupe_preserve_order(items)
    assert result == ["c.md", "a.md", "b.md"], "must preserve first-seen order, not hash order"

    # Must be identical across repeated calls in this process, and would
    # be identical across process restarts too since it never touches a
    # Python set for ordering (only for O(1) membership testing).
    assert _dedupe_preserve_order(items) == result


def test_extract_cross_references_does_not_use_a_bare_set_for_ordering():
    parser = ReferenceParser(repo_root=".")
    text = "## Cross References\n- `ZEBRA.md`\n- `APPLE.md`\n- `MANGO.md`\n"
    refs = parser.extract_cross_references(text, "SOURCE.md")
    # Order must match the order the references appear in the text
    # (deterministic, since regex extraction from a fixed string is
    # itself deterministic), not an arbitrary hash-based order.
    assert refs == ["ZEBRA.md", "APPLE.md", "MANGO.md"]


def test_extract_depends_on_does_not_use_a_bare_set_for_ordering():
    parser = ReferenceParser(repo_root=".")
    text = "## Depends On\n- `ZEBRA.md`\n- `APPLE.md`\n"
    deps = parser.extract_depends_on(text, "SOURCE.md")
    assert deps == ["ZEBRA.md", "APPLE.md"]


def test_sqlite_store_produces_byte_identical_files_across_rebuilds(tmp_path):
    """Regression test for the SQLite non-determinism found during
    Repository Canonicality Repair: repeatedly writing the same logical
    document set to the same on-disk SQLite file (via incremental
    INSERT OR REPLACE) previously produced different bytes each time,
    because of B-tree/rowid internals. `fresh=True` (the default) fixes
    this by deleting and rebuilding the file from scratch every time.
    """
    db_path = tmp_path / "test.db"
    docs = [
        DocumentMetadata(path="a.md", type="REFERENCE", owner="Team A"),
        DocumentMetadata(path="b.md", type="CONTRACT", owner="Team B"),
    ]

    store1 = SqliteStore(str(db_path))
    store1.upsert_documents(docs)
    store1.conn.close()
    hash1 = db_path.read_bytes()

    store2 = SqliteStore(str(db_path))  # fresh=True by default: deletes and rebuilds
    store2.upsert_documents(docs)
    store2.conn.close()
    hash2 = db_path.read_bytes()

    assert hash1 == hash2, "SqliteStore must produce byte-identical files for identical logical content"


def test_sqlite_store_get_all_paths_is_sorted(tmp_path):
    db_path = tmp_path / "test2.db"
    docs = [
        DocumentMetadata(path="z.md", type="REFERENCE"),
        DocumentMetadata(path="a.md", type="REFERENCE"),
    ]
    store = SqliteStore(str(db_path))
    store.upsert_documents(docs)
    paths = store.get_all_paths()
    assert paths == sorted(paths)


def test_upsert_closure_documents_sorts_input_for_determinism(tmp_path):
    """Regression test for a real non-determinism defect found during
    WS5 implementation: cli/main.py's `run` command passed
    `all_closures[r.path]` (a `set[str]`, as returned by
    ClosureEngine.compute_closure()) directly to
    SqliteStore.upsert_closure_documents(), whose target table
    (closure_documents) is WITHOUT ROWID -- meaning SQLite's B-tree page
    layout, and therefore the database file's exact bytes, depends on
    INSERT order. Iterating a Python set is subject to per-process
    string-hash randomisation (PYTHONHASHSEED), so two consecutive
    `apex-gov run` invocations in the SAME process produced different
    governance.db byte content, confirmed via
    test_evidence_engine_record_hash_is_reproducible failing. Fixed by
    sorting inside upsert_closure_documents() itself (defense in depth,
    not just at the call site) -- this test passes an intentionally
    unsorted/set-derived iterable and asserts the resulting database
    bytes are identical regardless of insertion order.
    """
    db_path1 = tmp_path / "order1.db"
    db_path2 = tmp_path / "order2.db"

    store1 = SqliteStore(str(db_path1))
    store1.upsert_closures([{"root_path": "root.md", "closure_hash": "h", "version": 1}])
    store1.upsert_closure_documents("root.md", ["c.md", "a.md", "b.md"])
    store1.conn.close()

    store2 = SqliteStore(str(db_path2))
    store2.upsert_closures([{"root_path": "root.md", "closure_hash": "h", "version": 1}])
    store2.upsert_closure_documents("root.md", ["b.md", "c.md", "a.md"])  # different insertion order
    store2.conn.close()

    assert db_path1.read_bytes() == db_path2.read_bytes(), (
        "closure_documents rows must produce byte-identical database files "
        "regardless of the input iterable's order"
    )
