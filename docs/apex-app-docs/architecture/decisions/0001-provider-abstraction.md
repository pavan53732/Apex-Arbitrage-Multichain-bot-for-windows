---
metadata_schema_version: 1.0
document_id: DOC-0070
title: ADR 0001 Provider Abstraction
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/architecture/decisions/0001-provider-abstraction.md
related_concepts:
  - CONCEPT-0070
dependencies:
  - DOC-0308
  - DOC-0307
  - DOC-0305
  - DOC-0104
consumers:
  - DOC-0262
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Architecture
type: ADR
purpose: "Records the architectural decision to use provider abstraction with four authority classes: Oracle (price-reference), DEX (execution), RPC (connectivity), and AI (analysis-only)."
scope: "Provider abstraction pattern, authority classification, non-promotion constraint, and fallback behavior."
---

# ADR 0001: Provider Abstraction

## Status
**Accepted** | **Version:** 2.0.0 | **Last Updated:** 2026-08-01

## Context
APEX integrates multiple external provider types: oracles for price data, DEXes for execution, RPC providers for blockchain connectivity, and AI providers for analysis. Each provider type has different authority levels, trust characteristics, and operational requirements.

Without explicit abstraction and authority classification, the system risks:
- Confusing advisory data with authoritative data
- Accidentally promoting analysis-only providers to execution authority
- Inconsistent freshness and validation requirements
- Ambiguous fallback behavior during provider failures

## Problem
How should APEX abstract and classify external providers to ensure:
1. Clear separation between advisory and authoritative data sources?
2. Prevention of accidental authority promotion?
3. Consistent validation, freshness, and fallback behavior?
4. Explicit trust boundaries for each provider type?

## Decision
**Adopt provider abstraction with four immutable authority classes:**

### Provider Authority Classes

| Class | Authority Type | Trust Level | Execution Role | Validation Role |
|-------|----------------|-------------|----------------|-----------------|
| **Oracle** | PRICE_REFERENCE | HIGH | ❌ NO | ✅ Validates DEX quotes |
| **DEX Quote** | EXECUTION_AUTHORITY | HIGH | ✅ YES | ⚠️ Validated by oracles |
| **RPC** | CONNECTIVITY_AUTHORITY | MEDIUM | ❌ NO | ❌ NO |
| **AI Provider** | ANALYSIS_ONLY | MEDIUM | ❌ NO | ❌ NO |

### Authority Invariants

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

### Fallback Constraints

- **Oracle fallback:** Use median of ≥2 oracles, reject outliers >3%
- **DEX fallback:** Try alternative DEX on failure, validate against oracle
- **RPC fallback:** Automatic failover to backup RPC, multi-RPC redundancy required
- **AI fallback:** Degraded to no AI analysis, core logic continues

## Alternatives Considered

### Alternative 1: Single Provider Interface
**Approach:** All providers implement same interface, authority determined at runtime.

**Rejected because:**
- Risks runtime authority confusion
- Harder to enforce authority boundaries
- More complex validation logic
- Increased risk of authority promotion bugs

### Alternative 2: Provider-Agnostic Abstraction
**Approach:** Treat all providers as equal data sources with equal weight.

**Rejected because:**
- Ignores fundamental authority differences
- Would allow AI to override oracle prices
- No protection against advisory data becoming authoritative
- Violates safety requirements for Phase 2/3 execution

### Alternative 3: Hard-Coded Provider Logic
**Approach:** No abstraction, hard-code each provider type separately.

**Rejected because:**
- Difficult to add new providers
- Duplication of validation logic
- Harder to test and maintain
- Inconsistent fallback behavior

## Consequences

### Positive
- ✅ Clear authority boundaries prevent accidental promotion
- ✅ Consistent validation and freshness requirements
- ✅ Deterministic fallback behavior
- ✅ AI providers explicitly prohibited from trading-truth authority
- ✅ Easier to add new providers within same authority class
- ✅ Improved testability with explicit authority mocks

### Negative
- ⚠️ More complex adapter layer than single-interface approach
- ⚠️ Requires discipline to maintain authority invariants
- ⚠️ Additional metadata overhead in all provider responses

### Neutral
- Provider abstraction now documented in canonical architecture
- Implementation must follow authority classification
- Future provider additions must fit existing authority classes

## Implementation Constraints

1. **Authority type must be immutable** — set at adapter initialization, cannot change
2. **All responses must include metadata** — source, timestamp, freshness, confidence, health
3. **AI adapters must explicitly prohibit** — trading-truth, execution, validation authority
4. **Fallback behavior must be deterministic** — no random selection, use priority ordering
5. **Multi-source validation required for Phase 3** — ≥2 oracles, multi-RPC, multi-DEX

## Related Documents

### Canonical Specifications
- `../market/registries/oracle-registry.md` — Oracle authority and validation
- `../market/registries/dex-registry.md` — DEX execution authority
- `../market/connectivity/rpc-manager.md` — RPC connectivity
- `../ai/providers/ai-provider-manager.md` — AI provider management
- `../interfaces/adapters/interface-provider-adapter.md` — Provider adapter contract

### Architecture
- `../apex-os.md` — Platform constitution and design principles
- `../architecture.md` — System architecture and subsystem boundaries

## Compliance

**This ADR records existing architecture, does not create new decisions.**

Authority classification is already documented in:
- `../market/registries/oracle-registry.md` (Section 0: Provider Trust Model)
- `../market/core/market-data.md` (Section 0: Provider Trust Boundaries)
- `../interfaces/adapters/interface-provider-adapter.md` (Section 0: Provider Adapter Classes)

This ADR formalizes those decisions for governance and architectural lineage.
