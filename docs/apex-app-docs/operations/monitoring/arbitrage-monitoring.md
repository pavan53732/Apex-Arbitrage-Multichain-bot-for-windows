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
canonical_source: docs/apex-app-docs/operations/monitoring/arbitrage-monitoring.md
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
Document type: [CONTRACT]

## Purpose
Defines monitoring for spread windows, execution latency, fill status, and profitability.

## Ownership
- Owns spread visibility, arbitrage window timing, and per-trade P&L monitoring.
- Does not own execution mechanics or risk limits.

## Monitoring contract
- Live spreads are computed from market data on the monitoring cadence.
- Alert thresholds are operator-configurable and bounded by policy.
- A stale quote is detected and flagged; it is never presented as live.
- Window states are tracked: success, partial success, failed opportunity, and expired window.
- Per-trade P&L is computed from fills and recorded to the decision log.
- Execution latency is measured per leg against the window budget.
- Fill status is tracked per leg from dispatch through confirmation.
- Profitability is measured net of gas and fees on a per-trade basis.
- Spread snapshots are retained for performance analysis.
- A window that exceeds its latency budget is invalidated and monitored as such.
- Degraded market data is flagged before it reaches spread computation.
- Monitoring runs at the cadence required by the performance SLOs.
- Every window outcome maps to a monitoring metric; none are dropped.
- Operators can drill from a metric to the underlying window record.
- Thresholds are validated before activation; an invalid threshold is rejected.
- Alert fatigue is bounded by severity aggregation rules.
- Monitoring data feeds the arbitrage dashboard and notification center.
- A monitoring outage is treated as a risk, per the operations contract.
- Monitoring state survives restart via the persistence layer.

## Dashboards
- Spread visibility and window timing are shown in the monitoring surface.
- Expired and failed windows are visible with their cause, not hidden.

## Cross-references
- `./metrics.md`
- `../../market/opportunities/opportunity-ranking.md`
- `../../performance/performance-slos.md`
- `../../execution/decision-log.md`

## Operational Contract

This document owns arbitrage-specific monitoring: spreads, window timing, fill status, and per-trade P&L. General metrics and health are owned by the metrics and health contracts.

## Example
An expired window is recorded with its expiry cause and shown on the monitoring surface rather than disappearing.
