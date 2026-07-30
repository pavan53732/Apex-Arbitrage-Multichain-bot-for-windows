---
type: SPECIFICATION
owner: Runtime Team
status: Canonical
version: 3.0.0
last_updated: 2026-07-31
purpose: Defines the complete repository rebuild model for an AI-agent-ready, docs-governed engineering repository, explicitly separating the Repository Operating Model from the Product Specification plane and defining the taxonomy, governance, validators, workflows, and migration approach required to rebuild the system correctly.
scope: Repository operating model, product-specification governance, AI-agent execution rules, documentation taxonomy, validator design, repo hygiene, migration planning, and future rebuild sequencing.
audience: AI agents, maintainers, repository architects, automation engineers, and contributors responsible for rebuilding or governing the repository.
canonical_source: REBUILD-SYSTEM-SPECIFICATION.md
---

# REBUILD-SYSTEM-SPECIFICATION

## Purpose

This document defines the full rebuild model required to turn the repository into an AI-agent-ready, docs-governed engineering system.

The repository is not just a place where documentation happens to exist. It should operate as a controlled engineering environment where documentation governs how work is performed, how truth is located, how structure is maintained, how changes are validated, and how AI agents are prevented from improvising against ambiguous or non-canonical material.

The rebuilt system must therefore define two different but connected planes of authority:

1. The Repository Operating Model.
2. The Product Specification.

Those planes must be explicitly separated in the repository concept model, in documentation taxonomy, in validator behavior, and in AI-agent workflows.

## Central architectural distinction

The most important rebuild principle is this:

The documentation in this repository has two fundamentally different responsibilities, and those responsibilities must not be mixed.

### Plane 1 — Repository Operating Model

This plane defines how humans and AI agents work inside the repository.

It governs things like:

- canonical documentation rules
- documentation classes
- repository hygiene
- validation rules
- traceability expectations
- agent operating rules
- review workflow
- implementation workflow
- completion workflow
- deprecation handling
- change classification
- source-versus-generated boundaries
- documentation lifecycle

This plane is repository infrastructure.

It is not the application.

It is the operating system of the repository.

### Plane 2 — Product Specification

This plane defines the software product being built.

It governs things like:

- runtime architecture
- AI architecture inside the product
- dashboard behavior
- plugin architecture
- deployment behavior
- security behavior
- interfaces and contracts
- state machines
- testing behavior
- platform integration

This plane is the software specification.

It is not the contribution system.

It describes what is being built, not how work in the repository is governed.

## Why this distinction matters

If these two planes are blurred together, AI agents and even human contributors will make predictable mistakes.

Typical failure modes include:

- treating repository-governance documents as if they were product design documents
- treating product-AI architecture documents as if they were instructions for agent contribution behavior
- editing the wrong class of document because authority boundaries are unclear
- creating duplicate “AI” documentation where one file is about product intelligence and another is about repository agent behavior
- applying validation rules meant for product specs to repository-operating documents or vice versa
- losing the ability to reason about what is canonical in each context

The rebuild must eliminate that ambiguity structurally and semantically.

## The repository stack

The rebuilt repository should be understood conceptually like this:

Repository
    ↓
Repository Operating Model
    ↓
Governance, standards, validation, traceability, agent workflows
    ↓
AI agents and human contributors
    ↓
Product Specification
    ↓
Source code, tests, and implementation work

This stack matters because everything above the product specification governs how the product specification is created and maintained.

## System objectives

The rebuilt repository must satisfy all of the following objectives.

### 1. Explicit two-plane authority

The repository must clearly distinguish between:

- how the repository operates
- what the product is

No major document should leave that ambiguous.

### 2. Canonical truth per concept

Every important concept must have a canonical source.

An AI agent must be able to determine:

- the canonical file for a repository-operating concept
- the canonical file for a product concept
- whether a file is canonical, secondary, reference, historical, generated, or deprecated

### 3. Deterministic placement

An AI agent must know where to place a document before creating it.

This includes knowing whether the new document belongs to the repository-operating plane or the product-specification plane.

