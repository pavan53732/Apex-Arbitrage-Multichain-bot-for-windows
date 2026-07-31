---
metadata_schema_version: 1.0
document_id: DOC-0357
title: Performance Targets
plane: Product Specification
domain: Performance
class: Reference
authority: Reference
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/performance/performance-slos.md
related_concepts:
  - CONCEPT-0356
dependencies:
  - DOC-0356
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: Performance Targets documentation.
scope: Reference documentation.
---

# Performance Targets

## Document type
This document is an overview, reference, or index as noted below.

# Performance Targets

## Purpose
Defines measurable response-time, throughput, latency, recovery, and freshness targets.

## Scope
These targets apply to UI, IPC, market data, AI requests, execution, reconciliation, queues, and recovery workflows.

## UI targets
- Initial window render must be responsive without blocking on AI or market warmup.
- Common view transitions must remain fluid under normal market load.
- Critical alerts must surface without noticeable delay.

## IPC targets
- Standard request/response flows must remain low-latency enough for operator interaction.
- Execution-adjacent IPC must not be blocked by non-critical AI enrichment.

## Market and AI targets
- Market freshness must remain within the configured freshness window for scoring.
- Cloud AI latency must fit within operator-visible budgets for the task tier.
- AI cost budgets must be enforced per request class and per session.
- Fallback routing must prefer lower-cost providers when quality and policy allow.

## Execution targets
- Opportunity ranking, route selection, and execution planning must remain bounded by configured latency budgets.
- Execution retries must not multiply latency beyond safe retry policy.
- Reconciliation must complete within a bounded post-transaction window.

## Recovery targets
- Worker restart, failover, and recovery must stay within the configured recovery budget.
- Queue backlog must not exceed the saturation thresholds for sustained periods.
- Emergency stop must take effect immediately from the operator perspective.

## Determinism targets
- Identical input snapshots and configuration must yield identical decisions.
- Any non-deterministic provider behavior must be isolated behind approved fallback policy.

## Monitoring linkage
- Every target must emit a measurable metric and an alert threshold.
- Regression against target baselines must be visible in dashboards and logs.

## Cross-references
- `../operations/monitoring-observability.md`
- `../operations/runtime-operations.md`
- `../ai/ai-pipeline.md`
- `../ai/cloud-ai-integration.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
