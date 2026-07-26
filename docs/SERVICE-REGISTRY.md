# Service Registry

## Purpose
Defines the canonical registration and lookup mechanism for runtime services.

## Contract
Nothing instantiates services directly; everything registers with the kernel-managed registry.

## State machine
```mermaid
stateDiagram-v2
  [*] --> UNREGISTERED
  UNREGISTERED --> REGISTERING
  REGISTERING --> AVAILABLE
  AVAILABLE --> SUSPENDED
  SUSPENDED --> AVAILABLE
  AVAILABLE --> RETIRED
```

## Validation
Service identifiers must be unique, stable, and versioned.

## Failure modes
Duplicate registration, stale service reference, unavailable dependency, version mismatch.

## Recovery
Unregister stale services, rebind dependencies, and rehydrate from kernel state.

## Cross-references
- `APEX-KERNEL.md`
- `REGISTRY-SYSTEM.md`
- `ORCHESTRATOR.md`

## Governance Rules
Defines service identity, registration, status, ownership, and versioned service metadata.

## Example
A service entry exposes health, version, and lifecycle state before it is scheduled.

## Required details
- Define SCM mapping, dependencies, recovery, and lookup.
