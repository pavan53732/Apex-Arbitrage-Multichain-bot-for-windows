# Market Intelligence

## Purpose
Owns scoring and ranking of market entities used by strategy and execution decisions.

## Ownership
- Owns token, pair, chain, DEX, and opportunity scoring.
- Consumes canonical market data from `MARKET-DATA.md`.

## Scope
- Token scoring.
- Pair scoring.
- Chain scoring.
- DEX scoring.
- Opportunity detection and ranking.
- Confidence, volatility, trend, correlation, volume, liquidity health, and risk scoring.

## Responsibilities
- Convert raw market data into deterministic scores.
- Apply hard gates for freshness, liquidity, chain health, and venue health.
- Produce explainable component scores for downstream consumers.
- Expose stable outputs for strategy, AI, and UI consumers.

## Scoring lifecycle
Snapshot -> FeatureExtracted -> Scored -> Ranked -> Published -> Expired.

### Transition rules
- Snapshot -> FeatureExtracted when normalized inputs are transformed into feature vectors.
- FeatureExtracted -> Scored when scoring functions are applied.
- Scored -> Ranked when scores are ordered for a given universe and constraints.
- Ranked -> Published when risk and policy gates approve the results.
- Published -> Expired on TTL or on upstream market data invalidation.

## Idempotency and retry
- For a given snapshot id and configuration, feature extraction and scoring must be deterministic.
- Re-evaluating the same snapshot under the same configuration must produce the same scores and ranking order.
- Retry is only allowed for transient computation or data-fetch failures and must not change the result for identical inputs.

## Failure and recovery
- Missing or stale market data must produce a hard reject rather than speculative scores.
- If risk or policy gates fail, no opportunity should be published for execution.
- On computation failure, emit diagnostics and do not publish partial or inconsistent scores.

## Persistence
- Persist snapshot id, feature hashes, scores, ranking, and reject reasons where backtesting or audit requires it.
- Persist configuration versions used for scoring.

## Monitoring
- Scoring latency.
- Ranking throughput.
- Candidate rejection rate and reasons.
- Score and ranking drift across releases.

## Cross-references
- `MARKET-DATA.md`
- `OPPORTUNITY-DETECTION.md`
- `OPPORTUNITY-RANKING.md`
- `STRATEGIES.md`
- `DATABASE-SCHEMA.md`
- `MONITORING-OBSERVABILITY.md`
