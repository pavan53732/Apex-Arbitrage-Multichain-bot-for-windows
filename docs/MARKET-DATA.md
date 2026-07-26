# Market Data

## Purpose
This document is the authoritative implementation specification for ingestion, normalization, freshness management, and distribution of market data.

## Responsibilities
- Ingest chain, DEX, pair, token, price, liquidity, and volume data.
- Normalize source-specific payloads into canonical records.
- Maintain freshness and staleness state.
- Publish snapshots and deltas to downstream systems.

## Data model
Market data records must store source, timestamp, asset identifiers, pair identifiers, venue, price, liquidity, volume, and freshness flags.

## Validation
- Reject stale or malformed payloads.
- Deduplicate repeated observations.
- Mark data stale when freshness thresholds expire.

## Monitoring
Freshness age, ingestion latency, source health, normalization failures, and drop rate.

## Cross-references
- `PRICE-DISCOVERY.md`
- `LIQUIDITY-ANALYSIS.md`
- `ROUTING-ENGINE.md`
- `STRATEGIES.md`
- `OPPORTUNITY-DETECTION.md`
- `OPPORTUNITY-RANKING.md`
