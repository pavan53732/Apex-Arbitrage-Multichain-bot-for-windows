---
metadata_schema_version: 1.0
document_id: DOC-0012
title: Governance Overview
plane: Repository Operating Model
domain: Governance
class: Guide
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/governance/governance-overview.md
related_concepts:
  - CONCEPT-0012
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Governance
type: OVERVIEW
purpose: Readme Governance documentation.
scope: Reference documentation.
---

# Governance Overview

## Document type
Document type: [GUIDE]

## Purpose
Describes how this repository is governed: the two-plane documentation model, canonical source-of-truth discipline, documentation classes, authority rules, and the governance processes that contributors and AI agents must follow.

## Scope
Repository governance conventions for APEX documentation and architecture validation. This document is an orientation guide; it defers to the canonical governance owners listed under `## Canonical owners` and does not duplicate their content.

## The two-plane model
- The **Repository Operating Model** plane defines how work happens in the repository: governance, documentation classes, validation, traceability, agent rules, and hygiene.
- The **Product Specification** plane defines the APEX software system: architecture, runtime, AI, execution, dashboard, security, windows, plugins, interfaces, testing, and state machines.
- Every document belongs to exactly one plane. Mixing plane semantics is a documentation-class violation (ROM-008).

## Canonical source of truth
- Every important concept has exactly one canonical owner (ROM-001).
- The path is a location; the document ID is the identity (ROM-002, ROM-003).
- Registries and navigation must always reflect repository state (ROM-004).
- If two files appear to define the same concept, establish or clarify a canonical relationship instead of guessing.
- A lower-authority file must never silently override a canonical file.

## Documentation classes
- Repository Operating Model.
- Product Specification.
- ADR.
- Reference.
- Guide.
- Historical.
- Certification (only if intentionally restored).
- Generated, which is non-canonical by default.

## Governance rules
- Metadata must be complete and valid (ROM-005).
- Cross-references must resolve (ROM-006).
- Traceability endpoints and relationship types must be valid (ROM-007).
- Plane, domain, authority, class, and placement must comply (ROM-008).
- Canonical authority must be consistent (ROM-009).
- Generated execution artifacts are never canonical sources (ROM-010).
- CI/CD and GitHub Actions are prohibited (ROM-011).
- Temporary execution artifacts and workspace clutter are prohibited (ROM-012).

## Governance freeze

The governance architecture is stable. AI agents must not redesign, replace, or expand the governance framework unless the user explicitly requests a governance revision. Normal repository work focuses on product implementation, product documentation, validator compliance, and repository maintenance.

## Canonical owners
- `AGENTS.md` — agent operating contract.
- `REBUILD-SYSTEM-SPECIFICATION.md` — repository knowledge architecture.
- `REPOSITORY-EXECUTION-MODEL.md` — execution, validation, and commit model.
- `docs/apex-repository-docs/registries/` — concept, document, and traceability registries.

## Cross-references
- `../../../AGENTS.md`
- `../../../REBUILD-SYSTEM-SPECIFICATION.md`
- `../../../REPOSITORY-EXECUTION-MODEL.md`
- `../registries/CONCEPT-REGISTRY.md`
- `../registries/DOCUMENT-REGISTRY.md`
- `../registries/TRACEABILITY-REGISTRY.md`

## Operational Contract

This document owns the high-level orientation narrative for repository governance. It does not own any governance rule itself: every rule listed above is owned by the canonical owner identified in `## Canonical owners`. Changes to governance rules must be made in those canonical owners and mirrored here only as orientation.

## Example
A contributor who needs to know whether a document belongs in the repository or the product plane reads this overview, then follows the canonical owner for placement rules.
