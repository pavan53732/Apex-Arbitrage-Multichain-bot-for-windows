# Market Intelligence

## Purpose
Owns scoring and ranking of market entities used by strategy and execution decisions.

## Responsibilities
- Convert raw market data into deterministic scores.
- Apply hard gates for freshness, liquidity, chain health, and venue health.
- Produce explainable component scores for downstream consumers.
- Expose stable outputs for strategy, AI, and UI consumers.

## Data inputs
- Normalized market data.
- Token metadata and pair metadata.
- Chain health and RPC status.
- DEX quotes and pool depth.
- Historical time series where available.

## Outputs
- Scored tokens, pairs, chains, and DEXs.
- Candidate opportunity sets.
- Ranked opportunity sets.
- Score rationale and reject reasons.

## Scoring rules
- Freshness is a hard gate, not a soft preference.
- Liquidity and impact thresholds must be met before an opportunity can rank for execution.
- Risk score and confidence score are separate values and must not be conflated.
- Ranking must be deterministic for identical input snapshots.

## Cross-references
- `MARKET-DATA.md`
- `OPPORTUNITY-DETECTION.md`
- `OPPORTUNITY-RANKING.md`
- `STRATEGIES.md`
- `DATABASE-SCHEMA.md`
