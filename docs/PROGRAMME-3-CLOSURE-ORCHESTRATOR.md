---
type: SPECIFICATION
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Defines the Closure Orchestrator engine for Programme 3, responsible for hierarchical execution of behavioural root dependency closures.
scope: Orchestrates closure -> dimension -> document -> section -> validation -> freeze for each behavioural root.
last_updated: 2026-07-29
canonical_source: docs/PROGRAMME-3-CLOSURE-ORCHESTRATOR.md
---

# Programme 3 Closure Orchestrator

## Summary

The Closure Orchestrator is a governance engine that executes Programme 3 hierarchically. Instead of repairing an entire behavioural root closure in one pass, it decomposes work into deterministic units:

- Behavioural Root
- Closure
- Dimension
- Document
- Section
- Validation
- Freeze

Each unit is processed independently, with clear acceptance criteria and evidence, preventing context explosion and architectural inference.

## Responsibilities

- Compute full transitive dependency closure for each behavioural root.
- Build dimension queues for all maturity dimensions (structure, interfaces, events, configuration, schemas, state machines, recovery, security, validation, algorithms).
- Build document queues per dimension, limited to critical and required documents.
- Build section queues per document and dimension (e.g., Events Produced, Interfaces, Configuration Keys).
- Dispatch repair tasks to the Repair Planner.
- Enforce execution order: closure -> dimension -> document -> section -> validation -> freeze.
- Ensure only one dimension is active at a time for a given closure.
- Ensure the LLM worker never sees more than one document, one dimension, one section at a time.

## Execution Model

For each behavioural root:

1. Compute closure.
2. Generate Closure Manifest.
3. For each dimension in the maturity model:
   - Build document queue (critical + required only).
   - For each document:
     - Build section queue for that dimension.
     - For each section:
       - Create a repair task and hand it to the Repair Planner.
       - Validate the result using governance validators.
       - Mark section as frozen.
   - When all documents in the dimension pass, mark the dimension as frozen.
4. When all dimensions reach 100%, mark the closure as implementation-ready and freeze it.

## Interfaces

The orchestrator exposes deterministic interfaces:

- `compute_closure(root_path) -> ClosureManifest`
- `build_dimension_queue(root_path, closure) -> list[DimensionTask]`
- `build_document_queue(root_path, dimension, closure) -> list[DocumentTask]`
- `build_section_queue(document_path, dimension) -> list[SectionTask]`
- `run_dimension(root_path, dimension) -> DimensionResult`
- `freeze_dimension(root_path, dimension)`
- `freeze_closure(root_path)`

## Quality Gates

The orchestrator enforces Programme 3 quality gates:

- Only critical and required documents can block a dimension.
- Optional documents may remain lightweight if they are not implementation dependencies.
- A dimension cannot be frozen until all blocking documents pass its acceptance criteria.
- A closure cannot be frozen until all dimensions are frozen and implementation readiness reaches 100%.

## Evidence and Audit

For every task, the orchestrator records:

- Behavioural root ID.
- Dimension.
- Document path.
- Section.
- Validator(s) invoked.
- Repair result.
- Validation outcome.
- Commit hash.
- Timestamp.

All evidence is persisted in the governance progress database and exported as closure audit artefacts.
