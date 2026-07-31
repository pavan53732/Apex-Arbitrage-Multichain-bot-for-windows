---
metadata_schema_version: 1.0
document_id: DOC-0300
title: Wallet Command Center
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/wallet-command-center.md
related_concepts:
  - CONCEPT-0300
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
purpose: Wallet Command Center documentation.
scope: Reference documentation.
---

# Wallet Command Center

## Document type
This document is an overview, reference, or index as noted below.

# Wallet Command Center

## Purpose
Defines wallet balances, approvals, positions, PnL, gas spent, assets, transaction history, allowance checking, and security alerts.

## Cross-references
- `../interfaces/domain-model.md`
- `../operations/healthchecks.md`


## State Machine
- UNINITIALIZED -> LOCKED -> UNLOCKED -> APPROVING -> SIGNING -> ERROR.
- ERROR -> LOCKED on recovery.
- Signing requires desktop approval.

## Operational Contract
Defines wallet actions, approvals, routing, execution safety, and operational visibility.

## Example
A transfer request requires explicit confirmation before signing.
