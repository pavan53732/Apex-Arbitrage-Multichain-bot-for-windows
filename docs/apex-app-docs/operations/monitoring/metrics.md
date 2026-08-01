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
