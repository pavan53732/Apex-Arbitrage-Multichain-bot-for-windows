# Market Data

## Purpose
Owns ingestion, normalization, caching, freshness, and distribution of market data.

## Responsibilities
- Ingest chain, DEX, pair, token, price, liquidity, and route data.
- Normalize provider-specific payloads into canonical shapes.
- Maintain freshness, TTL, and stale-data rejection rules.
- Publish snapshots to market intelligence, routing, strategy, and execution consumers.

## Data model
- Snapshot id.
- Provider id.
- Chain id.
- Asset ids.
- Quote timestamp.
- Freshness state.
- Integrity hash.

## Rules
- Consumers receive only validated, timestamped snapshots.
- Stale data may be cached for display but cannot gate live execution.

## Cross-references
- `docs/ROUTING-ENGINE.md`
- `docs/LIQUIDITY-ANALYSIS.md`
- `docs/STRATEGIES.md`
- `docs/MARKET-INTELLIGENCE.md`
