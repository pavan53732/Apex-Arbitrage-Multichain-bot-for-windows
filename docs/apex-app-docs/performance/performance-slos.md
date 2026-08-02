---
metadata_schema_version: 1.0
document_id: DOC-0356
title: Performance SLOs
plane: Product Specification
domain: Performance
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/performance/performance-slos.md
related_concepts:
  - CONCEPT-0356
dependencies: []
consumers:
  - DOC-0354
  - DOC-0357
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Performance
type: REFERENCE
purpose: Performance Slos documentation.
scope: Reference documentation.
---

# Performance SLOs

## Document type
Document type: [CONTRACT]

## Purpose
Defines numeric performance targets for core platform paths.

## Targets
- AI inference p95 <= 500ms for small models.
- AI inference p95 <= 2000ms for large models.
- Orchestrator cycle <= 200ms overhead per decision.
- Dashboard refresh <= 100ms to render.
- Execution broadcast <= 3s from EXECUTING to BROADCASTING.
- Simulation <= 500ms per run.
- Budget enforcement must check cost cap before every AI call.

## SLO semantics
- Targets are p95 unless stated otherwise; outliers are measured, not ignored.
- A sustained breach is an incident and triggers the alerting path.
- SLOs are measured by the metrics pipeline and reviewed on a defined cadence.
- Startup, latency, render, and recovery paths have measured baselines.

## Measurement rules
- SLOs are measured from production-like workloads; synthetic numbers are labeled.
- A measurement window is explicit and consistent across surfaces.
- Breach counts and severity are defined per SLO.
- An SLO change is a reviewed change recorded in this document.
- SLOs never include trading decisions; they bound platform paths only.
- Degraded mode is measured separately and never reported as normal performance.
- Alerting thresholds sit below the SLO to catch degradation early.
- SLOs are reviewed on a defined cadence against measured baselines.
- New surfaces declare their SLOs here before release.
- A missed SLO drives a remediation item, not a silent adjustment.
- SLO coverage is tracked by the metrics pipeline per surface.

## Recovery SLOs
- A failed component recovers within its recovery budget or is escalated.
- Degraded mode must not silently meet an SLO meant for normal operation.

## Cross-references
- `../ai/providers/ai-cost-management.md`
- `../operations/monitoring/metrics.md`
- `../operations/monitoring/health-checks.md`

## Operational Contract

Defines numeric performance targets for core platform paths. Metrics are owned by the metrics contract; this document owns the targets measured against them.

## Example
A dashboard render that exceeds 100ms p95 triggers a breach alert and is investigated before the next release.
