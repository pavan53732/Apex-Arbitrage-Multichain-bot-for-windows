---
metadata_schema_version: 1.0
document_id: DOC-0327
title: Price Discovery
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/market/tokens/price-discovery.md
related_concepts:
  - CONCEPT-0327
dependencies:
  - DOC-0308
  - DOC-0328
consumers:
  - DOC-0317
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: "Defines price discovery process with explicit authority boundaries between oracle price-reference and DEX execution authority."
scope: "Price discovery, validation, and execution pricing with freshness, consensus, and deviation rules."
---

# Price Discovery

## Document type
This document is a reference.

## Version
**Version:** 2.0.0 | **Status:** Canonical | **Last Updated:** 2026-08-01 | **Owner:** Runtime Team

## Purpose
Defines the price discovery process with explicit authority boundaries between oracle price-reference and DEX execution authority.

**CRITICAL: Discovered prices are NOT execution authority unless backed by an executable DEX route quote.**

---

## 0. Price Authority Boundaries

### Price Source Hierarchy
```
ORACLE PRICE (price-reference authority)
    ↓ Validates and constrains
DEX QUOTE PRICE (execution authority)
    ↓ Backed by executable route
EXECUTABLE ROUTE (execution feasibility)
    ↓ Submits to
TRANSACTION (connectivity authority)
```

### Authority Classification

| Price Source | Authority Type | Execution Role | Validation Role |
|--------------|----------------|----------------|-----------------|
| Oracle (Chainlink, Pyth) | PRICE_REFERENCE | ❌ NO | ✅ Validates DEX quotes |
| DEX Quote (Uniswap, Pancake) | EXECUTION_AUTHORITY | ✅ YES | ⚠️ Validated by oracles |
| Discovered Price (aggregated) | ADVISORY | ❌ NO | ✅ Market analysis only |
| AI Price Estimate | ANALYSIS_ONLY | ❌ NO | ❌ NO authority |

### Critical Invariants

1. **DEX quotes are the ONLY execution pricing authority**
   - Oracle prices validate but NEVER override DEX quotes
   - Discovered prices are advisory only
   - AI estimates have no authority

2. **Discovered prices require executable route backing**
   - Price discovery without executable DEX quote = ADVISORY ONLY
   - Must have valid route with sufficient liquidity
   - Must pass oracle validation (within 2% of oracle reference)

3. **Freshness requirements apply to all price sources**
   - Phase 1/2: < 5 minutes freshness
   - Phase 3: < 1 minute freshness
   - Stale prices = REJECT for execution

---

## 1. Price Discovery Process

### 1.1 Price Discovery Stages
```
1. DISCOVER: Aggregate prices from multiple sources
2. VALIDATE: Check oracle consensus and freshness
3. EXECUTE: Obtain executable DEX quote
4. RE-VALIDATE: Oracle vs DEX deviation check
5. DECIDE: Approve or reject based on validation
```

### 1.2 Discovery Sources
**Authoritative Sources:**
- Oracle feeds (Chainlink, Pyth, DIA)
- DEX pool prices (Uniswap, PancakeSwap, SushiSwap)
- On-chain TWAP (time-weighted average price)

**Advisory Sources:**
- Aggregated price indices
- Third-party price APIs (CoinGecko, CoinMarketCap)
- AI price estimates

**Rule:** Advisory sources can inform analysis but NEVER determine execution prices.

---

## 2. Freshness and Consensus Rules

### 2.1 Freshness Tiers
**Applies to:** Oracle prices, DEX quotes, discovered prices

| Tier | Freshness | Phase Eligibility | Action |
|------|-----------|-------------------|--------|
| Tier 1 | < 1 minute | Phase 1, 2, 3 | ✅ Accept for all phases |
| Tier 2 | < 5 minutes | Phase 1, 2 | ✅ Accept for Phase 1/2 only |
| Tier 3 | > 5 minutes | NONE | ❌ REJECT for all phases |

### 2.2 Consensus Requirements
**Oracle Consensus (Phase 3):**
- Minimum 2 oracle sources required
- Oracle prices must agree within 2%
- Use median price if ≥3 oracles available
- Outliers >3% from median rejected

**DEX Quote Validation:**
- DEX quote must be within 2% of oracle median
- Deviation >2% = REJECT trade
- Deviation 1-2% = FLAG for review, reduce confidence
- Deviation <1% = Normal confidence

