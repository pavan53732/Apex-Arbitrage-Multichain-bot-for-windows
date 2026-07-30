---
type: SPECIFICATION
owner: Runtime Team
status: Canonical
version: 4.0.0
last_updated: 2026-07-31
purpose: Defines the repository knowledge architecture for an AI-agent-ready, docs-governed engineering repository, extending the two-plane model with stable document identity, domain classification, authority separation, canonical registries, and first-class traceability so every document can be identified, related, validated, and safely reorganized.
scope: Repository knowledge model, repository operating model, product specification plane, document identity, concept registry, document registry, traceability, validator design, repo hygiene, migration planning, and future rebuild sequencing.
audience: AI agents, maintainers, repository architects, automation engineers, and contributors responsible for rebuilding or governing the repository.
canonical_source: REBUILD-SYSTEM-SPECIFICATION.md
---

# REBUILD-SYSTEM-SPECIFICATION

## Purpose

This document defines the repository knowledge architecture required to turn the repository into an AI-agent-ready, docs-governed engineering system.

The repository must not be treated as a flat set of markdown files. It must behave like a knowledge system with explicit identity, canonical authority, traceability, and domain meaning for every important document and concept.

The rebuilt system therefore has three connected layers of meaning:

1. The Repository Operating Model.
2. The Product Specification.
3. The Repository Knowledge Model that identifies and relates everything in the repository.

The first two layers define what the repository is and what the product is.
The third layer defines how documents, concepts, relationships, and authority are represented so AI agents can reason safely and deterministically.

## Core architectural view

The rebuilt repository should be understood as a knowledge architecture, not just a folder tree.

The architecture is:

Repository
    ↓
Repository Knowledge Model
    ↓
Plane
    ↓
Domain
    ↓
Class
    ↓
Authority
    ↓
Document
    ↓
Concept
    ↓
Implementation relationship

This is the true operating model for an AI-agent-ready repository.

## The three layers of meaning

### Layer 1 — Repository Operating Model

This layer defines how humans and AI agents work in the repository.

It includes:

- repository governance
- canonical documentation rules
- documentation classes
- validation expectations
- traceability expectations
- repository hygiene rules
- review and completion workflow
- agent operating rules
- source-versus-generated boundaries
- deprecation and migration rules
- lifecycle rules for repository knowledge itself

This layer is repository infrastructure.

### Layer 2 — Product Specification

This layer defines the software system being built.

It includes:

- architecture
- runtime behavior
- product AI systems
- dashboard behavior
- plugin behavior
- deployment behavior
- interfaces and contracts
- security behavior
- state machines
- testing behavior
- platform integration

This layer is the software specification.

### Layer 3 — Repository Knowledge Model

This layer identifies what each document is, what concept it owns, where it belongs, what it depends on, and how it relates to other knowledge objects.

It includes:

- stable document identity
- domain classification
- authority classification
- canonical registries
- traceability relationships
- supersession relationships
- validator coverage relationships
- ownership relationships

This layer is the missing foundation that makes the whole repository safe to reorganize.

## Why the knowledge layer matters

The two-plane model is necessary, but not sufficient.

Without a knowledge layer, the repository still depends too much on filenames and folders to infer meaning.

That creates avoidable failure modes:

- documents move and their meaning becomes harder to track
- multiple files appear to own the same concept
- AI agents infer authority from location instead of metadata
- validators operate on files but not on concepts
- traceability is mentioned but not structurally enforced
- humans must remember too much implicit knowledge

The knowledge layer fixes this by making identity and relationships explicit.

## System objectives

The rebuilt repository must satisfy all of the following objectives.

### 1. Explicit two-plane authority

The repository must distinguish between:

- how the repository operates
- what the product is

No major document should leave that ambiguous.

### 2. Stable knowledge identity

Every important document and concept must have a stable identity that survives folder moves, filename changes, and structural refactors.

### 3. Canonical truth per concept

Every important concept must have exactly one canonical owner unless the repository explicitly documents a split or federation of responsibility.

