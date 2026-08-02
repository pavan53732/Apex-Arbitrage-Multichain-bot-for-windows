---
metadata_schema_version: 1.0
document_id: DOC-0444
title: Registry Governance Standard
plane: Repository Operating Model
domain: Registries
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/registries/registry-governance-standard.md
related_concepts:
  - CONCEPT-0006
  - CONCEPT-0007
  - CONCEPT-0008
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
purpose: Defines governance rules for all canonical registries including who may edit, update order, alias rules, deletion policy, regeneration policy, and validation policy.
scope: Concept Registry, Document Registry, and Traceability Registry.
---

# Registry Governance Standard

## Purpose

This standard defines the governance rules for all three canonical registries to ensure consistency, auditability, and safe concurrent updates.

## Who May Edit Registries

| Role | Permissions |
| --- | --- |
| Runtime Team | Full edit access to all registries |
| Architecture Team | Read access; may propose changes via PR |
| AI Agents | May update registries only when executing a pre-approved change that includes registry updates in the same atomic commit |
| Other Contributors | Read-only; must request Runtime Team for changes |

**Rule**: Registry edits must never be made in isolation. Every registry change must be accompanied by the corresponding document changes in the same commit.

## Update Order

When a change affects multiple registries, apply updates in this strict order:

1. **Concept Registry** — Define/resolve concept identity first
2. **Document Registry** — Register document with correct concept role
3. **Traceability Registry** — Add relationships last (depends on 1 and 2)

**Rationale**: Concept identity is the foundation; document registration depends on it; traceability depends on both.

## Alias Rules

### Concept Aliases (Superseded Concepts)
- Created only when a concept is consolidated into another active concept
- Superseded concept ID is retained as an alias with `Canonical Concept ID` pointing to the active concept
- Alias entries are **immutable** — never modified after creation
- Alias entries are **never deleted** — they preserve ID history permanently
- Alias format: Status = "Superseded", `Canonical Concept ID` = active concept ID

### Document Aliases
- Not supported. Documents use `supersedes` / `superseded_by` fields instead
- Historical documents retain their DOC-ID with status "Historical" or "Superseded"

## Deletion Policy

| Registry Item | Deletion Allowed? | Conditions |
| --- | --- | --- |
| Active concept | No | Must be superseded first |
| Superseded concept alias | No | Immutable, permanent history |
| Active document | No | Must be superseded first |
| Superseded document | No | Immutable, permanent history |
| Traceability relationship | Yes | Only if both source and target still exist and relationship is invalid |
| Registry version metadata | No | Immutable, append-only |

**Emergency deletion**: Requires Runtime Team unanimous approval + documented justification in commit message.

## Regeneration Policy

Registries may be regenerated (full rebuild from source) under these conditions:

- **Trigger**: Schema version change (registry_schema_version increment)
- **Authority**: Runtime Team only
- **Process**:
  1. Create new registry file with incremented version
  2. Validate all entries against live documents
  3. Run full validator suite (VAL-001 through VAL-008)
  4. Commit as single atomic change with all affected documents
  5. Update `last_regenerated` timestamp
- **Never**: Regenerate registries as a routine maintenance task

## Validation Policy

Registry changes must pass these validators before commit:

| Validator | Registry Check |
| --- | --- |
| VAL-002 | Metadata schema compliance |
| VAL-003 | Concept uniqueness (no duplicate owners) |
| VAL-004 | Registry consistency (entries match filesystem) |
| VAL-008 | Traceability ID resolution |

**Minimum**: All 4 validators must pass with 0 errors.

## Registry Schema Evolution

| Version | Changes | Migration |
| --- | --- | --- |
| 1.0 | Initial schema | N/A |
| 1.1 | Added registry_model, concept-centric model | Concept IDs made stable; aliases introduced |
| 1.2+ | Future | Documented in REBUILD-SYSTEM-SPECIFICATION.md |

**Rule**: Schema version increments require Runtime Team approval and full regeneration.

## Commit Message Format for Registry Changes

```
docs(registry): [concept|document|traceability] <action> <concept-id|doc-id>

<detailed reason>

Registry-Version: X.Y.Z
Validator-Pass: VAL-002,VAL-003,VAL-004,VAL-008
```

Example:
```
docs(registry): concept supersede CONCEPT-0069 into CONCEPT-0079

APEX Architecture consolidated into Architecture canonical concept

Registry-Version: 1.1.1
Validator-Pass: VAL-002,VAL-003,VAL-004,VAL-008
```

## Related Documents
- [Concept Registry](CONCEPT-REGISTRY.md)
- [Document Registry](DOCUMENT-REGISTRY.md)
- [Traceability Registry](TRACEABILITY-REGISTRY.md)
- [REBUILD-SYSTEM-SPECIFICATION.md](../../../REBUILD-SYSTEM-SPECIFICATION.md)
- [Validation Specification](../validation/validation-specification.md)