---
metadata_schema_version: 1.0
document_id: DOC-0329
title: Route Scoring Model
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/route-scoring-model.md
related_concepts:
  - CONCEPT-0329
dependencies:
  - DOC-0282
  - DOC-0283
  - DOC-0328
consumers:
  - DOC-0049
  - DOC-0310
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Route Scoring Model documentation.
scope: Reference documentation.
---

# Route Scoring Model

## Document type
This document is an overview, reference, or index as noted below.

# Route Scoring Model

## Purpose
Defines the mathematical scoring model used for route selection.

## Score factors
Profit, confidence, historical success, gas, liquidity, latency, complexity.

## State machine
```mermaid
stateDiagram-v2
  [*] --> GATHERING_INPUTS
  GATHERING_INPUTS --> SCORING
  SCORING --> RANKING
  RANKING --> SELECTING
  SELECTING --> DISPATCHING
```

## Failure modes
Invalid inputs, unstable ranking, stale market data.

## Recovery
Recompute score, refresh data, or fall back to next-best route.

## Cross-references
- `./route-optimization.md`
- `../execution/simulation-engine.md`
- `../execution/risk-engine.md`

## Operational Contract
Defines route features, weights, score calculation, and selection criteria.

## Example
A route with stronger liquidity and lower cost ranks higher.

## Required details
- Define scoring formula, weights, calibration, and drift checks.

## Scoring model
- Define the scoring formula, weights, and normalization inputs.
- Define calibration, regression, and drift detection.
