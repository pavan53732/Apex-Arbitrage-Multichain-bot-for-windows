---
metadata_schema_version: 1.0
document_id: DOC-0274
title: File Storage
plane: Product Specification
domain: Data
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/data/persistence/file-storage.md
related_concepts:
  - CONCEPT-0274
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Data
type: REFERENCE
purpose: File Storage documentation.
scope: Reference documentation.
---

# File Storage

## Document type
Document type: [REFERENCE]

## Purpose
Defines the file-storage model for the APEX platform: where files live, what is stored on disk, and how storage is governed.

## Scope
The database schema owns structured persistence; this document covers file-based storage: logs, exports, workspace snapshots, plugin archives, and cache spill.

## Storage locations
- **User scope** (`%APPDATA%/Apex`): logs, exports, workspace snapshots, and user preferences.
- **System scope** (`%PROGRAMDATA%/Apex`): service data and shared state.
- **Cache** (`%LOCALAPPDATA%/Apex/cache`): disposable cache spill; cleared on restart boundaries.

## File rules
- Files are written atomically (write temp, then rename) so a crash never leaves a partial file.
- Sensitive files are encrypted at rest; keys are held by the OS keychain.
- Retention and cleanup follow the data governance rules; exports are user-initiated.
- Plugin archives are validated and signature-checked before extraction.

## File categories
- Logs: rolling, retention-bounded.
- Exports: user-initiated, versioned.
- Workspace snapshots: restorable.
- Plugin archives: signature-checked before extraction.
- Cache spill: disposable, cleared on restart boundaries.

## Storage governance
- Storage, retention, encryption, and audit follow the data governance rules.
- Atomic writes prevent partial files on crash.
- Cleanup is scheduled and retention-aware.
- Paths are resolved against the user or system scope; the renderer never writes system-scope files directly.
- Disk-pressure handling is bounded: cleanup runs before new writes when free space falls below the configured floor.
- Storage locations are versioned with the app; a layout change migrates data under an explicit migration.
- File writes are authenticated by the owning service; no file is written outside its owning domain.
- Corruption detection is explicit: an unreadable file is quarantined and reported, never silently recreated.
- Backups and exports are user-initiated and never scheduled without consent.

## Cross-references
- `./database-schema.md`
- `../knowledge/data-governance.md`
- `../../operations/reliability/runtime-operations.md`
- `../../security/security.md`

## Operational Contract

Defines the file-storage layout and rules for the platform. Structured persistence is owned by `database-schema.md`; this document covers non-database files. Both are governed by data governance.

## Example
A log export is written atomically to the user-scope directory and encrypted before persistence.
