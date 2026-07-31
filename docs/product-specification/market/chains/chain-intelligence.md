---
metadata_schema_version: 1.0
document_id: DOC-0312
title: Chain Intelligence
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/market/chains/chain-intelligence.md
related_concepts:
  - CONCEPT-0312
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
purpose: Chain Intelligence documentation.
scope: Reference documentation.
---

# Chain Intelligence

## Document type
This document is an overview, reference, or index as noted below.

# Chain Intelligence

## Purpose
Owns chain-level scoring, health classification, and execution suitability for supported networks.

## Why this is separate
Chain scoring has its own lifecycle, health model, and consumer set that do not safely merge into market data or routing without creating duplicated authority.

## Responsibilities
- Score chain health, finality, RPC stability, congestion, and fee conditions.
- Provide deterministic chain suitability scores to routing, execution, and strategy owners.
- Emit alerts for chain degradation and reorg risk.

## Inputs
- RPC health.
- Congestion metrics.
- Finality windows.
- Fee estimates.
- Reorg observations.

## Outputs
- Chain scores.
- Suitability class.
- Reject reasons.
- Health events.

## Cross-references
- `../core/market-data.md`
- `../routing/routing-engine.md`
- `../../execution/transactions/execution-engine.md`
- `../../operations/monitoring-observability.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
