---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Wallet Management documentation.
scope: Reference documentation.
canonical_source: docs/WALLET-MANAGEMENT.md
---

# Wallet Management

## Document type
This document is an overview, reference, or index as noted below.

# Wallet Management

## Purpose
Owns wallet discovery, creation, import, unlock, lock, rotation, permissions, and signing boundaries.

## Responsibilities
- Manage non-custodial wallet metadata and signing sessions.
- Track chain-specific balances and approvals.
- Enforce signer permission boundaries and secret handling rules.

## Cross-references
- `docs/SECURITY.md`
- `docs/PERMISSION-MODEL.md`
- `docs/TRANSACTION-LIFECYCLE.md`
- `TOKEN-REGISTRY.md`

## Operational Contract
Defines wallet inventory, labeling, address hygiene, funding status, and authorization boundaries.

## Example
An active wallet is excluded from trading if its funding falls below threshold.

## Required details
- Define credential storage, hardware wallet integration, and recovery.

## Wallet rules
- Define credential storage, hardware wallet support, and recovery handling on Windows.
- Define clipboard safety and address validation.
