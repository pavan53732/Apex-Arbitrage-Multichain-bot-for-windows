---
metadata_schema_version: 1.0
document_id: DOC-0072
title: ADR 0003 Plugin First Architecture
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/architecture/decisions/0003-plugin-first-architecture.md
related_concepts:
  - CONCEPT-0072
dependencies:
  - DOC-0110
  - DOC-0282
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
purpose: "Records the architectural decision to use a plugin-first architecture with explicit plugin boundaries, lifecycle, capability registration, sandboxing, and prohibition against bypassing risk/execution controls."
scope: "Plugin boundaries, lifecycle, capability registration, sandboxing, and safety constraints."
---

# ADR 0003: Plugin-First Architecture

## Status
**Accepted** | **Version:** 2.0.0 | **Last Updated:** 2026-08-01

## Context
APEX must support extensibility for new trading strategies, market data providers, execution venues, and analysis capabilities. Without explicit plugin architecture, the system risks plugins bypassing risk controls, unbounded resource consumption, state corruption, and security vulnerabilities.

## Problem
How should APEX enable plugin extensibility while ensuring plugins cannot bypass risk or execution controls, are sandboxed to prevent system-wide failures, and have explicit capability registration and lifecycle?

## Decision
**Adopt a plugin-first architecture with explicit boundaries and safety constraints:**

### Plugin Boundaries

| Boundary | Constraint | Enforcement |
|----------|------------|-------------|
| **Execution** | Cannot execute trades directly | Kernel mediates all execution |
| **Risk** | Cannot bypass risk checks | Risk engine has veto authority |
| **State** | Cannot access global state directly | State API with validation |
| **Resources** | Cannot exceed allocated resources | Kernel enforces quotas |
| **Network** | Cannot make arbitrary network calls | Provider adapters only |
| **Persistence** | Cannot write to database directly | Persistence API with validation |

### Plugin Lifecycle
```
UNLOADED -> LOADING -> LOADED -> ACTIVE -> DEACTIVATED -> UNLOADING -> UNLOADED
                        |
                   FAILED (recovery or terminate)
```

**Lifecycle Ownership:**
- **Kernel** owns: plugin loading, unloading, lifecycle transitions
- **Plugin** owns: local state, task execution, capability implementation
- **Orchestrator** owns: plugin activation, deactivation, coordination

### Capability Registration
**All plugins must register capabilities before activation:**
- `name` — e.g., "triangular_arbitrage_strategy"
- `type` — STRATEGY | PROVIDER | ANALYSIS | EXECUTION
- `authority_level` — READ_ONLY | ADVISORY | EXECUTION
- `required_permissions` — e.g., [MARKET_DATA_READ, EXECUTION_WRITE]
- `resource_limits` — CPU, memory, network quotas

### Sandboxing
**All plugins run in sandboxed environments:**
- **Memory:** Isolated heap, bounds checking
- **CPU:** CPU quotas, time limits
- **Network:** Provider adapters only
- **State:** State API with validation
- **Execution:** Risk engine mediation

### Prohibition Against Bypassing Controls
**Plugins are explicitly prohibited from:**
1. Bypassing risk controls — must go through risk engine
2. Bypassing execution gates — must use execution engine
3. Accessing global state directly — must use state API
4. Exceeding resource limits — kernel enforces quotas
5. Making unauthorized network calls — provider adapters only

## Alternatives Considered

### Alternative 1: No Plugin Architecture
**Rejected** — no extensibility, difficult to maintain, no isolation.

### Alternative 2: Unrestricted Plugins
**Rejected** — plugins could bypass risk controls, single bug could crash system.

### Alternative 3: Static Plugin Loading
**Rejected** — no dynamic strategy deployment, requires restart for updates.

## Consequences

### Positive
- Safe extensibility without compromising system integrity
- Plugin failures isolated, cannot cascade
- Explicit capability registration prevents unauthorized actions
- Sandboxing protects against resource exhaustion
- Risk and execution controls cannot be bypassed

### Negative
- More complex than unrestricted approach
- Sandboxing adds runtime overhead
- Capability registration adds development friction

## Implementation Constraints

1. **Plugins must declare all capabilities** — no implicit capabilities
2. **Plugins must respect risk and execution controls** — risk engine has veto authority
3. **Plugins must not access global state directly** — must use state API
4. **Plugins must not exceed resource quotas** — kernel enforces limits
5. **Plugins must use provider adapters for network calls** — no arbitrary HTTP/RPC

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

Plugin-first architecture is already documented in:
- `../runtime/apex-kernel.md` (Plugin Mode, lifecycle, sandboxing)
- `../runtime/orchestrator.md` (Plugin activation, coordination)
- `../runtime/flow-lifecycle.md` (Plugin lifecycle in flows)
- `../runtime/state-management.md` (Plugin state isolation)

This ADR formalizes those decisions for governance and architectural lineage.
