---
metadata_schema_version: 1.0
document_id: DOC-0332
title: Token Intelligence
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/token-intelligence.md
related_concepts:
  - CONCEPT-0332
dependencies:
  - DOC-0252
  - DOC-0312
  - DOC-0317
consumers:
  - DOC-0049
  - DOC-0310
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Token Intelligence documentation.
scope: Reference documentation.
---

# Token Intelligence

## Document type
This document is an overview, reference, or index as noted below.

# Token Intelligence

## Purpose
Defines token metadata ingestion, scoring, ranking, caching, and refresh behavior.

## State machine
```mermaid
stateDiagram-v2
  [*] --> FETCH_METADATA
  FETCH_METADATA --> COMPUTE_SCORE
  COMPUTE_SCORE --> RANK
  RANK --> CACHE
  CACHE --> REFRESH
  REFRESH --> FETCH_METADATA
```

## Scoring
Combines liquidity, volatility, historical spread, protocol coverage, and DEX availability using configurable weights.

## Configuration
- SCORE_WEIGHTS.
- MIN_SCORE.
- REFRESH_INTERVAL.

## Failure modes
If metadata source fails, use cached values and log a warning.

## Cross-references
- `./market-data.md`
- `./chain-intelligence.md`
- `../interfaces/domain-model.md`

## Operational Contract
Defines token enrichment, scoring inputs, validation, metadata aggregation, and downstream usage.

## Example
An enriched token record includes symbol, chain, liquidity, risk, and discovery source.
