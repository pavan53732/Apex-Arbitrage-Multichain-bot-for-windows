---
metadata_schema_version: 1.0
document_id: DOC-0065
title: README Governance Standard
plane: Repository Operating Model
domain: Standards
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/standards/readme-governance-standard.md
related_concepts:
  - CONCEPT-0065
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Standards
type: STANDARD
purpose: Defines the mandatory structure and content for all domain README files.
scope: All domain-level README.md files in both Repository Operating Model and Product Specification planes.
---

# README Governance Standard

## Purpose

This standard defines the required structure for every domain-level README.md file. It ensures that any AI agent or human contributor can determine ownership, boundaries, canonical documents, and creation rules for a domain without guessing.

## Mandatory Sections

Every domain README must contain the following sections in this order:

### 1. Purpose and Scope

A 1-2 sentence description of what this domain covers at the product or repository level.

### 2. What Belongs Here

Explicit list of document types, subdomains, and concerns that are owned by this domain.

### 3. What Does Not Belong Here

Explicit list of document types, subdomains, and concerns that are explicitly excluded and where they belong instead.

### 4. Canonical Owner Map

A table mapping each subdomain to its canonical concept identity:

| Subdomain | Concept ID | Canonical Owner | Subdomain README |
| --- | --- | --- | --- |
| subdomain-name | CONCEPT-XXXX | [Canonical Document (`./subdomain/canonical-document.md`) | [Subdomain README (`./subdomain/README.md`) |

Rules:
- Every subdomain folder must have a corresponding entry
- Concept ID must reference an active concept in the Concept Registry
- Canonical Owner must be the document with `concept_role: Owner` for that concept
- Subdomain README must exist and follow this same standard

### 5. Document Classes Expected

List of documentation classes that are valid for this domain. Must be a subset of the global classes:
- Specification
- Guide
- Reference
- ADR
- Historical
- Certification
- Registry
- Policy
- Workflow
- Manifest
- Index
- Generated

### 6. Relationship to Adjacent Domains

Explicit statement of:
- Which domains this domain consumes from
- Which domains consume from this domain
- What this domain must not redefine (boundary enforcement)

### 7. Subdomain Navigation

For each subdomain listed in the Canonical Owner Map, a detailed section:

```
### subdomain-name

- Concept: `CONCEPT-XXXX`
- Canonical Owner: [Canonical Document (`./subdomain/canonical-document.md`)
- Folder README: [Subdomain README (`./subdomain/README.md`)

Documents:
- [Document Title (`./subdomain/document.md`) — Class
```

Every document in the subdomain must be listed with its class.

### 8. Before Adding a Document Here

A mandatory checklist that every agent must follow before creating a new document in this domain:

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.

## Folder Split Policy

To prevent unbounded folder growth, the following thresholds apply to every domain and subdomain folder:

| Threshold | Document Count | Action |
| --- | --- | --- |
| Target | ≤ 15 | Preferred maximum; no action needed |
| Soft Limit | 20 | Warning: plan a semantic split |
| Hard Limit | 25 | Mandatory: split by semantic subdomain before adding more documents |

**Split Rules:**
- Split by semantic subdomain, never alphabetically
- Each new subdomain must have its own Concept ID and canonical owner
- Parent README must be updated with new Canonical Owner Map entries
- Concept Registry must be updated with new subdomain concepts
- Document Registry must reflect new document locations
- Traceability relationships must be preserved

## Metadata Requirements

Every README must include the standard YAML frontmatter with these fields:
- `metadata_schema_version`
- `document_id` (stable DOC-XXXX)
- `title`
- `plane` (Repository Operating Model | Product Specification)
- `domain` (the domain name)
- `class: Index`
- `authority: Derived`
- `status: Active`
- `owner` (team name)
- `version`
- `canonical_source` (path to this README)
- `related_concepts` (array of Concept IDs this README indexes)
- `dependencies` (canonical documents this README derives from)
- `concept_role: Index`
- `owned_domains: []`

## Compliance

Validators must check:
1. All mandatory sections present
2. Canonical Owner Map matches actual subdomain folders
3. Concept IDs resolve to active concepts in Concept Registry
4. Canonical Owner documents have `concept_role: Owner` for the referenced concept
5. All subdomain documents listed in navigation
6. Document classes match global taxonomy
7. Folder document count ≤ 25 (hard limit)
8. "Before Adding" checklist present and unmodified

## Template

```markdown
---
metadata_schema_version: 1.0
document_id: DOC-XXXX
title: [Domain] README
plane: [Repository Operating Model | Product Specification]
domain: [Domain]
class: Index
authority: Derived
status: Active
owner: [Team]
version: 1.0.0
canonical_source: docs/[plane]/[domain]/README.md
related_concepts:
  - CONCEPT-XXXX
dependencies:
  - DOC-XXXX
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: YYYY-MM-DD
concept_role: Index
owned_domains: []
---

# [Domain]

## Purpose and scope

[1-2 sentences]

## What belongs here

[Explicit list]

## What does not belong here

[Explicit list with redirects]

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| subdomain | CONCEPT-XXXX | [Doc (`./subdomain/doc.md`) | [README (`./subdomain/README.md`) |

## Document classes expected

- [Class1]
- [Class2]

## Relationship to adjacent domains

[Consumes from X, consumed by Y, must not redefine Z]

## Subdomain navigation

### subdomain

- Concept: `CONCEPT-XXXX`
- Canonical Owner: [Doc (`./subdomain/doc.md`)
- Folder README: [README (`./subdomain/README.md`)

Documents:
- [Doc Title (`./subdomain/doc.md`) — Class

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
```