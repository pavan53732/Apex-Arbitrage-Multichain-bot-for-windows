---
last_updated: 2026-07-29
type: CONTRACT
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Arbitrage Window Manager documentation.
scope: Reference documentation.
canonical_source: docs/ARBITRAGE-WINDOW-MANAGER.md
---

# Arbitrage Window Manager

## Document type
This document is an overview, reference, or index as noted below.

# Arbitrage Window Manager

## Purpose
Defines the lifecycle of arbitrage windows from detection through expiry or execution.

## Ownership
- Owns window creation, timing budgets, expiry, and stale-opportunity invalidation.
- Does not own trade execution or route scoring.

## Window contract
- Must define latency budget per leg, expiry conditions, and timing synchronization.
- Must define what happens when the opportunity becomes stale mid-flow.

## Cross-references
- `TRADING-LIFECYCLE.md`
- `OPPORTUNITY-RANKING.md`
- `RISK-ENGINE.md`
- `ORCHESTRATOR.md`
