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
canonical_source: docs/product-specification/performance/performance-slos.md
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
- `../ai/ai-cost-management.md`
- `../operations/monitoring/metrics.md`
- `../operations/health-checks.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define startup, latency, render, and recovery SLOs.
