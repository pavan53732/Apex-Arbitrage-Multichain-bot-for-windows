---
last_updated: 2026-07-29
type: REFERENCE
owner: UI Team
status: Canonical
version: 1.0.0
purpose: Non Functional Requirements documentation.
scope: Reference documentation.
canonical_source: docs/NON-FUNCTIONAL-REQUIREMENTS.md
---

# Non Functional Requirements

## Document type
This document is an overview, reference, or index as noted below.

# Non-Functional Requirements

## Purpose
Defines global performance, reliability, security, maintainability, and operability goals.

## Requirements
- Deterministic decisions for the same input snapshot and configuration.
- Fail-closed behavior on invalid risk, security, or freshness conditions.
- Structured logging and observability for all critical paths.
- Recoverability after crash, restart, queue failure, and chain reorg.
- Bounded latency for execution, reconciliation, and operator-facing workflows.
- Cloud AI must use paid API keys only in production.
- AI costs must be measurable, capped, and visible per session and provider.
- Local LLM inference must not be assumed by any production requirement.

## Reliability goals
- No silent data loss on execution, order, transaction, or risk state changes.
- No duplicate side effects from retried idempotent operations.
- Durable state must be restorable from persistence after restart.
- Recovery workflows must reconcile state before resuming live work.

## Security goals
- Secrets and signing material must never be exposed in logs or telemetry.
- Privileged operations must be gated by policy and permission checks.
- AI prompt and output handling must not leak sensitive internal state.

## Maintainability goals
- Every subsystem must have a single authoritative owner document.
- Cross-cutting rules must be centralized rather than duplicated.
- Configuration names, error codes, and event names must remain stable.

## Operability goals
- Operators must see health, alerts, recovery state, and queue pressure.
- Diagnostics must be exportable without compromising secrets.
- Backups, restores, and upgrades must be auditable and reproducible.

## Cross-references
- `docs/PERFORMANCE-TARGETS.md`
- `docs/security/SECURITY.md`
- `docs/MONITORING-OBSERVABILITY.md`
- `docs/ai/runtime/AI-PIPELINE.md`
- `docs/RUNTIME-OPERATIONS.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Windows requirements
- Must define performance, reliability, and security requirements for Windows.

## Required details
- Define Windows performance, reliability, and security targets.

## Requirements
- Define Windows performance, reliability, security, and recoverability targets.
- Define latency and startup expectations.

## NFR rules
- Define latency, reliability, durability, and supportability targets.
- Define Windows desktop and service constraints.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
