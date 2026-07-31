---
metadata_schema_version: 1.0
document_id: DOC-0291
title: Order Management
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/order-management.md
related_concepts:
  - CONCEPT-0291
dependencies:
  - DOC-0266
  - DOC-0280
  - DOC-0282
  - DOC-0299
consumers:
  - DOC-0031
  - DOC-0049
  - DOC-0285
  - DOC-0294
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Order Management documentation.
scope: Reference documentation.
---

# Order Management

## Document type
This document is an overview, reference, or index as noted below.

# Order Management

## Purpose
Owns order creation, validation, lifecycle tracking, amendment, cancellation, and reconciliation.

## Ownership
- Owns canonical order records and order state transitions.
- Bridges execution plans to chain transactions and settlement records.

## Responsibilities
- Create canonical order records from execution plans.
- Validate order fields before submission.
- Track order state and exchange/chain acknowledgements.
- Handle amendments, cancellations, and terminal transitions.
- Persist order audit data for reconciliation and reporting.

## State machine
Draft -> Validated -> Placed -> PartiallyFilled -> Filled -> Reconciled.
Draft -> Validated -> Cancelled -> Reconciled.
Draft -> Validated -> Rejected -> Reconciled.
Placed -> Replaced -> Placed.
Placed | PartiallyFilled -> CancelRequested -> Cancelled | Filled.

### Transition rules
- Draft -> Validated only after schema, policy, and risk pre-checks.
- Validated -> Placed only after execution engine approval.
- Placed -> PartiallyFilled when a partial fill is confirmed.
- PartiallyFilled -> Filled on complete fill or settlement completion.
- Any active order -> CancelRequested only when cancellation policy is allowed.
- CancelRequested -> Cancelled only after acknowledgement or irreversible timeout handling.
- Rejected orders are terminal and never broadcast.

## Inputs
- Execution plan.
- Chain transaction updates.
- Fill and receipt events.
- Risk and cancellation signals.

## Outputs
- Order state updates.
- Fill records.
- Cancellation and rejection reasons.
- Reconciliation events.

## Idempotency and retry
- Creating an order with the same plan id and idempotency key must reuse the existing record.
- Cancellation requests must be idempotent.
- Retry must not duplicate fill records or overwrite terminal states.

## Persistence
- Persist order id, plan id, transaction lineage, asset ids, quantities, prices, fees, state, timestamps, and reject reasons.
- Persist fill slices and partial-fill metadata.
- Persist cancellation lineage and reconciliation result.

## Failure and recovery
- If transaction and order states diverge, order reconciliation must reconcile from chain truth.
- Stale or duplicate acknowledgements must be ignored by monotonic state rules.
- Unresolved orders must be surfaced to monitoring and recovery workflows.

## Monitoring
- Order create latency.
- Fill latency.
- Partial fill rate.
- Cancellation success rate.
- Reconciliation backlog.
- State divergence count.

## Cross-references
- `./execution-engine.md`
- `./transaction-lifecycle.md`
- `../data/database-schema.md`
- `./risk-engine.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
