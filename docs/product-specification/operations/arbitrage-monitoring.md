---
metadata_schema_version: 1.0
document_id: DOC-0343
title: Arbitrage Monitoring
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/arbitrage-monitoring.md
related_concepts:
  - CONCEPT-0343
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: REFERENCE
purpose: Arbitrage Monitoring documentation.
scope: Reference documentation.
---

# Arbitrage Monitoring

## Document type
This document is an overview, reference, or index as noted below.

# Arbitrage Monitoring

## Purpose
Defines monitoring for spread windows, execution latency, fill status, and profitability.

## Ownership
- Owns spread visibility, arbitrage window timing, and per-trade P&L monitoring.
- Does not own execution mechanics or risk limits.

## Monitoring contract
- Must define live spread calculation, alert thresholds, and stale quote detection.
- Must define success, partial success, failed opportunity, and expired window states.

## Cross-references
- `./monitoring/metrics.md`
- `../market/opportunities/opportunity-ranking.md`
- `../performance/performance-slos.md`
- `../execution/decision-log.md`

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
