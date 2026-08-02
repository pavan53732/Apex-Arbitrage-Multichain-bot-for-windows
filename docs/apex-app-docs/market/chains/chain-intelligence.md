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
canonical_source: docs/apex-app-docs/market/chains/chain-intelligence.md
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
Document type: [CONTRACT]

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

## Scoring rules
- Scores are deterministic for the same input snapshot.
- Suitability class is derived from score bands and the chain's feature profile.
- A chain with an active reorg alert is unsuitable for execution.
- Score history is retained for monitoring and alerting.

## Consumer contract
- Routing, execution, and strategy owners consume the suitability score before dispatch.
- A score below the execution floor rejects the chain for that decision.
- Health events are published to monitoring and alerting surfaces.
- A chain under a reorg alert is excluded from execution until the alert clears.
- Scoring inputs are versioned so score history stays reproducible.
- A suitability class change is recorded with its reason and timestamp.

## Cross-references
- `../core/market-data.md`
- `../routing/routing-engine.md`
- `../../execution/transactions/execution-engine.md`
- `../../operations/monitoring/monitoring-observability.md`

## Operational Contract

This document owns chain-level scoring, health classification, and execution suitability. Chain identity lives in the chain registry; market data owns prices. This document classifies chain health for consumers.

## Example
A chain with repeated RPC timeouts is scored unsuitable and excluded from routing until health recovers.
