---
metadata_schema_version: 1.0
document_id: DOC-0420
title: Execution Transactions README
plane: Product Specification
domain: Execution
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/transactions/execution-engine.md
related_concepts:
  - CONCEPT-0280
dependencies:
  - DOC-0280
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Execution Transactions

## Purpose and scope

Execution engine, execution lifecycle, policies, transaction lifecycle, and order management documentation.

## What belongs here

Transaction execution, order management, execution lifecycle, and execution policy documents.

## What does not belong here

Trading strategy, market discovery, or wallet portfolio ownership.

## Expected document classes

- Index
- Specification
- Reference
- Policy where this subdomain owns execution constraints

## Canonical boundaries

This folder indexes execution documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Execution Engine](execution-engine.md) | Specification |
| [Execution Lifecycle](execution-lifecycle.md) | Reference |
| [Execution Policies](execution-policies.md) | Reference |
| [Order Management](order-management.md) | Reference |
| [Transaction Lifecycle](transaction-lifecycle.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