### 4. Deterministic placement

An AI agent must know where a document belongs before creating it.

### 5. Validation before trust

Important repository assumptions must be testable.

### 6. Traceability as a first-class system

Every important document should be able to participate in traceability chains across requirements, decisions, validators, tests, and implementation artefacts.

### 7. Lightweight but real governance

The system must be stronger than ad hoc documentation but lighter than the deleted governance stack.

## Document identity model

The repository should not rely on filenames as the primary identity of important knowledge objects.

### Stable Document ID

Every important document should have a stable document identifier.

Example format:

- DOC-0001
- DOC-0002
- DOC-00124

Document IDs should remain stable even if the document moves or is renamed.

### Why document IDs matter

They allow:

- stable cross references
- migration-safe linking
- registry lookup
- validator targeting
- concept ownership tracking
- relationship mapping across reorganizations

### Document identity rule

The path is a location.
The document ID is the identity.

AI agents must not confuse the two.

## Knowledge dimensions

Every important document should be classified across multiple orthogonal dimensions.

### 1. Plane

The high-level authority plane.

Values:

- Repository Operating Model
- Product Specification

### 2. Domain

The semantic area the document belongs to.

Examples:

- Governance
- Agent System
- Traceability
- Validation
- Standards
- Documentation Lifecycle
- AI
- Runtime
- Dashboard
- Deployment
- Security
- Testing
- Windows
- Plugins
- Interfaces

Domains are stable semantic categories. Folders may change, but domain meaning should remain stable.

### 3. Class

The document type or function.

Examples:

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

### 4. Authority

The document’s authority relationship.

Values:

- Canonical
- Derived
- Reference
- Historical
- Generated

Authority is not the same as status.

### 5. Status

The document lifecycle state.

Values:

- Draft
- Review
- Approved
- Active
- Deprecated
- Archived
- Superseded
- Experimental

Status is not the same as authority.

### 6. Owner

The person, team, or system responsible for the document.

### 7. Version

A version number or revision marker that helps track evolution.

### 8. Canonical source

The canonical source path or canonical source document ID.

### 9. Traceability relationships

Links to requirements, decisions, tests, validators, and dependent docs.

## Authority versus status

Authority and status must be separate.

### Authority describes what kind of source the document is

- Canonical
- Derived
- Reference
- Historical
- Generated

### Status describes the document’s lifecycle condition

- Draft
- Review
- Approved
- Active
- Deprecated
- Archived
- Superseded
- Experimental

This distinction matters because a document can be canonical and active, canonical and deprecated, derived and active, reference and archived, or generated and temporary.

Mixing authority and status leads to confusion and validator ambiguity.

## Repository knowledge objects

The repository should treat documents as part of a broader knowledge system.

### Concept

A concept is a semantic entity the repository cares about.

Examples:

- Agent Operating Model
- Product AI Runtime
- Dashboard Architecture
- Validation Policy
- Traceability Model
- Document Registry

### Document

A document is the file or artefact that expresses one or more concepts.

### Relationship

A relationship connects concepts, documents, requirements, validators, tests, and implementation references.

### Implementation artefact

An implementation artefact is a code file, script, config, schema, or test that realizes or checks a concept.

The knowledge model must let the repository connect all of these cleanly.

## Canonical registries

The knowledge layer should have explicit registries.

### 1. Concept Registry

Purpose:

Defines concepts and their canonical owners.

A concept registry entry should include at least:

- concept ID
- concept name
- plane
- domain
- canonical document ID
- canonical document path
- authority
- status
- related concepts
- dependencies
- consumers
- notes

Why it matters:

This prevents duplicate concepts and gives AI agents a stable source of semantic authority.

### 2. Document Registry

Purpose:

Defines every important document as a tracked knowledge object.

A document registry entry should include at least:

- document ID
- path
- title
- plane
- domain
- class
- authority
- status
- owner
- version
- canonical source
- related concepts
- supersedes
- superseded by
- dependencies
- consumers
- validator coverage
- traceability IDs

