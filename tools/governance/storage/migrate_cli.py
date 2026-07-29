"""Standalone database migration script (WS5: "Migration scripts
created").

Usage:
    python3 -m governance.storage.migrate_cli [--db-path .governance/governance.db] [--check]

Applies every pending migration in storage/schema.py's MIGRATIONS list
to the target database, bringing it to the current SCHEMA_VERSION. Safe
to run against:
- A database file that does not exist yet (creates it fresh at the
  current schema version).
- A database already at the current schema version (no-op).
- A database at an older schema version, once a future migration is
  added to MIGRATIONS (applies only the missing migrations).

This does NOT delete/rebuild the database (unlike SqliteStore's
fresh=True default, which exists purely for byte-level determinism of
canonical `apex-gov run` output) -- it performs a real, additive
migration, preserving any existing rows, which is what a standalone
migration tool for a persistent/production database must do.
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

from .schema import FROZEN_TABLE_NAMES, SCHEMA_VERSION, get_user_version, migrate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Apply pending governance database migrations.")
    parser.add_argument("--db-path", default=".governance/governance.db")
    parser.add_argument("--check", action="store_true", help="Report status only; do not modify the database.")
    args = parser.parse_args(argv)

    db_path = Path(args.db_path)
    db_existed = db_path.exists()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(db_path))
    before_version = get_user_version(conn)

    if args.check:
        status = "up to date" if before_version == SCHEMA_VERSION else "needs migration"
        print(f"db_path={db_path} exists={db_existed} current_version={before_version} "
              f"target_version={SCHEMA_VERSION} status={status}")
        conn.close()
        return 0 if before_version == SCHEMA_VERSION else 1

    after_version = migrate(conn)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing_tables = {row[0] for row in cur.fetchall()}
    missing = set(FROZEN_TABLE_NAMES) - existing_tables
    conn.close()

    print(f"db_path={db_path} before_version={before_version} after_version={after_version}")
    if missing:
        print(f"ERROR: missing frozen tables after migration: {sorted(missing)}", file=sys.stderr)
        return 1
    print(f"All {len(FROZEN_TABLE_NAMES)} frozen tables present. Migration successful.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
