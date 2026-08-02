---
metadata_schema_version: 1.0
document_id: DOC-0294
title: Position Management
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/execution/wallet-portfolio/position-management.md
related_concepts:
  - CONCEPT-0294
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Position Management documentation.
scope: Reference documentation.
---

# Position Management

## Document type
Document type: [CONTRACT]

## Purpose
Tracks active positions, exposure, cost basis, unrealized and realized PnL, and position risk.

## Responsibilities
- Maintain position open, scale, reduce, close, and reconcile lifecycle.
- Tie positions to orders and transactions.
- Publish position risk and accounting state.

## Position lifecycle
- A position is opened by an order and tied to its transactions for accounting.
- Positions scale up and reduce in steps, each step recorded against the position.
- Closure settles realized PnL and removes the position from active exposure.
- Reconciliation after a failed or partial trade recomputes position state and surfaces drift.

## Risk and sizing
- Position sizing follows risk policy; a position that breaches exposure limits is reduced.
- Cost basis and PnL are computed deterministically from transaction records.
- Position risk is published to the risk engine and the portfolio snapshot.

## Position records
- Open, scale, reduce, close, and reconcile actions are recorded against the position.
- Every position is tied to its orders and transactions.

## Accounting
- Cost basis is maintained per position.
- Unrealized PnL uses current prices; realized PnL settles on close.

## Risk
- Position risk is published to the risk engine.
- An exposure breach triggers reduction per policy.

## Reconciliation
- Reconciliation runs after failed or partial trades and recomputes position state from transaction records.
- Drift between the position model and the portfolio snapshot is surfaced, never silently absorbed.
- Closed positions retain their accounting history for audit and analytics.
- Position records are queryable by wallet, chain, and strategy.
- Every lifecycle action is recorded with its actor and timestamp.
- A position that cannot be priced is labeled stale rather than marked current.
- Open positions are reported with cost basis and unrealized PnL in the same units.
- Scale and reduce steps are validated against risk policy before applying.

## Cross-references
- `../transactions/order-management.md`
- `./portfolio-management.md`
- `../risk-policy/risk-engine.md`

## Operational Contract

Defines position creation, sizing, adjustment, risk limits, and closure handling. Orders and transactions are owned by the order and execution lifecycle; this document tracks the resulting positions.

## Example
A position is reduced when exposure breaches policy, and the reduction is recorded and reconciled against the portfolio.
