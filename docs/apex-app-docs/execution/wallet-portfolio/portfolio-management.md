---
metadata_schema_version: 1.0
document_id: DOC-0293
title: Portfolio Management
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/execution/wallet-portfolio/portfolio-management.md
related_concepts:
  - CONCEPT-0293
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Portfolio Management documentation.
scope: Reference documentation.
---

# Portfolio Management

## Document type
Document type: [CONTRACT]

## Purpose
Aggregates balances and positions into portfolio value, allocation, and utilization snapshots.

## Responsibilities
- Compute total value, allocation, exposure, and utilization.
- Aggregate positions and wallet balances.
- Feed risk, reporting, and UI dashboards.

## Portfolio rules
- Portfolio aggregation spans multiple wallets and chains; every value is chain- and asset-aware.
- Allocation and exposure are computed deterministically and fed to the risk engine.
- A rebalance is blocked if exposure exceeds policy; the block is recorded with its reason.
- Reconciliation after failed or partial trades recomputes the snapshot and surfaces drift.
- Utilization compares deployed capital against available capital per strategy and wallet.

## Snapshot semantics
- Snapshots are point-in-time and labeled with their timestamp.
- A stale snapshot is never served as current to the UI or risk engine.

## Snapshot content
- Total value.
- Allocation by asset, chain, and strategy.
- Exposure and utilization.
- Position counts and wallet balances.

## Consistency
- Snapshots are computed atomically from position and balance state.
- Drift after partial trades triggers reconciliation.
- Snapshot timestamps are explicit and never implied.
- A rebalance applies only when the post-state remains within policy bounds.
- Utilization compares deployed capital against available capital per strategy and wallet.
- Portfolio state is the single input to risk, reporting, and UI dashboards.
- A wallet that cannot be priced is excluded with a labeled gap, not silently zeroed.
- Snapshot history is retained for analytics and audit.
- Allocation is chain- and asset-aware across all wallets.

## Cross-references
- `./position-management.md`
- `./wallet-management.md`
- `./portfolio-analytics.md`
- `../../market/core/market-data.md`

## Operational Contract

Defines portfolio ownership, allocation, rebalancing, exposure limits, and wallet/strategy bindings. Positions are owned by position management; balances by wallet management; this document aggregates them into portfolio state.

## Example
A portfolio rebalance is blocked if exposure exceeds policy; the snapshot is reconciled after a partial trade completes.
