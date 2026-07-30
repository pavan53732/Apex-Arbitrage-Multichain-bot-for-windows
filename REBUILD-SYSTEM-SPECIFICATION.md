---
type: SPECIFICATION
owner: Runtime Team
status: Canonical
version: 2.0.0
last_updated: 2026-07-31
purpose: Defines the complete docs-governed repository operating model that must be rebuilt for AI agents, including canonical specifications, repository hygiene, validation systems, governance boundaries, change workflows, and the reasons each layer exists.
scope: Repository operating model, AI-agent execution rules, canonical documentation system, validator design, governance boundaries, repo hygiene, and future rebuild sequencing.
audience: AI agents, maintainers, repository architects, automation engineers, and future contributors rebuilding the system.
canonical_source: REBUILD-SYSTEM-SPECIFICATION.md
---

# REBUILD-SYSTEM-SPECIFICATION

## Purpose

This document defines the full system that must be rebuilt so the repository becomes a docs-governed operating environment for AI agents.

The repository should not be treated as a random set of files that an AI edits opportunistically. It should behave as a controlled workspace where documentation is the canonical source of truth, repository structure is intentional, generated artefacts are excluded, validators catch structural drift, and governance boundaries stop agents from improvising outside approved rules.

The target outcome is a repository where an AI agent can reliably understand what the system is, where truth lives, what is safe to change, what must be validated, and what must never be committed.

## Core idea

The rebuild is not only about adding documents back.

The rebuild is about constructing a docs-governed repository operating model for AI agents made of five tightly connected layers:

1. Canonical specifications.
2. Repository hygiene.
3. Validators and integrity checks.
4. Governance boundaries and operating rules.
5. Agent execution workflows.

Those five layers work together so agents operate against source-of-truth instead of guessing, duplicating concepts, or silently drifting the repository into inconsistency.

## Why this system is needed

Without a docs-governed operating model, AI agents usually behave in unsafe and inconsistent ways.

Typical failure modes without this system include:

- creating duplicate documents for the same concept
- editing a non-canonical file while the real source of truth remains unchanged
- moving files without repairing inbound references
- committing generated artefacts, temporary exports, caches, or reports
- introducing structural drift between docs, rules, and implementation plans
- making changes without understanding which architecture or policy document governs the change
- treating every file as equally authoritative even when some are reference-only, historical, or obsolete

A docs-governed repository operating model exists to prevent those failure modes.

## System objectives

The rebuilt system must achieve the following objectives.

### 1. Canonical truth

Every major concept must have a canonical home.

An AI agent must be able to answer questions like:

- Where is the canonical architecture description?
- Where is the canonical runtime behavior specification?
- Where is the canonical AI behavior specification?
- Where are deployment, testing, security, and operations truths defined?
- Which file is the source of truth if multiple files mention the same concept?

If those answers are unclear, the repository is not agent-ready.

### 2. Deterministic placement

An AI agent must know where new files belong before it creates them.

Placement must not depend on style preference or guesswork. The repository structure has to tell the agent where architecture docs, guides, reference docs, state machines, AI docs, deployment docs, testing docs, and future tooling docs belong.

### 3. Validation before trust

Repository content should not be trusted merely because it exists.

Validators must prove that high-value structural assumptions are still true. Examples include link validity, canonical metadata presence, absence of duplicate canonical files, and generated-artifact exclusion.

### 4. Clear operating boundaries

An AI agent must know what it can change, what requires extra caution, and what is not allowed.

The repository must define safe and unsafe change zones, required review conditions, and categories of files that should never be treated casually.

### 5. Lightweight governance

The rebuilt system must be strong enough to guide agents, but lighter than the deleted governance stack.

The goal is not maximal bureaucracy. The goal is high clarity, low ambiguity, and proportional enforcement.

## Target operating model

The rebuilt repository operating model should work like this.

### Step 1. Agent enters the repository

The agent first reads root-level entry points and canonical guidance.

At minimum, that should include:

- AGENTS.md
- REBUILD-SYSTEM-SPECIFICATION.md
- docs/README.md or an equivalent docs index
- the canonical domain document relevant to the requested task

The agent does not start by editing. It starts by locating authority.

### Step 2. Agent identifies canonical sources

Before touching any file, the agent must determine:

- the primary canonical file for the concept being changed
- any dependent docs that must remain consistent with that file
- whether the target file is canonical, reference-only, guide-only, historical, or generated

If the agent cannot answer those questions, it should not proceed blindly.

### Step 3. Agent classifies the change

Every change must be classified before execution.

Minimum change classes:

- documentation-only
- structure-only
- canonical-specification change
- agent-policy change
- repository-hygiene change
- validation-tooling change
- architecture-affecting change
- generated-artefact cleanup

