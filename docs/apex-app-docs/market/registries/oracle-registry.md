---
metadata_schema_version: 1.0
document_id: DOC-0308
title: Oracle Registry
plane: Product Specification
domain: Market
class: Registry
authority: Canonical
status: Active
owner: Trading Team
version: 2.0.0
canonical_source: docs/apex-app-docs/market/registries/oracle-registry.md
related_concepts:
  - CONCEPT-0308
dependencies: []
consumers:
  - DOC-0317
  - DOC-0282
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Market
type: CONTRACT
purpose: "Defines the authoritative registry of supported oracle sources with explicit trust boundaries, freshness requirements, and manipulation protections."
scope: "Oracle listing, metadata, trust classification, fallback order, and circuit-breaker behavior. **Oracles are PRICE-REFERENCE AUTHORITY only, not execution authority.**"
---

# Oracle Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 2.0.0 | **Status:** Canonical | **Last Updated:** 2026-08-01 | **Owner:** Trading Team

## Purpose
Defines the authoritative registry of supported oracle sources with explicit trust boundaries, freshness requirements, and manipulation protections.

**CRITICAL: Oracles provide price-reference authority for validation and risk checks. Oracles are NOT execution authority — executable prices come from DEX quotes only.**

---

## 0. Provider Trust Model

### Oracle Authority Classification
**Trust Level:** HIGH | **Authority:** PRICE_REFERENCE | **Execution Authority:** NO

**Oracle Role:**
- ✅ Provide reference prices for spread integrity checks
- ✅ Validate DEX quote reasonableness
- ✅ Detect price manipulation and anomalies
- ✅ Feed risk engine for exposure calculations
- ❌ NOT used for trade execution pricing
- ❌ NOT used for slippage calculations
- ❌ NOT authoritative for PNL calculation

**Execution Authority:**
- DEX quotes are the ONLY execution pricing authority
- Oracle prices are advisory/validation only
- Disagreement between oracle and DEX triggers rejection

### Trust Hierarchy
```
ORACLE (price-reference) → Validates DEX quotes
    ↓
DEX QUOTE (execution-authority) → Actual trade pricing
    ↓
RPC (connectivity-authority) → Transaction submission
    ↓
AI PROVIDER (analysis-only) → Never trading-truth authority
```

---

## 1. Oracle Registry Fields

### 1.1 Core Fields
- **oracle_name:** Unique identifier (e.g., "Chainlink", "Pyth", "DIA")
- **chain_id:** Chain where oracle feed is available
- **feed_identifier:** Oracle-specific feed address or ID
- **supported_assets:** List of assets covered by this oracle
- **update_cadence:** Expected update frequency (e.g., "1m", "5m")
- **confidence_policy:** Confidence threshold for price acceptance

### 1.2 Trust Fields
- **trust_level:** HIGH | MEDIUM | LOW
- **authority_type:** PRICE_REFERENCE | EXECUTION_AUTHORITY | ANALYSIS_ONLY
- **manipulation_resistance:** HIGH | MEDIUM | LOW
- **decentralization_score:** 0.0 to 1.0

### 1.3 Operational Fields
- **fallback_priority:** Integer (1 = highest priority)
- **health_status:** HEALTHY | DEGRADED | UNHEALTHY
- **last_update_timestamp:** ISO 8601 timestamp
- **freshness_threshold_seconds:** Max acceptable staleness

---

## 2. Freshness and Circuit Breakers

### 2.1 Freshness Requirements
**Default:** Oracle data must be < 5 minutes old for Phase 1/2, < 1 minute for Phase 3

**Freshness Tiers:**
- **Tier 1 (CRITICAL):** < 1 minute old — required for Phase 3 execution
- **Tier 2 (STANDARD):** < 5 minutes old — acceptable for Phase 1/2
- **Tier 3 (STALE):** > 5 minutes old — REJECT for all phases

### 2.2 Circuit Breakers

**Stale Data Circuit Breaker:**
- **Trigger:** 3 consecutive stale oracle readings (>5 min old)
- **Action:** Mark oracle as UNHEALTHY, failover to backup
- **Recovery:** Oracle must provide 5 consecutive fresh readings

**Manipulation Circuit Breaker:**
- **Trigger:** Oracle price deviates >5% from DEX quotes
- **Action:** Reject oracle price, flag for review, use backup oracle
- **Recovery:** Manual operator review required

**Consensus Circuit Breaker:**
- **Trigger:** Multiple oracles disagree by >3%
- **Action:** Use median price, reject outliers, alert operator
- **Recovery:** Investigate outlier oracles

---

## 3. Oracle Manipulation Protection

### 3.1 Spread Integrity Check
**Purpose:** Detect oracle manipulation or DEX price anomalies

