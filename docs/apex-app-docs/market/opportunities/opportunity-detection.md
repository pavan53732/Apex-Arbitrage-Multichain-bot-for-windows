---
metadata_schema_version: 1.0
document_id: DOC-0323
title: Opportunity Detection
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/opportunities/opportunity-detection.md
related_concepts:
  - CONCEPT-0323
dependencies: []
consumers:
  - DOC-0414
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Opportunity Detection documentation.
scope: Reference documentation.
---

# Opportunity Detection

## Document type
Document type: [CONTRACT]

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

## Detection rules
- Candidates below freshness or liquidity thresholds are rejected with a reason code.
- Detection is deterministic for the same input snapshot; AI hints may not override deterministic filters.
- A candidate that violates risk or policy gates is rejected before ranking.
- Reason codes and confidence are recorded for every candidate.
- Every candidate carries its detection inputs and timestamps for traceability.
- A candidate is emitted only when the underlying market snapshot is fresh.
- Detection capacity is bounded; the detector backlogs rather than drops events silently.
- A detection failure is surfaced and the detector retries with backoff.
- Candidate volume is monitored against thresholds; an anomaly triggers review.
- Rejection reasons are queryable by strategy and gate for tuning.
- Policy gates are evaluated in a fixed order; the first failing gate produces the reason.
- A candidate reused across strategies is detected once and shared by reference.
- Detection outputs are versioned with the detector configuration.
- Detector configuration changes are validated before activation.

## Monitoring
Candidate rate, rejection rate, freshness failures.

## Validation
Determinism for same input snapshot.

## Cross-references
- `../core/market-intelligence.md`
- `../core/market-data.md`
- `../../execution/trading/strategies.md`
- `../../execution/risk-policy/risk-engine.md`

For opportunity lifecycle, see `./opportunity-lifecycle.md`.

## Operational Contract

Defines the detection pipeline, signal sources, filters, validation, and promotion into ranking. Market data and risk are owned by their canonical owners; this document detects candidates from them.

## Example
A detected spread passes minimum profit and liquidity checks before scoring; a stale quote is rejected with its freshness reason.
