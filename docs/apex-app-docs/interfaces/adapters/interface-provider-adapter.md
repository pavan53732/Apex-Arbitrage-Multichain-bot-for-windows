---
metadata_schema_version: 1.0
document_id: DOC-0262
title: Interface Provider Adapter
plane: Product Specification
domain: Interfaces
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/interfaces/adapters/interface-provider-adapter.md
related_concepts:
  - CONCEPT-0262
dependencies:
  - DOC-0308
  - DOC-0307
  - DOC-0305
  - DOC-0104
consumers:
  - DOC-0425
  - DOC-0317
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Interfaces
type: CONTRACT
purpose: "Defines provider adapter classes with explicit authority boundaries, metadata requirements, and prohibition on authority promotion."
scope: "Provider adapter contracts for Oracle, DEX, RPC, and AI providers with source identity, freshness, confidence, health, and failure metadata."
---

# Interface: Provider Adapter

## Document type
Document type: [CONTRACT]

## Version
**Version:** 2.0.0 | **Status:** Canonical | **Last Updated:** 2026-08-01 | **Owner:** Runtime Team

## Purpose
Defines provider adapter classes with explicit authority boundaries, metadata requirements, and prohibition on authority promotion.

**CRITICAL: Provider adapters must expose source identity, freshness, and authority type. Adapters are PROHIBITED from silently promoting advisory providers into execution or trading-truth authority.**

---

## 0. Provider Adapter Classes

### Adapter Authority Taxonomy

| Adapter Class | Authority Type | Trust Level | Execution Role | Phase 1 | Phase 2 | Phase 3 |
|---------------|----------------|-------------|----------------|---------|---------|---------|
| Oracle Adapter | PRICE_REFERENCE | HIGH | Validation only | ✅ | ✅ | ✅ |
| DEX Adapter | EXECUTION_AUTHORITY | HIGH | Actual trade pricing | ✅ | ✅ | ✅ |
| RPC Adapter | CONNECTIVITY_AUTHORITY | MEDIUM | Transaction submission | ✅ | ✅ | ✅ |
| AI Adapter | ANALYSIS_ONLY | MEDIUM | Never trading-truth | ✅ | ✅ | ✅ |

### Critical Invariants

1. **Authority type is immutable per adapter class**
   - Oracle adapter cannot become execution authority
   - AI adapter cannot become trading-truth authority
   - RPC adapter cannot become pricing authority

2. **Adapters must expose metadata**
   - Source identity (provider name, version)
   - Timestamp and freshness tier
   - Confidence score (0.0 to 1.0)
   - Health status (HEALTHY, DEGRADED, UNHEALTHY)
   - Failure reason (if applicable)

3. **Prohibition on authority promotion**
   - Adapter abstraction CANNOT silently change authority
   - Advisory providers CANNOT be promoted to execution authority
   - Analysis-only providers CANNOT override market data

---

## 1. Adapter Interface Contract

### 1.1 Base Adapter Interface
- `AUTHORITY_TYPE` — Immutable: PRICE_REFERENCE | EXECUTION_AUTHORITY | CONNECTIVITY_AUTHORITY | ANALYSIS_ONLY
- `TRUST_LEVEL` — Immutable: HIGH | MEDIUM | LOW
- `PROVIDER_ID` — Unique provider identifier
- `get_metadata()` — Returns source, freshness, confidence, health
- `health_check()` — Returns HEALTHY | DEGRADED | UNHEALTHY
- `query(request)` — Executes provider-specific query with metadata

### 1.2 Metadata Requirements
**All adapter responses MUST include:**
- `source_identity` — Provider name and version
- `timestamp` — Data timestamp
- `freshness_tier` — TIER_1 (<1min) | TIER_2 (<5min) | TIER_3 (stale)
- `confidence` — 0.0 to 1.0
- `health_status` — HEALTHY | DEGRADED | UNHEALTHY
- `failure_reason` — If failed, reason code
- `authority_type` — Immutable authority classification

---

## 2. Oracle Adapter (Price-Reference Authority)

