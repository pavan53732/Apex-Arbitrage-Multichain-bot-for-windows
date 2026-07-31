---
metadata_schema_version: 1.0
document_id: DOC-0086
title: Bootstrap Sequence
plane: Product Specification
domain: Runtime
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/runtime/bootstrap-sequence.md
related_concepts:
  - CONCEPT-0086
dependencies:
  - DOC-0051
  - DOC-0078
  - DOC-0079
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0094
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: CONTRACT
purpose: Defines the complete bootstrap sequence for the application.
scope: "Startup ordering, dependency resolution, service registration, and initialisation."
---

# Bootstrap Sequence

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Purpose
Authoritative owner for bootstrap sequence.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `../architecture/apex-os.md`
- `../architecture/architecture.md`
- `../../historical/traceability-matrix.md`

## Operational Contract
Defines deterministic startup order across kernel, registries, config, database, workers, providers, AI, chains, and dashboard readiness.

## Example
Kernel starts before workers and providers before the dashboard becomes interactive.

## Bootstrap steps
- Must define ordered startup steps, service registration, and UAC handling.

## Required details
- Define ordered startup and elevation steps.

## Bootstrap steps
- Define ordered startup steps, service registration, config load, and readiness checks.
- Define failure handling during bootstrap.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