The class determines how much validation and review is required.

### Step 4. Agent performs the change

The agent edits only the files justified by the change plan.

The agent must avoid:

- creating duplicate concept docs
- introducing new root clutter
- adding generated files to git
- changing canonical meaning in one file while leaving dependent docs stale
- editing a reference document when a canonical document exists upstream

### Step 5. Agent validates the result

After changing files, the agent runs applicable validation checks.

The change is not complete until structural integrity is re-verified.

### Step 6. Agent commits with traceable reasoning

The commit should explain what changed, why it changed, which operating layer it affected, and whether it altered canonical behavior, structure, hygiene, or validation.

## Layer 1 — Canonical specifications

Canonical specifications are the foundation of the whole model.

### What they are

Canonical specifications are the authoritative documents that define how the repository, the system architecture, the AI behavior model, and the operating rules are supposed to work.

### What they must do

Canonical specifications must:

- define the authoritative meaning of a concept
- have a clear owner
- state their purpose
- show their status
- identify their canonical source path
- be discoverable from an index or registry
- remain stable enough that agents can rely on them

### What they help with

They help AI agents by removing semantic ambiguity.

If a repository has three files talking about memory or deployment, but only one is canonical, the agent must know which one carries decision authority. Without that, the agent may update the wrong file and accidentally create drift.

### Minimum canonical doc metadata

Every important canonical document should contain at least:

- type
- owner
- status
- version
- last_updated
- purpose
- scope
- audience
- canonical_source

Optional but useful:

- dependencies
- consumers
- supersedes
- superseded_by
- related_documents

### Canonical hierarchy

The rebuilt system should define a hierarchy of authority.

A practical order is:

1. Root repository operating specifications.
2. Canonical architecture documents.
3. Canonical domain documents.
4. Domain reference documents.
5. Guides and workflows.
6. Historical or deprecated documents.

That hierarchy tells the agent how to resolve conflicts when multiple files discuss similar subjects.

## Layer 2 — Repository hygiene

Repository hygiene is the structural discipline that keeps the knowledge base clean and dependable.

### What repository hygiene means

Repository hygiene means the repository contains intentional, reviewable, source-of-truth material rather than mixed-quality runtime output, stale duplicates, and arbitrary placement.

### Hygiene rules that must be rebuilt

The rebuilt repository hygiene model should define all of the following.

#### A. Root-level discipline

The root should remain small and intentional.

Root files should be limited to top-level entry points and repository-level control documents such as:

- README.md
- AGENTS.md
- AGENTS_RULES.md if still needed
- REBUILD-SYSTEM-SPECIFICATION.md
- .gitignore

Everything else should have a justified folder location.

#### B. Folder purpose clarity

Each major folder must have a clear purpose.

Examples:

- docs/ for source-of-truth documentation and supporting reference material
- future scripts/ only for intentionally maintained deterministic helper scripts
- future tools/ only for intentionally maintained reusable tooling
- future schemas/ only if structured schemas are reintroduced as canonical source material

#### C. Generated artefact exclusion

Generated files must not be committed unless there is a deliberate exception.

Examples of files that should normally stay out of git:

- exports
- graphs
- caches
- database files
- temporary reports
- machine-generated dashboards
- closure artefacts
- analysis dumps
- local run outputs

#### D. Duplicate suppression

The system should actively prevent duplicate files representing the same concept without a clear canonical relationship.

#### E. Deprecation handling

If a document is replaced, the system should mark the relationship rather than silently leaving old files to drift.

### What repository hygiene helps with

Repository hygiene helps AI agents by making the workspace predictable. Agents make fewer mistakes when the repo has strong placement rules, fewer duplicate concepts, and cleaner separation between canonical content and generated output.

## Layer 3 — Validators and integrity checks

Validators are the enforcement layer that turns documentation intent into something testable.

### Why validators matter

Without validators, the repository can slowly become inconsistent while still looking acceptable to humans at a glance.

Validators give the repository a way to detect drift automatically.

### What validators should exist in the rebuilt system

The rebuilt validator stack should be smaller than the deleted one, but it must still cover the highest-value checks.

#### 1. Cross-reference validator

Checks:

- markdown links resolve
- referenced files exist
- moved files do not leave stale paths behind
- key index documents still resolve to real targets

Benefit for AI agents:

- catches mistakes immediately after file moves, renames, or doc rewrites

#### 2. Canonical metadata validator

Checks:

- important documents contain required metadata
- canonical_source fields are present and accurate
- status values are valid
- owner and purpose are not missing

Benefit for AI agents:

- ensures every important document can be interpreted programmatically and semantically

#### 3. Duplicate canonical-concept detector

Checks:

- two files do not present themselves as the same canonical concept without an explicit relationship
- suspicious overlaps are flagged for human review

Benefit for AI agents:

- reduces the chance of agents reinforcing duplicate truth sources

#### 4. Orphan document detector

Checks:

- important docs are reachable from at least one index, map, or canonical registry
- obviously disconnected docs are flagged

Benefit for AI agents:

- prevents important material from becoming invisible and therefore ignored

#### 5. Generated-artifact guard

Checks:

- no ignored generated outputs are accidentally staged or committed
- generated directories remain excluded

Benefit for AI agents:

- prevents repo pollution from automated runs

#### 6. Root-layout validator

Checks:

- unauthorized root-level clutter is not introduced
- repository-level files remain intentional

Benefit for AI agents:

- preserves the navigational clarity of the repository

### Validator design principles

The rebuilt validators should be:

- deterministic
- fast
- understandable
- focused on high-value failure modes
- easy for agents to run locally
- strict enough to prevent drift but not so heavy that they create ceremonial overhead

## Layer 4 — Governance boundaries

Governance boundaries define the safe operating envelope for AI agents.

### What governance boundaries are

Governance boundaries are the rules that tell an agent what kinds of actions are allowed, what requires stronger justification, and what is prohibited without explicit instruction.

### Boundary types that should be rebuilt

#### A. Edit-scope boundaries

The repository should define which file classes can be edited directly and which require extra caution.

Examples:

- guide docs can be updated freely if canonical meaning is unchanged
- canonical architecture docs require careful consistency updates
- root-level operating specs require the highest caution
- deprecated documents should not be revived accidentally

#### B. Generated-versus-source boundaries

Agents must know the difference between source-of-truth files and generated artefacts.

Generated output should never quietly become canonical.

#### C. Structural boundaries

Agents should not introduce new top-level folders or new document families without a structural justification.

#### D. Authority boundaries

Agents should not override a canonical document by editing a lower-authority summary or guide.

#### E. Risk boundaries

Changes affecting agent policy, canonical architecture, or repository control rules should trigger stronger validation and more explicit explanation.

### What governance boundaries help with

Governance boundaries stop AI agents from treating every file and every action as equivalent. That reduces unsafe improvisation and preserves system coherence.

## Layer 5 — Agent execution workflows

This layer defines how an AI agent should behave operationally inside the repository.

### Pre-change workflow

Before editing anything, an AI agent should do all of the following:

1. Read AGENTS.md and the relevant canonical domain document.
2. Identify the exact concept being changed.
3. Locate the canonical source for that concept.
4. Identify dependent docs that may also require updates.
5. Determine whether the target is canonical, reference, guide, or historical.
6. Classify the change type.
7. Confirm the change does not involve committing generated artefacts.

### Change workflow

During the change, an AI agent should:

1. Edit the smallest justified set of files.
2. Preserve canonical relationships.
3. Update internal references if paths or names change.
4. Avoid creating duplicate files when an existing canonical file should be updated instead.
5. Keep repository placement rules intact.

### Post-change workflow

After the change, an AI agent should:

1. Run relevant validators.
2. Re-check changed references.
3. Confirm no generated files were added.
4. Confirm metadata still reflects reality.
5. Write a commit message that explains architectural intent, not just file movement.

### Human-review workflow

Some change classes should be marked as requiring explicit human review or at least extra caution.

Examples:

- changes to root-level operating specs
- changes to canonical architecture definitions
- changes to governance boundaries
- changes that deprecate or replace canonical docs
- changes that reintroduce tooling or schemas as new source-of-truth layers

## Canonical documentation system to rebuild

The repository should include a coherent documentation control system.

### Required parts

#### 1. Docs index

A central docs index should explain the documentation tree and point agents to domain entry points.

#### 2. Canonical registry

A simple registry should list major concepts and their canonical files.

Possible registry fields:

- concept_name
- canonical_file
- document_type
- owner
- status
- related_docs
- notes

#### 3. Domain entry points

Each major documentation domain should have a clear entry document so agents do not need to scan the whole tree blindly.

#### 4. Deprecation mapping

If any file is replaced, the repository should record what replaced it.

### What this system helps with

This system turns documentation from passive reading material into an active navigation model that agents can follow during work.

## File and folder policy to rebuild

The repository should define explicit placement rules.

### Root

Root should contain only repository-level control files.

### docs/

docs/ should contain the canonical knowledge base and structured supporting docs.

### Future tools/

If tools/ is reintroduced, it should contain only intentionally maintained reusable programs, not generated output and not one-off experiments.

### Future scripts/

If scripts/ is reintroduced, it should contain deterministic helper scripts that are clearly scoped, documented, and safe for automation.

### Future schemas/

