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
version: 1.1.0
canonical_source: docs/apex-repository-docs/contribution/contributing.md
related_concepts:
  - CONCEPT-0062
dependencies: []
consumers:
  - DOC-0061
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Contribution
type: REFERENCE
purpose: Contributing documentation.
scope: Reference documentation.
---

# Contributing

## Document type
Document type: [GUIDE]

## Purpose
Describes how contributors and AI agents make changes to this repository: setup, classification, implementation, validation, and review.

## Scope
Repository-wide contribution workflow for documentation and validator changes. This repository is local-first: all work is performed explicitly by humans and AI agents, never by automated pipelines.

## Setup
- Clone the repository from GitHub.
- Install the validator dependencies: `pip install -r validators/requirements.txt`.
- Run the validation suite with `python3 validators/runner.py` from the repository root.
- Confirm the working tree is clean before starting work.

## Before making a change
1. Read the canonical governance owners: `AGENTS.md`, `REBUILD-SYSTEM-SPECIFICATION.md`, and `REPOSITORY-EXECUTION-MODEL.md`.
2. Classify the change: determine plane (Repository Operating Model or Product Specification), domain, class, authority, and status.
3. Identify the canonical file for the concept. If a canonical owner exists, update it; do not create a duplicate.
4. If the change is structural or semantic, confirm the canonical relationship before editing.

## Implementation rules
- Edit canonical sources rather than creating parallel documents.
- Update registries, README navigation, and cross-references in the same change.
- Do not create temporary execution artifacts or generated reports in the repository.
- Keep root-level structure minimal and intentional.

## Validation gates
- Run `python3 validators/runner.py` after every change.
- Review the result: 0 errors expected; warnings must be understood, not ignored.
- Verify metadata is valid and cross-references resolve before opening a review.

## Review requirements
- Reviews check plane selection, canonical ownership, registry consistency, and traceability.
- A change is complete only when validated, committed with an explanatory message, and pushed to `main`.

## Definition of done
- Validated: 0 errors from the validator suite.
- Metadata valid and registries updated in the same change.
- Workspace clean; no temporary artifacts remain.
- The commit message explains what changed, why it changed, the plane, and the document class.
- Cross-references and registry rows are updated in the same change as the edit they describe.

## Cross-references
- `../standards/coding-standards.md`
- `../../apex-app-docs/reference/implementation-roadmap.md`
- `../../REPOSITORY-EXECUTION-MODEL.md`
- `../documentation-lifecycle/documentation-lifecycle.md`

## Operational Contract

This document owns the contributor workflow guidance. Repository execution policy, commit workflow, and validation lifecycle are owned by `REPOSITORY-EXECUTION-MODEL.md` and referenced above.

## Example
A contributor adding a new product document classifies it as Product Specification, records it in the registries, runs the validators, and resolves all errors before opening the change for review.
