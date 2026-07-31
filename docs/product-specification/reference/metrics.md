---
metadata_schema_version: 1.0
document_id: DOC-0364
title: Metrics
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/reference/metrics.md
related_concepts:
  - CONCEPT-0364
dependencies: []
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0126
  - DOC-0128
  - DOC-0217
  - DOC-0283
  - DOC-0292
  - DOC-0311
  - DOC-0314
  - DOC-0343
  - DOC-0356
  - DOC-0361
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Metrics documentation.
scope: Reference documentation.
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
