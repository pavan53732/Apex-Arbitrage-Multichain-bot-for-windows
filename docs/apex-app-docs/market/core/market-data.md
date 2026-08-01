---
metadata_schema_version: 1.0
document_id: DOC-0317
title: Market Data
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/market/core/market-data.md
related_concepts:
  - CONCEPT-0317
dependencies: []
consumers:
  - DOC-0310
  - DOC-0412
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Market Data documentation.
scope: Reference documentation.
---

# Market Data

## Document type
This document is an overview, reference, or index as noted below.

# Market Data

## Purpose
Owns ingestion, normalization, caching, freshness, and distribution of market data.

## 0. Provider Trust Boundaries

### Data Source Authority
**Market data sources are classified by trust level and authority type:**

| Provider Type | Trust Level | Authority | Execution Role |
|---------------|-------------|-----------|----------------|
| Oracle (Chainlink, Pyth) | HIGH | PRICE_REFERENCE | Validation only |
| DEX Quote (Uniswap, Pancake) | HIGH | EXECUTION_AUTHORITY | Actual trade pricing |
| RPC Provider | MEDIUM | CONNECTIVITY_AUTHORITY | Transaction submission |
| AI Provider | MEDIUM | ANALYSIS_ONLY | Never trading-truth |

### Critical Rule: AI Providers
**AI providers (LLMs, analysis agents) are ANALYSIS-ONLY authority:**
- ✅ Can analyze market trends and patterns
- ✅ Can suggest strategies and opportunities
- ✅ Can explain execution outcomes
- ❌ CANNOT provide authoritative prices
- ❌ CANNOT bypass risk controls
- ❌ CANNOT be source of trading-truth

### Freshness and Stale Data Protection
**All market data must meet freshness requirements:**
- **Tier 1 (CRITICAL):** < 1 minute — required for Phase 3 execution
- **Tier 2 (STANDARD):** < 5 minutes — acceptable for Phase 1/2
- **Tier 3 (STALE):** > 5 minutes — REJECT for all phases

**Stale data circuit breaker:** 3 consecutive stale readings trigger failover to backup provider.

### Disagreement Resolution
**When providers disagree:**
1. Oracle vs DEX quote > 2% deviation: REJECT trade (possible manipulation)
2. Multiple oracles disagree > 3%: Use median, reject outliers
3. RPC provider disagreement: Use fastest healthy RPC
4. AI analysis vs market data: Market data ALWAYS wins

---

## Ownership
- Owns market-snapshot lifecycle, source adapters, and freshness policy.
- Does not own scoring, ranking, or routing.

## Responsibilities
- Ingest price, quote, depth, chain, and venue data from configured providers.
- Normalize source-specific payloads into canonical market snapshots.
- Cache with bounded time-to-live and explicit freshness metadata.
- Publish updates to intelligence, strategy, execution, and monitoring consumers via typed IPC and internal events.

## Data contract
A canonical market snapshot must include: snapshot id, provider id, source timestamp, chain id, venue id, asset ids, pair id, prices, bid/ask depth, liquidity fields, gas context, freshness metadata, validation status, and correlation id.

## Snapshot lifecycle
Raw -> Parsed -> Normalized -> Validated -> Published -> Expired.

### Transition rules
- Raw -> Parsed on successful decode from the provider client.
- Parsed -> Normalized when mapped into canonical entities.
- Normalized -> Validated after schema, range, and sanity checks.
- Validated -> Published after freshness and completeness checks pass.
- Published -> Expired when TTL elapses or an explicit invalidation event is emitted.

## Freshness policy
- Every snapshot must carry source time and ingestion time.
- Freshness thresholds are chain and venue specific.
- Stale snapshots must be rejected before scoring or execution.
- If freshness cannot be determined, the snapshot is treated as stale.

## Idempotency and retry
- The same provider payload and timestamp must yield the same normalized snapshot id.
- Reprocessing an identical payload must not create duplicate durable records.
- Retry is allowed for transient provider or network errors only and must not silently relax validation.
- Duplicate provider delivery must be deduplicated by source id and snapshot hash.

## Failure and recovery
- On decode or mapping failure, emit a validation error and do not publish.
- On downstream publish failure, retries are bounded; unresolved failures must surface to monitoring.
- On provider outage, mark the corresponding market domain as stale and fail closed for dependent consumers.
- On partial provider data, publish nothing until required fields are complete or an explicit partial-data policy allows reduced use.

## Persistence
- Persist canonical snapshots, source ids, timestamps, freshness metadata, validation status, and snapshot hashes where historical analysis is required.
- Persist provider health, provider latency, and error statistics for monitoring and replay.
- Persist explicit invalidation events and stale-domain markers.

## Monitoring
- Snapshot ingest rate.
- Freshness lag per chain and venue.
- Validation failure rate.
- Provider outage and recovery events.
- Deduplication hit rate.
- Partial-data rejection rate.

## Cross-references
- `../routing/routing-engine.md`
- `../routing/liquidity-analysis.md`
- `./market-intelligence.md`
- `../../execution/trading/strategies.md`
- `../../operations/monitoring/monitoring-observability.md`
- `../tokens/token-registry.md`
- `../tokens/oracle-registry.md`
- `../chains/chain-registry.md`
- `../dex/dex-registry.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
