# Price Discovery

## Purpose
Defines the canonical algorithm for producing tradable reference prices from market inputs.

## Inputs
Canonical market snapshots, venue quotes, liquidity depth, and freshness state.

## Outputs
Reference price, confidence score, source provenance, and freshness indicator.

## Algorithm
- Prefer freshest valid routeable quotes.
- Exclude stale, inconsistent, or illiquid sources.
- Compute a reference price from validated inputs.
- Attach confidence proportional to source agreement and liquidity quality.

## Validation
Reference price must be reproducible from the same inputs.

## Cross-references
- `MARKET-DATA.md`
- `ROUTING-ENGINE.md`
- `LIQUIDITY-ANALYSIS.md`
