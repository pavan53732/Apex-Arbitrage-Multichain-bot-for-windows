---
metadata_schema_version: 1.0
document_id: DOC-0091
title: Update Manager
plane: Product Specification
domain: Runtime
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/runtime/update-manager.md
related_concepts:
  - CONCEPT-0091
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Runtime
type: CONTRACT
purpose: Update Manager documentation.
scope: Reference documentation.
---

# Update Manager

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Document type
This document is an overview, reference, or index as noted below.

# Update Manager

## Purpose
Authoritative owner for update manager.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `../architecture/apex-os.md`
- `../architecture/architecture.md`

## Operational Contract
Defines application, plugin, prompt, and model update handling, rollback, migration, and integrity checks.

## Example
A plugin update is rolled back after an integrity failure.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
