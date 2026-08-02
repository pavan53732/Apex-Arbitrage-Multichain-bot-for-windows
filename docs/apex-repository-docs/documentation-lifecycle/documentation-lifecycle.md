---
metadata_schema_version: 1.0
document_id: DOC-0056
title: Documentation Lifecycle
plane: Repository Operating Model
domain: Documentation Lifecycle
class: Workflow
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/documentation-lifecycle/documentation-lifecycle.md
related_concepts:
  - CONCEPT-0056
dependencies: []
consumers:
  - DOC-0060
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Documentation Lifecycle
type: PROCEDURE
purpose: Documentation Lifecycle documentation.
scope: Reference documentation.
---

# Documentation Lifecycle

## Document type
Document type: [REFERENCE]

## Purpose
Defines the lifecycle states of repository documents and the transitions between them: draft, review, approved, active, deprecated, and archived.

## Scope
Applies to all tracked documents in the repository knowledge system. Lifecycle state is recorded in each document's front matter as `status`.

## Lifecycle states
- **Draft** — content is being authored; not yet authoritative.
- **Review** — content is being reviewed by owners; may still change.
- **Approved** — content is accepted by the owner but not yet active.
- **Active** — the document is authoritative and enforced by validators.
- **Deprecated** — the document is superseded or withdrawn; readers are redirected to the replacement.
- **Archived** — the document is historical and no longer authoritative; it is retained for lineage.

## Transition rules
- A document enters **Draft** when it is first created.
- Promotion to **Active** requires owner approval and must pass repository validation.
- A document moves to **Deprecated** only when a replacement is registered or the concept is retired.
- An **Archived** document must not be consumed as a source of truth.
- `superseded_by` and `supersedes` front matter must be updated together with any status change.

## Edit-first rule
- If a canonical document already owns the concept, update that document; do not create a duplicate.
- Do not split authority across multiple documents for one concept.
- Do not duplicate a specification that already has a canonical owner.

## Registry synchronization
- Every lifecycle change must be reflected in the Concept Registry, Document Registry, and Traceability Registry in the same change (ROM-004).
- Document IDs remain stable across moves, renames, and status changes (ROM-002).

## Enforcement
- Validators enforce lifecycle metadata completeness (ROM-005).
- A status change without registry updates fails validation.
- Supersession records are mandatory on deprecation.
- A document in `Draft` or `Review` is not authoritative and must not be consumed as a source of truth.
- `last_updated` is bumped on every substantive change; an `Active` document unreviewed for 90 days is flagged stale.

## Cross-references
- `../registries/DOCUMENT-REGISTRY.md`
- `../registries/CONCEPT-REGISTRY.md`
- `../registries/TRACEABILITY-REGISTRY.md`
- `../documentation-lifecycle/document-lifecycle-policy.md`
- `../documentation-lifecycle/documentation-map.md`

## Operational Contract

This document owns the lifecycle-state model for repository documents. The document lifecycle policy and documentation map govern the operational workflow and are referenced above. Validators enforce metadata completeness (ROM-005) and registry consistency (ROM-004) against this model.

## Example
A document that is superseded by a new canonical owner is marked `Deprecated`, records the replacement in `superseded_by`, and the registry is updated in the same commit.
