# Cross-Exchange Arbitrage

## Purpose
Defines how arbitrage opportunities are coordinated across multiple exchanges or venues.

## Ownership
- Owns multi-venue arbitrage coordination, leg ordering, and atomicity expectations.
- Does not own provider selection, which belongs to routing and execution owners.

## Execution contract
- Must define opportunity detection, quote comparison, leg sequencing, and failure rollback.
- Must specify partial fill handling and reconciliation rules.

## Cross-references
- `DEX-INTEGRATION.md`
- `EXECUTION-LIFECYCLE.md`
- `TRADING-LIFECYCLE.md`
- `RISK-ENGINE.md`
