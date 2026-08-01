---
metadata_schema_version: 1.0
document_id: DOC-0079
title: Architecture
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Architecture Team
version: 1.0.0
canonical_source: docs/apex-app-docs/architecture/architecture.md
related_concepts:
  - CONCEPT-0079
dependencies: []
consumers:
  - DOC-0068
  - DOC-0069
  - DOC-0360
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Architecture
type: REFERENCE
purpose: Architecture documentation.
scope: Reference documentation.
---

# Architecture

## Document type
Document type: [OVERVIEW]

# Architecture

## Purpose
Defines the system architecture, subsystem boundaries, and orchestration model.

## System layers
- Desktop shell and renderer UI.
- Typed IPC and preload bridge.
- Main-process services and orchestrators.
- Domain engines and adapters.
- Persistence, monitoring, and operator tooling.

## Canonical boundaries
- Trading decisions are owned by the trading engine.
- Transaction submission and reconciliation are owned by the execution engine.
- Price, liquidity, and route viability are owned by market data, liquidity analysis, routing, slippage, gas, and MEV subsystems.
- Durable history is owned by the database schema and repository layer.
- Runtime coordination is owned by runtime operations.

## Deterministic orchestration rules
For authoritative runtime flow, see `../runtime/orchestrator.md`.
- Main process is the source of truth for operational state. For authoritative runtime flow, see `../runtime/orchestrator.md`.
- Renderer state is derived and must not bypass typed IPC.
- Risk gates must execute before any live submission.
- For the authoritative runtime state machine and orchestration flow, see `../runtime/orchestrator.md`.
- Recovery must reconcile persisted state before new execution is admitted.

## Cross-references
- `../execution/trading/trading-engine.md`
- `../execution/transactions/execution-engine.md`
- `../ai/runtime/ai-pipeline.md`
- `../operations/reliability/runtime-operations.md`
- `../data/state/state-management.md`
- `../market/chains/chain-registry.md`
- `../market/dex/dex-registry.md`
- `../market/tokens/token-registry.md`
- `../market/tokens/oracle-registry.md`
- `../dashboard/dashboard-layout.md`
- `../dashboard/dashboard-widgets.md`
- `../ui/ux-guidelines.md`
- `../deployment/versioning.md`

- `../interfaces/api/domain-model.md`


For canonical data contracts, see `../interfaces/api/domain-model.md`.


## Enterprise Contract – Architecture
- Interfaces: `../interfaces/messages/interface-agent-message.md`, `../interfaces/messages/interface-tool-call.md`.
- State machine: `../runtime/orchestrator.md`, `../execution/trading/trading-lifecycle.md`, `../execution/transactions/execution-lifecycle.md`.
- Security boundaries: `../security/security-contracts.md`.
- Performance SLOs: `../performance/performance-slos.md`.
- Failure modes: sequencing failure, ambiguous ownership, runtime drift; recover via authoritative owner docs and orchestrator retry.

For trading lifecycle, see `../execution/trading/trading-lifecycle.md`.
For execution lifecycle, see `../execution/transactions/execution-lifecycle.md`.
For event handling, see `../interfaces/events/event-bus.md`.
For worker scheduling, see `../runtime/worker-pool.md`.
For workspace persistence, see `../dashboard/dashboard-workspaces.md`.
For dependency graph details, see `./dependency-graph.md`.
For live architecture visualization, see `./live-architecture-viewer.md`.
For data governance, see `../data/knowledge/data-governance.md`.
For constitution and philosophy, see `./apex-os.md`.
For opportunity lifecycle, see `../market/opportunities/opportunity-lifecycle.md`.
## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Ownership boundary
- This document describes system boundaries and layering only.
- It does not own trading logic, execution logic, provider selection, registry records, or lifecycle behavior.
- Those responsibilities remain with their authoritative owner documents.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.

## Authority Boundary

**This document is the whole-system canonical architecture reference.**

- **Owns:** System architecture, subsystem boundaries, cross-subsystem relationships, authority chain documentation, overall component model.
- **Does NOT own:** Implementation details, subsystem internal behavior, kernel-specific behavior (owned by APEX Kernel), runtime sequencing (owned by Orchestrator), flow definitions (owned by Runtime Flow Lifecycle), state semantics (owned by State Management), component state machines (owned by respective components).
- **Authority level:** Canonical — subordinate to `apex-os.md` (constitution), superior to all subsystem architecture docs.
- **Superordinate document:**
  - `apex-os.md` — Platform constitution and design principles
- **Subordinate documents:**
  - `apex-kernel.md` — Kernel lifecycle, event infrastructure, service registration, plugin loading
  - `orchestrator.md` — Runtime sequencing, cross-subsystem coordination
  - `runtime-flow-lifecycle.md` — Named flow definitions and lifecycle
  - `state-management.md` — State semantics, persistence expectations, synchronization rules
  - All component state machine documents — local transition behavior

**Authority hierarchy (unidirectional, documentation only):**
```
APEX OS (constitution)
  → Architecture (this doc — whole-system canonical reference)
    → APEX Kernel (kernel-specific behavior)
      → Orchestrator (runtime sequencing)
        → Runtime Flow Lifecycle (named flows)
          → State Management (state/persistence semantics)
            → Component State Machines (local transitions)
```

**Cross-references are navigational or dependency references, not circular authority delegation.** This document documents the architecture; it does not replace detailed canonical subsystem specifications.

**This document defers to `apex-os.md` for platform constitution and design principles.** It defers to subsystem docs for implementation details.
