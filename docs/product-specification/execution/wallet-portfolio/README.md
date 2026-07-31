---
metadata_schema_version: 1.0
document_id: DOC-0421
title: Execution Wallet Portfolio README
plane: Product Specification
domain: Execution
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/wallet-portfolio/wallet-management.md
related_concepts:
  - CONCEPT-0301
dependencies:
  - DOC-0301
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Execution Wallet Portfolio

## Purpose and scope

Wallet, asset, portfolio, position, and wallet command-center documentation.

## What belongs here

Wallet management, asset management, portfolio analytics, portfolio management, position management, and wallet command-center documents.

## What does not belong here

Market token discovery, transaction execution, or security secret lifecycle ownership.

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
| [Asset Management](./asset-management.md) | Reference |
| [Portfolio Analytics](./portfolio-analytics.md) | Reference |
| [Portfolio Management](./portfolio-management.md) | Reference |
| [Position Management](./position-management.md) | Reference |
| [Wallet Command Center](./wallet-command-center.md) | Reference |
| [Wallet Management](./wallet-management.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
