---
metadata_schema_version: 1.0
document_id: DOC-0383
title: Contract Registry
plane: Product Specification
domain: Configuration
class: Registry
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/configuration/registries/contract-registry.md
related_concepts:
  - CONCEPT-0383
dependencies: []
consumers:
  - DOC-0431
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Configuration
type: CONTRACT
purpose: Contract Registry documentation.
scope: Reference documentation.
---

# Contract Registry

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Document type
This document is an overview, reference, or index as noted below.

# Contract Registry

## Purpose
Authoritative owner for contract registry.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `../../architecture/apex-os.md`
- `../../architecture/architecture.md`

## Operational Contract
Defines the authoritative registry for deployed contracts, versions, ABIs, chain mappings, and status.

## Example
Flash loan receiver and execution contract entries remain versioned and chain-scoped.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