**Formula:**
```
price_deviation_pct = |oracle_price - dex_quote_price| / oracle_price
condition: price_deviation_pct <= max_acceptable_deviation
default: max_acceptable_deviation = 0.02 (2%)
```

**Action:**
- If deviation > 2%: REJECT trade, flag for review
- If deviation > 5%: Mark oracle as potentially manipulated
- If deviation > 10%: EMERGENCY HALT, alert operator

### 3.2 Multi-Oracle Consensus
**Purpose:** Validate oracle price against multiple sources

**Consensus Algorithm:**
```
1. Collect prices from all available oracles
2. Calculate median price
3. Reject outliers > 3% from median
4. Use median as reference price
5. If < 2 oracles agree: REJECT (insufficient consensus)
```

### 3.3 Time-Weighted Protection
**Purpose:** Detect flash manipulation attacks

**Validation:**
```
1. Compare current oracle price to 5-minute average
2. If deviation > 5%: flag as potential manipulation
3. If deviation > 10%: REJECT, use historical average
4. Alert operator if sustained deviation > 3%
```

---

## 4. Fallback and Disagreement Behavior

### 4.1 Fallback Order
**Priority:** 1 (highest) to N (lowest)

**Example Configuration:**
```yaml
oracles:
  - name: "Chainlink"
    fallback_priority: 1
    trust_level: HIGH
  - name: "Pyth"
    fallback_priority: 2
    trust_level: HIGH
  - name: "DIA"
    fallback_priority: 3
    trust_level: MEDIUM
  - name: "Internal_Twap"
    fallback_priority: 4
    trust_level: LOW
```

### 4.2 Disagreement Resolution
**Scenario:** Oracle A and Oracle B disagree by >2%

**Resolution Steps:**
1. Collect prices from all available oracles
2. Calculate median and standard deviation
3. Reject outliers (>2 std dev from median)
4. Use median of remaining oracles
5. If only 1 oracle remains: REJECT (insufficient consensus)
6. Alert operator if disagreement persists

### 4.3 Evidence Requirements
**For Phase 2/3 Execution:**
- Oracle price must have ≥2 oracle consensus
- All oracles must be TIER_1 or TIER_2 fresh
- No oracle can deviate >3% from median
- DEX quote must be within 2% of oracle median

**Evidence Logged:**
- All oracle prices used
- Oracle timestamps and freshness
- Consensus calculation
- Final reference price

---

## 5. Supported Oracles

### 5.1 Chainlink
- **Trust Level:** HIGH
- **Authority:** PRICE_REFERENCE
- **Chains:** Ethereum, BSC, Polygon, Arbitrum, Optimism
- **Update Cadence:** Variable (typically 1-5 min)
- **Manipulation Resistance:** HIGH (decentralized oracle network)
- **Fallback Priority:** 1

### 5.2 Pyth
- **Trust Level:** HIGH
- **Authority:** PRICE_REFERENCE
- **Chains:** Solana, Ethereum, BSC, Polygon, Arbitrum
- **Update Cadence:** Sub-second (push model)
- **Manipulation Resistance:** HIGH (institutional data providers)
- **Fallback Priority:** 2

### 5.3 DIA
- **Trust Level:** MEDIUM
- **Authority:** PRICE_REFERENCE
- **Chains:** Multi-chain (80+ chains)
- **Update Cadence:** Variable (configurable)
- **Manipulation Resistance:** MEDIUM (crowdsourced)
- **Fallback Priority:** 3

### 5.4 Internal TWAP (Fallback)
- **Trust Level:** LOW
- **Authority:** PRICE_REFERENCE
- **Chains:** All supported chains
- **Update Cadence:** Real-time (from DEX pools)
- **Manipulation Resistance:** LOW (on-chain only)
- **Fallback Priority:** 4 (last resort)

---

## 6. Interface Contract

### 6.1 Oracle Query Interface
- `get_reference_price(asset, chain_id, min_freshness)` — Returns reference price from highest-priority healthy oracle
- `validate_dex_quote(dex_price, oracle_reference, max_deviation)` — Validates DEX quote against oracle reference
- `get_consensus_price(asset, chain_id, min_oracles)` — Returns median price from multiple oracles

### 6.2 Health Monitoring
- Track oracle freshness for each feed
- Monitor oracle response latency
- Detect oracle failures and trigger failover
- Alert operator on consensus failures

---

## Cross-references
- `../core/market-data.md` — market data ingestion and freshness
- `../routing/route-optimization.md` — route scoring and selection
- `../routing/slippage-model.md` — slippage calculations
- `../../execution/risk-policy/risk-engine.md` — risk checks using oracle prices
- `../../data/persistence/database-schema.md` — oracle data persistence
- `../../interfaces/adapters/interface-provider-adapter.md` — provider adapter contract
