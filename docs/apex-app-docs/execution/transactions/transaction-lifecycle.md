---
metadata_schema_version: 1.0
document_id: DOC-0299
title: Transaction Lifecycle
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/transactions/transaction-lifecycle.md
related_concepts:
  - CONCEPT-0299
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
purpose: Transaction Lifecycle documentation.
scope: Reference documentation.
---

# Transaction Lifecycle

## Document type
Document type: [CONTRACT]

## Purpose
Defines submission, confirmation, replacement, cancellation, and finality handling for chain transactions.

## Ownership
- Owns transaction state, receipt tracking, replacement, cancellation, and finality boundaries.
- Does not own trade ranking or risk policy.

## Transaction rules
- A transaction is submitted with a validated payload and gas policy; submission is recorded.
- Pending transactions are tracked until confirmation or failure.
- Replacement uses explicit nonce bumping and bounded retry limits.
- Cancellation is allowed only before confirmation and is itself a recorded action.
- Finality is determined per chain profile; a reorg moves confirmed state back to pending for reconciliation.

## Persistence and recovery
- Pending state persists across Windows restarts; a restart rehydrates transactions from the store.
- A failed transaction is recorded with its error and a decision to retry or abandon is made by policy.
- Reorg, pending, and failed handling is explicit and surfaced to the execution lifecycle.

## Lifecycle model
- Initial state: `SUBMITTED`.
- Terminal state: `CONFIRMED` or `FAILED`.
- Allowed transitions: submission, pending, confirmation, replacement, cancellation, and finality.
- Forbidden transitions: cancelling a confirmed transaction; replacing without nonce bump.
- Recovery transitions: rehydrate pending state on restart; reorg reconciliation.
- Failure transitions: failed transactions recorded and routed to policy.

## Finality
- Finality follows the chain profile for the executing chain.
- A reorg moves confirmed state back to pending for reconciliation.
- Receipt tracking records confirmations as they arrive.
- Cancellation is recorded and audited like any other transaction action.
- Confirmation depth thresholds are per chain and configured, never implicit.
- A transaction stranded beyond its retry budget is recorded and routed to policy.
- Receipts are persisted with the transaction for audit and reconciliation.

## Cross-references
- `./execution-engine.md`
- `../../data/persistence/database-schema.md`
- `../../market/routing/gas-optimisation.md`
- `../wallet-portfolio/wallet-management.md`

## Operational Contract

This document owns transaction state, receipt tracking, replacement, cancellation, and finality boundaries. Execution mechanics are owned by the execution engine; gas policy by gas optimisation; wallets by wallet management.

## Example
A pending transaction survives a restart, is rehydrated, and is replaced with a nonce bump when gas policy allows.
