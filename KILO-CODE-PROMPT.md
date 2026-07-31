# Prompt for Kilo Code

## Context

You are working inside this repository:

`Apex-Arbitrage-Multichain-bot-for-windows`

Your job is to perform a **full repository knowledge architecture refactor** for the markdown documentation system.

You must work carefully, deterministically, and with full respect for existing canonical material.

---

## Mission

Implement the repository knowledge model end-to-end across the markdown documentation system.

This means you must:

1. Read all markdown files in the repo.
2. Classify them correctly.
3. Reorganize them into the correct folder structure.
4. Create a **Concept Registry**.
5. Create a **Document Registry**.
6. Assign stable **Document IDs** to all important docs.
7. Add metadata to all important docs.
8. Repair links and references.
9. Preserve canonical meaning.
10. Commit and push the work cleanly to `main`.

This is not a superficial file move.
This is a **repository knowledge-system migration**.

---

## Canonical governing files

Treat these files as the primary authority for the migration:

1. `AGENTS.md`
2. `AGENTS_RULES.md`
3. `REBUILD-SYSTEM-SPECIFICATION.md`
4. `REPOSITORY-EXECUTION-MODEL.md` **(new)**

Read these first and obey them.

Especially obey the latest `REBUILD-SYSTEM-SPECIFICATION.md`, which now defines:

- Repository Knowledge Model
- Plane
- Domain
- Class
- Authority
- Status
- Concept Registry
- Document Registry
- Traceability Registry
- migration sequencing
- validator expectations

Also obey `REPOSITORY-EXECUTION-MODEL.md`, which defines:

- Local-first execution policy
- No GitHub Actions or CI/CD
- No remote automation pipelines
- No repository bots or scheduled automation
- All validation and quality gates executed locally by humans or AI agents

Do not contradict those files.

---

## Architectural model to implement

The repository now uses a knowledge architecture with these dimensions:

### 1. Plane

Allowed values:
- `Repository Operating Model`
- `Product Specification`

### 2. Domain

Use stable semantic domains, not path guesses.

Examples include:

- Governance
- Agent System
- Validation
- Traceability
- Standards
- Documentation Lifecycle
- Contribution
- Registries
- Architecture
- Runtime
- AI
- Dashboard
- Deployment
- Security
- Testing
- Windows
- Plugins
- Interfaces
- Data
- Execution
- Market
- Operations
- Performance
- Reference
- State Machines
- Configuration
- UI

You may add small justified domain refinements only if clearly needed, but avoid domain explosion.

### 3. Class

Allowed or preferred values:

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

Allowed values:

- Canonical
- Derived
- Reference
- Historical
- Generated

### 5. Status

Allowed values:

- Draft
- Review
- Approved
- Active
- Deprecated
- Archived
- Superseded
- Experimental

Authority and Status must be treated as separate fields.

---

## Non-negotiable principles

### A. Do not guess recklessly

If a document is ambiguous, classify conservatively and document the ambiguity.

### B. Do not destroy canonical meaning

If a file appears important, preserve it unless there is a very strong reason not to.

### C. Concepts and documents are different

A concept may have many related documents, but only one canonical owner.

### D. Paths are not identity

Folders may change.
Filenames may change.
Stable IDs and registries are the real control plane.

### E. Registries must become the primary intelligence layer

Do not just shuffle files around.
Create a real machine-readable and human-readable knowledge map.

### F. Generated artifacts are non-canonical by default

Do not commit generated noise.

### G. Root-level discipline must remain strong

Do not clutter the root.

### H. No CI/CD or repository automation

Do not create:
- GitHub Actions workflows
- CI/CD pipeline files
- automation YAMLs
- repository bots
- scheduled automation

All repository operations are executed locally by humans and AI agents.

---

## Work to perform

### Phase 1 — Inventory everything

Read all `*.md` files in the repository.

For each markdown file, determine:

- path
- title
- likely plane
- likely domain
- likely class
- likely authority
- likely status
- whether it is canonical
- whether it duplicates another concept
- whether it is historical, generated, or active
- whether it should move

Produce an internal inventory before making major moves.

