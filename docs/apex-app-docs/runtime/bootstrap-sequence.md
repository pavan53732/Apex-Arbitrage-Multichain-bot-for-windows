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
version: 1.1.0
canonical_source: docs/apex-app-docs/runtime/bootstrap-sequence.md
related_concepts:
  - CONCEPT-0086
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
purpose: Defines the complete bootstrap sequence for the application.
scope: "Startup ordering, dependency resolution, service registration, and initialisation."
---

# Bootstrap Sequence

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

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

## Failure Handling

Bootstrap is ordered and fails fast. Because later stages depend on earlier ones,
a stage that cannot complete stops the sequence rather than allowing a partially
initialised system to accept work.

| Failure | Stage | Outcome |
| --- | --- | --- |
| Kernel fails to initialise | Kernel | Startup aborts; no dependent stage is attempted |
| Configuration invalid or unreadable | Config load | Startup aborts with a configuration error; no implicit defaults are substituted for required values |
| Database unavailable or migration fails | Database | Startup aborts; the application does not run against an unmigrated schema |
| Registry population fails | Registries | Startup aborts, as downstream resolution would silently return empty results |
| Worker pool fails to start | Workers | Startup aborts; the system does not accept work it cannot schedule |
| Provider initialisation fails | Providers | Degraded start: unavailable providers are marked unavailable and the sequence continues, since providers are individually optional |
| Chain adapter unavailable | Chains | Degraded start: the affected chain is withdrawn while other chains proceed |
| UAC elevation declined | Service registration | Startup continues without elevated features; elevation-dependent capabilities are disabled rather than silently skipped |
| Readiness check fails | Dashboard readiness | The dashboard remains non-interactive; it never presents itself as ready over an unready runtime |

Aborted startups report the failing stage and cause through the Windows event
path, so a failed bootstrap is diagnosable without attaching a debugger. Stages
that abort do not leave partially registered services behind: registration is
unwound in reverse order.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-08-02 | Added Failure Handling section defining fail-fast and degraded-start behaviour per bootstrap stage. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
