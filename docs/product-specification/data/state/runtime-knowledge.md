---
metadata_schema_version: 1.0
document_id: DOC-0277
title: Runtime Knowledge
plane: Product Specification
domain: Data
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/data/state/runtime-knowledge.md
related_concepts:
  - CONCEPT-0277
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Data
type: REFERENCE
purpose: Runtime Knowledge documentation.
scope: Reference documentation.
---

# Runtime Knowledge

## Document type
This document is an overview, reference, or index as noted below.

# Runtime Knowledge

## Purpose
Defines what the running system knows about itself at runtime.

## Contents
Active chains, loaded plugins, running workers, connected wallets, provider capabilities, health state, runtime metrics.

## State machine
```mermaid
stateDiagram-v2
  [*] --> COLLECTING
  COLLECTING --> INDEXING
  INDEXING --> SERVING
  SERVING --> REFRESHING
  REFRESHING --> COLLECTING
```

## Failure modes
Stale knowledge, missing runtime state, inconsistent service view.

## Recovery
Refresh from kernel, registries, health probes, and event stream.

## Cross-references
- `../../architecture/apex-kernel.md`
- `../../operations/monitoring/health-checks.md`
- `../../operations/monitoring/monitoring-observability.md`
- `../../dashboard/dashboard-workspaces.md`

## Operational Contract
Defines the live system view of active chains, plugins, workers, wallets, provider capabilities, health, and metrics.

## Example
The dashboard reads runtime knowledge to show active workers and healthy providers.

## Windows runtime context
- Must define tray, notifications, and service state visibility.

## Required details
- Define runtime state and Windows surfaces.

## Runtime rules
- Define service state, tray state, and Windows notification visibility.
- Define how runtime knowledge survives restarts.
