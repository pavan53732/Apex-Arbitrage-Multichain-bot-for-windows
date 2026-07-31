---
metadata_schema_version: 1.0
document_id: DOC-0298
title: Trading Lifecycle
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.0
canonical_source: docs/product-specification/execution/trading/trading-lifecycle.md
related_concepts:
  - CONCEPT-0298
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Trading Lifecycle documentation.
scope: Reference documentation.
---

# Trading Lifecycle

## Document type
This document is a reference.

# Trading Lifecycle

## Purpose
Defines the canonical trade state machine.

## State machine
```mermaid
stateDiagram-v2
  [*] --> IDLE
  IDLE --> SCANNING
  SCANNING --> OPPORTUNITY_DETECTED
  OPPORTUNITY_DETECTED --> RISK_CHECK
  RISK_CHECK --> SIMULATING
  SIMULATING --> EXECUTING
  EXECUTING --> VERIFYING
  VERIFYING --> SETTLED
  VERIFYING --> FAILED
  FAILED --> RETRY
  RETRY --> SCANNING
  SETTLED --> IDLE
```

## Allowed transitions
- IDLE -> SCANNING.
- SCANNING -> OPPORTUNITY_DETECTED.
- OPPORTUNITY_DETECTED -> RISK_CHECK.
- RISK_CHECK -> SIMULATING.
- SIMULATING -> EXECUTING.
- EXECUTING -> VERIFYING.
- VERIFYING -> SETTLED or FAILED.
- FAILED -> RETRY.
- RETRY -> SCANNING.

## Forbidden transitions
- EXECUTING -> SETTLED.
- IDLE -> EXECUTING.
- SETTLED -> SCANNING.
- IDLE -> EXECUTING.
- SCANNING -> SETTLED.

## Recovery
- FAILED transitions to RETRY.
- RETRY returns to SCANNING after operator or policy approval.

## Cross-references
- `../../runtime/orchestrator.md`
- `../transactions/execution-lifecycle.md`
- `../risk-policy/risk-engine.md`
- `../simulation/simulation-engine.md`

## Operational Contract
Defines the full trade lifecycle from opportunity to execution, confirmation, reconciliation, and closure.

## Example
Trading pauses if execution confirmation fails.

## Required details
- Define arb scan, match, execute, settle, recover, and expire states.

## Arb flow
- Scan, rank, validate, execute, reconcile, expire, and recover must be explicit states or transitions.

## Lifecycle model
- Initial state: defined by the lifecycle owner.
- Terminal state: defined by the lifecycle owner.
- Allowed transitions: explicitly listed by the lifecycle owner.
- Forbidden transitions: explicitly listed by the lifecycle owner.
- Recovery transitions: explicitly listed by the lifecycle owner.
- Failure transitions: explicitly listed by the lifecycle owner.

## Initial state
- IDLE.

## Terminal state
- SETTLED.

## Recovery transitions
- FAILED -> RETRY.
- RETRY -> SCANNING.

## Failure transitions
- VERIFYING -> FAILED.
- EXECUTING -> FAILED.
- SIMULATING -> FAILED.
