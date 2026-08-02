---
metadata_schema_version: 1.0
document_id: DOC-0053
title: Coding Standards
plane: Repository Operating Model
domain: Standards
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-repository-docs/standards/coding-standards.md
related_concepts:
  - CONCEPT-0053
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Standards
type: SPECIFICATION
purpose: Coding Standards documentation.
scope: Reference documentation.
---

# Coding Standards

## Document type
Document type: [STANDARD]

## Purpose
Defines the coding standards that apply to implementation work in this repository: formatting, testing, packaging, review expectations, and safety rules for trading logic and Windows build output.

## Scope
Applies to any code artifact produced from this specification, including the APEX application packages, validators, scripts, and Windows packaging. This document sets standards; the product architecture owns design.

## Formatting standards
- Follow the language-standard formatter for the module in use; do not reformat unrelated code in a change.
- Keep names descriptive and consistent with the domain model in `docs/apex-app-docs/interfaces/api/domain-model.md`.
- Keep functions small and focused on a single responsibility.

## Testing standards
- Every behavior change must include or update a test.
- Deterministic logic (risk calculations, scoring, rankings) must have deterministic tests with fixed inputs and fixed expected outputs.
- Simulation and backtesting paths must produce reproducible results; randomness must be seeded.
- Tests must run locally before validation and commit.

## Trading logic safety
- Trading and risk logic must be deterministic and auditable; AI must not own final financial calculations.
- Every state-changing action must be validated before it executes.
- Financial calculations must be covered by unit tests with fixed-point expectations.

## Windows build output
- Windows builds must produce signed artifacts, installers, and update metadata per `docs/apex-app-docs/deployment/build-release.md`.
- Build output must not be committed to the repository; packaging artifacts are generated.

## Review expectations
- Reviews verify standards compliance, safety rules, and test coverage.
- A change is not complete until validators pass and the review confirms the change is minimal and canonical.

## Enforcement
- Standards are checked in code review and local validation.
- A change that violates a standard is not merged.

## Tooling
- Formatting and linting run locally before validation.
- Build gates enforce import and dependency rules.
- Test and backtest suites run locally before validation.
- Randomized test paths require deterministic seeds for reproducibility.
- A test that cannot run deterministically is marked and addressed before merge.

## Cross-references
- `../../apex-app-docs/architecture/project-structure.md`
- `../../apex-app-docs/testing/testing-guide.md`
- `../../apex-app-docs/deployment/build-release.md`
- `./dependency-authority-rules.md`

## Operational Contract

This document owns the coding standards for repository implementation work. It does not own product behavior; product behavior is owned by the product specification. Implementation work must comply with these standards and pass the repository validators before commit.

## Example
A change to the risk engine adds a deterministic unit test for the position-sizing calculation and runs the full validator suite locally before committing.
