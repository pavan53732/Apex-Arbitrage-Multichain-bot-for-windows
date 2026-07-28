---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: Mev Protection Detail documentation.
scope: Reference documentation.
canonical_source: docs/MEV-PROTECTION-DETAIL.md
---

# Mev Protection Detail

## Document type
This document is an overview, reference, or index as noted below.

# MEV Protection Detail

## Purpose
Defines the detailed MEV protection behavior required for arbitrage execution.

## Ownership
- Owns private transaction routing, sandwich risk mitigation, and inclusion strategy.
- Does not own general execution policy or gas optimization policy.

## MEV contract
- Must define private mempool handling, relay selection, and fallback behavior.
- Must define simulation checks and protection failure behavior.

## Cross-references
- `MEV-PROTECTION.md`
- `GAS-OPTIMISATION.md`
- `EXECUTION-ENGINE.md`
- `TRANSACTION-LIFECYCLE.md`