### 2.1 Authority
**Authority Type:** PRICE_REFERENCE  
**Trust Level:** HIGH (for Tier 1 oracles)  
**Execution Role:** Validation only, NEVER execution pricing

### 2.2 Interface
- `get_reference_price(asset, chain_id)` — Returns reference price with metadata (NOT execution pricing)
- `validate_dex_quote(dex_price, max_deviation)` — Validates DEX quote, returns FAIL if deviation > 2%

### 2.3 Metadata Requirements
- **source_identity:** "Chainlink", "Pyth", "DIA", etc.
- **timestamp:** Oracle feed update timestamp
- **freshness_tier:** TIER_1 (<1min), TIER_2 (<5min), TIER_3 (stale)
- **confidence:** Based on oracle reputation and freshness
- **health_status:** HEALTHY if fresh, DEGRADED if aging, UNHEALTHY if stale
- **authority_type:** PRICE_REFERENCE (immutable)

### 2.4 Prohibitions
- ❌ CANNOT be used for execution pricing
- ❌ CANNOT override DEX quotes
- ❌ CANNOT be promoted to EXECUTION_AUTHORITY
- ❌ CANNOT bypass freshness validation

---

## 3. DEX Adapter (Execution Authority)

### 3.1 Authority
**Authority Type:** EXECUTION_AUTHORITY  
**Trust Level:** HIGH (for Tier 1 DEXes)  
**Execution Role:** Actual trade pricing and execution

### 3.2 Interface
- `get_quote(token_in, token_out, amount_in)` — Returns executable quote (ONLY execution pricing authority)
- `execute_swap(quote, wallet)` — Executes swap, returns actual execution price

### 3.3 Metadata Requirements
- **source_identity:** "Uniswap V3", "PancakeSwap V3", "SushiSwap", etc.
- **timestamp:** Quote generation timestamp
- **freshness_tier:** TIER_1 (<1min), TIER_2 (<5min), TIER_3 (stale)
- **confidence:** Based on liquidity and historical accuracy
- **health_status:** HEALTHY if liquid, DEGRADED if thin liquidity, UNHEALTHY if illiquid
- **authority_type:** EXECUTION_AUTHORITY (immutable)

### 3.4 Prohibitions
- ❌ CANNOT be used without oracle validation (Phase 2/3)
- ❌ CANNOT override oracle validation failures
- ❌ CANNOT execute with stale quotes
- ❌ CANNOT be downgraded to advisory

---

## 4. RPC Adapter (Connectivity Authority)

### 4.1 Authority
**Authority Type:** CONNECTIVITY_AUTHORITY  
**Trust Level:** MEDIUM  
**Execution Role:** Transaction submission and chain queries only

### 4.2 Interface
- `send_transaction(tx)` — Submits transaction, returns hash and receipt
- `query_balance(address, token)` — Queries account or token balance

### 4.3 Metadata Requirements
- **source_identity:** "Alchemy", "Infura", "QuickNode", etc.
- **timestamp:** Last successful query timestamp
- **freshness_tier:** TIER_1 (<1min), TIER_2 (<5min), TIER_3 (stale)
- **confidence:** Based on success rate and latency
- **health_status:** HEALTHY if responsive, DEGRADED if slow, UNHEALTHY if failing
- **authority_type:** CONNECTIVITY_AUTHORITY (immutable)

### 4.4 Prohibitions
- ❌ CANNOT influence pricing decisions
- ❌ CANNOT validate or reject trades
- ❌ CANNOT be promoted to pricing authority
- ❌ CANNOT bypass multi-RPC redundancy

---

## 5. AI Adapter (Analysis-Only Authority)

### 5.1 Authority
**Authority Type:** ANALYSIS_ONLY  
**Trust Level:** MEDIUM  
**Execution Role:** NEVER trading-truth, NEVER execution, NEVER validation

### 5.2 Interface
- `analyze_market(market_snapshot)` — Returns market analysis (NOT authoritative prices)
- `suggest_strategy(market_data, portfolio)` — Returns strategy suggestions (does NOT override deterministic logic)

