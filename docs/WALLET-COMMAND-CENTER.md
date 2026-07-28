---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Wallet Command Center documentation.
scope: Reference documentation.
canonical_source: docs/WALLET-COMMAND-CENTER.md
---

# Wallet Command Center

## Document type
This document is an overview, reference, or index as noted below.

# Wallet Command Center

## Purpose
Defines wallet balances, approvals, positions, PnL, gas spent, assets, transaction history, allowance checking, and security alerts.

## Cross-references
- `DOMAIN-MODEL.md`
- `HEALTHCHECKS.md`


## State Machine
- UNINITIALIZED -> LOCKED -> UNLOCKED -> APPROVING -> SIGNING -> ERROR.
- ERROR -> LOCKED on recovery.
- Signing requires desktop approval.

## Operational Contract
Defines wallet actions, approvals, routing, execution safety, and operational visibility.

## Example
A transfer request requires explicit confirmation before signing.
