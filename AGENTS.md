---
metadata_schema_version: 1.0
governance_version: 2.0.0
document_id: DOC-0001
title: AGENTS
plane: Repository Operating Model
domain: Agent System
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: AGENTS.md
related_concepts:
  - CONCEPT-0001
dependencies: []
consumers:
  - DOC-0016
  - DOC-0017
  - DOC-0019
  - DOC-0045
  - DOC-0046
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
---

# AGENTS.md

## Purpose

This file defines how AI agents and human contributors must operate inside this repository.

This repository follows a two-plane documentation model:

1. Repository Operating Model
2. Product Specification

Agents must understand that these two planes are different and must not be mixed.

## Plane 1 — Repository Operating Model

The Repository Operating Model defines how work happens in this repository.

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

When a task changes how the repository is governed, how docs are classified, how validation should work, how AI agents should behave, or how documentation should be organized, the task belongs to this plane.

## Plane 2 — Product Specification

The Product Specification defines the software system being built.

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

When a task changes how the software product should behave or be structured, the task belongs to this plane.

## Repository AI versus Product AI

Agents must distinguish between two meanings of AI in this repository.

### Repository AI

Repository AI means AI agents that work on the repository itself.

Examples:

- ChatGPT
- Claude Code
- Cursor
- Copilot
- Kilo Code
- future coding or documentation agents

Documents about how these agents must work belong to the Repository Operating Model plane.

### Product AI

Product AI means AI capabilities inside the software product.

Examples:

- AI pipeline
- AI memory
- AI planner
- AI provider manager
- AI gateway
- AI runtime behavior
- AI tool invocation inside the application

Documents about these systems belong to the Product Specification plane.

## Required behavior for agents

Before making changes, every agent must:

1. Read REBUILD-SYSTEM-SPECIFICATION.md.
2. Determine whether the task belongs to the Repository Operating Model plane or the Product Specification plane.
3. Identify the canonical file or files for the concept being changed.
4. Determine the document class involved.
5. Avoid creating duplicate concept documents if an existing canonical file should be edited.
6. Avoid committing generated artefacts.
7. Keep root-level structure intentional and minimal.
8. Do not create GitHub Actions workflows, CI/CD pipeline files, automation YAMLs, or repository automation unless explicitly requested.
9. Before creating any new file, determine whether it represents permanent repository knowledge or temporary execution output. If it is temporary execution output, return it directly in the conversation instead of creating a file.

## Canonical source-of-truth rules

Agents must follow these rules:

- Do not treat all markdown files as equally authoritative.
- Prefer canonical specifications over summaries, guides, or historical material.
- If two files appear to define the same concept, do not guess. Clarify or establish a canonical relationship.
- Do not edit a lower-authority file in a way that silently overrides a canonical file.
- If a file is replaced, ensure the replacement relationship is explicit.

## Documentation classes

The repository uses documentation classes.

Primary classes include:

- Repository Operating Model
- Product Specification
- ADR
- Reference
- Guide
- Historical
- Certification if intentionally restored later
- Generated, which is non-canonical by default

Agents must preserve class boundaries and should not casually mix repository-operating documents with product-specification documents.

## Validation expectations

After structural or canonical changes, agents should ensure that applicable validation checks can later verify:

- cross-references remain valid
- canonical metadata is complete
- duplicate canonical concepts are not introduced
- important documents are not orphaned
- generated artefacts are not committed
- root-level clutter is not introduced
- repository-operating and product-specification semantics remain distinct

## Root-level discipline

The root of the repository is reserved for repository-level control and entry files.

Agents should not add new root files or folders unless there is a strong structural reason.

## Change classes

Agents should classify changes before execution.

Recommended classes:

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

## High-caution changes

The following changes require extra caution:

- changes to REBUILD-SYSTEM-SPECIFICATION.md
- changes to AGENTS.md
- changes to canonical architecture definitions
- taxonomy or structure changes
- deprecation or supersession changes
- validator-rule changes
- reintroduction of tools/, scripts/, schemas/, or governance artefact systems as canonical layers

## Repository execution model

This repository follows a local-first execution model.

All repository operations are executed locally by:
- human contributors
- AI coding agents
- local scripts
- local validators
- local development tools

The repository intentionally excludes:
- GitHub Actions
- CI/CD pipelines
- remote automation platforms
- repository bots
- scheduled automation

All validation and quality gates are executed explicitly by contributors before committing.

See `./REPOSITORY-EXECUTION-MODEL.md` for the canonical policy.

## Temporary Execution Output Policy

The repository is not a workspace for temporary AI outputs.

Unless the user explicitly requests a permanent repository document, AI agents MUST NOT create temporary files during execution.

This prohibition includes, but is not limited to:

- AUDIT.md
- REVIEW.md
- REPORT.md
- SUMMARY.md
- ANALYSIS.md
- FINDINGS.md
- NOTES.md
- PLAN.md
- TODO.md
- MIGRATION.md
- IMPLEMENTATION-REPORT.md
- COMPLETION-REPORT.md
- STATUS.md
- LOG.md
- RESULT.md

## File Creation Decision Policy

Before creating any file, the agent must answer:

1. Is this permanent repository knowledge?
2. Does this concept already exist?
3. Can an existing canonical file be updated?
4. Is a new file architecturally required?

## Canonical Edit-First Rule

If a canonical document already owns the concept:

- update the canonical document
- do not create another document
- do not split authority
- do not duplicate specifications

This preserves source-of-truth discipline.



If the answer to any of these is no, do not create the file.

This prevents repository growth from unnecessary documents.



or equivalent markdown, text, JSON, HTML, CSV, XML or PDF artifacts.

Temporary execution output belongs in the conversation.

It does not belong in:

- the repository
- the workspace
- the project root
- temporary folders
- docs/
- generated/
- reports/

unless explicitly requested by the user.

## Generated artefact rule

Generated outputs are non-canonical by default and should not be committed unless explicitly justified.

Examples include:

- exports
- caches
- graphs
- local databases
- analysis outputs
- temporary reports
- tool-generated summaries
- CI/CD workflow files and repository automation unless explicitly approved

Temporary execution files are prohibited even if they are not committed.

Avoid creating temporary artifacts entirely unless the user explicitly requests them.

## Commit expectations

Good commits should explain:

- what changed
- why it changed
- which plane it affected
- which document class it affected
- whether canonical meaning, structure, validation behavior, or repository hygiene changed

## Post-Change Verification Checklist

After every implementation, verify:

- [ ] metadata valid
- [ ] registries updated
- [ ] links repaired
- [ ] references repaired
- [ ] duplicate concepts not introduced
- [ ] workspace clean
- [ ] git status clean
- [ ] commit created
- [ ] pushed to `main`
- [ ] synchronization verified



## Default operating principle

Agents must work against source-of-truth, not improvisation.

If a task is ambiguous, the correct action is to clarify authority, class, plane, and canonical source before making structural or semantic changes.
