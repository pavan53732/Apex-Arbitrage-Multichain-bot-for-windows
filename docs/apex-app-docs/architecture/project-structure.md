---
metadata_schema_version: 1.0
document_id: DOC-0085
title: Project Structure
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/architecture/project-structure.md
related_concepts:
  - CONCEPT-0085
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Architecture
type: REFERENCE
purpose: Project Structure documentation.
scope: Reference documentation.
---

# Project Structure

## Document type
Document type: [CONTRACT]

## Purpose
Defines the canonical repository layout and ownership boundaries for implementation of the APEX application.

## Scope
Top-level directory layout for the implementation repository, including apps, packages, scripts, tests, contracts, and Windows packaging. This document is the layout contract; module import rules are owned by `./module-dependency.md`.

## Repository layout
- `apps/` — runnable application shells: the desktop renderer and the Windows service host.
- `packages/core/` — platform-independent domain logic: market, trading, execution, risk, AI, and data.
- `packages/windows/` — Windows-specific integration: tray, notifications, service management, and packaging glue.
- `packages/adapters/` — external integrations: chains, DEXs, providers, and RPC.
- `scripts/` — deterministic local helper scripts (build, package, validate).
- `contracts/` — schemas, ABIs, and typed interface definitions.
- `tests/` — unit, integration, and backtesting suites.
- `docs/` — the documentation knowledge base (this repository).
- `installers/` — Windows packaging inputs and output staging (generated, not committed).

## Structure rules
- Top-level folders separate docs, services, workers, tests, and tooling.
- Core packages never import Windows packages; Windows packages depend on core.
- Packaging artifacts and generated outputs live outside `packages/` and are never committed.
- Each package owns its tests beside the source, with cross-package tests in `tests/`.
- A new top-level folder requires architecture approval and a layout update here.

## Layout governance
- A new top-level directory requires architecture approval.
- Packaging and generated outputs are never committed to source control.
- The layout contract and the module dependency rules change together.
- Tests live beside source; cross-package suites live in `tests/`.
- Every top-level entry has a stated purpose and an owning document; an unexplained folder is removed or documented.
- The repository root remains limited to control and entry files per the repository operating model.

## Cross-references
- `./architecture.md`
- `./module-dependency.md`
- `./component-diagrams.md`
- `../deployment/build-release.md`
- `../deployment/versioning.md`

## Operational Contract

This document owns the implementation repository layout. It aligns with the component diagrams and module dependency rules; any layout change updates this contract and the module import rules together. It does not own runtime behavior.

## Example
A Windows packaging artifact is generated into `installers/` during the build and excluded from source control, matching the build-release contract.
