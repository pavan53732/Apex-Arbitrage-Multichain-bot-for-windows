---
metadata_schema_version: 1.0
document_id: DOC-0314
title: DEX Intelligence
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/dex/dex-intelligence.md
related_concepts:
  - CONCEPT-0314
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
purpose: Dex Intelligence documentation.
scope: Reference documentation.
---

# DEX Intelligence

## Document type
Document type: [CONTRACT]

## Purpose
Defines DEX-level liquidity, TVL, fees, latency, pools, performance, and supported-token views.

## View content
- Liquidity and TVL per DEX.
- Fee structure and latency.
- Pool counts and supported tokens.
- Historical performance and route quality.

## Arbitrage intelligence
- DEX ranking factors include liquidity depth, fee sensitivity, latency, and historical fill quality.
- Route-quality signals feed arbitrage opportunity detection and ranking.
- A DEX with stale data is excluded from ranking until refreshed.
- Intelligence is deterministic for the same input snapshot.

## Views and refresh
- Liquidity and TVL views refresh on the dashboard cadence and on pool-change events.
- Fee and latency views reflect the current integration state with their timestamp.
- Pool counts and supported tokens are derived from the DEX registry, not duplicated.
- Historical performance views retain the data needed for route-quality analysis.
- A view for a venue without a registry entry is not rendered.
- Data quality is monitored: stale or missing fields are flagged, not silently zeroed.
- Intelligence outputs are consumed read-only by opportunity detection and ranking.
- DEX ranking changes are recorded with their reason for audit.
- Refresh failures degrade the view visibly rather than blocking the command center.
- The intelligence contract is bounded: pricing and execution behavior live in their owners.
- Ranking weights are configuration, validated before use.
- Intelligence refresh latency meets the performance SLO for the surface.
- Views follow the dashboard and design-system contracts.

## Governance
- DEX metadata and registry identity are owned by the DEX registry and integration contracts.
- This document owns the intelligence views derived from them.

## Cross-references
- `../../interfaces/api/domain-model.md`
- `../../operations/monitoring/metrics.md`
- `./dex-registry.md`
- `../opportunities/opportunity-ranking.md`

## Operational Contract

Defines DEX-level liquidity, TVL, fees, latency, pools, performance, and supported-token views. DEX identity is owned by the DEX registry; this document owns the intelligence over it.

## Example
A DEX with high fees and shallow liquidity is ranked below a lower-fee venue for route selection.
