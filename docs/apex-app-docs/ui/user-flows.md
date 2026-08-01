---
metadata_schema_version: 1.0
document_id: DOC-0396
title: User Flows
plane: Product Specification
domain: UI
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ui/user-flows.md
related_concepts:
  - CONCEPT-0396
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - UI
type: REFERENCE
purpose: User Flows documentation.
scope: Reference documentation.
---

# User Flows

## Document type
This document is an overview, reference, or index as noted below.

# User Flows

## Purpose
Defines major user workflows from onboarding through live trading, monitoring, emergency stop, crash recovery, backup, restore, updates, export/import, and settings management.

## Workflow contract
Every workflow defines preconditions, user actions, system actions, validation rules, decision points, sequence, state transitions, success path, failure path, recovery path, and completion criteria.

## Onboarding
Preconditions: app installed and launched.
User actions: create or import config, connect providers, verify settings.
System actions: validate configuration, hydrate defaults, test dependencies.
Validation rules: required fields and credentials must pass.
Decision points: provider selection and security confirmation.
State transitions: uninitialized -> configured -> ready.
Success path: user reaches dashboard.
Failure path: validation failure blocks progression.
Recovery path: correct config and re-submit.
Completion criteria: onboarding state saved.

## Live trading setup
Preconditions: valid config and healthy environment.
User actions: choose mode, strategy, risk profile, and AI policy.
System actions: load state, test health, lock session settings.
Validation rules: risk, market, wallet, and provider checks.
Decision points: manual approval or autonomous mode.
State transitions: ready -> armed -> live.
Success path: session becomes active.
Failure path: blocked by policy or unhealthy dependency.
Recovery path: fix condition and re-arm.
Completion criteria: live session recorded.

## Monitoring
Preconditions: session active or paused.
User actions: inspect health, alerts, PnL, queue, and AI status.
System actions: stream telemetry and update dashboards.
Validation rules: display authoritative state only.
Decision points: acknowledge or escalate alerts.
State transitions: active -> monitored.
Success path: operator remains informed.
Failure path: missing telemetry or stale view.
Recovery path: refresh and re-sync state.
Completion criteria: operator acknowledges state.

## Emergency stop
Preconditions: active or armed session.
User actions: trigger stop.
System actions: halt planning, stop execution, reconcile state.
Validation rules: stop must always win.
Decision points: confirm if configured.
State transitions: active -> stopping -> halted.
Success path: no new work admitted.
Failure path: unresolved in-flight work.
Recovery path: reconcile then reset.
Completion criteria: session safe-halted.

## Crash recovery
Preconditions: app restarts after crash.
User actions: relaunch app.
System actions: restore persisted state, reconcile queues and sessions.
Validation rules: durable state is authoritative.
Decision points: manual reset may be required.
State transitions: crashed -> recovering -> restored.
Success path: state matches persistence.
Failure path: recovery mismatch.
Recovery path: re-run reconciliation.
Completion criteria: work resumes safely or remains halted.

## Backup and restore
Preconditions: operator has backup access.
User actions: create backup or restore from backup.
System actions: export/import verified encrypted state.
Validation rules: integrity and version compatibility.
Decision points: select restore point.
State transitions: normal -> backing_up -> backed_up; restored -> validated.
Success path: data preserved and usable.
Failure path: corrupt or incompatible backup.
Recovery path: choose alternate backup.
Completion criteria: verified backup or restore.

## Updates and migration
Preconditions: new release available.
User actions: approve update.
System actions: stage upgrade, migrate state, verify compatibility.
Validation rules: version and migration checks.
Decision points: rollout or rollback.
State transitions: current -> upgrading -> migrated -> active.
Success path: app runs on new version.
Failure path: migration error.
Recovery path: rollback and restore.
Completion criteria: upgraded and verified.

## Export and import
Preconditions: user has export or import permission.
User actions: export settings/data or import a package.
System actions: serialize or validate package.
Validation rules: schema, integrity, and security checks.
Decision points: overwrite or merge.
State transitions: idle -> exporting/importing -> complete.
Success path: usable data transferred.
Failure path: validation error.
Recovery path: retry with corrected package.
Completion criteria: package applied or saved.

## Settings management
Preconditions: authenticated user.
User actions: edit AI, risk, provider, strategy, or UI settings.
System actions: validate, persist, and reconfigure subsystems.
Validation rules: immutable policy settings cannot be violated.
Decision points: save, discard, or revert.
State transitions: editing -> validating -> saved.
Success path: settings applied.
Failure path: invalid or unsafe settings.
Recovery path: restore last valid config.
Completion criteria: settings confirmed.

## Cross-references
- `../execution/trading/trading-engine.md`
- `../operations/reliability/runtime-operations.md`
- `../ai/runtime/ai-pipeline.md`
- `../security/security.md`
- `../configuration/core/configuration.md`
- `../dashboard/dashboard-layout.md`
- `../dashboard/dashboard-widgets.md`
- `./ux-guidelines.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
