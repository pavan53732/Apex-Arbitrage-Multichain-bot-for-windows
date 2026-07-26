# Market Data

## Purpose
Owns ingestion, normalization, caching, freshness, and distribution of market data.

## Ownership
- Owns market-snapshot lifecycle, source adapters, and freshness policy.
- Does not own scoring (see `MARKET-INTELLIGENCE.md`) or routing (see `ROUTING-ENGINE.md`).

## Responsibilities
- Ingest price, quote, depth, chain, and venue data from configured providers.
- Normalize source-specific payloads into canonical market snapshots.
- Cache with bounded time-to-live and explicit freshness metadata.
- Publish updates to intelligence, strategy, and execution consumers via typed IPC and internal events.

## Snapshot lifecycle
Raw -> Parsed -> Normalized -> Validated -> Published -> Expired.

### Transition rules
- Raw -> Parsed on successful decode from the provider client.
- Parsed -> Normalized when mapped into canonical entities (assets, pairs, venues, chains).
- Normalized -> Validated after schema, range, and sanity checks.
- Validated -> Published after freshness and completeness checks pass.
- Published -> Expired when TTL elapses or an explicit invalidation event is emitted.

## Idempotency and retry
- The same provider payload and timestamp must yield the same normalized snapshot id.
- Reprocessing an identical payload must not create duplicate durable records.
- Retry is allowed for transient provider or network errors only and must not silently relax validation.

## Failure and recovery
- On decode or mapping failure, emit a validation error and do not publish.
- On downstream publish failure, retries are bounded; unresolved failures must surface to monitoring.
- On provider outage, mark the corresponding market domain as stale and fail closed for dependent consumers.

## Persistence
- Persist canonical snapshots, source ids, timestamps, freshness metadata, and validation status where historical analysis is required.
- Persist provider health and error statistics for monitoring.

## Monitoring
- Snapshot ingest rate.
- Freshness lag per chain and venue.
- Validation failure rate.
- Provider outage and recovery events.

## Cross-references
- `ROUTING-ENGINE.md`
- `LIQUIDITY-ANALYSIS.md`
- `MARKET-INTELLIGENCE.md`
- `STRATEGIES.md`
- `MONITORING-OBSERVABILITY.md`