Why it matters:

This gives AI agents and validators a single structured way to find and reason about important docs.

### 3. Traceability Registry

Purpose:

Defines the relationship graph between documents, concepts, requirements, validators, tests, and implementation artefacts.

A traceability entry should include at least:

- traceability ID
- source ID
- target ID
- relationship type
- rationale
- status
- evidence references

Why it matters:

This makes traceability first-class instead of a vague promise.

## Traceability as a first-class system

Traceability must become the backbone of the repository knowledge architecture.

### What traceability means here

Traceability is the ability to answer:

- what concept a document defines
- what requirement it satisfies
- what decision it depends on
- what validator checks it
- what tests or checks prove it
- what documents it consumes or produces
- what documents it supersedes or is superseded by

### Example traceability model

A document may carry relationships such as:

- Implements: REQ-041
- Implements: REQ-044
- Consumes: ADR-0005
- Produces: API-009
- Related: DOC-0089
- Related: DOC-0112
- Validated by: VAL-013
- Validated by: VAL-028
- Tested by: TEST-114
- Tested by: TEST-203

### Why traceability matters

Traceability means an AI agent never has to guess what a document is for, what it depends on, or what proves it.

It also means reorganizing the repository becomes much safer because the registry carries meaning even when folders move.

## Validation model

Validators should validate knowledge relationships, not just file existence.

### Validator principle

Validators should check:

- documents
- concepts
- registry consistency
- relationship consistency
- plane boundaries
- domain consistency
- authority consistency
- status consistency
- traceability consistency
- generated artefact boundaries

### Required validator families

#### 1. Cross-reference validator

Checks:

- links resolve
- references point to valid IDs or paths
- moved files do not leave stale references

#### 2. Metadata validator

Checks:

- required metadata exists
- plane, domain, class, authority, and status are valid
- owner and canonical source are present where required

#### 3. Concept uniqueness validator

Checks:

- one canonical owner per concept unless explicitly split
- no ambiguous duplicate concept ownership

#### 4. Registry consistency validator

Checks:

- document registry matches actual files
- concept registry matches actual canonical docs
- traceability registry relationships are valid

#### 5. Orphan detector

Checks:

- important documents are reachable from the registry or index surfaces

#### 6. Generated-artifact guard

Checks:

- generated outputs are not accidentally committed

#### 7. Documentation-class validator

Checks:

- documents are assigned to the correct class
- repository-operating and product-spec documents remain semantically separate

#### 8. Traceability validator

Checks:

- traceability IDs resolve
- requirements, validators, tests, and docs form valid chains

## The relationship hierarchy

The repository should preserve the following hierarchy:

Repository
    ↓
Knowledge Model
    ↓
Plane
    ↓
Domain
    ↓
Class
    ↓
Authority
    ↓
Status
    ↓
Document
    ↓
Concept
    ↓
Traceability relationships
    ↓
Implementation artefacts

This hierarchy is the mental model AI agents should use.

## Repository Operating Model side

This side should conceptually contain areas such as:

- governance
- operating-model
- agent-system
- contribution
- traceability
- validation
- standards
- documentation rules
- workflows
- registries

## Product Specification side

This side should conceptually contain areas such as:

- architecture
- runtime
- ai
- dashboard
- plugins
- deployment
- interfaces
- security
- state-machines
- testing
- platform integration

## Migration rule

The repository should not be reorganized until the knowledge model is explicit.

Before large movement, the repository should define:

1. document IDs
2. plane assignments
3. domain assignments
4. class assignments
5. authority assignments
6. status assignments
7. canonical source assignments
8. registry entries
9. traceability relationships
10. move sequencing

Only then should large-scale reorganization begin.

## File and folder policy

Folders are implementation details of the knowledge model, not the model itself.

### Root

The root should contain only repository-level control files and top-level entry points.

### docs/

docs/ remains the main documentation knowledge base unless a planned structural split is executed later.

### Future folders

