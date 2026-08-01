---
metadata_schema_version: 1.0
document_id: DOC-0077
title: ADR 0008 Orchestrator State Machine
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/architecture/decisions/0008-orchestrator-state-machine.md
related_concepts:
  - CONCEPT-0077
dependencies:
  - DOC-0111
  - DOC-0236
consumers:
  - DOC-0284
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Architecture
type: ADR
purpose: "Records the architectural decision for orchestrator state machine with runtime authority chain: Orchestrator owns sequencing, Runtime Flow Lifecycle owns named flows, State Management owns state/persistence semantics, and Component state machines own local transitions."
scope: "Orchestrator state machine, runtime authority chain, state ownership, and lifecycle coordination."
---

# ADR 0008: Orchestrator State Machine

## Status
**Accepted** | **Version:** 2.0.0 | **Last Updated:** 2026-08-01

## Context
APEX requires a runtime architecture that coordinates multiple subsystems (kernel, orchestrator, workers, state management) with clear authority boundaries and deterministic state transitions. Without explicit state machine ownership, the system risks conflicting state transitions, race conditions, and unclear authority for state changes.

## Problem
How should APEX define orchestrator state machine ownership to ensure:
1. Clear authority chain for runtime operations?
2. Deterministic state transitions across subsystems?
3. No conflicting state changes between components?
4. Proper lifecycle coordination between kernel, orchestrator, and flows?

## Decision
**Adopt orchestrator state machine with explicit runtime authority chain:**

### Runtime Authority Chain

| Authority | Owner | Responsibility |
|-----------|-------|----------------|
| **Sequencing** | Orchestrator | Flow execution order, state transitions |
| **Named Flows** | Runtime Flow Lifecycle | Flow definition, lifecycle, validation |
| **State/Persistence** | State Management | Persistence semantics, snapshots, recovery |
| **Local Transitions** | Component State Machines | Component-specific state transitions |

### State Machine Ownership

```
┌─────────────────────────────────────────────┐
│         Orchestrator (Sequencing)           │
│  - Owns: flow execution order               │
│  - Owns: state transition requests          │
│  - Does NOT own: flow definitions           │
│  - Does NOT own: persistence semantics      │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│    Runtime Flow Lifecycle (Named Flows)     │
│  - Owns: flow definitions                   │
│  - Owns: flow lifecycle validation          │
│  - Does NOT own: execution sequencing       │
│  - Does NOT own: persistence                │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│      State Management (Persistence)         │
│  - Owns: persistence semantics              │
│  - Owns: snapshots and recovery             │
│  - Does NOT own: flow logic                 │
│  - Does NOT own: execution sequencing       │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│   Component State Machines (Local)          │
│  - Owns: local state transitions            │
│  - Owns: component lifecycle                │
│  - Does NOT own: global state               │
│  - Does NOT own: other components           │
└─────────────────────────────────────────────┘
```

### Orchestrator State Machine

```
INITIALIZING -> READY -> RUNNING -> PAUSED -> RUNNING
                    |           |
                    v           v
                STOPPING -> STOPPED
                    |
                    v
                 FAILED
```

**State Definitions:**
- **INITIALIZING:** Orchestrator starting, loading flows
- **READY:** Orchestrator ready, waiting for execution trigger
- **RUNNING:** Orchestrator actively executing flows
- **PAUSED:** Orchestrator paused, flows suspended
- **STOPPING:** Orchestrator shutting down gracefully
- **STOPPED:** Orchestrator stopped, can restart
- **FAILED:** Orchestrator failed, requires recovery

### Authority Boundaries

| Component | Owns | Does NOT Own |
|-----------|------|--------------|
| **Orchestrator** | Sequencing, state transition requests | Flow definitions, persistence |
| **Flow Lifecycle** | Flow definitions, lifecycle validation | Execution sequencing |
| **State Management** | Persistence semantics, snapshots | Flow logic, sequencing |
| **Component SM** | Local state transitions | Global state, other components |

## Alternatives Considered

### Alternative 1: Centralized State Authority
**Approach:** Single authority owns all state transitions.

**Rejected because:**
- Single point of failure
- Bottleneck for concurrent operations
- No isolation between components
- Difficult to scale

### Alternative 2: No State Machine
**Approach:** Components manage state independently without coordination.

**Rejected because:**
- Risk of conflicting state changes
- No deterministic lifecycle
- Difficult to debug and recover
- No audit trail

### Alternative 3: Event-Only Coordination
**Approach:** All state changes via events, no explicit authority.

**Rejected because:**
- Events can be lost or duplicated
- No clear authority for state changes
- Difficult to ensure consistency
- Event ordering challenges

## Consequences

### Positive
- Clear authority chain for runtime operations
- Deterministic state transitions across subsystems
- No conflicting state changes between components
- Proper lifecycle coordination
- Audit trail for state changes
- Easier debugging and recovery

### Negative
- More complex than centralized approach
- Requires discipline to maintain authority boundaries
- Additional coordination overhead

### Neutral
- Orchestrator state machine now documented in canonical architecture
- Implementation must follow authority chain
- Future state changes must preserve ownership invariants

## Implementation Constraints

1. **Orchestrator must not own flow definitions** — Flow Lifecycle owns flow definitions
2. **Flow Lifecycle must not own sequencing** — Orchestrator owns execution order
3. **State Management must not own flow logic** — only persistence semantics
4. **Component SM must not own global state** — only local transitions
5. **State transitions must be atomic** — no partial state changes

## Related Documents

### Canonical Specifications
- `../runtime/orchestrator.md` — Orchestrator canonical specification
- `../runtime/flow-lifecycle.md` — Flow lifecycle ownership
- `../runtime/state-management.md` — State management and persistence

### Architecture
- `../apex-os.md` — Platform constitution and design principles
- `../architecture.md` — System architecture and subsystem boundaries

## Compliance

**This ADR records existing architecture, does not create new decisions.**

Orchestrator state machine is already documented in:
- `../runtime/orchestrator.md` (Orchestrator authority, state machine)
- `../runtime/flow-lifecycle.md` (Flow lifecycle ownership)
- `../runtime/state-management.md` (State persistence semantics)

This ADR formalizes those decisions for governance and architectural lineage.
