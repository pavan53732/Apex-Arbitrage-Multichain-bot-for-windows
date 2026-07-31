---
metadata_schema_version: 1.0
document_id: DOC-0065
title: APEX Kernel
plane: Product Specification
domain: Architecture
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/architecture/apex-kernel.md
related_concepts:
  - CONCEPT-0065
dependencies:
  - DOC-0087
  - DOC-0093
  - DOC-0247
  - DOC-0253
  - DOC-0335
consumers:
  - DOC-0049
  - DOC-0068
  - DOC-0078
  - DOC-0082
  - DOC-0088
  - DOC-0093
  - DOC-0096
  - DOC-0277
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: CONTRACT
purpose: "Defines the runtime kernel that owns service registration, lifecycle, events, health, dependency injection, configuration, and plugin loading."
scope: "Kernel is the root coordination layer beneath the UI, orchestrator, workers, strategies, AI, and blockchain adapters."
---

# Apex Kernel

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Purpose
Defines the runtime kernel that owns service registration, lifecycle, events, health, dependency injection, configuration, and plugin loading.

## State machine
```mermaid
stateDiagram-v2
  [*] --> BOOTING
  BOOTING --> REGISTERING
  REGISTERING --> RESOLVING_DEPENDENCIES
  RESOLVING_DEPENDENCIES --> ACTIVE
  ACTIVE --> DEGRADED
  DEGRADED --> ACTIVE
  ACTIVE --> SHUTTING_DOWN
  SHUTTING_DOWN --> [*]
```

## Responsibilities
The kernel is the root coordination layer beneath the UI, orchestrator, workers, strategies, AI, and blockchain adapters.

## Inputs
Startup config, plugin manifests, service registrations, health signals, and dependency declarations.

## Outputs
Registered services, lifecycle events, dependency bindings, health state, and plugin activation results.

## Failure modes
Dependency resolution failure, plugin load failure, health degradation, and configuration corruption.

## Recovery
Retry registration, isolate failed plugins, fall back to safe defaults, and alert through the observability stack.

## Cross-references
- `../runtime/orchestrator.md`
- `../interfaces/event-bus.md`
- `../runtime/service-registry.md`
- `../operations/healthchecks.md`
- `../plugins/plugin-sdk.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
