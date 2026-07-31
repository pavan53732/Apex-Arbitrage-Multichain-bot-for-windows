---
metadata_schema_version: 1.0
document_id: DOC-0347
title: Provider Resilience
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/provider-resilience.md
related_concepts:
  - CONCEPT-0347
dependencies:
  - DOC-0104
  - DOC-0119
  - DOC-0335
  - DOC-0356
consumers:
  - DOC-0049
  - DOC-0119
  - DOC-0342
  - DOC-0351
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Provider Resilience documentation.
scope: Reference documentation.
---

# Provider Resilience

## Document type
This document is an overview, reference, or index as noted below.

# Provider Resilience

## Purpose
Defines provider health checking, failover, capability detection, latency monitoring, and reinstatement.

## State machine
```mermaid
stateDiagram-v2
  [*] --> ACTIVE
  ACTIVE --> HEALTH_CHECK
  HEALTH_CHECK --> UNHEALTHY
  UNHEALTHY --> FAILOVER
  FAILOVER --> RECOVER
  RECOVER --> REINSTATE
  REINSTATE --> ACTIVE
```

## Content
Primary and secondary provider lists are explicitly configured. Health probes run at a fixed interval and compare latency, capability, and availability.

## Configuration
- PRIMARY_PROVIDER.
- SECONDARY_PROVIDERS.
- HEALTH_CHECK_INTERVAL.
- FAILOVER_THRESHOLD.
- FAILBACK_POLICY.

## Failure modes
If all providers fail, enter degraded mode and alert operations.

## Cross-references
- `../ai/ai-provider-manager.md`
- `../ai/ai-gateway.md`
- `./healthchecks.md`
- `../performance/performance-slos.md`

## Operational Contract
Defines provider failover, redundancy, circuit breaking, and recovery behavior.

## Example
A backup provider takes over after repeated timeout errors.

## Required details
- Define provider health, latency, weighting, and circuit breaker behavior.

## Provider rules
- Define health scoring, latency weighting, circuit breakers, and fallback order.
- Define recovery timing after provider failure.
