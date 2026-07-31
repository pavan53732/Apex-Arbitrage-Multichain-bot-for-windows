---
metadata_schema_version: 1.0
document_id: DOC-0019
title: Agent Guide
plane: Repository Operating Model
domain: Agent System
class: Guide
authority: Derived
status: Active
owner: UI Team
version: 1.0.0
canonical_source: docs/repository-operating-model/agent-system/agent-guide.md
related_concepts:
  - CONCEPT-0019
dependencies: []
consumers:
  - DOC-0016
  - DOC-0049
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: GUIDE
purpose: Agent Guide documentation.
scope: Reference documentation.
---

# Agent Guide


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Document type
This document is an overview, reference, or index as noted below.

# Agent Guide

## What a gate is
A gate is a file that tells a coding assistant which documents to read before making changes. It is not a source of behavior by itself.

## What authority means
Authoritative documents define the real contract: ownership, lifecycle, interface, schema, or architecture boundaries. Navigation and index documents only point to those sources.

## How to work safely
- Read the authoritative owner docs for the subsystem you are changing.
- Do not infer behavior from short summary docs.
- Do not expand scope beyond what the owner docs define.
- If a contract is missing or ambiguous, stop and ask for clarification.

## Why this matters
These rules prevent coding agents from inventing behaviors that are not written down. That keeps implementation aligned with the repository’s actual contracts.
