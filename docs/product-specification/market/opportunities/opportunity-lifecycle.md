---
metadata_schema_version: 1.0
document_id: DOC-0324
title: Opportunity Lifecycle
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/opportunities/opportunity-lifecycle.md
related_concepts:
  - CONCEPT-0324
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
purpose: Opportunity Lifecycle documentation.
scope: Reference documentation.
---

# Opportunity Lifecycle

## Document type
This document is an overview, reference, or index as noted below.

# Opportunity Lifecycle

## Purpose
Defines the lifecycle from detection to archival.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DETECTED
  DETECTED --> VALIDATED
  VALIDATED --> SCORED
  SCORED --> SIMULATED
  SIMULATED --> APPROVED
  APPROVED --> EXECUTED
  EXECUTED --> CLOSED
  CLOSED --> ARCHIVED
```

## Cross-references
- `./opportunity-detection.md`
- `./opportunity-ranking.md`
- `../../execution/trading/trading-lifecycle.md`

## Operational Contract
Defines the lifecycle from discovery through validation, scoring, simulation, approval, execution, closure, and archive.

## Example
An opportunity moves to approval only after scoring and simulation pass configured thresholds.

## Lifecycle model
- Initial state: defined by the lifecycle owner.
- Terminal state: defined by the lifecycle owner.
- Allowed transitions: explicitly listed by the lifecycle owner.
- Forbidden transitions: explicitly listed by the lifecycle owner.
- Recovery transitions: explicitly listed by the lifecycle owner.
- Failure transitions: explicitly listed by the lifecycle owner.
