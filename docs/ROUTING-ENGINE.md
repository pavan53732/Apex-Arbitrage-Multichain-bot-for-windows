# Routing Engine

## Document type
This document is an overview, reference, or index as noted below.

# Routing Engine

## Purpose
Determines optimal execution paths across DEXs, chains, pools, and bridges.

## Ownership
- Owns route construction, route ranking, and route invalidation rules.
- Produces execution-ready route plans for the execution engine.

## Responsibilities
- Build route candidates from market data and execution constraints.
- Rank routes by edge, gas, slippage, liquidity, finality, and MEV exposure.
- Reject invalid, stale, or unsafe routes.
- Produce route plans with stable fingerprints and validation metadata.

## Route lifecycle
Candidate -> Scored -> Validated -> Approved -> Bound -> Invalidated -> Replaced.

### Transition rules
- Candidate -> Scored after quote and liquidity analysis completes.
- Scored -> Validated after gas, slippage, MEV, and chain checks pass.
- Validated -> Approved only after execution-risk gating passes.
- Approved -> Bound when the route is attached to an execution plan.
- Bound -> Invalidated when market, chain, or wallet state changes materially.
- Any route can move to Replaced only via a new validated route with a new fingerprint.

## Inputs
- Market data.
- Liquidity analysis.
- Gas estimates.
- Slippage model.
- MEV protection signals.
- Chain suitability and wallet readiness.

## Outputs
- Route fingerprints.
- Ranked route candidates.
- Reject reasons.
- Execution-ready route plans.

## Idempotency and retry
- The same input snapshot must yield the same route ranking.
- Re-evaluating a route under unchanged inputs must preserve the same fingerprint.
- Retry of route computation must not mutate state.

## Failure and recovery
- Stale quotes, invalid gas data, or unsafe MEV exposure must reject the route.
- If route validity is lost after binding, execution must revalidate before submission.
- If no safe route exists, return a hard reject rather than a degraded unsafe path.

## Persistence
- Persist route fingerprint, scoring breakdown, reject reasons, chain id, DEX ids, pool ids, and input snapshot hash.
- Persist route invalidation events and replacement lineage.

## Monitoring
- Route compute latency.
- Route rejection rate.
- Route invalidation rate.
- Re-ranking count.
- Fingerprint stability count.

## Cross-references
- `MARKET-DATA.md`
- `LIQUIDITY-ANALYSIS.md`
- `SLIPPAGE-MODEL.md`
- `GAS-OPTIMISATION.md`
- `MEV-PROTECTION.md`
- `EXECUTION-ENGINE.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Routing behavior
- Must define failover, chain changes, and proxy-aware routing.

## Required details
- Define routing failover and proxy-aware decisions.

## Routing rules
- Define route selection, failover, and proxy-aware decision inputs.
- Define handling for changing network conditions.
