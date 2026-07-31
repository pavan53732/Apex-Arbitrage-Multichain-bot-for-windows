---
metadata_schema_version: 1.0
document_id: DOC-0313
title: Chain Rotation
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/market/chains/chain-rotation.md
related_concepts:
  - CONCEPT-0313
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Chain Rotation documentation.
scope: Reference documentation.
---

# Chain Rotation

## Document type
This document is an overview, reference, or index as noted below.

# Chain Rotation

## Purpose
Defines how configured chains are scored, prioritized, and allocated scanning capacity.

## State machine
```mermaid
stateDiagram-v2
  [*] --> SCANNING
  SCANNING --> SCORING
  SCORING --> PRIORITIZING
  PRIORITIZING --> ALLOCATING
  ALLOCATING --> MONITORING
  MONITORING --> SCANNING
```

## Scoring
Factors include gas price, latency, opportunity density, and historical reliability with configurable weights.

## Configuration
- CHAIN_WEIGHTS.
- MIN_GAS_LIMIT.
- ALLOCATION_QUANTUM.

## Failure modes
If a chain is unreachable, demote it and fallback to the next best chain.

## Cross-references
- `./chain-registry.md`
- `../../runtime/orchestrator.md`
- `../../operations/monitoring/health-checks.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
