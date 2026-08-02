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
version: 1.1.0
canonical_source: docs/apex-app-docs/configuration/registries/contract-registry.md
related_concepts:
  - CONCEPT-0383
dependencies: []
consumers:
  - DOC-0431
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Configuration
type: CONTRACT
purpose: Contract Registry documentation.
scope: Reference documentation.
---

# Contract Registry

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

## Document type
This document is an overview, reference, or index as noted below.

## Purpose
Authoritative owner for contract registry.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Registry fields
- Contract id.
- Version.
- ABI reference.
- Chain mapping.
- Deployment status.
- Governance approval record.

## Registry rules
- A contract is identified by id and version; the pair is unique.
- ABIs are stored and versioned in the ABI store.
- Chain mappings are explicit and validated.
- Deployment status transitions follow the contract lifecycle.
- Entries are immutable after approval; changes create a new version.
- Flash loan receivers and execution contracts are versioned and chain-scoped.
- A contract cannot be selected for deployment without recorded governance approvals.

## Registry lifecycle
- A contract enters the registry at `Registered` with a proposed version and ABI reference.
- Approval records attach to the entry; deployment is blocked until approvals are present.
- An upgrade creates a new version of the entry; the previous version remains immutable for audit.
- A withdrawn contract is marked withdrawn, not deleted; its history stays queryable.
- Registry changes are validated against the chain mappings before they take effect.

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
| 1.1.0 | 2026-08-02 | Expanded canonical content: replaced placeholder directives and generic boilerplate with grounded ownership, rules, lifecycle, failure, and cross-reference detail. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
