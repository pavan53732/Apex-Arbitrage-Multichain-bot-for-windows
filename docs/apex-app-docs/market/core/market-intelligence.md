---
metadata_schema_version: 1.0
document_id: DOC-0318
title: Market Intelligence
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/core/market-intelligence.md
related_concepts:
  - CONCEPT-0318
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Market Intelligence documentation.
scope: Reference documentation.
---

# Market Intelligence

## Document type
This document is an overview, reference, or index as noted below.

# Market Intelligence

## Purpose
Owns scoring and ranking of market entities used by strategy and execution decisions.

## Ownership
- Owns token, pair, chain, DEX, and opportunity scoring.
- Consumes canonical market data from `./market-data.md`.

## Scope
- Token scoring.
- Pair scoring.
- Chain scoring.
- DEX scoring.
- Opportunity detection and ranking.
- Confidence, volatility, trend, correlation, volume, liquidity health, and risk scoring.

## Shared contract
Every intelligence module defines algorithm, inputs, outputs, ranking criteria, thresholds, configuration, monitoring, and validation.

## Scoring lifecycle
Snapshot -> FeatureExtracted -> Scored -> Ranked -> Published -> Expired.

### Transition rules
- Snapshot -> FeatureExtracted when normalized inputs are transformed into feature vectors.
- FeatureExtracted -> Scored when scoring functions are applied.
- Scored -> Ranked when scores are ordered for a given universe and constraints.
- Ranked -> Published when risk and policy gates approve the results.
- Published -> Expired on TTL or on upstream market data invalidation.

## Determinism rules
- For a given snapshot id and configuration, feature extraction and scoring must be deterministic.
- Re-evaluating the same snapshot under the same configuration must produce the same scores and ranking order.
- Ranking ties must be broken by documented stable rules.
- Retry is only allowed for transient computation or data-fetch failures and must not change the result for identical inputs.

## Token scoring
Purpose: rank tokens by tradability and execution quality.
Inputs: liquidity, volume, volatility, concentration, provider trust, age, and asset metadata.
Outputs: token score, reject reasons, trust class.
Validation: reject stale, illiquid, or malformed tokens.

## Pair scoring
Purpose: rank tradable pairs by spread quality and execution feasibility.
Inputs: pair liquidity, spread, volume, volatility, chain health, and fee tier.
Outputs: pair score, route readiness, reject reasons.
Validation: reject pairs below liquidity or freshness threshold.

## Chain scoring
Purpose: classify chains by execution suitability.
Inputs: finality, congestion, fee pressure, RPC health, reorg risk.
Outputs: chain score, health class, reject reasons.
Validation: reject chains below finality or health threshold.

## DEX scoring
Purpose: rank DEXs by route quality and reliability.
Inputs: liquidity, fee tier, latency, historical failure rate, MEV exposure.
Outputs: DEX score, route class, reject reasons.
Validation: reject unsupported or unstable venues.

## Opportunity detection
Purpose: detect candidate trading opportunities from scored market data.
Inputs: token, pair, chain, DEX, and route scores.
Outputs: opportunity candidates, confidence, reason codes.
Validation: only publish when hard gates pass.

## Opportunity ranking
Purpose: order candidate opportunities for execution priority.
Inputs: scores, risk, cost, latency, and confidence.
Outputs: ranked opportunity list, tie-break outputs.
Validation: ranking must be deterministic for identical input set.

## Confidence scoring
Purpose: quantify belief in a candidate opportunity.
Inputs: model quality, data freshness, provider trust, feature agreement.
Outputs: confidence score and rationale.
Validation: confidence cannot override hard risk gates.

## Volatility analysis
Purpose: measure price movement instability.
Inputs: price series and realized volatility.
Outputs: volatility score and regime label.
Validation: thresholds must be versioned.

## Trend analysis
Purpose: determine directional bias.
Inputs: trend features, moving averages, momentum, breakouts.
Outputs: trend score and regime label.
Validation: stale data must fail closed.

## Correlation analysis
Purpose: measure relationship stability across assets or venues.
Inputs: paired return series and correlation windows.
Outputs: correlation score and stability label.
Validation: regime shifts must invalidate prior assumptions.

## Volume analysis
Purpose: quantify participation and support.
Inputs: volume, turnover, windowed averages.
Outputs: volume score and liquidity support label.
Validation: abnormal spikes require separate handling.

## Liquidity health
Purpose: measure whether depth supports execution.
Inputs: depth, slippage curves, spread, pool concentration.
Outputs: liquidity health score and rejection reasons.
Validation: thin liquidity fails safe.

## Risk scoring
Purpose: quantify market-side risk used by higher-level gating.
Inputs: volatility, liquidity, chain health, correlation, spread stability.
Outputs: market risk score and alert class.
Validation: risk output must align with risk-engine thresholds.

## Failure and recovery
- Missing or stale market data must produce a hard reject rather than speculative scores.
- If risk or policy gates fail, no opportunity should be published for execution.
- On computation failure, emit diagnostics and do not publish partial or inconsistent scores.
- If feature extraction fails, the entire snapshot is rejected rather than partially scored.

## Persistence
- Persist snapshot id, feature hashes, scores, ranking, tie-break rule, and reject reasons where backtesting or audit requires it.
- Persist configuration versions used for scoring.
- Persist explanation metadata for traceability.

## Monitoring
- Scoring latency.
- Ranking throughput.
- Candidate rejection rate and reasons.
- Score and ranking drift across releases.
- Feature extraction failures.

## Cross-references
- `./market-data.md`
- `../opportunities/opportunity-detection.md`
- `../opportunities/opportunity-ranking.md`
- `../../execution/trading/strategies.md`
- `../../data/persistence/database-schema.md`
- `../../operations/monitoring/monitoring-observability.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define data freshness, path handling, and reconnect behavior.
