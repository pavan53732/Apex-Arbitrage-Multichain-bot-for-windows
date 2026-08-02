---
metadata_schema_version: 1.0
document_id: DOC-0366
title: Changelog
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/reference/changelog.md
related_concepts:
  - CONCEPT-0366
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Reference
type: REFERENCE
purpose: Changelog documentation.
scope: Reference documentation.
---

# Changelog

## Document type
Document type: [REFERENCE]

## Purpose
Maintains versioned release notes for the APEX platform.

## Changelog rules
- Record user-visible changes, fixes, and migrations by version.
- Keep entries brief and release-oriented.
- Each entry references its canonical owner where relevant.

## Entry format
- Entries are grouped by release version, newest first.
- Breaking changes and migrations are flagged explicitly.
- Each entry names the affected surface and its canonical owner.
- Security fixes are labeled with severity and remediation.
- Entries never contain secrets or customer data.

## Release discipline
- A changelog entry is written in the same change as the release it describes.
- Unreleased changes accumulate under an "Unreleased" section until the next release.
- Release dates are recorded per version.
- A revert or hotfix appends an entry rather than rewriting history.
- The changelog is user-visible; internal validator changes are documented in the repository docs.
- Deprecations are announced here at least one minor version before removal.
- The changelog links to the deployment and versioning contracts for release mechanics.
- Every version entry is reviewed with the release gate.
- Historical entries are retained; they are never rewritten after release.
- The changelog is the single release-history surface for the platform.
- Migration entries state the upgrade path and rollback.
- Release notes are generated from this changelog.

## Current entries
| Version | Date | Changes |
| --- | --- | --- |
| 0.1.0 (planned) | — | Initial desktop shell, simulation pipeline, validator suite, and governance model. |

## Structure
- Entries are grouped by release version, newest first.
- Breaking changes and migrations are flagged explicitly.
- The decision log tracks autonomous decisions; this changelog tracks user-visible releases.

## Cross-references
- `../execution/decision-log.md`
- `./implementation-roadmap.md`
- `../deployment/versioning.md`

## Operational Contract

This document owns the versioned release changelog. Each release entry is written at release time and reflects user-visible changes, fixes, and migrations.

## Example
A Windows packaging fix is recorded under its release version with a reference to the deployment contract.
