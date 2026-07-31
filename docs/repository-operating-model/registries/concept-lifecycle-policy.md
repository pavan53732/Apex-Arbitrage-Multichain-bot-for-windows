---
metadata_schema_version: 1.0
document_id: DOC-0069
title: Concept Lifecycle Policy
plane: Repository Operating Model
domain: Registries
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/registries/concept-lifecycle-policy.md
related_concepts:
  - CONCEPT-0006
  - CONCEPT-0069
dependencies:
  - DOC-0006
  - DOC-0007
  - DOC-0008
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Registries
type: STANDARD
purpose: Defines the lifecycle states and transition rules for semantic concepts in the Concept Registry.
scope: All concepts across both Repository Operating Model and Product Specification planes.
---

# Concept Lifecycle Policy

## Purpose

This policy defines the lifecycle states for semantic concepts (CONCEPT-XXXX IDs) in the Concept Registry. Concepts are distinct from documents — a concept is a stable semantic identity; documents are its representations. This policy ensures concepts evolve predictably while preserving history.

## Lifecycle States

```
Proposed → Active → Merged → Superseded → Alias Only → Historical
```

### State Definitions

| State | Meaning | Registry Status | Can Have Owner Document? |
| --- | --- | --- | --- |
| **Proposed** | New concept under evaluation | Not in registry yet | No |
| **Active** | Canonical concept with owner | Active | Yes (exactly one) |
| **Merged** | Consolidated into another active concept | Active (as alias) | No (points to target) |
| **Superseded** | Replaced by new concept | Superseded (as alias) | No (points to replacement) |
| **Alias Only** | Retained for ID history only | Superseded | No |
| **Historical** | Retired, no active references | Superseded | No |

## Promotion Rules

### Proposed → Active
**Trigger**: New permanent concept approved
**Requirements**:
- Concept does not already exist (check Concept Registry)
- Canonical owner document created with `concept_role: Owner`
- Domain owner approves (from Domain Ownership Matrix)
- Concept added to Concept Registry with:
  - `status: Active`
  - `canonical_document` = DOC-ID of owner
  - No `canonical_concept_id` (it IS the canonical)

**Approver**: Domain owner + Runtime Team

### Active → Merged
**Trigger**: Two concepts consolidated (semantically identical)
**Requirements**:
- Both concepts currently Active
- Target concept retains Active status
- Source concept updated:
  - `status: Superseded` (or Merged)
  - `canonical_concept_id` = target CONCEPT-ID
- Owner document of source updated:
  - `concept_role: Reference` (no longer Owner)
  - `supersedes` = target DOC-ID
- Target document gets `superseded_by` = source DOC-ID
- Traceability: `Superseded By Concept` relationship added
- All in same commit

**Approver**: Domain owners of both concepts + Runtime Team

### Active → Superseded
**Trigger**: Concept replaced by new/refined concept (not merge)
**Requirements**:
- New concept created (Proposed → Active) first
- Old concept updated:
  - `status: Superseded`
  - `canonical_concept_id` = new CONCEPT-ID
- Old owner document updated:
  - `concept_role: Reference`
  - `supersedes` = new DOC-ID
- New document gets `superseded_by` = old DOC-ID
- Traceability: `Superseded By Concept` relationship added
- All in same commit

**Approver**: Domain owner + Runtime Team

## Alias Rules (Immutable History)

### Superseded → Alias Only
**Trigger**: Automatic after Superseded state confirmed
**Requirements**:
- No active documents reference the superseded concept (traceability check)
- Registry entry remains with:
  - `status: Superseded`
  - `canonical_concept_id` = active target
  - All other fields frozen
- **Never modified again**

### Alias Only → Historical
**Trigger**: After 12 months in Alias Only with zero references
**Requirements**:
- Traceability Registry confirms zero active relationships
- Registry entry remains, marked as Historical for reporting
- **Never deleted**

## Deletion Policy

| Concept State | Deletion Allowed? |
| --- | --- |
| Proposed | Yes (never entered registry) |
| Active | No |
| Merged | No (alias preserved) |
| Superseded | No (alias preserved) |
| Alias Only | No |
| Historical | No |

**Emergency**: Runtime Team unanimous + documented justification.

## Metadata Requirements per State

| Field | Proposed | Active | Merged | Superseded | Alias Only | Historical |
| --- | --- | --- | --- | --- | --- | --- |
| `concept_id` | CONCEPT-XXXX | CONCEPT-XXXX | CONCEPT-XXXX | CONCEPT-XXXX | CONCEPT-XXXX | CONCEPT-XXXX |
| `status` | — | Active | Superseded | Superseded | Superseded | Superseded |
| `canonical_concept_id` | — | (self) | Target ID | Target ID | Target ID | Target ID |
| `canonical_document` | — | DOC-ID | (none) | (none) | (none) | (none) |
| `description` | Draft | Final | Frozen | Frozen | Frozen | Frozen |
| `domain` | Proposed | Active | Frozen | Frozen | Frozen | Frozen |
| `plane` | Proposed | Active | Frozen | Frozen | Frozen | Frozen |

## Concept ID Allocation

- **Format**: CONCEPT-XXXX (4 digits, zero-padded)
- **Allocation**: Sequential from Concept Registry
- **Authority**: Runtime Team only
- **Reservation**: Not allowed — allocate when Proposed → Active

## Compliance

Validators check:
- VAL-003: Exactly one Owner per Active concept
- VAL-004: Registry consistency (concepts match documents)
- VAL-008: Traceability chains valid for Merged/Superseded
- VAL-005: No orphaned Active concepts

## Related Documents
- [Concept Registry](../registries/CONCEPT-REGISTRY.md)
- [Registry Governance Standard](../registries/registry-governance-standard.md)
- [Domain Ownership Matrix](../traceability/module-ownership-matrix.md)
- [Document Lifecycle Policy](../documentation-lifecycle/document-lifecycle-policy.md)