### 2.3 Deviation and Rejection Rules

**Oracle vs DEX Deviation:**
```python
deviation_pct = abs(oracle_price - dex_quote_price) / oracle_price

if deviation_pct > 0.02:  # > 2%
    return REJECT_TRADE("ORACLE_DEX_DEVIATION_EXCEEDED")
elif deviation_pct > 0.01:  # 1-2%
    return FLAG_REVIEW("ORACLE_DEX_DEVIATION_ELEVATED")
else:  # < 1%
    return ACCEPT("NORMAL_CONFIDENCE")
```

**Manipulation Detection:**
```python
if deviation_pct > 0.05:  # > 5%
    return EMERGENCY_HALT("POSSIBLE_MANIPULATION")
    # Action: Flag source, alert operator, use backup
```

**Multi-Oracle Disagreement:**
```python
if oracle_disagreement > 0.03:  # > 3%
    return USE_MEDIAN_AND_FLAG("ORACLE_CONSENSUS_WEAK")
    # Action: Use median, reject outliers, alert operator
```

---

## 3. Execution Pricing Authority

### 3.1 Execution Price Determination
**Phase 1 (Simulation):**
- Use DEX quotes for simulated execution
- Validate against oracle reference
- No actual execution, so deviation >2% = log warning only

**Phase 2 (Operator-Approved):**
- Use DEX quotes for actual execution
- Mandatory oracle validation (within 2%)
- Operator can override with audit trail

**Phase 3 (Autonomous):**
- Use DEX quotes for execution
- Mandatory multi-oracle consensus (≥2 oracles)
- Deviation >2% = AUTO_REJECT
- No operator override (fully automated)

### 3.2 Price Finality
**Execution price is final when:**
- DEX transaction confirmed on-chain
- Receipt includes actual execution price
- Price reconciled with pre-trade quote (within acceptable slippage)

**Discrepancy Handling:**
- If actual price differs from quote by > slippage tolerance: FLAG for review
- If discrepancy > 5%: EMERGENCY_HALT, investigate DEX behavior

---

## 4. Cross-References

### 4.1 Related Documents
- `../registries/oracle-registry.md` — oracle authority and freshness
- `../routing/route-optimization.md` — route validation and execution
- `../core/market-data.md` — market data ingestion and trust
- `../registries/dex-registry.md` — DEX authority and capabilities
- `../../execution/risk-policy/risk-engine.md` — risk checks using prices
- `../../execution/simulation/simulation-engine.md` — simulation pricing

### 4.2 Authority Chain
- Oracle Registry → Price-reference authority
- DEX Registry → Execution authority
- Route Optimization → Execution feasibility
- Risk Engine → Validation and gating
- Simulation Engine → Pre-execution validation

---

## 5. Operational Contract

### 5.1 Price Discovery Responsibilities
- Aggregate prices from multiple sources
- Validate freshness and consensus
- Detect and flag anomalies
- Provide authoritative and advisory prices with clear labels

### 5.2 Invariants
- Never use advisory prices for execution
- Never bypass oracle validation
- Never execute with stale prices (>5 min in Phase 1/2, >1 min in Phase 3)
- Never execute without DEX quote backing

### 5.3 Failure Modes
- **Stale data:** Reject opportunity, log warning
- **Oracle failure:** Failover to backup oracle
- **Consensus failure:** Reject trade, alert operator
- **DEX quote failure:** Reject route, try alternative DEX

---

## Example

**Valid Price Discovery:**
```
1. Oracle consensus: $100.00 (Chainlink $99.95, Pyth $100.05)
2. DEX quote: $100.50 (within 2% of oracle)
3. Route validation: Sufficient liquidity, gas OK
4. Decision: EXECUTE (normal confidence)
```

**Invalid Price Discovery:**
```
1. Oracle consensus: $100.00
2. DEX quote: $105.00 (5% deviation — possible manipulation)
3. Decision: REJECT (ORACLE_DEX_DEVIATION_EXCEEDED)
4. Action: Flag DEX, alert operator, investigate
```

---

## Cross-references
- `../registries/oracle-registry.md` — oracle registry and validation
- `../routing/route-optimization.md` — route execution authority
- `../core/market-data.md` — market data trust boundaries
- `../registries/dex-registry.md` — DEX capabilities and trust
- `../../execution/risk-policy/risk-engine.md` — risk validation
- `../../execution/simulation/simulation-engine.md` — simulation behavior