### 5.3 Metadata Requirements
- **source_identity:** "OpenRouter/GPT-4", "Claude", "Qwen", etc.
- **timestamp:** Analysis generation timestamp
- **freshness_tier:** TIER_1 (<1min), TIER_2 (<5min), TIER_3 (stale)
- **confidence:** Model confidence score (0.0 to 1.0)
- **health_status:** HEALTHY if responsive, DEGRADED if high latency, UNHEALTHY if failing
- **authority_type:** ANALYSIS_ONLY (immutable)

### 5.4 Critical Prohibitions
- ❌ CANNOT provide authoritative prices
- ❌ CANNOT override market data
- ❌ CANNOT bypass risk controls
- ❌ CANNOT sign transactions
- ❌ CANNOT be promoted to trading-truth authority
- ❌ CANNOT be used for execution pricing
- ❌ CANNOT validate DEX quotes or oracle prices

### 5.5 Allowed Uses
- ✅ Analyze market trends and patterns
- ✅ Suggest strategies and opportunities
- ✅ Explain execution outcomes
- ✅ Generate reports and insights
- ✅ Assist with debugging and optimization

---

## 6. Adapter Composition and Validation

### 6.1 Multi-Adapter Validation (Phase 3)
**Execution validation flow:**
1. Oracle validation (PRICE_REFERENCE) — Check health, freshness, consensus
2. DEX quote (EXECUTION_AUTHORITY) — Check health, freshness, liquidity
3. Oracle vs DEX validation — Reject if deviation > 2%
4. AI analysis (ANALYSIS_ONLY) — Advisory only, cannot override

### 6.2 Health Monitoring
**All adapters must report health:**
- HEALTHY: Normal operation, within SLAs
- DEGRADED: Elevated latency or aging, failover recommended
- UNHEALTHY: Failing or stale, failover mandatory

### 6.3 Failure Handling
**Adapter failure cascade:**
1. Primary fails → failover to backup
2. All unhealthy → reject opportunity, alert operator
3. Persistent failures → mark provider UNHEALTHY, remove from rotation

---

## 7. Consistency Verification

### 7.1 Authority Consistency Check
**Verify across all provider-trust documents:**

- ✅ DEX quotes are the only execution-pricing authority
- ✅ Oracles validate pricing but do not override DEX prices
- ✅ RPC providers are connectivity authority only
- ✅ AI providers are analysis-only and never trading-truth authority
- ✅ Phase 1/2 freshness is < 5 minutes
- ✅ Phase 3 freshness is < 1 minute
- ✅ Oracle vs DEX deviation > 2% rejects the trade
- ✅ Manipulation deviation > 5% rejects and flags the source
- ✅ Phase 3 requires ≥2 approved oracle sources
- ✅ Simulation Phase 1 remains non-signing and non-broadcasting

### 7.2 Adapter Authority Matrix
| Adapter | Authority | Execution | Validation | Phase 1 | Phase 2 | Phase 3 |
|---------|-----------|-----------|------------|---------|---------|---------|
| Oracle | PRICE_REFERENCE | ❌ | ✅ | ✅ | ✅ | ✅ |
| DEX | EXECUTION_AUTHORITY | ✅ | ⚠️ Validated | ✅ | ✅ | ✅ |
| RPC | CONNECTIVITY_AUTHORITY | ❌ | ❌ | ✅ | ✅ | ✅ |
| AI | ANALYSIS_ONLY | ❌ | ❌ | ✅ | ✅ | ✅ |

---

## Cross-references
- `../market/registries/oracle-registry.md` — oracle authority and validation
- `../market/registries/dex-registry.md` — DEX execution authority
- `../market/connectivity/rpc-manager.md` — RPC connectivity
- `../ai/providers/ai-provider-manager.md` — AI provider management
- `../market/core/market-data.md` — market data trust boundaries
- `../market/routing/route-optimization.md` — route validation
- `../market/tokens/price-discovery.md` — price discovery process
