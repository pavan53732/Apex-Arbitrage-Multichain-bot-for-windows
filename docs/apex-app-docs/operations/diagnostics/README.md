---
metadata_schema_version: 1.0
document_id: DOC-0398
title: Diagnostics README
plane: Product Specification
domain: Operations
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/diagnostics/diagnostics.md
related_concepts:
  - CONCEPT-0333
dependencies:
  - DOC-0333
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Diagnostics

## Purpose and scope

Operational diagnostics, troubleshooting, error handling, error catalog, and error-code references.

## What belongs here

Diagnostics specifications, error handling/logging, error catalogs, troubleshooting, and error-code references.

## What does not belong here

Monitoring, recovery orchestration, notifications, or runtime reliability unless diagnostics owns the concern.

## Expected document classes

- Index
- Specification
- Reference
- Guide for operational procedures

## Canonical boundaries

This folder indexes operations documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Diagnostics](diagnostics.md) | Specification |
| [Error Catalog](error-catalog.md) | Index |
| [Error Codes](error-codes.md) | Reference |
| [Error Handling and Logging](error-handling-and-logging.md) | Specification |
| [Troubleshooting](troubleshooting.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
