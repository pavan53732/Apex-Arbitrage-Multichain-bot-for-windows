# Asset Management

## Purpose
Owns canonical asset metadata, identifiers, decimals, display symbols, and chain-specific asset normalization.

## Responsibilities
- Maintain canonical asset registry across chains.
- Resolve symbol collisions and wrapped asset aliases.
- Validate asset metadata before it is used in execution or display.
- Emit change events when asset metadata is updated.

## Data model
- Asset id.
- Chain id.
- Contract address or native marker.
- Symbol.
- Name.
- Decimals.
- Display precision.
- Alias set.
- Verification status.

## Validation rules
- Duplicate canonical ids are rejected.
- Conflicting symbols must be resolved with chain-aware aliases.
- Unknown decimals block execution until verified.

## Cross-references
- `MARKET-DATA.md`
- `PORTFOLIO-MANAGEMENT.md`
- `WALLET-MANAGEMENT.md`
- `STRATEGIES.md`
- `TOKEN-REGISTRY.md`
