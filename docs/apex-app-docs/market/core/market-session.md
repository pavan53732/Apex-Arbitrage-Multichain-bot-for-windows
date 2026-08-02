---
metadata_schema_version: 1.0
document_id: DOC-0320
title: Market Session
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/market/core/market-session.md
related_concepts:
  - CONCEPT-0320
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Market Session documentation.
scope: Reference documentation.
---

# Market Session

## Document type
Document type: [CONTRACT]

## Purpose
Defines the market condition labels used to guide strategy selection and scheduling.

## Regimes
- Trending.
- Volatile.
- Quiet.
- Congested.
- Recovery.
- High MEV.

## Session semantics
- A session label is derived from the market regime classification and published to consumers.
- Labels are deterministic for the same inputs; a classification change publishes a new session.
- Strategy selection and scheduling consume the current session label.
- A session label is never guessed: an unknown state is labeled unknown, not inferred.
- High-MEV sessions restrict routing and execution per the MEV protection rules.
- Trending sessions favor momentum-aware strategies; volatile sessions tighten slippage guards.
- Quiet sessions suppress high-cost scanning and throttle opportunity detection.
- Congested sessions raise gas-awareness and reduce submission frequency.
- Recovery sessions restore baseline scanning after a disruption.
- A session transition publishes a timestamped event consumed by scheduling.
- Session history is retained for backtesting and regime analysis.
- The current session is exposed in the dashboard's market intelligence panel.
- An operator can view the session label and its classification inputs.
- Session labels never drive financial calculations directly; they gate strategy selection only.
- A classification outage keeps the last valid session with a staleness marker.
- Session semantics change in this document together with the regime classifier contract.
- A high-MEV session raises MEV protection strictness across routing.
- Labels are stable identifiers published through the domain model.

## Cross-references
- `./market-regime-detection.md`
- `./market-intelligence.md`
- `../../execution/trading/strategy-rotation.md`

## Operational Contract

This document owns the market-session labels. Regime classification is owned by market regime detection; this document defines the labels and their consumption.

## Example
A volatile session suppresses quiet-market strategies and raises slippage guards across routing.
