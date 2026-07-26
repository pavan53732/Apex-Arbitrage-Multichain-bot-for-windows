# Wallet Management

## Purpose
Owns wallet onboarding, key boundaries, balance checks, approvals, signing workflows, and wallet health.

## State machine
Unconfigured -> Imported | Created | Connected -> Ready -> Signing -> Busy -> Error -> Recovery.

## Interfaces
- IPC: wallet.connect, wallet.validate, wallet.sign, wallet.balance, wallet.approve.
- Depends on security, configuration, chain, and transaction lifecycle.