### 4. Validation before trust

Important repository assumptions must be testable.

Documentation should not be trusted merely because it exists. Structural integrity, metadata completeness, canonical relationships, and source-versus-generated rules must be validated.

### 5. Lightweight but real governance

The new system must be strong enough to guide AI agents reliably but lighter than the deleted governance stack.

The target is not bureaucracy. The target is clarity, authority, and enforceable structure with minimal unnecessary ceremony.

## Documentation class system

The rebuilt system should not govern “all markdown files” as a flat universe.

It should govern explicit documentation classes.

### Required documentation classes

#### 1. Repository Operating Model

Purpose:

Defines how the repository is governed and how humans and AI agents must work inside it.

Examples:

- AGENTS.md
- REBUILD-SYSTEM-SPECIFICATION.md
- repository governance rules
- agent workflow specs
- validation policy docs
- traceability rules
- documentation lifecycle rules
- contribution workflow rules

Canonical status:

Yes, for repository-level operating behavior.

#### 2. Product Specification

Purpose:

Defines what the software system is, how it should behave, and how its components fit together.

Examples:

- architecture docs
- runtime docs
- product AI docs
- deployment docs
- security docs
- plugin docs
- interface contracts
- state machine specifications
- testing specifications

Canonical status:

Yes, for software behavior and structure.

#### 3. ADR

Purpose:

Captures architecture or governance decisions, rationale, trade-offs, and historical decision context.

Canonical status:

Canonical for decision history, but not a replacement for active current-state specification.

#### 4. Reference

Purpose:

Provides support material such as catalogs, glossaries, FAQs, metrics definitions, lookup docs, and support indexes.

Canonical status:

Canonical for lookup/reference purposes if explicitly declared, but normally subordinate to primary specs.

#### 5. Guide

Purpose:

Provides workflows, tutorials, operator instructions, contributor guidance, and procedural explanations.

Canonical status:

Usually not the primary source of truth for architecture, but may be canonical for process guidance if stated.

#### 6. Historical

Purpose:

Preserves older, replaced, superseded, or archived materials that are kept for context rather than current authority.

Canonical status:

No, except as historical record.

#### 7. Certification

Purpose:

Stores formal governance certification, decision packs, approval artefacts, or compliance evidence if ever reintroduced intentionally.

Canonical status:

Canonical for the certification event itself, but not a substitute for active specs.

#### 8. Generated

Purpose:

Produced by tooling, analysis, exports, graphs, or automation.

Canonical status:

No by default.

Generated artefacts should remain uncommitted unless there is an explicit, justified exception.

## Repository AI versus Product AI

One of the most important sources of ambiguity must be eliminated explicitly.

The repository contains two different meanings of AI.

### Repository AI

Repository AI refers to AI systems that contribute to the repository itself.

Examples include:

- ChatGPT
- Claude Code
- Cursor
- Copilot
- Kilo Code
- future coding agents or documentation agents

Documents in this category belong to the Repository Operating Model plane.

They define:

- how AI agents behave in the repository
- what they must read first
- what they can and cannot change
- what validations they must run
- how they should classify changes
- how they should commit work

These are not product-AI docs.

These are agent contribution system docs.

### Product AI

Product AI refers to the AI inside the software being built.

Examples include:

- AI pipeline
- AI memory
- AI planner
- AI provider manager
- AI gateway
- AI tool invocation contract
- AI safety boundary within the application
- AI runtime context behavior

Documents in this category belong to the Product Specification plane.

They define product behavior, not repository contribution behavior.

### Naming principle

The rebuilt repository should avoid relying on the ambiguous word “AI” alone when the class is not obvious.

Where needed, use labels such as:

- Agent Operating System
- Agent Contribution System
- Product AI Architecture
- Application AI Runtime

That naming discipline reduces interpretation errors for both humans and agents.

## Canonical truth model

Canonical truth is the foundation of the repository.

### What canonical means

A canonical document is the authoritative source for a concept.

Other files may summarize, reference, teach, or contextualize the concept, but they must not silently replace the canonical document.

