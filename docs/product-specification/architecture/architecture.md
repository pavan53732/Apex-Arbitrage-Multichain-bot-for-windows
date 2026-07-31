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
dependencies:
  - DOC-0078
  - DOC-0081
  - DOC-0082
  - DOC-0087
  - DOC-0092
  - DOC-0103
  - DOC-0213
  - DOC-0215
  - DOC-0216
  - DOC-0225
  - DOC-0227
  - DOC-0252
  - DOC-0253
  - DOC-0260
  - DOC-0263
  - DOC-0267
  - DOC-0272
  - DOC-0280
  - DOC-0284
  - DOC-0289
  - DOC-0298
  - DOC-0306
  - DOC-0307
  - DOC-0308
  - DOC-0309
  - DOC-0324
  - DOC-0338
  - DOC-0356
  - DOC-0393
consumers:
  - DOC-0005
  - DOC-0020
  - DOC-0021
  - DOC-0022
  - DOC-0023
  - DOC-0024
  - DOC-0025
  - DOC-0026
  - DOC-0027
  - DOC-0028
  - DOC-0029
  - DOC-0030
  - DOC-0031
  - DOC-0032
  - DOC-0033
  - DOC-0034
  - DOC-0035
  - DOC-0036
  - DOC-0037
  - DOC-0038
  - DOC-0039
  - DOC-0040
  - DOC-0041
  - DOC-0042
  - DOC-0043
  - DOC-0049
  - DOC-0068
  - DOC-0069
  - DOC-0080
  - DOC-0081
  - DOC-0083
  - DOC-0085
  - DOC-0086
  - DOC-0091
  - DOC-0265
  - DOC-0305
  - DOC-0370
  - DOC-0371
  - DOC-0383
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
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
