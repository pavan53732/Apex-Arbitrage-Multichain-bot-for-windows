---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Slippage Model documentation.
scope: Reference documentation.
canonical_source: docs/SLIPPAGE-MODEL.md
---

# Slippage Model

## Document type
This document is an overview, reference, or index as noted below.

# Slippage Model

## Purpose
Defines how expected slippage is estimated and bounded.

## Ownership
- Owns slippage estimation, slippage budgets, and tolerance checks.
- Feeds routing and execution validation.

## Inputs
- Quote freshness.
- Order size.
- Pool depth.
- Route path.
- Volatility.
- Historical impact data.

## Model rules
- Slippage ceilings are strategy- and route-specific.
- Quotes must be fresh enough for the configured slippage budget.
- Estimated impact plus safety margin must remain below configured limits.
- High volatility increases estimated slippage and can invalidate a route.

## Outputs
- Expected slippage.
- Maximum allowed slippage.
- Reject reason.
- Route safety label.

## Validation
- Reject stale quotes.
- Reject routes whose estimated impact exceeds the configured ceiling.
- Reject if the safety margin cannot be computed.

## Persistence
- Persist model version, route fingerprint, quote hash, estimated slippage, max threshold, and reject reason.

## Monitoring
- Slippage estimate error.
- Slippage rejection count.
- Threshold breach count.

## Cross-references
- `EXECUTION-ENGINE.md`
- `STRATEGIES.md`
- `ROUTING-ENGINE.md`

## Operational Contract
Defines slippage estimation, variables, bounds, calibration, and downstream decision inputs.

## Example
A route is rejected when predicted slippage exceeds the allowed limit.
