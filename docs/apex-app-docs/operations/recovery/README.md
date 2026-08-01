---
metadata_schema_version: 1.0
document_id: DOC-0423
title: Operations Recovery README
plane: Product Specification
domain: Operations
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/recovery/recovery-coordination.md
related_concepts:
  - CONCEPT-0337
dependencies:
  - DOC-0337
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Operations Recovery

## Purpose and scope

Recovery coordination, failover, self-healing, failure matrices, and recovery playbook documentation.

## What belongs here

Recovery orchestration, failover, failure matrices, self-healing, and recovery playbooks.

## What does not belong here

Monitoring, diagnostics, or transaction execution rollback unless recovery owns the concern.

## Expected document classes

- Index
- Specification
- Reference
- Guide for operational procedures

## Canonical boundaries

This folder indexes operations documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Failure Matrix](failure-matrix.md) | Index |
| [Failure Recovery Matrix](failure-recovery-matrix.md) | Index |
| [Recovery And Failover](recovery-and-failover.md) | Reference |
| [Recovery Coordination](recovery-coordination.md) | Specification |
| [Recovery Playbook](recovery-playbook.md) | Reference |
| [Self Healing](self-healing.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
