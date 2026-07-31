---
metadata_schema_version: 1.0
document_id: DOC-0062
title: Contributing
plane: Repository Operating Model
domain: Contribution
class: Guide
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/contribution/contributing.md
related_concepts:
  - CONCEPT-0062
dependencies: []
consumers:
  - DOC-0061
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Contribution
type: REFERENCE
purpose: Contributing documentation.
scope: Reference documentation.
---

# Contributing

## Document type
This document is an overview, reference, or index as noted below.

# CONTRIBUTING

## Purpose
Navigation-only document pointing to the authoritative owner(s).

## Cross-references
- `../standards/coding-standards.md`
- `../../product-specification/reference/implementation-roadmap.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define setup, branch, test, and review requirements.
- Run `../scripts/validate_markdown_refs.sh` from the repository root before opening a review when you touched markdown navigation or canonical references.
