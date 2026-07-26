# Documentation Map

## Purpose
Defines ownership, authority, and cross-reference rules for the documentation set.

## Ownership rules
- Each subsystem must have exactly one authoritative owner document.
- Overview, navigation, and index files must not claim subsystem authority.
- If a topic has its own lifecycle, state machine, APIs, workflows, or data model, it requires a single owner document.
- Shared cross-cutting topics such as logging, configuration, state, and security are owned once and referenced elsewhere.
- Navigation stubs must point to the owner document and must not redefine behavior.

## Canonical owners
- Documentation map: `docs/DOCUMENTATION-MAP.md`
- Architecture: `docs/ARCHITECTURE.md`
- Root architecture overview: `APEX-ARCHITECTURE.md`
- Project structure: `docs/PROJECT-STRUCTURE.md`
- Module dependency: `docs/MODULE-DEPENDENCY.md`
- Trading engine: `docs/TRADING-ENGINE.md`
- Execution engine: `docs/EXECUTION-ENGINE.md`
- Strategy engine and strategy catalog: `docs/STRATEGIES.md`
- Risk engine: `docs/RISK-ENGINE.md`
- AI decision pipeline: `docs/AI-PIPELINE.md`
- Cloud AI integration: `docs/CLOUD-AI-INTEGRATION.md`
- AI settings: `docs/AI-SETTINGS.md`
- Market data: `docs/MARKET-DATA.md`
- Market intelligence: `docs/MARKET-INTELLIGENCE.md`
- Opportunity detection detail: `docs/OPPORTUNITY-DETECTION.md` (owned under market intelligence authority)
- Opportunity ranking detail: `docs/OPPORTUNITY-RANKING.md` (owned under market intelligence authority)
- Routing engine: `docs/ROUTING-ENGINE.md`
- Liquidity analysis: `docs/LIQUIDITY-ANALYSIS.md`
- Slippage model: `docs/SLIPPAGE-MODEL.md`
- Gas optimisation: `docs/GAS-OPTIMISATION.md`
- MEV protection: `docs/MEV-PROTECTION.md`
- Order management: `docs/ORDER-MANAGEMENT.md`
- Transaction lifecycle: `docs/TRANSACTION-LIFECYCLE.md`
- Chain integration: `docs/CHAIN-INTEGRATION.md`
- Chain intelligence: `docs/CHAIN-INTELLIGENCE.md`
- DEX integration: `docs/DEX-INTEGRATION.md`
- Portfolio management: `docs/PORTFOLIO-MANAGEMENT.md`
- Position management: `docs/POSITION-MANAGEMENT.md`
- Wallet management: `docs/WALLET-MANAGEMENT.md`
- Asset management: `docs/ASSET-MANAGEMENT.md`
- Simulation framework: `docs/SIMULATION-ENGINE.md`
- Backtesting methodology: `docs/BACKTESTING.md` (consumes simulation engine)
- Runtime operations: `docs/RUNTIME-OPERATIONS.md`
- Worker architecture: `docs/WORKER-ARCHITECTURE.md`
- Queue management: `docs/QUEUE-MANAGEMENT.md`
- Recovery and failover: `docs/RECOVERY-AND-FAILOVER.md`
- Monitoring and observability: `docs/MONITORING-OBSERVABILITY.md`
- Error handling and logging: `docs/ERROR-HANDLING-LOGGING.md`
- Security: `docs/SECURITY.md`
- Permission model: `docs/PERMISSION-MODEL.md`
- Configuration: `docs/CONFIGURATION.md`
- Database schema: `docs/DATABASE-SCHEMA.md`
- State management: `docs/STATE-MANAGEMENT.md`
- IPC protocol: `docs/IPC-PROTOCOL.md`
- IPC message catalog: `docs/IPC-MESSAGE-CATALOG.md` (catalog under IPC protocol authority)
- API contracts: `docs/API-CONTRACTS.md`
- API reference: `docs/API-REFERENCE.md`
- Event flow: `docs/EVENT-FLOW.md`
- Data flow: `docs/DATA-FLOW.md`
- Performance targets: `docs/PERFORMANCE-TARGETS.md`
- Non-functional requirements: `docs/NON-FUNCTIONAL-REQUIREMENTS.md`
- User workflows: `docs/USER-FLOWS.md`
- User guide: `docs/USER-GUIDE.md`
- Deployment and operations: `docs/DEPLOYMENT.md`
- Windows desktop shell: `docs/WINDOWS-DESKTOP.md`
- UI component spec: `docs/UI-COMPONENT-SPEC.md`
- Designer protocols: `docs/DESIGNER-PROTOCOLS.md`
- Testing guide: `docs/TESTING-GUIDE.md`
- Skills and agents: `docs/SKILLS.md`, `docs/AGENTS.md`
- Implementation roadmap: `docs/IMPLEMENTATION-ROADMAP.md`
- Component diagrams: `docs/COMPONENT-DIAGRAMS.md`

## Navigation-only stubs
These must not claim ownership and should only point to owners:
- `docs/README.md`
- `docs/BUILD-RELEASE-CICD.md`
- `docs/CHANGELOG.md`
- `docs/CODING-STANDARDS.md`
- `docs/CONTRIBUTING.md`
- `docs/DECISION-LOG.md`
- `docs/DESIGN-SYSTEM.md`
- `docs/ENHANCEMENT-ROADMAP.md`
- `docs/FAQ.md`
- `docs/FEATURE-MATRIX.md`
- `docs/FILE-STORAGE.md`
- `docs/GLOSSARY.md`
- `docs/KNOWN-LIMITATIONS.md`
- `docs/PAIR-DISCOVERY.md`
- `docs/PRICE-DISCOVERY.md`
- `docs/TOKEN-DISCOVERY.md`
- `docs/TROUBLESHOOTING.md`

## Cross-reference rules
- Every owner document must include a `Cross-references` section.
- Navigation stubs must reference only their authoritative owners.
- Do not duplicate lifecycle or ownership claims across multiple docs.
- When two docs touch the same topic, the non-owner must link to the owner.

## Cross-references
- `APEX-ARCHITECTURE.md`
- `docs/ARCHITECTURE.md`
- `docs/PROJECT-STRUCTURE.md`
