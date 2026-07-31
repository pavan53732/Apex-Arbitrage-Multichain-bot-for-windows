---
metadata_schema_version: 1.0
document_id: DOC-0285
title: Execution README
plane: Product Specification
domain: Execution
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/trading/trading-engine.md
related_concepts:
  - CONCEPT-0284
dependencies:
  - DOC-0284
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Execution

## Purpose and scope

Trading, transaction execution, risk and policy gates, wallet/portfolio behavior, and simulation documentation.

## What belongs here

Product execution specifications and references for trading, transaction execution, risk policy, wallet portfolio state, and simulation.

## What does not belong here

Market discovery, product AI orchestration, generic operations monitoring, or security secret lifecycle behavior unless explicitly execution-owned.

## Subdomains

| Subdomain | README | Canonical owner |
| --- | --- | --- |
| risk-policy | [Execution Risk Policy README](risk-policy/README.md) | [Risk Engine](./risk-policy/risk-engine.md) |
| simulation | [Execution Simulation README](simulation/README.md) | [Simulation Engine](./simulation/simulation-engine.md) |
| trading | [Execution Trading README](trading/README.md) | [Trading Engine](./trading/trading-engine.md) |
| transactions | [Execution Transactions README](transactions/README.md) | [Execution Engine](./transactions/execution-engine.md) |
| wallet-portfolio | [Execution Wallet Portfolio README](wallet-portfolio/README.md) | [Wallet Management](./wallet-portfolio/wallet-management.md) |

## Additional execution references

- [Decision Log](./decision-log.md) remains at the execution domain root until a later ownership decision moves it.

## Document creation rule

Before adding an execution document, identify the active execution concept owner and place the document in the matching subdomain. Do not create duplicate execution ownership documents.