### Canonical requirements

Every important canonical document should:

- define one or more authoritative concepts clearly
- have explicit metadata
- be reachable from an index or registry
- have a stable place in the taxonomy
- not compete with another undeclared canonical peer for the same concept

### Minimum canonical metadata

Every important canonical document should include at least:

- type
- owner
- status
- version
- last_updated
- purpose
- scope
- audience
- canonical_source

Recommended additional metadata:

- class
- plane
- dependencies
- consumers
- related_documents
- supersedes
- superseded_by

### Canonical conflict rule

If two files appear to define the same concept authoritatively, the repository must either:

- designate one as canonical and the other as derived, guide, reference, or historical
- or split the concepts more clearly so they no longer compete

An agent should never be left to guess.

## Canonical hierarchy

The repository should operate with a hierarchy of authority.

Recommended order:

1. Root repository operating specifications.
2. Repository Operating Model canonical docs.
3. Product Specification canonical docs.
4. ADRs and formal decisions.
5. Reference and guide material.
6. Historical archives.
7. Generated artefacts.

This hierarchy does not mean higher layers describe the product in more detail. It means they govern authority and interpretation.

## Repository hygiene model

Repository hygiene is the discipline that keeps the knowledge base clear, intentional, and trustworthy.

### Root-level discipline

The repository root should remain small and highly intentional.

Root-level items should normally be limited to repository entry points and repository-level control files such as:

- README.md
- AGENTS.md
- AGENTS_RULES.md if still needed
- REBUILD-SYSTEM-SPECIFICATION.md
- .gitignore
- narrowly justified additional root control files

Everything else should have a clear folder home.

### Folder-purpose discipline

Each major folder must have a defined purpose.

No folder should exist merely because content needed “somewhere to go.”

### Generated-artifact discipline

Generated outputs must not be committed by default.

Examples that should generally remain outside git include:

- analysis outputs
- export snapshots
- graph files
- caches
- local databases
- temporary dashboards
- one-off reports
- rebuildable summary artefacts

### Duplicate suppression

The rebuilt system should actively suppress duplicate concept documentation unless there is an explicit canonical relationship.

### Deprecation discipline

If a document is replaced, the relationship should be explicit.

The repository should say what replaced it, not leave both files to compete indefinitely.

## Validator model

Validators are how the repository proves that important structural assumptions are still true.

The rebuilt validator system should be much smaller than the deleted one, but it must still be meaningful.

### Validator design principles

Validators should be:

- deterministic
- fast
- understandable
- easy for AI agents to run
- focused on high-value failure modes
- strong enough to stop drift, but not ceremonial

### Required validator families

#### 1. Cross-reference validator

Checks:

- markdown links resolve
- referenced files exist
- renamed or moved files do not leave stale references
- key entry documents still point to valid locations

Why it matters:

Protects structural integrity after refactors, renames, and taxonomy changes.

#### 2. Canonical metadata validator

Checks:

- required metadata is present on important docs
- class and plane values are valid
- canonical_source values are accurate
- owners, purposes, and statuses are not missing

Why it matters:

Makes documents interpretable to both agents and maintainers.

#### 3. Duplicate canonical-concept detector

Checks:

- no two active docs silently claim the same canonical concept
- suspicious overlaps are flagged

Why it matters:

Protects source-of-truth discipline.

#### 4. Orphan-document detector

Checks:

- important docs are reachable from an index, registry, or documented parent path
- disconnected critical files are flagged

Why it matters:

Prevents important material from becoming invisible.

#### 5. Generated-artifact guard

Checks:

- generated outputs are not accidentally staged or committed
- ignored output locations remain excluded

Why it matters:

Prevents repository pollution from automated runs.

#### 6. Root-layout validator

Checks:

- unauthorized root clutter is not introduced
- root remains an intentional entry surface

Why it matters:

Protects the repository’s navigational clarity.

#### 7. Documentation-class validator

Checks:

