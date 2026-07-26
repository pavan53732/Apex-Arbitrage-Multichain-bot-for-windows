# App Builder Plugin System

## Document type
This document is an overview, reference, or index as noted below.

# App Builder Plugin System

## Purpose
Defines how the desktop app loads, isolates, versions, and updates plugins.

## Ownership
- Owns plugin discovery, registration, sandboxing, and compatibility checks.
- Does not own plugin business logic or trading strategy policy.

## Plugin contract
- Must define plugin manifest, signature requirements, and version compatibility.
- Must define hot reload, failure isolation, and uninstall behavior.

## Cross-references
- `PLUGIN-LIFECYCLE.md`
- `PLUGIN-MARKETPLACE.md`
- `SECURITY-CONTRACTS.md`
- `SYSTEM-CAPABILITY-REGISTRY.md`
