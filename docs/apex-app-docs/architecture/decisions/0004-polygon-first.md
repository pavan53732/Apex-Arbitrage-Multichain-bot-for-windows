---
metadata_schema_version: 1.0
document_id: DOC-0073
title: ADR 0004 Polygon First
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/architecture/decisions/0004-polygon-first.md
related_concepts:
  - CONCEPT-0073
dependencies:
  - DOC-0302
consumers:
  - DOC-0302
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Architecture
type: ADR
purpose: "Records the architectural decision to use Polygon as the first live-network integration after simulation-only MVP phase, motivated by EVM compatibility, lower costs, and ecosystem support."
scope: "Platform scope decision for initial live network selection, multi-chain expansion strategy, and Phase 1 simulation constraints."
---

# ADR 0004: Polygon-First

## Status
**Accepted** | **Version:** 2.0.0 | **Last Updated:** 2026-08-01

## Context
APEX requires a strategic decision on which blockchain network to target for initial live deployment after the simulation-only MVP phase (Phase 1). The decision must balance technical feasibility, cost efficiency, ecosystem support, and future multi-chain expansion.

Phase 1 (current) is simulation/paper-trading only and does not require a live network. However, the architecture must be designed with a clear target for Phase 2 (operator-approved execution) and Phase 3 (autonomous execution).

## Problem
Which blockchain network should APEX target for first live integration, considering:
1. EVM compatibility for existing tooling and developer experience?
2. Transaction costs for arbitrage execution viability?
3. Ecosystem support (DEXes, oracles, RPC providers)?
4. Iteration speed for development and testing?
5. Future multi-chain expansion strategy?

## Decision
**Adopt Polygon as the first intended live-network integration after simulation-only MVP phase.**

### Rationale
Polygon is selected based on:

1. **EVM Compatibility**
   - Full EVM compatibility enables reuse of Ethereum tooling
   - Existing Solidity contracts work without modification
   - Familiar development environment for Ethereum developers

2. **Lower Transaction Costs**
   - Significantly lower gas fees compared to Ethereum mainnet
   - Enables profitable arbitrage with smaller trade sizes
   - Reduces capital requirements for Phase 2/3 operation

3. **Ecosystem Support**
   - Mature DEX ecosystem (Uniswap, SushiSwap, QuickSwap, etc.)
   - Oracle support (Chainlink, Pyth, DIA)
   - Multiple RPC provider options (Alchemy, Infura, QuickNode, etc.)
   - Strong developer community and documentation

4. **Faster Practical Iteration**
   - Lower costs enable more frequent testing and iteration
   - Faster block times (~2 seconds) for quicker feedback
   - Easier to test Phase 2 operator-approved workflows

5. **Multi-Chain Expansion Path**
   - Polygon does not preclude future expansion to other chains
   - Architecture designed for multi-chain from the start
   - Future chains require same provider-trust, risk, execution, and operator-approval controls

### Critical Constraints

1. **Phase 1 remains simulation-only**
   - No live network required for Phase 1
   - Polygon-first applies to Phase 2/3 planning only
   - Simulation uses historical/mainnet data, not live Polygon

2. **Polygon is not the only future network**
   - Multi-chain expansion is expected and planned
   - Future chains: Ethereum, BSC, Arbitrum, Optimism, etc.
   - Each chain requires same safety controls and validation

3. **No exact guarantees**
   - Do not claim exact fee, latency, liquidity, or provider guarantees
   - Actual costs and performance depend on network conditions
   - Provider availability and reliability may change

## Alternatives Considered

### Alternative 1: Ethereum Mainnet First
**Approach:** Deploy to Ethereum mainnet first for maximum liquidity and security.

**Rejected because:**
- High gas fees make small arbitrage unprofitable
- Slower iteration due to cost constraints
- Overkill for Phase 2 initial deployment
- Better suited for later expansion after Polygon validation

### Alternative 2: BSC (Binance Smart Chain) First
**Approach:** Deploy to BSC first for low fees and high throughput.

**Rejected because:**
- Less decentralized than Polygon
- Smaller ecosystem of DEXes and oracles
- More centralized governance concerns
- Polygon offers better balance of decentralization and cost

### Alternative 3: Arbitrum/Optimism First
**Approach:** Deploy to L2 (Arbitrum or Optimism) first.

**Rejected because:**
- More complex bridge and withdrawal mechanics
- Smaller DEX ecosystem at time of decision
- Higher complexity for initial deployment
- Better suited for later expansion

### Alternative 4: Multi-Chain-First Strategy
**Approach:** Launch on multiple chains simultaneously.

**Rejected because:**
- Increases complexity for Phase 2 deployment
- Dilutes focus and testing efforts
- Higher operational overhead
- Better to validate on one chain first, then expand

## Consequences

### Positive
- ✅ Clear target for Phase 2/3 deployment planning
- ✅ Lower costs enable more frequent testing and iteration
- ✅ EVM compatibility simplifies development
- ✅ Mature ecosystem reduces integration risks
- ✅ Multi-chain architecture designed from the start

### Negative
- ⚠️ Polygon has less liquidity than Ethereum mainnet
- ⚠️ Some DEXes or tools may not be available on Polygon
- ⚠️ Future multi-chain expansion requires additional work
- ⚠️ Must maintain Polygon-specific configuration and testing

### Neutral
- Polygon-first is platform scope decision, not application logic
- Implementation must follow provider-trust and risk controls
- Future chain expansion requires same validation and approval process

## Implementation Constraints

1. **Phase 1 remains simulation-only** — no live Polygon integration required
2. **Polygon-first applies to Phase 2/3 planning** — architecture must support Polygon deployment
3. **Multi-chain architecture required** — cannot be Polygon-only
4. **Same safety controls for all chains** — provider-trust, risk, execution, operator-approval
5. **No exact guarantees** — costs, latency, liquidity depend on network conditions

## Related Canonical Specifications

### Detailed Specifications
- `../market/chains/chain-integration.md` — Chain integration strategy and Polygon specifics
- `../market/registries/dex-registry.md` — DEX support on Polygon
- `../market/registries/oracle-registry.md` — Oracle support on Polygon
- `../market/connectivity/rpc-manager.md` — RPC provider support for Polygon

### Architecture
- `../architecture.md` — System architecture and multi-chain design
- `../apex-os.md` — Platform constitution and design principles

## Compliance

**This ADR records existing architecture, does not create new decisions.**

Polygon-first decision is already documented in:
- `../market/chains/chain-integration.md` (Chain integration strategy)
- `../execution/trading/trading-engine.md` (Multi-chain execution design)
- `../execution/risk-policy/risk-engine.md` (Risk controls for all chains)

This ADR formalizes the strategic decision for governance and architectural lineage.

**Authority Boundary:**
- ADR records strategic decision (Polygon-first)
- `chain-integration.md` owns detailed integration behavior
- Provider-trust documents own oracle, DEX, RPC validation
- Risk engine owns execution controls for all chains