---

### Phase 2 — Detect duplicates and overlaps

You must look for:

- duplicate concept docs
- near-duplicate architecture docs
- root docs duplicated under `docs/`
- multiple files claiming the same concept
- files whose names differ but meaning overlaps
- generated or stale governance remnants

You must not silently delete important overlapping files.

Instead:

- choose canonical owner
- mark others as derived/reference/historical where appropriate
- document relationships in the registry

---

### Phase 3 — Create the target knowledge structure

Implement a cleaner folder structure aligned to the knowledge model.

Use folder structure only as an implementation convenience, not as the source of truth.

A recommended target model is:

```text
docs/
├── repository-operating-model/
│   ├── governance/
│   ├── agent-system/
│   ├── validation/
│   ├── traceability/
│   ├── standards/
│   ├── contribution/
│   ├── documentation-lifecycle/
│   ├── workflows/
│   └── registries/
├── product-specification/
│   ├── architecture/
│   ├── runtime/
│   ├── ai/
│   ├── dashboard/
│   ├── deployment/
│   ├── interfaces/
│   ├── security/
│   ├── state-machines/
│   ├── testing/
│   ├── windows/
│   ├── plugins/
│   ├── configuration/
│   ├── operations/
│   ├── performance/
│   ├── ui/
│   └── reference/
├── adr/
├── historical/
└── generated/
```

Important:

- Use good judgment.
- Do not over-nest.
- Keep structure understandable.
- If some existing folders already map well, preserve them where practical.
- If a file belongs in root by policy, do not move it into `docs`.

---

### Phase 4 — Create canonical registries

You must create the following files.

#### 1. `docs/repository-operating-model/registries/CONCEPT-REGISTRY.md`

This should contain a table with columns like:

- Concept ID
- Concept Name
- Canonical Document ID
- Canonical Path
- Plane
- Domain
- Status
- Notes

Concept IDs can use format:
- `CONCEPT-0001`
- `CONCEPT-0002`

Each important concept must have exactly one canonical owner unless explicitly justified otherwise.

#### 2. `docs/repository-operating-model/registries/DOCUMENT-REGISTRY.md`

This should contain a table with columns like:

- Document ID
- Path
- Title
- Plane
- Domain
- Class
- Authority
- Status
- Owner
- Version
- Canonical Source
- Related Concepts
- Supersedes
- Superseded By

Use document ID format:
- `DOC-0001`
- `DOC-0002`

#### 3. `docs/repository-operating-model/registries/TRACEABILITY-REGISTRY.md`

This should contain a table with columns like:

- Traceability ID
- Source ID
- Relationship
- Target ID
- Status
- Notes

Use traceability ID format:
- `TRACE-0001`
- `TRACE-0002`

---

### Phase 5 — Add metadata to documents

Add frontmatter metadata to all important active docs.

At minimum, use fields like:

```yaml
---
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
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
---
```

Adapt values intelligently per file.

Rules:

- Do not wipe existing important metadata; merge carefully.
- Normalize old metadata into the new structure where possible.
- Preserve meaning while modernizing schema.

---

### Phase 6 — Assign IDs deterministically

Assign stable IDs to all important docs and concepts.

Rules:

- IDs must be unique.
- IDs must remain stable once assigned.
- Root canonical files should get low numbers.
- Important registries and core architectural docs should get early IDs.
- Similar concepts should still get separate IDs unless truly identical.

Suggested priority:

1. Root canonical files
2. Core repository-operating docs
3. Core product-spec docs
4. ADRs
5. Reference docs
6. Historical docs

---

### Phase 7 — Normalize authority and status

Separate these two fields everywhere.

Examples:

- Canonical + Active
- Derived + Active
- Reference + Active
- Historical + Archived
- Generated + Experimental

Do not use one field to represent both.

---

### Phase 8 — Repair cross-links

After moves and renames:

- update markdown links
- update indexes
- update maps
- update cross-references
- update canonical source fields
- ensure registry paths match actual files

Do a full pass for broken internal links.

---

### Phase 9 — Build relationship logic

Where possible, record:

