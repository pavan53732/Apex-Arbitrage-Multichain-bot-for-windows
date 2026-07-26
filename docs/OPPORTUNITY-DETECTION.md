# Opportunity Detection

## Purpose
Detects candidate opportunities from market, chain, and strategy inputs.

## Responsibilities
- Ingest market data and token/pair metadata.
- Produce candidate opportunities.
- Reject stale, illiquid, or policy-violating candidates.

## Inputs
Market snapshots, liquidity signals, token/pair scores, chain status, strategy requirements, AI hints.

## Outputs
Candidate list, reason codes, confidence, and timestamps.

## Algorithms
Rule-based filters, freshness gates, and strategy-specific pattern detectors.

## Thresholds
Candidates below freshness or liquidity thresholds are rejected.

## Monitoring
Candidate rate, rejection rate, freshness failures.

## Validation
Determinism for same input snapshot.


## Cross-references
- `MARKET-INTELLIGENCE.md`
- `MARKET-DATA.md`
- `STRATEGIES.md`
- `RISK-ENGINE.md`

For opportunity lifecycle, see `OPPORTUNITY-LIFECYCLE.md`.
## Operational Contract
Defines the detection pipeline, signal sources, filters, validation, and promotion into ranking.

## Example
A detected spread passes minimum profit and liquidity checks before scoring.
