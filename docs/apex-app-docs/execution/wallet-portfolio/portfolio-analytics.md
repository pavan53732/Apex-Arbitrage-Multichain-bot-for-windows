---
metadata_schema_version: 1.0
document_id: DOC-0292
title: Portfolio Analytics
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/wallet-portfolio/portfolio-analytics.md
related_concepts:
  - CONCEPT-0292
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Portfolio Analytics documentation.
scope: Reference documentation.
---

# Portfolio Analytics

## Document type
Document type: [CONTRACT]

## Purpose
Defines ROI, win rate, profit distribution, drawdown, Sharpe ratio, and comparison analytics.

## Metrics
- ROI and realized PnL.
- Win rate and profit distribution.
- Maximum drawdown.
- Sharpe ratio.
- Strategy contribution and comparison.
- Exposure and risk views.

## Analytics rules
- Metrics are computed from the portfolio and position state; the computation is deterministic.
- Multi-wallet aggregation is supported; each wallet's contribution is attributable.
- Live analytics update on position and market changes; a stale snapshot is labeled stale.
- Reports and exports are generated from the same deterministic metrics.

## Portfolio UI
- Live analytics, export, and widget behavior follow the dashboard contract.
- Presentation in the Windows UI prioritizes critical data: exposure, drawdown, and PnL.

## Reporting
- Reports are generated on demand and on a defined schedule.
- Exports are deterministic and versioned.

## Attribution
- PnL is attributed per strategy, wallet, and chain.
- Drawdown is computed from the equity curve.
- Win rate and profit distribution are period-based.
- Attribution is deterministic: the same state and period produce the same figures.
- Multi-wallet aggregation is attributable down to the wallet level.
- Period boundaries are explicit and documented on the report.
- Benchmark comparison uses a declared benchmark and period.
- Exposure and risk views derive from the risk engine's published state.

## Cross-references
- `../../interfaces/api/domain-model.md`
- `../../operations/monitoring/metrics.md`
- `./portfolio-management.md`
- `../../dashboard/ui-dashboard-spec.md`

## Operational Contract

Defines portfolio metrics, performance attribution, risk views, and reporting outputs. The portfolio and position state are owned by portfolio and position management; this document owns the analytics over them.

## Example
A report shows exposure, realized PnL, drawdown, and strategy contribution, computed deterministically from portfolio state.
