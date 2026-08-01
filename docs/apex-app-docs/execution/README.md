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
canonical_source: docs/apex-app-docs/execution/trading/trading-engine.md
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

Product execution specifications and references for acting on market opportunities and managing execution state.

## What does not belong here

Market discovery, product AI reasoning, operations monitoring, and security secret lifecycle behavior unless explicitly execution-owned.

## Canonical owner map

| Subdomain | Concept ID | Canonical owner | README |
| --- | --- | --- | --- |
| risk-policy | CONCEPT-0282 | [Risk Engine](risk-policy/risk-engine.md) | [Execution Risk Policy README](risk-policy/README.md) |
| simulation | CONCEPT-0283 | [Simulation Engine](simulation/simulation-engine.md) | [Execution Simulation README](simulation/README.md) |
| trading | CONCEPT-0284 | [Trading Engine](trading/trading-engine.md) | [Execution Trading README](trading/README.md) |
| transactions | CONCEPT-0280 | [Execution Engine](transactions/execution-engine.md) | [Execution Transactions README](transactions/README.md) |
| wallet-portfolio | CONCEPT-0301 | [Wallet Management](wallet-portfolio/wallet-management.md) | [Execution Wallet Portfolio README](wallet-portfolio/README.md) |

## Document classes expected

- Index
- Specification
- Reference
- Policy where execution constraints are owned

## Relationship to adjacent domains

Execution depends on Market for opportunity data, Security for trust boundaries, Operations for recovery visibility, and Interfaces for message/API contracts.

## Subdomain navigation

### risk-policy

- Concept: `CONCEPT-0282`
- Canonical owner: [Risk Engine](risk-policy/risk-engine.md)
- Folder README: [Execution Risk Policy README](risk-policy/README.md)

Documents:

- [Decision Engine](risk-policy/decision-engine.md) — Specification
- [Policy Engine](risk-policy/policy-engine.md) — Specification
- [Risk Engine](risk-policy/risk-engine.md) — Specification

### simulation

- Concept: `CONCEPT-0283`
- Canonical owner: [Simulation Engine](simulation/simulation-engine.md)
- Folder README: [Execution Simulation README](simulation/README.md)

Documents:

- [Simulation Engine](simulation/simulation-engine.md) — Specification

### trading

- Concept: `CONCEPT-0284`
- Canonical owner: [Trading Engine](trading/trading-engine.md)
- Folder README: [Execution Trading README](trading/README.md)

Documents:

- [Arbitrage Window Manager](trading/arbitrage-window-manager.md) — Specification
- [Cross Exchange Arbitrage](trading/cross-exchange-arbitrage.md) — Reference
- [Strategies](trading/strategies.md) — Reference
- [Strategy Rotation](trading/strategy-rotation.md) — Reference
- [Trade Explainer](trading/trade-explainer.md) — Reference
- [Trading Engine](trading/trading-engine.md) — Specification
- [Trading Lifecycle](trading/trading-lifecycle.md) — Reference

### transactions

- Concept: `CONCEPT-0280`
- Canonical owner: [Execution Engine](transactions/execution-engine.md)
- Folder README: [Execution Transactions README](transactions/README.md)

Documents:

- [Execution Engine](transactions/execution-engine.md) — Specification
- [Execution Lifecycle](transactions/execution-lifecycle.md) — Reference
- [Execution Policies](transactions/execution-policies.md) — Reference
- [Order Management](transactions/order-management.md) — Reference
- [Transaction Lifecycle](transactions/transaction-lifecycle.md) — Reference

### wallet-portfolio

- Concept: `CONCEPT-0301`
- Canonical owner: [Wallet Management](wallet-portfolio/wallet-management.md)
- Folder README: [Execution Wallet Portfolio README](wallet-portfolio/README.md)

Documents:

- [Asset Management](wallet-portfolio/asset-management.md) — Reference
- [Portfolio Analytics](wallet-portfolio/portfolio-analytics.md) — Reference
- [Portfolio Management](wallet-portfolio/portfolio-management.md) — Reference
- [Position Management](wallet-portfolio/position-management.md) — Reference
- [Wallet Command Center](wallet-portfolio/wallet-command-center.md) — Reference
- [Wallet Management](wallet-portfolio/wallet-management.md) — Reference

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.

## Execution Ownership Boundaries

- Transaction lifecycle documents own transaction and order state progression.
- Trading lifecycle documents own strategy and trade progression.
- Execution Engine owns execution coordination; the lifecycle documents have complementary scopes rather than duplicate ownership.
- Wallet and portfolio documents remain separate from execution-flow ownership.
