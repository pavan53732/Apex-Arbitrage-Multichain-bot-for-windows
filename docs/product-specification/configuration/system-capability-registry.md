---
metadata_schema_version: 1.0
document_id: DOC-0384
title: System Capability Registry
plane: Product Specification
domain: Configuration
class: Registry
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/configuration/system-capability-registry.md
related_concepts:
  - CONCEPT-0384
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Configuration
type: REFERENCE
purpose: System Capability Registry documentation.
scope: Reference documentation.
---

# System Capability Registry

## Document type
This document is an overview, reference, or index as noted below.

# System Capability Registry

## Purpose
Defines platform-wide capability discovery independent of implementation names.

## Examples
Supports Flash Loans, Permit2, Cross-Chain, Streaming AI, Vision Models, Tool Calling, Batch Execution.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DISCOVERING
  DISCOVERING --> VALIDATING
  VALIDATING --> PUBLISHING
  PUBLISHING --> MONITORING
  MONITORING --> REFRESHING
  REFRESHING --> DISCOVERING
```

## Failure modes
Wrong capability label, stale capability, incompatible version.

## Recovery
Re-scan adapters, revalidate manifests, and suspend stale capabilities.

## Cross-references
- `../data/registry-system.md`
- `../plugins/plugin-sdk.md`
- `../ai/providers/ai-provider-manager.md`
- `../ai/runtime/ai-gateway.md`

## Required details
- Define platform capabilities and runtime features.

## Capability rules
- Define platform, runtime, service, and plugin capabilities explicitly.
- Define how capability checks block unsupported features.

## Capability rules
- Define discoverable capabilities, feature flags, and compatibility.
- Define capability ownership and versioning.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
