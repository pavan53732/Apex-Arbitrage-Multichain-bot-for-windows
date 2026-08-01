---
metadata_schema_version: 1.0
document_id: DOC-0293
title: Portfolio Management
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/wallet-portfolio/portfolio-management.md
related_concepts:
  - CONCEPT-0293
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Portfolio Management documentation.
scope: Reference documentation.
---

# Portfolio Management

## Document type
This document is an overview, reference, or index as noted below.

# Portfolio Management

## Purpose
Aggregates balances and positions into portfolio value, allocation, and utilization snapshots.

## Responsibilities
- Compute total value, allocation, exposure, and utilization.
- Aggregate positions and wallet balances.
- Feed risk, reporting, and UI dashboards.

## Cross-references
- `./position-management.md`
- `./wallet-management.md`
- `../../market/core/market-data.md`

## Operational Contract
Defines portfolio ownership, allocation, rebalancing, exposure limits, and wallet/strategy bindings.

## Example
A portfolio rebalance is blocked if exposure exceeds policy.

## Required details
- Define multi-wallet aggregation and reconciliation.

## Portfolio rules
- Define portfolio aggregation across multiple wallets and chains.
- Define reconciliation after failed or partial trades.
