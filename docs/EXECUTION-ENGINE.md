# Execution Engine

## Purpose
Defines chain transaction execution, confirmation, cancellation, and recovery.

## Ownership
- Owns transaction submission and lifecycle coordination.
- Does not own opportunity ranking or high-level trading policy.

## Windows concerns
- Must define wallet signing context, proxy/failure handling, and crash recovery.
- Must define how the engine behaves when the Windows app restarts mid-trade.

## Cross-references
- `TRANSACTION-LIFECYCLE.md`
- `RISK-ENGINE.md`
- `GAS-OPTIMISATION.md`
- `MEV-PROTECTION.md`

## Required details
- Define wallet permissions, proxy, firewall, and crash recovery.
