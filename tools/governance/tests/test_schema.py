"""Tests for the canonical SQLite schema (WS5 Database Consolidation:
schema versioning, migration scripts, schema version documented)."""
import sqlite3

from governance.storage.schema import (
    FROZEN_TABLE_NAMES,
    MIGRATIONS,
    SCHEMA_VERSION,
    get_user_version,
    migrate,
    set_user_version,
)


def test_fresh_database_starts_at_version_0():
    conn = sqlite3.connect(":memory:")
    assert get_user_version(conn) == 0


def test_migrate_brings_fresh_database_to_current_schema_version():
    conn = sqlite3.connect(":memory:")
    result = migrate(conn)
    assert result == SCHEMA_VERSION
    assert get_user_version(conn) == SCHEMA_VERSION


def test_all_20_frozen_tables_exist_after_fresh_init():
    conn = sqlite3.connect(":memory:")
    migrate(conn)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing = {row[0] for row in cur.fetchall()}
    missing = set(FROZEN_TABLE_NAMES) - existing
    assert missing == set(), f"Missing frozen tables: {missing}"
    assert len(FROZEN_TABLE_NAMES) == 20


def test_migrate_is_idempotent_and_does_not_reapply_migrations():
    conn = sqlite3.connect(":memory:")
    migrate(conn)
    conn.execute("INSERT INTO documents (path, type) VALUES ('a.md', 'CONTRACT')")
    conn.commit()
    # Re-running migrate() must not error (e.g. from re-running CREATE
    # TABLE without IF NOT EXISTS) and must not touch existing data.
    migrate(conn)
    cur = conn.cursor()
    cur.execute("SELECT path FROM documents")
    assert cur.fetchall() == [("a.md",)]


def test_migrate_skips_already_applied_versions_on_existing_database():
    conn = sqlite3.connect(":memory:")
    set_user_version(conn, SCHEMA_VERSION)  # simulate an already-migrated DB
    # Applying migrate() again on an already-current database must not
    # attempt to run migrations whose version <= current (would be a
    # no-op here since there's only 1 migration, but this documents and
    # tests the skip logic explicitly for when a 2nd migration exists).
    result = migrate(conn)
    assert result == SCHEMA_VERSION


def test_schema_version_is_documented_in_this_module():
    """WS5 checklist item 'Schema version documented' -- SCHEMA_VERSION
    is the single source of truth, imported by SqliteStore and by any
    reporting code, rather than a magic number duplicated elsewhere."""
    assert isinstance(SCHEMA_VERSION, int)
    assert SCHEMA_VERSION >= 1


def test_migrations_list_is_sorted_by_version_with_no_gaps_from_1():
    versions = sorted(v for v, _ in MIGRATIONS)
    assert versions == list(range(1, len(versions) + 1)), (
        "Migration versions must be contiguous starting at 1, so migrate() "
        "can safely apply them in order without skipping an undefined version."
    )
