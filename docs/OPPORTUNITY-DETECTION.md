---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Opportunity Detection documentation.
scope: Reference documentation.
canonical_source: docs/OPPORTUNITY-DETECTION.md
---

# Opportunity Detection

## Document type
This document is an overview, reference, or index as noted below.

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
