---
metadata_schema_version: 1.0
document_id: DOC-0364
title: Metrics
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/monitoring/metrics.md
related_concepts:
  - CONCEPT-0364
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
purpose: Metrics documentation.
scope: Reference documentation.
---

# Metrics

## Document type
Document type: [CONTRACT]

## Purpose
Defines the metric names and categories used across runtime, trading, and desktop monitoring.

## Metric groups
- Trading metrics: spread, fill rate, execution success, realized P&L.
- Runtime metrics: uptime, restart count, queue depth, recovery count.
- Windows metrics: startup time, UI responsiveness, tray status, network reconnects.
- Recovery metrics: failover count, rollback count, heal duration.

## Reporting
- Every metric is defined with name, unit, source, and alert threshold.
- Critical metrics map to alerts or notifications.
- Metric names are stable and namespaced by domain.
- A metric without a defined unit or threshold is not reported as critical.

## Collection rules
- Metrics are collected on a fixed cadence; a gap is recorded, never silently filled.
- Labels are bounded and dimensioned by domain, component, and scope.
- A metric definition is versioned; renaming updates all consumers in the same change.
- Metrics are computed deterministically from the same source events.
- Raw events are retained per the retention policy; aggregates derive from them.
- Alert thresholds are operator-configurable and validated before activation.
- Every alert maps to a notification route per the notification center.
- Metrics are queryable from the monitoring surface and dashboards.
- A metric that no surface consumes is removed or its consumer re-established.
- Metrics never include secrets; sensitive values are excluded at collection.
- Historical metrics support trend and drift analysis.
- Collection overhead is bounded and measured.
- Metric definitions are added here in the same change as their collection.

## Definitions
- Trading: spread (bps), fill rate (%), execution success (%), realized P&L (USD).
- Runtime: uptime (s), restart count, queue depth, recovery count.
- Windows: startup time (ms), UI responsiveness (ms), tray status, network reconnects.

## Cross-references
- `./health-checks.md`
- `./monitoring-observability.md`
- `../../performance/performance-slos.md`

## Operational Contract

This document owns the metric catalog: names, units, sources, and alert thresholds. Measurement and collection are owned by the observability contracts.

## Example
A trading metric is reported as spread in basis points with an alert threshold set by the operator.
