---
metadata_schema_version: 1.0
document_id: DOC-0096
title: Service Lifecycle
plane: Product Specification
domain: Runtime
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/runtime/service-lifecycle.md
related_concepts:
  - CONCEPT-0096
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Runtime
type: REFERENCE
purpose: Service Lifecycle documentation.
scope: Reference documentation.
---

# Service Lifecycle

## Document type
This document is an overview, reference, or index as noted below.

# Service Lifecycle

## Purpose
Defines the canonical lifecycle for all services.

## State machine
```mermaid
stateDiagram-v2
  [*] --> REGISTERED
  REGISTERED --> INITIALIZING
  INITIALIZING --> STARTING
  STARTING --> HEALTHY
  HEALTHY --> PAUSED
  PAUSED --> RESTARTING
  RESTARTING --> STARTING
  HEALTHY --> STOPPING
  STOPPING --> DISPOSED
```

## Cross-references
- `../architecture/apex-kernel.md`
- `./orchestrator.md`
- `../operations/monitoring/health-checks.md`

## Operational Contract
Defines service registration, initialization, start, healthy, paused, restarting, stopping, and disposed transitions.

## Example
A worker service transitions to paused during maintenance.

## Windows service lifecycle
- Must define SCM states and recovery actions.

## Required details
- Define SCM lifecycle states and recovery actions.

## Windows SCM
- Define install, start, stop, restart, and recovery states under Windows SCM.
- Define delayed start and service account behavior.

## Service states
- Define install, start, stop, restart, and recovery states under Windows SCM.
- Define delayed start and service account behavior.

## Service rules
- Define install, start, stop, restart, and recovery states under Windows SCM.
- Define delayed start and service account behavior.

## Lifecycle model
- Initial state: defined by the lifecycle owner.
- Terminal state: defined by the lifecycle owner.
- Allowed transitions: explicitly listed by the lifecycle owner.
- Forbidden transitions: explicitly listed by the lifecycle owner.
- Recovery transitions: explicitly listed by the lifecycle owner.
- Failure transitions: explicitly listed by the lifecycle owner.
