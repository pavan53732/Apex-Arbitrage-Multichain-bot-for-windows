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
