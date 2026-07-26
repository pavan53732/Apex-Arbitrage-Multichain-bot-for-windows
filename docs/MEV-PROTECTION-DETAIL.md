# MEV Protection Detail

## Purpose
Defines the detailed MEV protection behavior required for arbitrage execution.

## Ownership
- Owns private transaction routing, sandwich risk mitigation, and inclusion strategy.
- Does not own general execution policy or gas optimization policy.

## MEV contract
- Must define private mempool handling, relay selection, and fallback behavior.
- Must define simulation checks and protection failure behavior.

## Cross-references
- `MEV-PROTECTION.md`
- `GAS-OPTIMISATION.md`
- `EXECUTION-ENGINE.md`
- `TRANSACTION-LIFECYCLE.md`