- supersedes / superseded_by
- related concepts
- dependencies
- consumers

Do not fabricate complex traceability if evidence is weak.
Use conservative relationships where justified.

---

### Phase 10 — Rationalize duplicates

If both root and `docs/` contain overlapping files:

- keep canonical file in the correct place
- preserve root-only policy files where appropriate
- remove or deprecate duplicates carefully
- if deleting duplicates, ensure registries and references are updated

Do not casually delete without checking meaning.

---

## Important classification guidance

### Repository Operating Model examples

These generally belong to repository-operating domains:

- `AGENTS.md`
- `AGENTS_RULES.md`
- `REPOSITORY-EXECUTION-MODEL.md`
- agent instruction docs
- governance docs
- validation docs
- traceability docs
- documentation lifecycle docs
- documentation rules
- canonical-source rules
- status/review workflow docs
- dependency authority rules
- cross-reference index if repo-operating in nature
- concept/document registry files

### Product Specification examples

These generally belong to product-specification domains:

- architecture
- AI runtime
- AI memory
- AI providers
- dashboard behavior
- deployment
- security
- state machines
- testing specs
- Windows integration
- plugin systems
- interfaces and contracts
- execution engine
- strategy docs
- market or trading behavior
- data/storage/runtime docs tied to the product

### ADRs

Keep in a dedicated ADR area.

### Historical

If clearly obsolete, superseded, or archival, move to historical rather than deleting immediately.

### Generated

Only create generated folder if there are genuinely generated docs worth preserving.
Otherwise avoid unnecessary generated clutter.

---

## Required outputs

You must leave the repository with:

1. A reorganized markdown documentation structure.
2. `CONCEPT-REGISTRY.md`
3. `DOCUMENT-REGISTRY.md`
4. `TRACEABILITY-REGISTRY.md`
5. Metadata added to important docs
6. Stable document IDs assigned
7. Updated internal links
8. Deprecated/historical handling where needed
9. Root discipline preserved
10. A clean git history of the migration

---

## Git workflow

You must:

- create a clean working branch if needed
- make logical commits
- use detailed commit messages
- push the branch or push to `main` if explicitly instructed by the user

If pushing to `main`, use detailed commit messages like:

- `docs(repo): create canonical concept, document, and traceability registries`
- `docs(repo): reorganize repository-operating-model documentation by domain`
- `docs(product): reorganize product specification docs by stable knowledge domains`
- `docs(repo): assign stable document metadata and canonical IDs across active docs`
- `docs(repo): repair links and normalize authority status and traceability fields`

If multiple commits are cleaner, do multiple commits.

---

## Safety rules

- Do not delete important docs without clear justification.
- If uncertain, mark as historical instead of deleting.
- Do not fabricate relationships.
- Do not invent product behavior.
- Do not invent owners unless reasonably inferable; use a safe shared owner like `Runtime Team` when necessary.
- Keep the system consistent rather than perfect.
- Prefer explicit notes over silent assumptions.
- Do not create GitHub Actions, CI/CD, or repository automation.

---

## Definition of done

This task is complete only when:

- all markdown files were reviewed
- all important docs have metadata or are represented in the registry
- all important concepts have canonical owners
- folders reflect the knowledge architecture well enough
- authority and status are separated
- traceability is first-class
- links are repaired
- docs can be understood without relying only on filenames
- the repo is materially closer to a true AI-agent-ready knowledge system

---

## Final report required from Kilo Code

After completing the work, provide a report with:

1. Summary of what changed
2. Folder migration map
3. Number of docs classified
4. Number of docs moved
5. Number of docs given IDs
6. Number of concepts registered
7. Number of duplicates resolved
8. Number of historical/deprecated docs identified
9. Remaining ambiguities
10. Git commits created

---

## Extra instruction to Kilo Code

Do not do a shallow cleanup.

This is a structural knowledge-architecture migration.

Think like a repository architect, not a formatter.

Preserve meaning.
Improve determinism.
Make the repository safer for future AI agents.

All repository operations must follow the local-first execution model defined in `REPOSITORY-EXECUTION-MODEL.md`.
