---
metadata_schema_version: 1.0
document_id: DOC-0071
title: ADR 0002 Event Driven Kernel
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/architecture/decisions/0002-event-driven-kernel.md
related_concepts:
  - CONCEPT-0071
dependencies:
  - DOC-0110
  - DOC-0111
consumers:
  - DOC-0236
  - DOC-0284
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Architecture
type: ADR
purpose: "Records the architectural decision to use an event-driven kernel architecture with APEX Kernel, Orchestrator, workers, lifecycle, and state ownership."
scope: "Event-driven kernel pattern, ownership boundaries, lifecycle, and state management."
---

# ADR 0002: Event-Driven Kernel

## Status
**Accepted** | **Version:** 2.0.0 | **Last Updated:** 2026-08-01

## Context
APEX requires a kernel architecture that supports:
- Asynchronous, non-blocking execution
- Concurrent worker execution across multiple chains and strategies
- Deterministic lifecycle management
- Clear state ownership and persistence
- Plugin extensibility without compromising kernel stability

Traditional request-response architectures are insufficient because:
- Market data arrives asynchronously from multiple sources
- Trading decisions must be made in real-time with low latency
- Multi-chain execution requires parallel processing
- System must remain responsive during long-running operations

## Problem
How should APEX structure its kernel to achieve:
1. High-throughput, low-latency event processing?
2. Clear ownership between kernel, orchestrator, and workers?
3. Deterministic lifecycle and state management?
4. Plugin extensibility without kernel instability?

## Decision
**Adopt an event-driven kernel architecture with explicit ownership boundaries:**

### Architecture Layers

```
┌─────────────────────────────────────────────┐
│           APEX Kernel (Kernel Mode)         │
│  - Event bus, worker lifecycle, state store │
│  - Owns: event dispatch, worker spawning    │
│  - Does NOT own: business logic, trading    │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         Orchestrator (User Mode)            │
│  - Sequencing, coordination, supervision    │
│  - Owns: flow execution, state transitions  │
│  - Does NOT own: kernel events, persistence │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         Workers (Plugin Mode)               │
│  - Strategy execution, market analysis      │
│  - Owns: local state, task completion       │
│  - Does NOT own: kernel state, other workers│
└─────────────────────────────────────────────┘
```

### Ownership Boundaries

| Component | Owns | Does NOT Own |
|-----------|------|--------------|
| **APEX Kernel** | Event bus, worker lifecycle, state persistence | Business logic, trading decisions |
| **Orchestrator** | Sequencing, coordination, flow state | Kernel events, worker implementation |
| **Workers** | Local state, task completion, strategy logic | Kernel state, other workers, global state |
| **State Management** | Persistence semantics, snapshots, recovery | Business logic, event dispatch |

### Event-Driven Kernel Characteristics

1. **Event Bus**
   - Typed events with schema validation
   - Async dispatch with delivery guarantees
   - Event routing to interested workers
   - Event sourcing for audit trail

2. **Worker Lifecycle**
   - Spawn: Kernel creates worker on demand
   - Execute: Worker processes assigned tasks
   - Complete: Worker reports completion or failure
   - Terminate: Kernel cleans up worker resources

3. **State Ownership**
   - Kernel owns global state store
   - Workers own local state (task-specific)
   - Orchestrator owns flow state (sequencing)
   - State Management owns persistence semantics

4. **Lifecycle Management**
   - Kernel: INITIALIZING → READY → RUNNING → STOPPING → STOPPED
   - Worker: IDLE → EXECUTING → COMPLETED → TERMINATED
   - Flow: CREATED → RUNNING → COMPLETED | FAILED

### State Machine Ownership

| State Machine | Owner | Authority |
|---------------|-------|-----------|
| **Kernel State** | APEX Kernel | Runtime lifecycle |
| **Orchestrator State** | Orchestrator | Flow sequencing |
| **Worker State** | Worker | Task execution |
| **Component State** | Component Owner | Local transitions |

## Alternatives Considered

### Alternative 1: Monolithic Kernel
**Approach:** All logic in kernel, no separation between kernel and workers.

**Rejected because:**
- No isolation between components
- Single failure can crash entire system
- Difficult to scale horizontally
- Plugin extensibility impossible

### Alternative 2: Request-Response Kernel
**Approach:** Synchronous request-response between kernel and workers.

**Rejected because:**
- Blocking I/O reduces throughput
- Cannot handle async market data efficiently
- Latency increases with worker count
- Poor resource utilization

### Alternative 3: Microservices Architecture
**Approach:** Each component as separate microservice.

**Rejected because:**
- Overkill for single-node deployment
- Increased operational complexity
- Network latency for inter-component communication
- Unnecessary for Phase 1/2 scope

## Consequences

### Positive
- ✅ High-throughput, low-latency event processing
- ✅ Clear ownership boundaries prevent coupling
- ✅ Deterministic lifecycle and state management
- ✅ Plugin extensibility without kernel instability
- ✅ Horizontal scalability via worker spawning
- ✅ Audit trail via event sourcing

### Negative
- ⚠️ More complex than monolithic approach
- ⚠️ Requires discipline to maintain ownership boundaries
- ⚠️ Event bus adds infrastructure overhead

### Neutral
- Event-driven architecture now documented in canonical architecture
- Implementation must follow ownership boundaries
- Future kernel changes must preserve ownership invariants

## Implementation Constraints

1. **Kernel must not contain business logic** — only event dispatch and lifecycle
2. **Orchestrator must not own kernel events** — only flow state
3. **Workers must not share state** — each worker isolated
4. **State Management must own persistence** — kernel and orchestrator use persistence API
5. **Event schema must be versioned** — backward compatibility required

## Related Documents

### Canonical Specifications
- `../runtime/apex-kernel.md` — APEX Kernel canonical specification
- `../runtime/orchestrator.md` — Orchestrator canonical specification
- `../runtime/flow-lifecycle.md` — Flow lifecycle ownership
- `../runtime/state-management.md` — State management and persistence

### Architecture
- `../apex-os.md` — Platform constitution and design principles
- `../architecture.md` — System architecture and subsystem boundaries

## Compliance

**This ADR records existing architecture, does not create new decisions.**

Event-driven kernel architecture is already documented in:
- `../runtime/apex-kernel.md` (Kernel Mode, ownership, lifecycle)
- `../runtime/orchestrator.md` (Orchestrator authority, state machine)
- `../runtime/flow-lifecycle.md` (Flow lifecycle ownership)
- `../runtime/state-management.md` (State persistence semantics)

This ADR formalizes those decisions for governance and architectural lineage.
