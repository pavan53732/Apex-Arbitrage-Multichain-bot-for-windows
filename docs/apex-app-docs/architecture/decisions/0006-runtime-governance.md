---
metadata_schema_version: 1.0
document_id: DOC-0075
title: ADR 0006 Runtime Governance
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/architecture/decisions/0006-runtime-governance.md
related_concepts:
  - CONCEPT-0075
dependencies:
  - DOC-0065
  - DOC-0087
  - DOC-0089
  - DOC-0267
consumers:
  - DOC-0087
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Architecture
type: ADR
purpose: "Records the architectural decision for runtime coordination and control with explicit authority chain: APEX Kernel, Orchestrator, Runtime Flow Lifecycle, State Management, and Component state machines."
scope: "Runtime coordination and control authority chain, state ownership, lifecycle coordination, and subsystem boundaries."
---

# ADR 0006: Runtime Governance

## Status
**Accepted** | **Version:** 2.0.0 | **Last Updated:** 2026-08-01

## Context
APEX requires a runtime architecture that coordinates multiple subsystems (kernel, orchestrator, workers, state management) with clear authority boundaries and deterministic state transitions. Without explicit runtime coordination, the system risks conflicting state transitions, race conditions, unclear authority for state changes, and system instability.

This ADR addresses runtime coordination and control, not repository governance or organizational governance.

## Problem
How should APEX structure runtime coordination and control to ensure:
1. Clear authority chain for runtime operations?
2. Deterministic state transitions across subsystems?
3. No conflicting state changes between components?
4. Proper lifecycle coordination between kernel, orchestrator, and flows?
5. State ownership and persistence semantics clearly defined?

## Decision
**Adopt runtime coordination and control with explicit authority chain:**

### Authority Chain

| Authority | Owner | Responsibility |
|-----------|-------|----------------|
| **Kernel Lifecycle** | APEX Kernel | Kernel lifecycle, event infrastructure, service registration, plugin loading |
| **System Sequencing** | Orchestrator | System sequencing, cross-subsystem coordination |
| **Named Flows** | Runtime Flow Lifecycle | Named runtime flows, flow lifecycle validation |
| **State Semantics** | State Management | State semantics, persistence expectations, snapshots, recovery |
| **Local Transitions** | Component State Machines | Local transition rules, component lifecycle |

### Ownership Boundaries

| Component | Owns | Does NOT Own |
|-----------|------|--------------|
| **APEX Kernel** | Kernel lifecycle, event infrastructure, service registration, plugin loading | Orchestrator sequencing, flow definitions, persistent state |
| **Orchestrator** | System sequencing, cross-subsystem coordination | Kernel event bus, all component lifecycle logic, persistent state |
| **Runtime Flow Lifecycle** | Named runtime flows, flow lifecycle validation | Execution sequencing, persistence semantics |
| **State Management** | State semantics, persistence expectations, snapshots, recovery | Flow logic, execution sequencing, component lifecycle |
| **Component State Machines** | Local transition rules, component lifecycle | Global state, other components, kernel events |

### Critical Invariants

1. **Orchestrator does NOT own Kernel event bus**
   - Kernel owns event infrastructure
   - Orchestrator uses event bus, does not own it

2. **Orchestrator does NOT own all component lifecycle logic**
   - Component state machines own local transitions
   - Orchestrator coordinates, does not micromanage

3. **Orchestrator does NOT own persistent state**
   - State Management owns persistence semantics
   - Orchestrator uses persistence API, does not own it

4. **Kernel does NOT own flow definitions**
   - Runtime Flow Lifecycle owns named flows
   - Kernel provides infrastructure, does not define flows

5. **State Management does NOT own flow logic**
   - Flow logic owned by Runtime Flow Lifecycle
   - State Management owns persistence, not business logic

## Alternatives Considered

### Alternative 1: Decentralized Peer Coordination
**Approach:** All components coordinate as peers without central orchestrator.

**Rejected because:**
- No clear authority for system sequencing
- Risk of conflicting state changes
- Difficult to coordinate cross-subsystem operations
- No deterministic lifecycle management

### Alternative 2: Event-Only Coordination
**Approach:** All coordination via events, no orchestrator or explicit authority.

**Rejected because:**
- Events can be lost or duplicated
- No clear authority for state changes
- Difficult to ensure consistency
- Event ordering challenges

### Alternative 3: Ad Hoc Component-Managed Sequencing
**Approach:** Each component manages its own sequencing independently.

**Rejected because:**
- No global coordination
- Risk of race conditions and conflicts
- Difficult to debug and recover
- No audit trail for state changes

### Alternative 4: Centralized Control
**Approach:** Single authority owns all runtime coordination and control.

**Rejected because:**
- Single point of failure
- Bottleneck for concurrent operations
- No isolation between components
- Difficult to scale

## Consequences

### Positive
- ✅ Clear authority chain for runtime operations
- ✅ Deterministic state transitions across subsystems
- ✅ No conflicting state changes between components
- ✅ Proper lifecycle coordination
- ✅ Audit trail for state changes
- ✅ Easier debugging and recovery

### Negative
- ⚠️ More complex than ad hoc approach
- ⚠️ Requires discipline to maintain authority boundaries
- ⚠️ Additional coordination overhead

### Neutral
- Runtime coordination now documented in canonical architecture
- Implementation must follow authority chain
- Future runtime changes must preserve ownership invariants

## Implementation Constraints

1. **Kernel owns event infrastructure** — Orchestrator uses but does not own
2. **Orchestrator owns sequencing** — but does not own component lifecycle or persistence
3. **Flow Lifecycle owns named flows** — Kernel provides infrastructure
4. **State Management owns persistence** — not flow logic or execution
5. **Component SM owns local transitions** — not global state or other components

## Related Canonical Specifications

### Detailed Specifications
- `../architecture/apex-kernel.md` — APEX Kernel canonical specification
- `../runtime/orchestrator.md` — Orchestrator canonical specification
- `../runtime/runtime-flow-lifecycle.md` — Runtime flow lifecycle ownership
- `../data/state/state-management.md` — State management and persistence semantics

### Architecture
- `../architecture.md` — System architecture and subsystem boundaries
- `../apex-os.md` — Platform constitution and design principles

## Compliance

**This ADR records existing architecture, does not create new decisions.**

Runtime governance decision is already documented in:
- `../architecture/apex-kernel.md` (Kernel ownership, lifecycle)
- `../runtime/orchestrator.md` (Orchestrator authority, sequencing)
- `../runtime/runtime-flow-lifecycle.md` (Flow lifecycle ownership)
- `../data/state/state-management.md` (State persistence semantics)

This ADR formalizes the runtime coordination decision for governance and lineage.

**Authority Boundary:**
- ADR records runtime coordination and control decision
- `apex-kernel.md` owns Kernel behavior and lifecycle
- `orchestrator.md` owns Orchestrator behavior and sequencing
- `runtime-flow-lifecycle.md` owns named flow lifecycle
- `state-management.md` owns state semantics and persistence
