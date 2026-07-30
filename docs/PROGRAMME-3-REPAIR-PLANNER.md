---
type: SPECIFICATION
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Defines the Repair Planner engine for Programme 3, responsible for transforming validator findings into deterministic repair tasks.
scope: Maps validator findings to canonical owners, sections, and repair steps for closure dimensions.
last_updated: 2026-07-29
canonical_source: docs/PROGRAMME-3-REPAIR-PLANNER.md
---

# Programme 3 Repair Planner

## Summary

The Repair Planner is a governance engine that converts validator findings into small, deterministic repair tasks. It removes ad-hoc decision making from AI agents by:

- Identifying canonical owners for each finding.
- Selecting the required document section based on the dimension.
- Assembling a repair task with explicit acceptance criteria.
- Ensuring the repair touches only the canonical owner document.
- Recording evidence and validation results.

## Responsibilities

- Consume validator findings across all maturity dimensions.
- Classify each finding into the gap taxonomy (metadata, ownership, dependency, interface, event, configuration, schema, state machine, recovery, security, validation, testing, performance, cross reference, duplicate authority, thin stub, missing algorithm, missing sequence, missing failure behaviour, missing lifecycle, missing contract).
- Map each finding to:
  - Behavioural root.
  - Dimension.
  - Canonical owner document.
  - Required section.
- Generate repair tasks with deterministic acceptance criteria.
- Dispatch repair tasks to AI workers or automated generators.
- Validate repairs via governance validators.
- Mark findings as resolved and update closure maturity.

## Repair Task Model

A repair task is defined as:

- `root_path`: Behavioural root.
- `dimension`: Maturity dimension (STRUCTURE, INTERFACE, EVENT, CONFIGURATION, SCHEMA, STATE_MACHINE, RECOVERY, SECURITY, VALIDATION, ALGORITHM).
- `document_path`: Canonical owner document.
- `section`: Section within the document (e.g., Events Produced, Interfaces, Configuration Keys).
- `finding_category`: Gap taxonomy category.
- `acceptance_criteria`: Deterministic checklist for the section.
- `validator_ids`: Validators that must pass.
- `status`: PENDING | IN_PROGRESS | COMPLETE.

## Example Task

Task 000184

- Root: `docs/ai/orchestration/AI-ORCHESTRATION.md`.
- Dimension: `EVENT`.
- Document: `docs/ai/runtime/AI-GATEWAY.md`.
- Section: `Events Produced`.
- Acceptance:
  - Producer defined.
  - Consumer(s) defined.
  - Payload schema defined.
  - Ordering specified.
  - Delivery semantics defined.
  - Retry policy defined.
  - Dead-letter handling defined.
  - Version compatibility defined.
  - Ownership documented.
- Validators:
  - `event_contract_validator`.
  - `schema_version_validator`.

Once all acceptance criteria pass and validators succeed, the task is marked COMPLETE and the dimension maturity is updated.

## Deterministic Repair Rules

The planner applies the Programme 3 repair rules:

- Always repair the canonical owner document.
- Never duplicate authority.
- Never move ownership.
- Never create competing contracts.
- Never invent a new subsystem.
- Only deepen existing canonical documents.

## Integration with Orchestrator

The Repair Planner integrates with the Closure Orchestrator via:

- `plan_repairs(dimension_tasks) -> list[RepairTask]`.
- `execute_repair(task) -> RepairResult`.
- `validate_repair(task) -> ValidationResult`.
- `mark_task_complete(task)`.

The orchestrator remains responsible for execution order; the planner remains responsible for mapping findings to deterministic repairs.
