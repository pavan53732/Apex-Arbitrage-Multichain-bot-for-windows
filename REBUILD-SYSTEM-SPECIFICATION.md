---
type: SPECIFICATION
owner: Runtime Team
status: Canonical
version: 1.0.0
last_updated: 2026-07-31
purpose: Defines what governance, tooling, scripts, and validation systems must be rebuilt after repository reset, why each exists, and how each helps AI agents operate safely and consistently.
scope: Repository governance, validation, AI-agent operating model, documentation enforcement, and deterministic repo automation.
audience: AI agents, maintainers, repository architects, automation engineers.
canonical_source: docs/REBUILD-SYSTEM-SPECIFICATION.md
---

# REBUILD-SYSTEM-SPECIFICATION

## Purpose

This document defines the systems that must be rebuilt after removing the previous governance, tooling, scripting, and validator layers from the repository.

The goal is not to restore complexity for its own sake. The goal is to rebuild a smaller, clearer, and more intentional agent-operating system around the repository so AI agents can work safely, consistently, and deterministically.

## Why rebuild these systems

The deleted systems were serving an important architectural purpose even if the previous implementation became too heavy.

Those systems existed to do five things:

1. Tell AI agents what the canonical source of truth is.
2. Prevent generated artefacts from polluting the repository.
3. Validate that documentation remains internally consistent.
4. Define safe operating boundaries for automated changes.
5. Make repository changes auditable and repeatable.

Without these systems, AI agents can still edit files, but they will operate with weaker guarantees. That increases the chance of drift, broken references, duplicate docs, and accidental deletion of important material.

## What must be rebuilt

### 1. Agent operating contract

A lightweight but explicit agent operating contract must be rebuilt.

This should define:

- What an AI agent is allowed to edit.
- What an AI agent must read before editing.
- What counts as canonical documentation.
- What files are generated and must never be committed.
- What validation checks must pass before a change is accepted.

This helps AI agents by reducing ambiguity. Instead of guessing what matters, they can follow an explicit operating contract.

### 2. Repository structure rules

A small repository-structure ruleset must be rebuilt.

This should define:

- What belongs at repo root.
- What belongs under docs/.
- What belongs under future schemas/, scripts/, or tools/ directories if they are reintroduced.
- Which folders are source-of-truth only.
- Which folders are rebuildable or generated.

This helps AI agents by making placement deterministic. If an agent creates or edits a file, it should know exactly where that file belongs.

### 3. Canonical documentation registry

A canonical documentation registry should be rebuilt in a simpler form.

This can be a single index document or compact manifest that defines:

- The major document domains.
- The canonical file for each concept.
- Deprecated or replaced documents.
- Key entry points for agent reasoning.

This helps AI agents by preventing duplicate concept creation. If an agent wants to change memory behavior, runtime behavior, deployment behavior, or architecture behavior, it can locate the canonical file first.

### 4. Cross-reference validation

Cross-reference validation must be rebuilt.

The new version should verify:

- Referenced markdown files exist.
- Internal doc links are not broken.
- Renamed or moved documents do not leave stale references.
- Key index documents still point to valid locations.

This helps AI agents by catching structural drift immediately after file moves or rewrites.

### 5. Ownership and metadata validation

Ownership and metadata checks should be rebuilt, but more lightly than before.

The new version should validate a minimum metadata set for important docs:

- owner
- purpose
- status
- canonical_source
- last_updated

This helps AI agents by making every important document interpretable. An agent should be able to tell whether a file is active, historical, authoritative, or incomplete.

### 6. Generated artefact policy

A generated artefact policy must be rebuilt.

This should define:

- What outputs are generated.
- Where generated outputs may be written locally.
- What must be ignored in git.
- What may be regenerated on demand.
- What should never be committed.

This helps AI agents by preventing repository pollution. Agents often generate summaries, exports, graphs, caches, databases, and temporary analysis outputs. Without rules, they may accidentally commit them.

### 7. Documentation quality checks

Basic documentation quality checks should be rebuilt.

The new version should check only high-value issues:

- Broken references.
- Missing canonical metadata on key docs.
- Duplicate filenames for canonical concepts.
- Empty placeholder files.
- Obvious orphan files not linked from any index.

This helps AI agents by maintaining a clean knowledge layer without recreating excessive governance overhead.

### 8. Change classification model

A change classification model should be rebuilt.

Every proposed change should fall into one of a few simple classes:

- documentation-only
- structure-only
- validation-only
- schema-affecting
- agent-policy-affecting
- architecture-affecting

This helps AI agents by telling them what level of caution and validation is required before committing.

### 9. Pre-change and post-change workflow

A compact workflow should be rebuilt for AI agents.

Before change:

- Read relevant canonical docs.
- Identify files being changed.
- Identify whether any canonical docs must also be updated.
- Identify whether generated outputs are involved.

After change:

- Run relevant validations.
- Confirm references still resolve.
- Confirm no generated files were added.
- Confirm the change is consistent with the agent operating contract.

This helps AI agents by making behavior procedural rather than improvisational.

### 10. Minimal tooling layer

A smaller tooling layer may be rebuilt later, but only for deterministic tasks.

Allowed rebuild targets include:

- markdown reference validator
- metadata validator
- canonical-doc index generator
- duplicate filename detector
- orphan-doc detector
- git hygiene checker

This helps AI agents by automating repeatable checks while keeping implementation small and understandable.

## What should not be rebuilt in the same heavy form

The repository should avoid immediately recreating a very heavy governance framework with large generated outputs, persistent local databases, large export trees, or deeply nested audit machinery.

The next version should stay focused on the minimum useful control plane for AI agents.

Do not rebuild the following unless there is a strong proven need:

- large generated graph directories
- exported document mirrors committed into git
- local governance databases committed to the repo
- bulky closure artefact trees
- multi-phase certification paperwork unless needed for real compliance

## Recommended rebuild order

### Phase A — Core control layer

Rebuild first:

1. AGENTS.md operating contract
2. docs index / canonical registry
3. generated artefact policy
4. .gitignore cleanup rules

This establishes the minimum safe behavior model.

### Phase B — Basic validation layer

Rebuild second:

1. markdown reference validator
2. metadata validator
3. orphan-doc detector
4. duplicate canonical-concept detector

This establishes repository integrity checks.

### Phase C — Agent workflow layer

Rebuild third:

1. pre-change checklist
2. post-change checklist
3. change classification rules
4. commit hygiene rules

This establishes deterministic agent behavior.

### Phase D — Optional automation layer

Rebuild last and only if needed:

1. compact helper scripts
2. lightweight reporting utilities
3. local non-committed generated dashboards
4. optional CI checks if repository workflows later need them

This keeps automation proportional to actual value.

## What this helps with

Rebuilding these systems helps in six concrete ways.

### For AI agents

- Reduces ambiguity.
- Makes file placement predictable.
- Prevents duplicate document creation.
- Forces use of canonical sources.
- Catches broken references after refactors.
- Prevents accidental commits of generated files.

### For maintainers

- Makes repository structure easier to reason about.
- Makes agent changes easier to review.
- Reduces hidden drift between docs.
- Preserves a clean source-of-truth layer.
- Makes future repository cleanup less painful.

### For future system rebuilds

- Creates a stable knowledge base before code generation.
- Lets agents rebuild tooling against clear specifications.
- Separates permanent design intent from temporary artefacts.
- Makes future automation modular instead of tangled.

## Minimum final target

At minimum, the rebuilt repository control system should answer these questions clearly:

- What is the canonical source for each major concept?
- What files are allowed to be committed?
- What files are generated and must stay out of git?
- What must an AI agent read before changing something?
- What checks must pass before a change is accepted?
- How can a maintainer tell whether a document is active and trustworthy?

If the rebuilt system answers those questions clearly, it is already doing its job.

## Final design principle

The rebuilt control layer should be lighter than the deleted one, but clearer than having nothing.

The objective is not maximum governance.
The objective is maximum clarity per unit of complexity.

That is the right foundation for a repository that will later be rebuilt with AI agents doing substantial portions of the work.
