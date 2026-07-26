# Market Intelligence

## Purpose
Owns scoring and ranking of tokens, pairs, chains, DEXs, and opportunities using deterministic market intelligence features.

## Responsibilities
- Token scoring.
- Pair scoring.
- Chain scoring.
- DEX scoring.
- Opportunity detection and ranking.
- Confidence, volatility, trend, correlation, volume, and liquidity health scoring.
- Risk scoring inputs for strategy and execution gates.

## Deterministic rules
- Output must be deterministic for the same market snapshot and configuration.
- Live market data always overrides stale derived signals.
- AI may assist with explanation, but may not override hard gates.
- Ranking must be reproducible from stored feature snapshots.

## Data model
- Feature snapshot id.
- Asset ids.
- Pair ids.
- Chain id.
- DEX id.
- Scoring feature set.
- Score version.
- Ranking timestamp.

## Cross-references
- `docs/MARKET-DATA.md`
- `docs/OPPORTUNITY-DETECTION.md`
- `docs/OPPORTUNITY-RANKING.md`
- `docs/PAIR-DISCOVERY.md`
- `docs/TOKEN-DISCOVERY.md`
- `docs/PRICE-DISCOVERY.md`