- documents are assigned to the correct class
- repository-operating docs are not mixed with product-spec docs semantically or structurally
- class-specific expectations are enforced

Why it matters:

This is the validator that directly enforces the two-plane architecture.

## Governance boundaries

Governance boundaries define the safe operating envelope for humans and AI agents.

### Boundary types

#### A. Plane boundaries

Repository Operating Model documents and Product Specification documents must not be casually merged conceptually or structurally.

#### B. Edit-scope boundaries

Some docs are safe for routine editing. Others require greater caution.

Examples:

- reference and guide updates are lower risk if canonical meaning does not change
- root repository operating docs are high risk
- canonical product architecture docs are high impact
- deprecated docs should not be revived by accident

#### C. Source-versus-generated boundaries

Generated output must never quietly become a source-of-truth document.

#### D. Structural boundaries

Agents should not create new top-level documentation families or root clutter without justification.

#### E. Authority boundaries

A lower-authority guide should not override a canonical spec.

#### F. Risk boundaries

Changes affecting canonical meaning, agent rules, or documentation taxonomy should trigger stronger caution and validation.

## Agent execution model

This section defines how AI agents should operate in the rebuilt repository.

### Entry workflow

When an agent enters the repo, it should first read:

- AGENTS.md
- REBUILD-SYSTEM-SPECIFICATION.md
- the central docs index
- the canonical domain document relevant to the task

The agent must begin by locating authority, not by editing.

### Pre-change workflow

Before making changes, the agent should:

1. Identify the concept being changed.
2. Determine whether the concept belongs to the Repository Operating Model or Product Specification plane.
3. Locate the canonical file.
4. Identify dependent or related files.
5. Determine document class.
6. Classify the change.
7. Confirm generated outputs are not involved improperly.

### Change workflow

During changes, the agent should:

1. Edit the smallest justified set of files.
2. Preserve canonical relationships.
3. Keep class and plane boundaries intact.
4. Update inbound and outbound references when structure changes.
5. Avoid creating duplicate concepts when an existing canonical file should be edited instead.

### Post-change workflow

After changes, the agent should:

1. Run relevant validators.
2. Confirm references still resolve.
3. Confirm metadata still reflects reality.
4. Confirm no generated artefacts were added.
5. Write a commit message that explains what changed and why in operating-model terms.

### High-caution changes

The following changes should be treated as high caution:

- root-level operating spec changes
- canonical architecture changes
- taxonomy changes
- class-model changes
- deprecation or supersession changes
- validator-rule changes
- reintroduction of tooling, scripts, schemas, or certification systems as canonical layers

## Target conceptual documentation taxonomy

The ChatGPT review was correct that the repository should be conceptually split, even if migration happens in phases.

The rebuilt target taxonomy should be modeled like this.

### Repository Operating Model side

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

### Product Specification side

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

### Supporting classes

Additional supporting classes should include:

- ADR
- reference
- guide
- historical
- certification if ever intentionally restored
- generated by exception only

## Migration rule

Even though the target taxonomy is correct, the repository should not be reorganized blindly in one large move without preparation.

### Why blind reorganization is risky

A direct large-scale move can cause:

- broken cross-references
- lost canonical relationships
- temporary agent confusion
- duplicated documents during transition
- validators failing without a proper migration map

### Required migration approach

Before major structural movement, the repository should define:

1. exact canonical mappings
2. document classes
3. plane assignments
4. index entry points
5. validator expectations
6. deprecation and supersession rules
7. move sequencing

Only then should structural reorganization proceed.

## File and folder policy

### Root

The root should contain only repository-level control files and top-level entry points.

### docs/

docs/ should remain the main documentation knowledge base unless and until a deliberate structural split is executed.

### Future repository-operating folders

If separate folders are created later for repository-operating classes, they should happen only through planned migration.

### Future product-spec folders

If separate folders are created later for product-spec classes, they should also happen through planned migration rather than spontaneous placement.

### Future tools/, scripts/, schemas/

If these are reintroduced, their purpose must be explicit and constrained:

