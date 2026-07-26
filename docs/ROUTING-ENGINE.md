# Routing Engine

## Purpose
Determines optimal execution paths across DEXs, chains, pools, and bridges.

## Responsibilities
- Build route candidates from market data and liquidity analysis.
- Score routes by edge, cost, slippage, gas, latency, and MEV risk.
- Select deterministic best route under configured policy.
- Emit route plan and fallback routes.

## Inputs
- Quotes.
- Liquidity depth.
- Gas state.
- Chain health.
- Bridge constraints.
- Slippage policy.

## Outputs
- Route candidates.
- Selected route.
- Rejection reasons.
- Fallback route set.

## Cross-references
- `docs/DEX-INTEGRATION.md`
- `docs/CHAIN-INTEGRATION.md`
- `docs/LIQUIDITY-ANALYSIS.md`
- `docs/GAS-OPTIMISATION.md`
- `docs/MEV-PROTECTION.md`
