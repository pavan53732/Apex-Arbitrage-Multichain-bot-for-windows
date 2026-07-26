# DOCUMENTATION-MAP.md

## Purpose
Maps the documentation system for APEX and identifies authority boundaries to reduce overlap and contradiction.

## Authority Rules
- `APEX-ARCHITECTURE.md` = overview and repo index only.
- Focused docs own implementation details for their specific domain.
- If architecture, security, IPC, config, or UI guidance is updated, the focused document must be updated first.

## Topic Ownership Map
| Topic | Authoritative Document | Related Docs |
|---|---|---|
| repository overview | `APEX-ARCHITECTURE.md` | `docs/README.md` |
| system architecture | `docs/ARCHITECTURE.md` | `PROJECT-STRUCTURE.md`, `MODULE-DEPENDENCY.md`, `COMPONENT-DIAGRAMS.md` |
| AI runtime | `docs/AI-PIPELINE.md` | `AI-SETTINGS.md`, `CLOUD-AI-INTEGRATION.md`, `API-CONTRACTS.md` |
| config | `docs/CONFIGURATION.md` | `AI-SETTINGS.md`, `DATABASE-SCHEMA.md`, `FILE-STORAGE.md` |
| IPC contracts | `docs/IPC-PROTOCOL.md` | `IPC-MESSAGE-CATALOG.md`, `STATE-MANAGEMENT.md` |
| DB | `docs/DATABASE-SCHEMA.md` | `FILE-STORAGE.md`, `DATA-FLOW.md` |
| strategies | `docs/STRATEGIES.md` | `RISK-ENGINE.md`, `CHAIN-INTEGRATION.md`, `DEX-INTEGRATION.md` |
| logging/errors | `docs/ERROR-HANDLING-LOGGING.md` | `MONITORING-OBSERVABILITY.md`, `SECURITY.md` |
| desktop packaging | `docs/WINDOWS-DESKTOP.md` | `BUILD-RELEASE-CICD.md`, `DEPLOYMENT.md` |
| UI system | `docs/DESIGN-SYSTEM.md` | `UI-COMPONENT-SPEC.md`, `DESIGNER-PROTOCOLS.md` |

## Overlap Review
- Root architecture file previously overlapped with architecture map, strategy references, and version notes. This was reduced by converting it into an index.
- `AI-SETTINGS.md` and `CLOUD-AI-INTEGRATION.md` remain related but separate: settings vs provider/runtime integration.
- `IPC-PROTOCOL.md` remains authoritative for contract shape; `IPC-MESSAGE-CATALOG.md` is an index.

## Missing Areas Before v3.2
The repository lacked explicit specs for structure, coding rules, config, state, observability, release flow, and developer-facing dependency/data/event maps. These gaps are now covered by dedicated docs.

## Next Review Priorities
- deepen `DESIGN-SYSTEM.md` and `UI-COMPONENT-SPEC.md` with concrete tokens and component states,
- expand `API-CONTRACTS.md` with service interfaces,
- expand `FEATURE-MATRIX.md` into release readiness table,
- add diagram images later if needed.
