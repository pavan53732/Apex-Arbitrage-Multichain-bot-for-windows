---
metadata_schema_version: 1.0
document_id: DOC-0078
title: APEX OS
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/architecture/apex-os.md
related_concepts:
  - CONCEPT-0078
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Architecture
type: REFERENCE
purpose: Apex Os documentation.
scope: Reference documentation.
---

# Apex Os

## Document type
This document is an overview, reference, or index as noted below.

# APEX OS

## Purpose
Defines the constitution of the platform: vision, mission, philosophy, design principles, architecture principles, runtime principles, AI principles, security principles, extensibility principles, roadmap, non-goals, and evolution strategy.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DEFINED
  DEFINED --> GOVERNING
  GOVERNING --> EVOLVING
  EVOLVING --> GOVERNING
```

## Cross-references
- `./apex-kernel.md`
- `../runtime/orchestrator.md`
- `../execution/policy-engine.md`
- `../plugins/plugin-sdk.md`
- `../windows/windows-desktop.md`
- `../operations/enterprise-operations.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
