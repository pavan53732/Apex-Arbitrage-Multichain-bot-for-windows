---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Provider Resilience documentation.
scope: Reference documentation.
canonical_source: docs/PROVIDER-RESILIENCE.md
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
- `ai/providers/AI-PROVIDER-MANAGER.md`
- `ai/runtime/AI-GATEWAY.md`
- `operations/HEALTHCHECKS.md`
- `performance/PERFORMANCE-SLOS.md`

## Operational Contract
Defines provider failover, redundancy, circuit breaking, and recovery behavior.

## Example
A backup provider takes over after repeated timeout errors.

## Required details
- Define provider health, latency, weighting, and circuit breaker behavior.

## Provider rules
- Define health scoring, latency weighting, circuit breakers, and fallback order.
- Define recovery timing after provider failure.
