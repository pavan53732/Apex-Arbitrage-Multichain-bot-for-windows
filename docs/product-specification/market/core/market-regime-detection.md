---
metadata_schema_version: 1.0
document_id: DOC-0319
title: Market Regime Detection
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/core/market-regime-detection.md
related_concepts:
  - CONCEPT-0319
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
purpose: Market Regime Detection documentation.
scope: Reference documentation.
---

# Market Regime Detection

## Document type
This document is an overview, reference, or index as noted below.

# Market Regime Detection

## Purpose
Defines the classification of market regimes that influence strategy selection and scheduling.

## Regimes
Trending, ranging, high volatility, low liquidity, congestion, panic, recovery.

## State machine
```mermaid
stateDiagram-v2
  [*] --> OBSERVING
  OBSERVING --> CLASSIFYING
  CLASSIFYING --> PUBLISHING
  PUBLISHING --> MONITORING
  MONITORING --> OBSERVING
```

## Failure modes
Misclassification, stale classification, noisy signal.

## Recovery
Reclassify with fresh data and reduce confidence if unstable.

## Cross-references
- `./market-intelligence.md`
- `../../execution/trading/strategy-rotation.md`
- `../../runtime/orchestrator.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
