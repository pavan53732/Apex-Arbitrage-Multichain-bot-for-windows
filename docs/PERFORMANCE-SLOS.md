---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Performance Slos documentation.
scope: Reference documentation.
canonical_source: docs/PERFORMANCE-SLOS.md
---

# Performance Slos

## Document type
This document is an overview, reference, or index as noted below.

# Performance SLOs

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

## Cross-references
- `AI-COST-MANAGEMENT.md`
- `METRICS.md`
- `HEALTHCHECKS.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define startup, latency, render, and recovery SLOs.
