---
last_updated: 2026-07-29
type: CONTRACT
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Defines the complete bootstrap sequence for the application.
scope: Startup ordering, dependency resolution, service registration, and initialisation.
canonical_source: docs/BOOTSTRAP-SEQUENCE.md
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
- `APEX-OS.md`
- `ARCHITECTURE.md`
- `TRACEABILITY-MATRIX.md`

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
