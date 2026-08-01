---
metadata_schema_version: 1.0
document_id: DOC-0323
title: Opportunity Detection
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/opportunities/opportunity-detection.md
related_concepts:
  - CONCEPT-0323
dependencies: []
consumers:
  - DOC-0414
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Opportunity Detection documentation.
scope: Reference documentation.
---

# Opportunity Detection

## Document type
This document is an overview, reference, or index as noted below.

# Opportunity Detection

## Purpose
Detects candidate opportunities from market, chain, and strategy inputs.

## Responsibilities
- Ingest market data and token/pair metadata.
- Produce candidate opportunities.
- Reject stale, illiquid, or policy-violating candidates.

## Inputs
Market snapshots, liquidity signals, token/pair scores, chain status, strategy requirements, AI hints.

## Outputs
Candidate list, reason codes, confidence, and timestamps.

## Algorithms
Rule-based filters, freshness gates, and strategy-specific pattern detectors.

## Thresholds
Candidates below freshness or liquidity thresholds are rejected.

## Monitoring
Candidate rate, rejection rate, freshness failures.

## Validation
Determinism for same input snapshot.


## Cross-references
- `../core/market-intelligence.md`
- `../core/market-data.md`
- `../../execution/trading/strategies.md`
- `../../execution/risk-policy/risk-engine.md`

For opportunity lifecycle, see `./opportunity-lifecycle.md`.
## Operational Contract
Defines the detection pipeline, signal sources, filters, validation, and promotion into ranking.

## Example
A detected spread passes minimum profit and liquidity checks before scoring.
