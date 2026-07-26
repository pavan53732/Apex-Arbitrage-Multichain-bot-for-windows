# APEX — Project Overview and Documentation Index

## Purpose
This file is the top-level project overview for APEX. It defines the mission, core principles, and authoritative documentation map. Detailed implementation requirements live in `docs/` and must be treated as the single source of truth by both human developers and AI agents.

## Vision
APEX is a Windows-first desktop application for AI-assisted multichain arbitrage analysis, strategy execution, safety enforcement, and operational monitoring.

## Core Principles
- Documentation is the implementation source of truth.
- Security boundaries must be explicit.
- Renderer code must stay unprivileged.
- All critical flows must be typed, testable, and observable.
- Automation must fail safe by default.

## Authoritative Reading Order
1. [docs/README.md](./docs/README.md)
2. [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)
3. [docs/PROJECT-STRUCTURE.md](./docs/PROJECT-STRUCTURE.md)
4. [docs/CODING-STANDARDS.md](./docs/CODING-STANDARDS.md)
5. [docs/CONFIGURATION.md](./docs/CONFIGURATION.md)
6. [docs/IPC-PROTOCOL.md](./docs/IPC-PROTOCOL.md)
7. [docs/DATABASE-SCHEMA.md](./docs/DATABASE-SCHEMA.md)
8. [docs/STATE-MANAGEMENT.md](./docs/STATE-MANAGEMENT.md)
9. [docs/STRATEGIES.md](./docs/STRATEGIES.md)
10. [docs/RISK-ENGINE.md](./docs/RISK-ENGINE.md)
11. [docs/SECURITY.md](./docs/SECURITY.md)
12. [docs/TESTING-GUIDE.md](./docs/TESTING-GUIDE.md)
13. [docs/BUILD-RELEASE-CICD.md](./docs/BUILD-RELEASE-CICD.md)

## Documentation Ownership Model
Each major topic must have one authoritative document. If guidance conflicts, the more specific implementation document in `docs/` takes precedence over overview prose in this file.

## Documentation Map
### Architecture and Structure
- [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)
- [docs/PROJECT-STRUCTURE.md](./docs/PROJECT-STRUCTURE.md)
- [docs/MODULE-DEPENDENCY.md](./docs/MODULE-DEPENDENCY.md)
- [docs/DATA-FLOW.md](./docs/DATA-FLOW.md)
- [docs/EVENT-FLOW.md](./docs/EVENT-FLOW.md)
- [docs/COMPONENT-DIAGRAMS.md](./docs/COMPONENT-DIAGRAMS.md)

### Runtime and Contracts
- [docs/CONFIGURATION.md](./docs/CONFIGURATION.md)
- [docs/STATE-MANAGEMENT.md](./docs/STATE-MANAGEMENT.md)
- [docs/API-CONTRACTS.md](./docs/API-CONTRACTS.md)
- [docs/IPC-PROTOCOL.md](./docs/IPC-PROTOCOL.md)
- [docs/IPC-MESSAGE-CATALOG.md](./docs/IPC-MESSAGE-CATALOG.md)
- [docs/FILE-STORAGE.md](./docs/FILE-STORAGE.md)
- [docs/PERMISSION-MODEL.md](./docs/PERMISSION-MODEL.md)

### Quality and Operations
- [docs/CODING-STANDARDS.md](./docs/CODING-STANDARDS.md)
- [docs/ERROR-HANDLING-LOGGING.md](./docs/ERROR-HANDLING-LOGGING.md)
- [docs/MONITORING-OBSERVABILITY.md](./docs/MONITORING-OBSERVABILITY.md)
- [docs/PERFORMANCE-TARGETS.md](./docs/PERFORMANCE-TARGETS.md)
- [docs/NON-FUNCTIONAL-REQUIREMENTS.md](./docs/NON-FUNCTIONAL-REQUIREMENTS.md)
- [docs/TESTING-GUIDE.md](./docs/TESTING-GUIDE.md)
- [docs/BUILD-RELEASE-CICD.md](./docs/BUILD-RELEASE-CICD.md)

### Domain and Feature Specs
- [docs/AI-PIPELINE.md](./docs/AI-PIPELINE.md)
- [docs/AI-SETTINGS.md](./docs/AI-SETTINGS.md)
- [docs/CLOUD-AI-INTEGRATION.md](./docs/CLOUD-AI-INTEGRATION.md)
- [docs/CHAIN-INTEGRATION.md](./docs/CHAIN-INTEGRATION.md)
- [docs/DEX-INTEGRATION.md](./docs/DEX-INTEGRATION.md)
- [docs/STRATEGIES.md](./docs/STRATEGIES.md)
- [docs/RISK-ENGINE.md](./docs/RISK-ENGINE.md)
- [docs/DATABASE-SCHEMA.md](./docs/DATABASE-SCHEMA.md)
- [docs/UI-COMPONENT-SPEC.md](./docs/UI-COMPONENT-SPEC.md)
- [docs/DESIGN-SYSTEM.md](./docs/DESIGN-SYSTEM.md)
- [docs/FEATURE-MATRIX.md](./docs/FEATURE-MATRIX.md)
- [docs/IMPLEMENTATION-ROADMAP.md](./docs/IMPLEMENTATION-ROADMAP.md)

### Governance and Reference
- [docs/ENHANCEMENT-ROADMAP.md](./docs/ENHANCEMENT-ROADMAP.md)
- [docs/DECISION-LOG.md](./docs/DECISION-LOG.md)
- [docs/KNOWN-LIMITATIONS.md](./docs/KNOWN-LIMITATIONS.md)
- [docs/GLOSSARY.md](./docs/GLOSSARY.md)
- [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md)
- [docs/CHANGELOG.md](./docs/CHANGELOG.md)

## Historical Note
Earlier revisions of this repository mixed overview, architecture, and implementation details in this root file. That model is deprecated. This file is now an index and project brief only.
