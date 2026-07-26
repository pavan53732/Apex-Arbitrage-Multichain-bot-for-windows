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
