---
metadata_schema_version: 1.0
document_id: DOC-0082
title: Live Architecture Viewer
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/architecture/live-architecture-viewer.md
related_concepts:
  - CONCEPT-0082
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Architecture
type: REFERENCE
purpose: Live Architecture Viewer documentation.
scope: Reference documentation.
---

# Live Architecture Viewer

## Document type
This document is an overview, reference, or index as noted below.

# Live Architecture Viewer

## Purpose
Defines the authoritative live topology and runtime visualization layer for modules, queues, events, and health.

## Scope
Strategies, workers, AI, chains, DEXs, wallets, providers, queues, and event routes.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DISCOVERING
  DISCOVERING --> RENDERING
  RENDERING --> SYNCED
  SYNCED --> STALE
  STALE --> REFRESHING
  REFRESHING --> SYNCED
```

## Failure modes
Stale graph, missing node, invalid edge, render failure.

## Recovery
Refresh topology from kernel, requery registries, and fall back to cached graph.

## Cross-references
- `./apex-kernel.md`
- `./dependency-graph.md`
- `../operations/health-checks.md`
- `../dashboard/ui-dashboard-spec.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
