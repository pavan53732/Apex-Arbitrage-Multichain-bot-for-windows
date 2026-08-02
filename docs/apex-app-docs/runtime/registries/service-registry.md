---
metadata_schema_version: 1.0
document_id: DOC-0093
title: Service Registry
plane: Repository Operating Model
domain: Registries
class: Registry
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/runtime/registries/service-registry.md
related_concepts:
  - CONCEPT-0093
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
purpose: "Defines service registration, discovery, and lifecycle."
scope: Service registry for runtime components.
---

# Service Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

## Purpose
Defines the canonical registration and lookup mechanism for runtime services.

## Contract
Nothing instantiates services directly; everything registers with the kernel-managed registry.

## Registration contract
- Service identifiers are unique, stable, and versioned; a duplicate registration is rejected.
- Every entry records health, version, lifecycle state, and declared dependencies.
- Lookup returns the current registration and never resolves a retired or suspended service as healthy.
- A service is schedulable only after its dependencies are available.

## Windows SCM mapping
- Desktop-mode services register with the in-process registry.
- Service-mode components map to Windows Service Control Manager entries with matching names and start types.
- SCM start type and failure recovery actions are declared in the service registration.

## State machine
```mermaid
stateDiagram-v2
  [*] --> UNREGISTERED
  UNREGISTERED --> REGISTERING
  REGISTERING --> AVAILABLE
  AVAILABLE --> SUSPENDED
  SUSPENDED --> AVAILABLE
  AVAILABLE --> RETIRED
```

## Validation
Service identifiers must be unique, stable, and versioned.

## Failure modes
Duplicate registration, stale service reference, unavailable dependency, version mismatch.

## Recovery
Unregister stale services, rebind dependencies, and rehydrate from kernel state.

## Cross-references
- `../architecture/apex-kernel.md`
- `../data/registries/registry-system.md`
- `./orchestrator.md`

## Governance Rules
Defines service identity, registration, status, ownership, and versioned service metadata.

## Example
A service entry exposes health, version, and lifecycle state before it is scheduled.

## Registry rules
- Define service names, dependencies, recovery actions, and lookup behavior.
- Define Windows SCM mapping for each registered service.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-08-02 | Expanded canonical content: replaced placeholder directives and generic boilerplate with grounded ownership, rules, lifecycle, failure, and cross-reference detail. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
