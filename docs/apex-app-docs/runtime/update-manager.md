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
version: 1.1.0
canonical_source: docs/apex-app-docs/runtime/update-manager.md
related_concepts:
  - CONCEPT-0091
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Runtime
type: CONTRACT
purpose: Update Manager documentation.
scope: Reference documentation.
---

# Update Manager

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

## Document type
Document type: [CONTRACT]

## Purpose
Authoritative owner for update manager behavior: application, plugin, prompt, and model updates.

## Scope
Cross-cutting platform governance for update channels, integrity verification, migration, rollback, and update visibility.

## Responsibilities
- Own update handling, rollback, migration, and integrity checks for all update classes.
- Publish update outcomes to the Windows UI so failures are visible.
- Do not own feature behavior; features are owned by their subsystems.

## Update sources
- Application installer and auto-update channel (`canary`, `beta`, `production`).
- Plugin archives (`.aplx`) from the plugin marketplace.
- Prompt packs and model provider endpoints for the AI pipeline.
- Each source is versioned and verified before application.

## Cross-references
- `../architecture/apex-os.md`
- `../architecture/architecture.md`
- `../plugins/plugin-sdk.md`
- `../ai/prompts/prompt-engineering.md`

## Operational Contract
Defines application, plugin, prompt, and model update handling, rollback, migration, and integrity checks.

## Failure Handling

Every update is reversible. An update that cannot be verified is not applied,
and an update that fails after application is rolled back to the last known
good version rather than left partially applied.

| Failure | Detection | Outcome |
| --- | --- | --- |
| Integrity check fails | Signature or checksum verification on the downloaded artifact | The update is discarded before application; the running version is untouched |
| Download incomplete or corrupted | Size or hash mismatch | The artifact is discarded and the update is not attempted |
| Migration fails mid-application | Migration step returns an error | The update is rolled back to the prior version and the migration is reverted as a unit |
| Post-update health check fails | Component fails to start or report healthy after update | Automatic rollback to the last known good version |
| Rollback itself fails | Prior version cannot be restored | The component is held in a stopped state and escalated; a partially updated component is never left running |
| Update source unreachable | Update check cannot contact its source | The check is retried on the normal schedule; an unreachable source is not treated as "no updates available" |

Update outcomes, including discarded and rolled-back updates, are surfaced to
the Windows UI so that a repeatedly failing update is visible rather than
silently retried.

## Example
A plugin update is rolled back after an integrity failure.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-08-02 | Added Failure Handling section defining integrity, migration, health-check, and rollback failure behaviour. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
