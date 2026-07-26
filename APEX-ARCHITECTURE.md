# APEX — Project Overview

## Purpose
This file is the top-level overview and navigation map for the APEX repository. It is intentionally concise. Detailed implementation guidance lives in the `docs/` directory, which is the single source of truth for application behaviour, architecture, interfaces, and delivery rules.

## Vision
APEX is a Windows-first desktop arbitrage platform with AI-assisted workflows, modular strategy execution, strict risk controls, and multi-chain/multi-DEX integration.

## Documentation Principles
- Every topic has one authoritative document.
- AI agents and human contributors must follow repository documentation before writing code.
- When documentation is missing or ambiguous, the correct action is to update the specification first.

## Documentation Map
### Core Architecture
- [`docs/README.md`](./docs/README.md)
- [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md)
- [`docs/PROJECT-STRUCTURE.md`](./docs/PROJECT-STRUCTURE.md)
- [`docs/MODULE-DEPENDENCY.md`](./docs/MODULE-DEPENDENCY.md)
- [`docs/DATA-FLOW.md`](./docs/DATA-FLOW.md)
- [`docs/EVENT-FLOW.md`](./docs/EVENT-FLOW.md)
- [`docs/COMPONENT-DIAGRAMS.md`](./docs/COMPONENT-DIAGRAMS.md)

### Engineering Standards
- [`docs/CODING-STANDARDS.md`](./docs/CODING-STANDARDS.md)
- [`docs/CONFIGURATION.md`](./docs/CONFIGURATION.md)
- [`docs/STATE-MANAGEMENT.md`](./docs/STATE-MANAGEMENT.md)
- [`docs/ERROR-HANDLING-LOGGING.md`](./docs/ERROR-HANDLING-LOGGING.md)
- [`docs/PERMISSION-MODEL.md`](./docs/PERMISSION-MODEL.md)
- [`docs/FILE-STORAGE.md`](./docs/FILE-STORAGE.md)
- [`docs/NON-FUNCTIONAL-REQUIREMENTS.md`](./docs/NON-FUNCTIONAL-REQUIREMENTS.md)
- [`docs/PERFORMANCE-TARGETS.md`](./docs/PERFORMANCE-TARGETS.md)

### AI, Trading, and Runtime Systems
- [`docs/AI-PIPELINE.md`](./docs/AI-PIPELINE.md)
- [`docs/AI-SETTINGS.md`](./docs/AI-SETTINGS.md)
- [`docs/CLOUD-AI-INTEGRATION.md`](./docs/CLOUD-AI-INTEGRATION.md)
- [`docs/STRATEGIES.md`](./docs/STRATEGIES.md)
- [`docs/RISK-ENGINE.md`](./docs/RISK-ENGINE.md)
- [`docs/CHAIN-INTEGRATION.md`](./docs/CHAIN-INTEGRATION.md)
- [`docs/DEX-INTEGRATION.md`](./docs/DEX-INTEGRATION.md)
- [`docs/IPC-PROTOCOL.md`](./docs/IPC-PROTOCOL.md)
- [`docs/IPC-MESSAGE-CATALOG.md`](./docs/IPC-MESSAGE-CATALOG.md)
- [`docs/API-REFERENCE.md`](./docs/API-REFERENCE.md)
- [`docs/API-CONTRACTS.md`](./docs/API-CONTRACTS.md)
- [`docs/DATABASE-SCHEMA.md`](./docs/DATABASE-SCHEMA.md)

### UI and Product Design
- [`docs/DESIGNER-PROTOCOLS.md`](./docs/DESIGNER-PROTOCOLS.md)
- [`docs/DESIGN-SYSTEM.md`](./docs/DESIGN-SYSTEM.md)
- [`docs/UI-COMPONENT-SPEC.md`](./docs/UI-COMPONENT-SPEC.md)
- [`docs/FEATURE-MATRIX.md`](./docs/FEATURE-MATRIX.md)

### Operations and Delivery
- [`docs/TESTING-GUIDE.md`](./docs/TESTING-GUIDE.md)
- [`docs/WINDOWS-DESKTOP.md`](./docs/WINDOWS-DESKTOP.md)
- [`docs/BUILD-RELEASE-CICD.md`](./docs/BUILD-RELEASE-CICD.md)
- [`docs/MONITORING-OBSERVABILITY.md`](./docs/MONITORING-OBSERVABILITY.md)
- [`docs/DEPLOYMENT.md`](./docs/DEPLOYMENT.md)
- [`docs/IMPLEMENTATION-ROADMAP.md`](./docs/IMPLEMENTATION-ROADMAP.md)
- [`docs/ENHANCEMENT-ROADMAP.md`](./docs/ENHANCEMENT-ROADMAP.md)
- [`docs/DECISION-LOG.md`](./docs/DECISION-LOG.md)
- [`docs/KNOWN-LIMITATIONS.md`](./docs/KNOWN-LIMITATIONS.md)

### Support and Shared Vocabulary
- [`docs/SECURITY.md`](./docs/SECURITY.md)
- [`docs/FAQ.md`](./docs/FAQ.md)
- [`docs/TROUBLESHOOTING.md`](./docs/TROUBLESHOOTING.md)
- [`docs/USER-GUIDE.md`](./docs/USER-GUIDE.md)
- [`docs/CONTRIBUTING.md`](./docs/CONTRIBUTING.md)
- [`docs/CHANGELOG.md`](./docs/CHANGELOG.md)
- [`docs/GLOSSARY.md`](./docs/GLOSSARY.md)

## Repository Workflow
Work directly on `main` unless the repository owner explicitly requests a feature branch. Before finishing any change:
1. Checkout `main`.
2. Pull latest `main`.
3. Make changes.
4. Commit with descriptive message and body.
5. Push to remote `main`.
6. Verify push succeeded.
7. Confirm `git status` is clean.

## Single Source of Truth Statement
If two documents conflict, the more focused document owns the topic. This overview file never overrides detailed implementation documents; it only links to them.
