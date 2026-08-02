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
version: 1.1.0
canonical_source: docs/apex-app-docs/market/tokens/token-intelligence.md
related_concepts:
  - CONCEPT-0332
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Token Intelligence documentation.
scope: Reference documentation.
---

# Token Intelligence

## Document type
Document type: [CONTRACT]

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
- `SCORE_WEIGHTS`.
- `MIN_SCORE`.
- `REFRESH_INTERVAL`.

## Intelligence rules
- Metadata is enriched with source provenance; a record without provenance is not served.
- A token below `MIN_SCORE` is ranked low and excluded from execution-facing surfaces.
- Scores and rankings are deterministic for the same inputs.
- If a metadata source fails, cached values are used and a warning is logged; a stale cache is labeled stale.
- Enriched records include symbol, chain, liquidity, risk, and discovery source.
- Score weights are configuration, validated before use.
- Refresh failures degrade the surface visibly rather than blocking consumers.
- Intelligence output is consumed read-only by detection and ranking.
- Token identity is owned by the token registry; this document derives intelligence from it.

## Failure modes
If metadata source fails, use cached values and log a warning.

## Cross-references
- `../core/market-data.md`
- `../chains/chain-intelligence.md`
- `../../interfaces/api/domain-model.md`
- `./token-registry.md`

## Operational Contract

Defines token enrichment, scoring inputs, validation, metadata aggregation, and downstream usage. Token identity is owned by the token registry; this document owns the intelligence derived from it.

## Example
An enriched token record includes symbol, chain, liquidity, risk, and discovery source, and is ranked below `MIN_SCORE` is withheld from execution surfaces.
