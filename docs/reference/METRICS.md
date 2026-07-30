---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Metrics documentation.
scope: Reference documentation.
canonical_source: docs/reference/METRICS.md
---

# Metrics

## Document type
This document is an overview, reference, or index as noted below.

# Metrics

## Purpose
Defines the metric names and categories used across runtime, trading, and desktop monitoring.

## Metric groups
- Trading metrics: spread, fill rate, execution success, realized P&L.
- Runtime metrics: uptime, restart count, queue depth, recovery count.
- Windows metrics: startup time, UI responsiveness, tray status, network reconnects.

## Reporting
- Metrics must be defined with names, units, and alert thresholds.
- Critical metrics must map to alerts or notifications.

## Definitions
- Define each metric with name, unit, source, and alert threshold.
- Include trading, runtime, Windows, and recovery metrics.
