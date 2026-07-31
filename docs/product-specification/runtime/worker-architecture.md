---
metadata_schema_version: 1.0
document_id: DOC-0098
title: Worker Architecture
plane: Product Specification
domain: Runtime
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/runtime/worker-architecture.md
related_concepts:
  - CONCEPT-0098
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Runtime
type: REFERENCE
purpose: Worker Architecture documentation.
scope: Reference documentation.
---

# Worker Architecture

## Document type
This document is an overview, reference, or index as noted below.

# Worker Architecture

## Purpose
Defines worker roles, task execution boundaries, and worker-to-queue relationships.

## Ownership
- Owns worker role definitions and execution boundaries.
- Does not own scheduler policy or queue metadata.

## Worker roles
- Market ingestion worker.
- AI orchestration worker.
- Strategy evaluation worker.
- Execution worker.
- Reconciliation worker.
- Monitoring worker.
- Maintenance worker.

## Responsibilities
- Consume tasks from the appropriate queue.
- Execute a single worker role deterministically.
- Report lifecycle, health, and error state to runtime operations.
- Avoid cross-domain side effects outside the assigned role.

## Worker lifecycle
Created -> Starting -> Ready -> Busy -> Draining -> Stopped.
Failure path: Busy -> Failed -> Recovering -> Ready or Stopped.

### Transition rules
- Created -> Starting when the process initializes.
- Starting -> Ready after dependencies and configuration validate.
- Ready -> Busy after a task is assigned.
- Busy -> Draining on stop, deploy, or maintenance.
- Busy -> Failed on unrecoverable task or process fault.
- Failed -> Recovering when automatic restart or replacement begins.
- Recovering -> Ready only after health checks pass.

## Idempotency and retry
- Worker tasks must be idempotent where retries are permitted.
- A retried task must preserve its correlation id and attempt count.
- Side effects must not occur twice if the same task is replayed.

## Failure and recovery
- A failed worker must be isolated from new task assignment until recovery completes.
- Worker replacement must use the same role definition and compatible configuration.
- If a worker cannot rejoin safely, it must remain stopped until operator review.

## Persistence
- Persist worker role, health state, assigned queue, last heartbeat, and recovery metadata.

## Monitoring
- Worker readiness.
- Busy time.
- Failure count.
- Restart count.
- Heartbeat freshness.

## Cross-references
- `../operations/runtime-operations.md`
- `../operations/queue-management.md`
- `../operations/recovery-and-failover.md`
- `../operations/monitoring-observability.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Arbitrage workers
- Must define worker roles for scanning, matching, execution, and reconciliation.

## Required details
- Define worker roles and failure boundaries.

## Worker rules
- Define worker roles, isolation, and failure boundaries.
- Define arbitrage-specific workers and desktop support workers.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
