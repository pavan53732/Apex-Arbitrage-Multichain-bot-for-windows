---
metadata_schema_version: 1.0
document_id: DOC-0093
title: Service Registry
plane: Product Specification
domain: Runtime
class: Registry
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/runtime/service-registry.md
related_concepts:
  - CONCEPT-0093
dependencies:
  - DOC-0065
  - DOC-0087
  - DOC-0276
consumers:
  - DOC-0049
  - DOC-0065
  - DOC-0081
  - DOC-0088
  - DOC-0094
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: CONTRACT
purpose: "Defines service registration, discovery, and lifecycle."
scope: Service registry for runtime components.
---

# Service Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Purpose
Defines the canonical registration and lookup mechanism for runtime services.

## Contract
Nothing instantiates services directly; everything registers with the kernel-managed registry.

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
- `../data/registry-system.md`
- `./orchestrator.md`

## Governance Rules
Defines service identity, registration, status, ownership, and versioned service metadata.

## Example
A service entry exposes health, version, and lifecycle state before it is scheduled.

## Required details
- Define SCM mapping, dependencies, recovery, and lookup.

## Registry rules
- Define service names, dependencies, recovery actions, and lookup behavior.
- Define Windows SCM mapping for each registered service.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
