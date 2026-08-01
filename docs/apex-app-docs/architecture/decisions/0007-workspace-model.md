---
metadata_schema_version: 1.0
document_id: DOC-0076
title: ADR 0007 Workspace Model
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/architecture/decisions/0007-workspace-model.md
related_concepts:
  - CONCEPT-0076
dependencies:
  - DOC-0100
  - DOC-0267
  - DOC-0089
consumers:
  - DOC-0100
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Architecture
type: ADR
purpose: "Records the architectural decision to implement workspace model for operator/dashboard context separation, active views, configuration scope, and applicable runtime context, while maintaining global risk, execution, wallet, and security controls."
scope: "Workspace isolation decision, user-context separation, configuration scope, and workspace state alignment with state management and flow lifecycle."
---

# ADR 0007: Workspace Model

## Status
**Accepted** | **Version:** 2.0.0 | **Last Updated:** 2026-08-01

## Context
APEX requires a workspace model to separate operator/dashboard context, active views, configuration scope, and applicable runtime context. Workspaces enable multiple operators to work with different configurations, views, and contexts without interfering with each other.

However, workspace isolation must not bypass global risk, execution, wallet, or security controls. Workspace state must align with State Management and Runtime Flow Lifecycle. The decision does not require full operating-system process isolation unless explicitly specified.

## Problem
How should APEX implement workspace model to:
1. Separate operator/dashboard context and active views?
2. Support configuration scope and applicable runtime context?
3. Maintain global risk, execution, wallet, and security controls?
4. Align workspace state with State Management and Flow Lifecycle?
5. Avoid unnecessary complexity (full OS process isolation)?

## Decision
**Implement workspace model for operator/dashboard context separation, active views, configuration scope, and applicable runtime context, while maintaining global risk, execution, wallet, and security controls.**

### Key Principles

1. **Workspace Isolation**
   - Workspaces separate operator/dashboard context
   - Active views and configuration scope are workspace-specific
   - Applicable runtime context is workspace-scoped

2. **Global Controls Preserved**
   - Workspace isolation does not bypass global risk controls
   - Workspace isolation does not bypass execution controls
   - Workspace isolation does not bypass wallet controls
   - Workspace isolation does not bypass security controls

3. **Workspace Manager Ownership**
   - Workspace Manager is detailed owner of workspace behavior
   - Workspace Manager owns workspace lifecycle and state
   - Workspace Manager coordinates with State Management and Flow Lifecycle

4. **State Alignment**
   - Workspace state aligns with State Management
   - Workspace state aligns with Runtime Flow Lifecycle
   - Workspace state is application state, not global state

5. **No Full OS Process Isolation**
   - Decision does not require full OS process isolation
   - Workspace isolation is application-level, not process-level
   - Unless explicitly specified in canonical specifications

## Alternatives Considered

### Alternative 1: Single Global Workspace
**Approach:** One global workspace for all operators and contexts.

**Rejected because:**
- No separation between operators
- Configuration conflicts
- Context mixing
- Poor user experience for multi-operator scenarios

### Alternative 2: No Persisted Workspace State
**Approach:** Workspaces exist but state is not persisted.

**Rejected because:**
- No continuity across sessions
- Configuration must be re-entered each time
- Poor user experience
- Lost context and views

### Alternative 3: Full OS Process Isolation
**Approach:** Each workspace runs in separate OS process.

**Rejected because:**
- Overly complex for application needs
- High resource overhead
- Difficult to coordinate across workspaces
- Better suited for security-critical isolation, not workspace context

### Alternative 4: Complete Process Isolation with Shared State
**Approach:** Full process isolation but shared state across workspaces.

**Rejected because:**
- Contradiction in isolation approach
- Complexity without clear benefit
- Shared state defeats isolation purpose
- Better to use application-level isolation

## Consequences

### Positive
- ✅ Operator/dashboard context separation
- ✅ Active views and configuration scope isolation
- ✅ Applicable runtime context per workspace
- ✅ Global risk, execution, wallet, security controls preserved
- ✅ Workspace state aligns with State Management and Flow Lifecycle
- ✅ No unnecessary OS process isolation complexity

### Negative
- ⚠️ Workspace implementation adds complexity
- ⚠️ Must coordinate workspace state with State Management
- ⚠️ Must coordinate workspace lifecycle with Flow Lifecycle
- ⚠️ Additional validation to ensure global controls not bypassed

### Neutral
- Workspace model is application-level isolation, not process-level
- Implementation must follow Workspace Manager specification
- Future workspace enhancements must preserve global controls

## Implementation Constraints

1. **Workspace isolation does not bypass global controls** — risk, execution, wallet, security
2. **Workspace Manager owns workspace behavior** — detailed specification
3. **Workspace state aligns with State Management** — not global state
4. **Workspace state aligns with Flow Lifecycle** — coordinated lifecycle
5. **No full OS process isolation required** — application-level isolation only

## Related Canonical Specifications

### Detailed Specifications
- `../runtime/workspace-manager.md` — Workspace Manager canonical specification
- `../data/state/state-management.md` — State management and persistence semantics
- `../runtime/runtime-flow-lifecycle.md` — Runtime flow lifecycle ownership

### Architecture
- `../architecture.md` — System architecture and workspace integration
- `../apex-os.md` — Platform constitution and workspace principles

## Compliance

**This ADR records existing architecture, does not create new decisions.**

Workspace model decision is already documented in:
- `../runtime/workspace-manager.md` (Workspace Manager behavior)
- `../data/state/state-management.md` (State management and persistence)
- `../runtime/runtime-flow-lifecycle.md` (Flow lifecycle coordination)

This ADR formalizes the workspace model decision for governance and lineage.

**Authority Boundary:**
- ADR records workspace model decision
- `workspace-manager.md` owns detailed workspace behavior
- `state-management.md` owns state semantics and persistence
- `runtime-flow-lifecycle.md` owns flow lifecycle coordination
- Global risk, execution, wallet, security controls owned by respective canonical specifications