- tools/ for maintained reusable tools
- scripts/ for deterministic helper scripts
- schemas/ only if schemas become true canonical source material

They should not reappear as dumping grounds.

## Change classification model

The rebuilt repository should use a change taxonomy strong enough to guide validation and review.

### Recommended change classes

- repository-operating-readability
- repository-operating-structure
- repository-operating-canonical
- product-spec-readability
- product-spec-structure
- product-spec-canonical
- repo-hygiene
- validator-change
- taxonomy-change
- deprecation-change
- generated-cleanup

### Why this matters

This tells both humans and AI agents:

- what class of truth is affected
- which validators must run
- whether plane boundaries are involved
- whether the change is low risk or high caution

## Commit and review model

### Commit messages should explain

- what changed
- why it changed
- which plane it affected
- which document class it affected
- whether it changed canonical meaning, structure, hygiene, or validation behavior

### Review should verify

- correct plane selection
- correct document class
- canonical source was updated when needed
- no duplicate truth source was introduced
- references remain valid
- metadata remains correct
- generated artefacts were not committed
- plane boundaries remain intact

## What should not be rebuilt in the same form

The rebuild should deliberately avoid recreating heavy structures before the lightweight core is stable.

Do not rebuild by default:

- bulky committed export trees
- large graph output repositories
- repository-committed local databases
- ceremonial multi-phase audit machinery with low operational value
- heavy closure artefact stacks
- broad certification systems before the core operating model is stable

The default rule should be:

build the minimum high-value control plane first, then add only what proves necessary.

## Recommended rebuild sequence

### Phase 1 — Repository operating foundation

Rebuild first:

1. AGENTS.md as the agent operating contract.
2. REBUILD-SYSTEM-SPECIFICATION.md as the root architecture of repository governance.
3. central docs index and entry surfaces.
4. canonical metadata conventions.
5. generated-artifact policy and .gitignore rules.

This establishes authority, entry, and boundaries.

### Phase 2 — Class and plane control

Rebuild second:

1. documentation classes
2. plane assignments
3. canonical registry
4. deprecation and supersession model
5. naming rules for Repository AI versus Product AI

This establishes semantic order.

### Phase 3 — Validator core

Rebuild third:

1. cross-reference validator
2. canonical metadata validator
3. duplicate canonical-concept detector
4. orphan-document detector
5. generated-artifact guard
6. root-layout validator
7. documentation-class validator

This establishes enforceable repository integrity.

### Phase 4 — Agent workflow enforcement

Rebuild fourth:

1. pre-change checklist
2. post-change checklist
3. change classification model
4. commit/review rules
5. high-caution boundary definitions

This establishes deterministic agent behavior.

### Phase 5 — Structural migration

Rebuild fifth:

1. define migration map
2. move docs gradually by class and plane
3. repair references incrementally
4. validate after each migration wave

This establishes safe reorganization rather than chaotic movement.

### Phase 6 — Optional supporting automation

Rebuild last and only if justified:

1. helper scripts
2. compact reusable tools
3. optional CI checks
4. local-only reporting utilities
5. certification systems only if there is real operational need

This prevents return to unnecessary governance weight.

## Success criteria

The rebuilt repository operating model is successful only if an AI agent can answer all of the following before changing anything:

- Am I working in the Repository Operating Model plane or the Product Specification plane?
- What is the canonical file for the concept I am changing?
- What class of document am I editing?
- Where does a new file of this type belong?
- What other files depend on this one?
- What validators must run after the change?
- What files must never be committed?
- Does this change affect structure, readability, canonical meaning, validation, or governance boundaries?

If the repository can answer those questions clearly, it is agent-operable.

## Final design principle

The rebuilt system must be more structured than ad hoc documentation and lighter than the deleted governance platform.

Its goal is not maximum governance overhead.

Its goal is explicit authority, source-of-truth discipline, deterministic placement, lightweight validation, clean repository hygiene, and safe AI-agent execution.

That is the correct foundation for rebuilding the repository end to end with multiple AI agents working consistently against canonical documentation instead of improvising across a flat collection of files.
