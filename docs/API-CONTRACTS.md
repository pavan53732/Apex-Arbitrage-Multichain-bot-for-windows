---
last_updated: 2026-07-29
type: CONTRACT
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Api Contracts documentation.
scope: Reference documentation.
canonical_source: docs/API-CONTRACTS.md
---

# Api Contracts

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Document type
This document is an overview, reference, or index as noted below.

# API-CONTRACTS.md

## Purpose
Defines internal service API contracts and external adapter contracts for APEX. This file is the contract-level counterpart to [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md) and [`PROJECT-STRUCTURE.md`](./PROJECT-STRUCTURE.md).

## Scope
Service interfaces, repository contracts, provider contracts, return-shape conventions, error semantics, and lifecycle expectations.

## Ownership
- `packages/core` owns shared service abstractions.
- Feature packages own their own interfaces.
- UI code consumes only stable adapter interfaces or IPC endpoints.

## Contract Design Rules
- All external boundaries must be typed.
- All contract payloads must be serializable.
- Contracts must reject unknown fields where security or correctness depends on strict validation.
- Every contract must define success shape, error shape, and retry semantics.

## Core Service Interfaces
| Interface | Responsibility | Owner |
|---|---|---|
| `ConfigService` | resolves validated runtime config | `packages/config` |
| `Logger` | structured logging and redaction | `packages/logging` |
| `DbService` | database access and migrations | `packages/db` |
| `AiOrchestrator` | prompt assembly, provider routing, schema validation | `packages/ai-orchestrator` |
| `StrategyEngine` | strategy lifecycle and evaluation | `packages/strategy-engine` |
| `RiskEngine` | validate, size, approve, or reject actions | `packages/risk-engine` |
| `ChainClient` | chain reads and transaction submission | `packages/chain-clients` |
| `DexClient` | quote, route, and calldata generation | `packages/dex-clients` |

## Service Contract Shape
Every service should define:
- input schema,
- output schema,
- error codes,
- side-effect notes,
- idempotency expectations,
- concurrency expectations.

## AI Contract Requirements
AI-oriented contracts must include:
- provider id,
- model id,
- prompt/task id,
- structured response schema,
- token/timeout budget,
- fallback behavior.

## Trading Contract Requirements
Trading-related contracts must include:
- chain id,
- asset identifiers,
- quote id,
- slippage ceiling,
- fee assumptions,
- risk state snapshot,
- execution mode.

## Contract Ownership by Domain
### Configuration
- `loadConfig()` returns a validated app config object.
- No consumer may mutate config in place.

### Strategy
- `registerStrategy()`, `listStrategies()`, `runStrategy()`, `disableStrategy()`.
- Strategy execution must be cancelable and observable.

### Risk
- `evaluateRisk()`, `computePositionSize()`, `isExecutionAllowed()`.
- Returns must clearly identify reject reasons.

### AI
- `requestAnalysis()`, `routeTask()`, `validateStructuredResponse()`.
- Provider failures must be distinguishable from validation failures.

### Database
- repositories expose query-by-purpose methods; no generic arbitrary query surfaces unless explicitly approved.

## Versioning and Compatibility
- Stable contracts require version identifiers.
- Breaking changes must introduce versioned endpoints or a migration path.
- Deprecated contracts must be documented with replacement and removal timeline.

## Cross-References
- [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md)
- [`MODULE-DEPENDENCY.md`](./MODULE-DEPENDENCY.md)
- [`STATE-MANAGEMENT.md`](./STATE-MANAGEMENT.md)
- [`ERROR-HANDLING-LOGGING.md`](./ERROR-HANDLING-LOGGING.md)

## Cross-references
- `deployment/VERSIONING.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Transport contracts
- Must define error mapping, versioning, and protocol compatibility.

## Required details
- Define transport and error compatibility.

## Transport contracts
- Define request/response shapes, error mapping, and protocol compatibility.
- Define Windows IPC and external client boundaries if applicable.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
