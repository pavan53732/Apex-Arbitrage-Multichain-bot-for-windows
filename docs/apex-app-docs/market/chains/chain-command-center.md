---
metadata_schema_version: 1.0
document_id: DOC-0311
title: Chain Command Center
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.1.0
canonical_source: docs/apex-app-docs/market/chains/chain-command-center.md
related_concepts:
  - CONCEPT-0311
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
purpose: Chain Command Center documentation.
scope: Reference documentation.
---

# Chain Command Center

## Document type
Document type: [CONTRACT]

## Purpose
Defines per-chain views for RPC, latency, gas, DEXs, flash loans, oracles, wallet balances, block height, and health.

## View content
- RPC status and latency.
- Gas conditions and fee estimates.
- Supported DEXs and flash-loan venues.
- Oracle health.
- Wallet balances per chain.
- Block height and chain health.

## Behavior
- Each chain view is bound to the chain registry entry and the domain model.
- A chain view reflects live health metrics; a degraded chain is shown as degraded, not healthy.
- Navigation moves between chains without leaving the command center.
- Views refresh on the dashboard cadence and on change events.
- A view for an unsupported chain shows the registry state and is not actionable.
- Gas and fee views present estimates from the gas optimisation owner with their timestamp.
- Flash-loan and DEX views reflect the supported venues from the chain registry.
- Oracle health is shown with its latest observed value and age.
- Block height is compared against the chain's expected cadence; lag is flagged.
- Wallet balances are read-only surfaces from wallet management.
- Each view exposes its refresh time; a stale view is labeled stale.
- Alerts raised by chain intelligence surface in the relevant chain view.
- Operator actions on a chain view route through the execution safety layer.
- The command center never mutates chain or registry state directly.
- RPC latency is shown against the performance SLO for the chain.
- View layout follows the design system and the dashboard panel contract.
- Every view is reachable from navigation per the user flows.

## Cross-references
- `../../interfaces/api/domain-model.md`
- `../../operations/monitoring/metrics.md`
- `../../operations/monitoring/health-checks.md`
- `./chain-registry.md`

## Operational Contract

This document owns the per-chain command-center surface. Chain health and metrics are owned by chain intelligence and monitoring; this surface renders them for operators.

## Example
An operator opens the Polygon view and sees RPC latency, gas, DEX coverage, and wallet balances; a degraded RPC is flagged in the view.
