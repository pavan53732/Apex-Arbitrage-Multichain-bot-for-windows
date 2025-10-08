# Archive Guide

## Overview
This archive contains deprecated modules, legacy releases, migration logs, old configurations, and archived tests for historical reference and rollback purposes.

## Folder Structure

### deprecated-modules/
Legacy code modules that have been superseded by newer implementations.

### previous-releases/
Archived builds and release bundles with integrity checksums.

### migrations-logs/
Historical database and system migration logs with failure tracking.

### old-configs/
Pre-upgrade configuration files for tokens, chains, DEXes, strategies, and risk profiles.

### archived-tests/
Legacy test suites and output logs from previous versions.

## Rollback Steps
1. Identify target version from previous-releases/
2. Verify integrity using SHA256 checksums
3. Review migration-logs/ for relevant changes
4. Restore old-configs/ if needed
5. Run archived-tests/ to validate rollback

## Traceability Map
- All migrations tracked in migrations-logs/migration-summary.csv
- Release notes in previous-releases/release-notes-v1.md
- Config changes documented in old-configs/README.md
- Test coverage in archived-tests/README.md
