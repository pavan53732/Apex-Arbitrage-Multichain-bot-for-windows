---
type: POLICY
owner: Runtime Team
status: Canonical
version: 1.0.0
last_updated: 2026-07-31
purpose: Defines the Repository Execution Model for this repository, explicitly stating the local-first philosophy, prohibition of CI/CD and GitHub Actions, and the human + AI interactive execution workflow.
scope: Repository execution, validation execution, commit workflow, local-first tooling, and prohibition of remote automation pipelines.
audience: AI agents, maintainers, contributors, and repository architects.
canonical_source: REPOSITORY-EXECUTION-MODEL.md
---

# REPOSITORY-EXECUTION-MODEL

## Purpose

This document defines how repository operations are executed.

The repository intentionally follows a **Local-First execution model**.

All repository work is performed explicitly by humans and AI agents working interactively, not by automated workflows or remote pipelines.

## Core principles

### 1. Local-first execution

All repository operations are executed locally by:
- human contributors
- AI coding agents
- local scripts
- local validators
- local development tools

No repository operation is executed automatically by remote systems.

### 2. No CI/CD

This repository permanently excludes:
- GitHub Actions
- Azure Pipelines
- GitLab CI
- CircleCI
- Jenkins pipelines
- Buildkite
- Travis CI
- or similar remote automation platforms

No CI/CD system is part of the repository architecture.

### 3. No repository automation

This repository excludes:
- scheduled automation
- repository bots
- background workflow engines
- automated commit workflows
- automated pull request automation
- automated release pipelines

All repository actions are performed explicitly by contributors or AI agents.

### 4. Human + AI collaboration

Repository work is performed by:
- human contributors making intentional commits
- AI agents executing tasks interactively under human supervision
- local tools that assist humans and agents

Automation is interactive, not autonomous.

## Validation execution model

All validation and quality gates are executed locally before committing.

### Who executes validators

Validators are executed by:
- human contributors
- AI agents working on behalf of contributors

### How validators are executed

Validators are run:
- locally on developer machines
- locally in AI agent environments
- manually or as part of explicit local workflows

Validators are not executed by:
- CI/CD platforms
- remote workflow engines
- automated pipelines

### Validator responsibilities

Validators check:
- document integrity
- cross-reference validity
- metadata completeness
- canonical registry consistency
- traceability relationships
- generated-artifact boundaries
- root-layout discipline
- documentation-class alignment

All validation results are reviewed by humans before committing.

## Commit workflow

All commits are created explicitly by contributors or AI agents.

### Required pre-commit steps

Before committing, the contributor or AI agent must:
1. execute relevant local validators
2. review validation results
3. confirm metadata is correct
4. confirm links and references are intact
5. confirm no generated artefacts are staged

### Commit responsibility

Every commit is the responsibility of:
- the human contributor who creates it, or
- the AI agent acting under explicit instruction

No commit is created automatically by a remote system.

## Repository automation policy

This repository does not use:
- GitHub Actions workflows
- CI/CD pipelines
- remote automation scripts
- scheduled tasks
- repository bots
- automated PR workflows
- automated release workflows

All repository operations are performed intentionally by humans and AI agents.

## Exception policy

Exceptions to this policy require:
- explicit approval from maintainers
- documentation of the exception in an ADR
- justification for why local execution is insufficient

No exception should be introduced casually.

## Repository Invariants

The following invariants must never be violated:

- One canonical owner per concept.
- One stable document ID per document.
- No temporary execution artifacts.
- No repository automation.
- No CI/CD.
- Repository always synchronizes to `main` after successful implementation.
- Root remains minimal.
- Knowledge registry always reflects repository state.
- All validation and quality gates executed locally.
- No GitHub Actions or remote pipelines.

## Relationship to other documents

## Conversation is the Default Output Channel

Unless explicitly instructed otherwise by the user:

- all reviews
- all audits
- all summaries
- all findings
- all migration reports
- all implementation reports
- all validation reports
- all completion reports

must be returned directly in the conversation.

AI agents must not create files merely to communicate execution results.

## Workspace Hygiene

AI agents must leave the workspace clean.

Temporary communication artifacts must never be created.

This includes:

- markdown files
- JSON files
- HTML files
- CSV files
- TXT files
- PDF files
- XML files

## Repository Synchronization Policy

Unless the user explicitly instructs otherwise:

- complete all requested work
- execute all required local validators
- stage all required changes
- commit all completed work
- push all committed changes directly to the `main` branch
- synchronize the local repository with the remote repository
- leave the repository in a clean synchronized state

A completed task is not considered complete until repository synchronization succeeds.

## Complete Execution Lifecycle

All AI agents must follow this exact sequence:

1. **Read** — read relevant canonical documents
2. **Understand** — confirm understanding of the task
3. **Classify** — determine plane, domain, class, authority
4. **Plan** — identify canonical files and required changes
5. **Implement** — make changes carefully
6. **Validate** — run relevant local validators
7. **Repair** — fix links, references, metadata
8. **Review** — self-review for quality and consistency
9. **Commit** — commit all completed work
10. **Push to main** — push directly to `main`
11. **Verify synchronization** — confirm remote is synchronized
12. **Return results in chat** — communicate execution results
13. **Leave workspace clean** — ensure no temporary artifacts remain

## Definition of Done

A task is complete only when:

- requested work is implemented
- validators passed
- metadata is valid
- links are repaired
- registries are updated
- git working tree is clean
- changes are committed
- changes are pushed to `main`
- remote is synchronized
- results are returned in chat
- no temporary artifacts remain

## Repository Completion Checklist

Before declaring a task complete, verify:

- [ ] all requested work implemented
- [ ] validators executed and passed
- [ ] metadata valid on all changed docs
- [ ] links repaired
- [ ] registries updated
- [ ] no duplicate concepts introduced
- [ ] workspace clean
- [ ] git status clean
- [ ] commit created with detailed message
- [ ] pushed to `main`
- [ ] remote synchronized
- [ ] results returned in chat
- [ ] no temporary artifacts remain



unless explicitly requested by the user.



This document is referenced by:
- AGENTS.md
- AGENTS_RULES.md
- REBUILD-SYSTEM-SPECIFICATION.md

It is the canonical source for repository execution policy.

## Final principle

This repository is intentionally local-first.

Its goal is explicit human and AI control, not autonomous automation.
