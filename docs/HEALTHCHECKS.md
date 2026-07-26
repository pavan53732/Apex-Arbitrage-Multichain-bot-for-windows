# Healthchecks

## Purpose
Defines runtime and AI health probes plus automated recovery actions.

## Cross-references
- `RUNTIME-OPERATIONS.md`
- `MONITORING-OBSERVABILITY.md`
- `AI-PIPELINE.md`
- `ORCHESTRATOR.md`

## Operational Contract
Defines health probes, status aggregation, thresholds, and degradation semantics for all services.

## Example
An RPC provider marked unhealthy triggers failover and operator alerting.

## Health definitions
- Must define actual health checks, thresholds, and alert outputs.
