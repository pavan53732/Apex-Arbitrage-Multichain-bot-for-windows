---
metadata_schema_version: 1.0
document_id: DOC-0301
title: Wallet Management
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/execution/wallet-portfolio/wallet-management.md
related_concepts:
  - CONCEPT-0301
dependencies: []
consumers:
  - DOC-0421
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: "Wallet management with explicit MVP phase boundaries. Phase 1: read-only. Phase 2: operator signing. Phase 3: autonomous."
scope: Reference documentation.
---

# Wallet Management

## Document type
This document is an overview, reference, or index as noted below.

# Wallet Management

## Purpose
Owns wallet discovery, creation, import, unlock, lock, rotation, permissions, and signing boundaries.

## Responsibilities
- Manage non-custodial wallet metadata and signing sessions.
- Track chain-specific balances and approvals.
- Enforce signer permission boundaries and secret handling rules.

## Cross-references
- `../../security/security.md`
- `../../security/permission-model.md`
- `../transactions/transaction-lifecycle.md`
- `../../market/tokens/token-registry.md`

## 0. MVP Execution Phases

### Phase 1 — Simulation Only (CURRENT)
**Wallet Mode:** READ_ONLY | **Signing:** DISABLED | **Broadcast:** DISABLED

**Wallet Manager Behavior:**
- Wallet metadata loaded and validated
- Balance queries active (read-only)
- No signing operations permitted
- No transaction broadcast permitted
- Wallet addresses used for simulation tracking only

**Hard Invariants:**
```python
if execution_mode == SIMULATION_ONLY:
    if wallet.attempt_sign():
        reject(operation, code="PHASE_1_SIGNING_BLOCK")
        return
    if wallet.attempt_broadcast():
        reject(operation, code="PHASE_1_BROADCAST_BLOCK")
        return
```

**Capabilities:**
- ✅ Query wallet balances
- ✅ Validate wallet addresses
- ✅ Track wallet metadata
- ✅ Simulate transaction nonces
- ❌ Sign transactions
- ❌ Broadcast transactions
- ❌ Move funds

### Phase 2 — Operator-Approved
**Wallet Mode:** OPERATOR_SIGNING | **Signing:** MANUAL | **Broadcast:** OPERATOR_INITIATED

**Wallet Manager Behavior:**
- Operator reviews transactions in dashboard
- Operator initiates signing via wallet UI
- Execution engine monitors signing status
- Transaction broadcast after operator confirmation
- Risk engine enforces reduced limits

### Phase 3 — Autonomous
**Wallet Mode:** AUTONOMOUS | **Signing:** AUTOMATED | **Broadcast:** AUTONOMOUS

**Wallet Manager Behavior:**
- Autonomous signing with spending limits
- Multi-wallet rotation for parallel execution
- MEV-protected transaction submission
- Automatic nonce management and gas optimization

---


## Operational Contract
Defines wallet inventory, labeling, address hygiene, funding status, and authorization boundaries.

## Example
An active wallet is excluded from trading if its funding falls below threshold.

## Required details
- Define credential storage, hardware wallet integration, and recovery.

## Wallet rules
- Define credential storage, hardware wallet support, and recovery handling on Windows.
- Define clipboard safety and address validation.