If schemas/ is reintroduced, it should happen only when schemas are truly part of canonical source material rather than speculative structure.

### Generated outputs

Generated outputs should go only to ignored locations and should be reconstructible.

## Change classification model to rebuild

The repository should implement a practical change taxonomy.

### Recommended classes

- docs-readability
- docs-structure
- docs-canonical
- docs-deprecation
- repo-hygiene
- validator-change
- agent-policy-change
- architecture-definition-change
- generated-cleanup

### Why classification matters

Classification lets agents and maintainers decide:

- which docs must be read before editing
- which validators must run
- which changes require stronger scrutiny
- which commit style to use

## Commit and review expectations

A rebuilt system should define commit expectations clearly.

### Good commit messages should explain

- what changed
- why it changed
- what operating layer it affected
- whether the change touched canonical truth, structure, validation, or governance rules
- whether generated artefacts were removed or prevented

### Review should verify

- canonical source was edited instead of a duplicate
- references remain valid
- metadata remains correct
- placement rules were followed
- no generated artefacts were committed
- the change class matches the actual impact

## What should not be rebuilt in the same form

The previous system became too heavy in certain areas. The rebuild should deliberately avoid recreating those heavy patterns unless there is a proven need.

Avoid rebuilding these by default:

- large committed export trees
- bulky graph output directories
- repository-committed local databases
- heavy closure artefact frameworks
- broad ceremonial audit paperwork with little operational value
- complex multi-phase governance machinery before the lightweight core is stable

The next system should begin with the smallest operating layer that still gives AI agents clear rules and dependable truth.

## Recommended rebuild sequence

### Phase 1 — Repository operating foundation

Rebuild first:

1. AGENTS.md as the primary agent operating contract.
2. REBUILD-SYSTEM-SPECIFICATION.md as the root architectural intent document.
3. docs/README.md or equivalent central docs index.
4. canonical registry for major concepts.
5. generated-artifact policy and .gitignore rules.

This phase establishes authority, entry points, and safe repository boundaries.

### Phase 2 — Canonical documentation control

Rebuild second:

1. canonical metadata conventions
2. canonical-versus-reference distinctions
3. deprecation and supersession rules
4. indexability rules for important docs

This phase establishes semantic order in the knowledge base.

### Phase 3 — Integrity validation

Rebuild third:

1. cross-reference validator
2. metadata validator
3. orphan-doc detector
4. duplicate canonical-concept detector
5. generated-artifact guard
6. root-layout validator

This phase establishes testable repository integrity.

### Phase 4 — Agent workflow enforcement

Rebuild fourth:

1. pre-change checklist
2. post-change checklist
3. change classification model
4. commit and review rules
5. high-risk change boundaries

This phase establishes deterministic agent execution behavior.

### Phase 5 — Optional supporting automation

Rebuild last and only if justified:

1. small helper scripts
2. compact reusable tools
3. optional CI integration
4. optional local-only reporting utilities

This phase adds convenience without recreating bloat.

## What this full operating model helps with

### For AI agents

- tells them where truth lives
- prevents improvisation against the wrong files
- makes file placement predictable
- distinguishes canonical docs from secondary docs
- catches broken references quickly
- prevents accidental generated-file commits
- gives procedural steps before and after changes
- reduces conflicting interpretations of repository structure

### For maintainers

- makes agent work easier to audit
- makes repository structure easier to understand
- reduces duplicate documentation and semantic drift
- preserves a cleaner source-of-truth layer
- makes resets and rebuilds less chaotic
- improves confidence that future automation is acting on the correct files

### For future rebuilds

- creates a stable knowledge substrate before code or tooling expansion
- lets future validators and tools be built against a well-defined repository model
- keeps automation modular instead of tangled
- creates a durable operating framework that multiple AI agents can share consistently

## Success criteria

The rebuilt repository operating model is successful only if an AI agent can answer all of these questions clearly before changing anything:

- What file is the canonical source for the concept I am changing?
- What other files depend on that canonical file?
- Is the target file canonical, reference, guide, historical, or generated?
- Where does a new file of this type belong?
- What validations must run after I change this?
- What files must never be committed?
- Does this change affect only readability, or does it affect repository truth and operating rules?

If the repository can answer those questions clearly, it is agent-operable.

## Final design principle

The rebuilt system must be stronger than ad hoc documentation, but lighter than the deleted governance stack.

It should give AI agents enough structure to act safely and consistently without forcing the repository back into heavyweight operational ceremony.

The correct design goal is:

high clarity, explicit authority, deterministic placement, lightweight validation, and strong source-of-truth discipline.

That is the right foundation for rebuilding the rest of the repository with AI agents working against canonical specifications instead of improvising from scattered files.
