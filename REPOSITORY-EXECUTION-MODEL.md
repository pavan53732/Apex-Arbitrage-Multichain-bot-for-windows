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

## Relationship to other documents

This document is referenced by:
- AGENTS.md
- AGENTS_RULES.md
- REBUILD-SYSTEM-SPECIFICATION.md

It is the canonical source for repository execution policy.

## Final principle

This repository is intentionally local-first.

Its goal is explicit human and AI control, not autonomous automation.
