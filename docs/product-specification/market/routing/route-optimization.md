---
metadata_schema_version: 1.0
document_id: DOC-0328
title: Route Optimization
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/routing/route-optimization.md
related_concepts:
  - CONCEPT-0328
dependencies: []
consumers:
  - DOC-0329
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Route Optimization documentation.
scope: Reference documentation.
---

# Route Optimization

## Document type
This document is an overview, reference, or index as noted below.

# Route Optimization

## Purpose
Defines route gathering, simulation, scoring, selection, execution, and verification.

## State machine
```mermaid
stateDiagram-v2
  [*] --> GATHER_ROUTES
  GATHER_ROUTES --> SIMULATE_EACH
  SIMULATE_EACH --> SCORE
  SCORE --> SELECT_BEST
  SELECT_BEST --> EXECUTE
  EXECUTE --> VERIFY
  VERIFY --> [*]
```

## Scoring
Multi-objective scoring uses profit, gas, slippage, historical success, confidence, and complexity with configurable weights.

## Configuration
- ROUTE_SCORE_WEIGHTS.
- MAX_ROUTES_TO_EVALUATE.
- MIN_PROFIT_THRESHOLD.

## Failure modes
If the best route fails simulation, fallback to the second best and log the failure.

## Cross-references
- `../../execution/simulation/simulation-engine.md`
- `../../execution/transactions/execution-lifecycle.md`
- `../../execution/trading/trading-lifecycle.md`

## Operational Contract
Defines optimization objectives, constraints, scoring, and route comparison logic.

## Example
The optimizer prefers the route with the best net expected return.

## Required details
- Define scoring, validation, replay, and batch optimization behavior.

## Optimization rules
- Define route scoring inputs, validation, replay, and batch optimization behavior.
- Define stale market data handling and route rejection rules.
