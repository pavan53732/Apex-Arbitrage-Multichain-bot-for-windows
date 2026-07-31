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
canonical_source: docs/product-specification/architecture/architecture.md
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
- `../execution/trading-engine.md`
- `../execution/execution-engine.md`
- `../ai/ai-pipeline.md`
- `../operations/runtime-operations.md`
- `../data/state-management.md`
- `../market/chain-registry.md`
- `../market/dex-registry.md`
- `../market/token-registry.md`
- `../market/oracle-registry.md`
- `../dashboard/dashboard-layout.md`
- `../dashboard/dashboard-widgets.md`
- `../ui/ux-guidelines.md`
- `../deployment/versioning.md`

- `../interfaces/domain-model.md`


For canonical data contracts, see `../interfaces/domain-model.md`.


## Enterprise Contract – Architecture
- Interfaces: `../interfaces/interface-agent-message.md`, `../interfaces/interface-tool-call.md`.
- State machine: `../runtime/orchestrator.md`, `../execution/trading-lifecycle.md`, `../execution/execution-lifecycle.md`.
- Security boundaries: `../security/security-contracts.md`.
- Performance SLOs: `../performance/performance-slos.md`.
- Failure modes: sequencing failure, ambiguous ownership, runtime drift; recover via authoritative owner docs and orchestrator retry.

For trading lifecycle, see `../execution/trading-lifecycle.md`.
For execution lifecycle, see `../execution/execution-lifecycle.md`.
For event handling, see `../interfaces/event-bus.md`.
For worker scheduling, see `../runtime/worker-pool.md`.
For workspace persistence, see `../dashboard/dashboard-workspaces.md`.
For dependency graph details, see `./dependency-graph.md`.
For live architecture visualization, see `./live-architecture-viewer.md`.
For data governance, see `../data/data-governance.md`.
For constitution and philosophy, see `./apex-os.md`.
For opportunity lifecycle, see `../market/opportunity-lifecycle.md`.
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