If separate folders are later created for operating-model or product-spec subdomains, they should follow registry and migration rules.

### Future tools/, scripts/, schemas/

If these are reintroduced, they must be constrained and explicit:

- tools/ for maintained reusable tools
- scripts/ for deterministic helper scripts
- schemas/ only if schemas are genuinely canonical knowledge objects

They should never be treated as dumping grounds.

## Change classification model

The repository should classify changes using multiple axes.

### Recommended change tags

- repository-operating-readability
- repository-operating-structure
- repository-operating-canonical
- product-spec-readability
- product-spec-structure
- product-spec-canonical
- knowledge-model-change
- registry-change
- traceability-change
- repo-hygiene
- validator-change
- taxonomy-change
- deprecation-change
- generated-cleanup

## Commit and review model

### Commit messages should explain

- what changed
- why it changed
- which plane it affected
- which domain it affected
- which class or authority it affected
- whether it changed registry or traceability behavior

### Review should verify

- correct plane selection
- correct domain selection
- correct class and authority selection
- canonical owner is correct
- registry entries are consistent
- traceability chains are intact
- references remain valid
- generated artefacts were not committed

## What should not be rebuilt in the same form

The rebuild should avoid recreating heavy structures before the lightweight core is stable.

Do not rebuild by default:

- bulky committed export trees
- large graph repositories
- repository-committed databases
- ceremonial audit machinery with low operational value
- heavy closure artefact stacks
- broad certification systems before the core knowledge architecture is stable

The default rule should be:

build the minimum high-value control plane first, then add only what proves necessary.

## Recommended rebuild sequence

### Phase 1 — Knowledge identity foundation

Rebuild first:

1. AGENTS.md as the agent operating contract.
2. REBUILD-SYSTEM-SPECIFICATION.md as the root repository knowledge architecture.
3. canonical metadata conventions.
4. stable document IDs.
5. generated-artifact policy.

### Phase 2 — Registries

Rebuild second:

1. Concept Registry
2. Document Registry
3. Traceability Registry
4. canonical index surfaces

### Phase 3 — Class and plane control

Rebuild third:

1. documentation classes
2. plane assignments
3. authority assignments
4. status assignments
5. deprecation and supersession model
6. naming rules for Repository AI versus Product AI

### Phase 4 — Validator core

Rebuild fourth:

1. cross-reference validator
2. metadata validator
3. concept uniqueness validator
4. registry consistency validator
5. orphan detector
6. generated-artifact guard
7. documentation-class validator
8. traceability validator

### Phase 5 — Agent workflow enforcement

Rebuild fifth:

1. pre-change checklist
2. post-change checklist
3. change classification model
4. commit/review rules
5. high-caution boundary definitions

### Phase 6 — Structural migration

Rebuild sixth:

1. define migration map
2. move docs gradually by registry and traceability rules
3. repair references incrementally
4. validate after each migration wave

### Phase 7 — Optional supporting automation

Rebuild last and only if justified:

1. helper scripts
2. compact reusable tools
3. optional CI checks
4. local-only reporting utilities
5. certification systems only if there is real operational need

## Success criteria

The rebuilt repository knowledge architecture is successful only if an AI agent can answer all of the following before changing anything:

- What document ID identifies this object?
- Which plane does it belong to?
- Which domain does it belong to?
- Which class does it belong to?
- What is its authority?
- What is its status?
- What concept does it own?
- What registry entries point to it?
- What does it trace to and from?
- Which validators cover it?
- What files or artefacts depend on it?
- What files must never be committed?

If the repository can answer those questions clearly, it is truly agent-operable.

## Final design principle

The rebuilt system must be more structured than ad hoc documentation and lighter than the deleted governance platform.

Its goal is explicit authority, stable identity, source-of-truth discipline, canonical registries, first-class traceability, deterministic placement, lightweight validation, clean repository hygiene, and safe AI-agent execution.

That is the correct foundation for rebuilding the repository end to end with multiple AI agents working consistently against canonical knowledge instead of improvising across a flat collection of files.
