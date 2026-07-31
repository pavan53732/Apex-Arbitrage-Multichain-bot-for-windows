---
metadata_schema_version: 1.0
document_id: DOC-0349
title: Recovery And Failover
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/operations/recovery/recovery-and-failover.md
related_concepts:
  - CONCEPT-0349
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
purpose: Recovery And Failover documentation.
scope: Reference documentation.
---

# Recovery And Failover

## Document type
This document is an overview, reference, or index as noted below.

# Recovery and Failover

## Purpose
Defines crash recovery, service failover, restart sequencing, and operator recovery workflow.

## Ownership
- Owns recovery orchestration when a worker, queue, or service becomes unhealthy.
- Coordinates with runtime operations, monitoring, and persistence owners.

## Responsibilities
- Detect unhealthy services and classify the fault domain.
- Restart, reassign, or fail over work in a bounded sequence.
- Preserve in-flight execution safety during recovery.
- Surface operator actions when automation cannot restore health safely.

## Recovery lifecycle
Detected -> Classified -> Contained -> Restored -> Reconciled -> Released.

### Transition rules
- Detected -> Classified when monitoring confirms failure scope.
- Classified -> Contained when unsafe work is paused or isolated.
- Contained -> Restored when fallback or restart completes.
- Restored -> Reconciled when state is compared against durable truth.
- Reconciled -> Released when the affected subsystem is safe to resume.

## Idempotency and retry
- Recovery actions must be idempotent where possible.
- Repeating a recovery command must not duplicate restarts, reassignments, or writes.
- Retry must stop once the recovery budget is exhausted.

## Failure and recovery boundaries
- Execution, wallet, and risk failures must fail closed until state is reconciled.
- Monitoring or diagnostics failures must not block containment of a production fault.
- Recovery may not release a subsystem until durable state matches live state.

## Persistence
- Persist fault classification, containment decisions, recovery attempts, reconciliation results, and operator overrides.

## Monitoring
- Mean time to contain.
- Mean time to recover.
- Recovery success rate.
- Failover count.
- Unresolved fault count.

## Cross-references
- `../reliability/runtime-operations.md`
- `../reliability/queue-management.md`
- `../../runtime/worker-architecture.md`
- `../monitoring/monitoring-observability.md`
- `../diagnostics/error-handling-and-logging.md`
- `../../../historical/traceability-matrix.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Windows recovery
- Must define service recovery, restart behavior, and in-flight transaction cleanup.

## Required details
- Define restart, failover, and cleanup recovery semantics.

## Recovery rules
- Define restart, failover, and cleanup recovery semantics.
- Define how partial trades and pending txs are resolved.
