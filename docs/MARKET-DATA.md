# Market Data

## Purpose
Owns ingestion, normalization, caching, freshness, and distribution of market data.

## Interfaces
- IPC: marketdata.snapshot, marketdata.delta, marketdata.refresh, marketdata.stale.
- Depends on chain adapters and observability.

