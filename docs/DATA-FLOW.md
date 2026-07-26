# Data Flow

## Purpose
Defines how data moves across market, trading, AI, risk, execution, persistence, and UI layers.

## Ownership
- Describes end-to-end flow only; message contracts stay in `IPC-PROTOCOL.md` and `API-REFERENCE.md`.

## Cross-references
- `EVENT-FLOW.md`
- `STATE-MANAGEMENT.md`
- `RUNTIME-OPERATIONS.md`

## Operational Contract
Defines the pipeline from raw RPC data through normalization, validation, caching, analytics, AI, and decision support.

## Example
Raw pool data is normalized before reaching opportunity ranking.
