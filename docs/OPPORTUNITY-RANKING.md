# Opportunity Ranking

## Purpose
Ranks opportunities for execution, AI review, or operator attention.

## Inputs
Detection score, AI confidence, risk score, liquidity score, and execution cost.

## Outputs
Ranked opportunity queue and rationale.

## Algorithm
- Combine profitability, confidence, risk, and route quality.
- Penalize stale, illiquid, or high-risk candidates.
- Produce a deterministic ranking order.

## Cross-references
- `OPPORTUNITY-DETECTION.md`
- `AI-PIPELINE.md`
- `RISK-ENGINE.md`
