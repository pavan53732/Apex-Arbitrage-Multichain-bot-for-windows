# Documentation Map

## Purpose
Defines ownership, authority, and cross-reference rules for the documentation set.

## Ownership rules
- Each subsystem must have exactly one authoritative owner document.
- Overview, navigation, and index files must not claim subsystem authority.
- If a topic has its own lifecycle, state machine, APIs, workflows, or data model, it requires a single owner document.
- Shared cross-cutting topics such as logging, configuration, state, and security are owned once and referenced elsewhere.

## Canonical owners
- Architecture: `docs/ARCHITECTURE.md`
- Project structure: `docs/PROJECT-STRUCTURE.md`
- Trading engine: `docs/TRADING-ENGINE.md`
- Execution engine: `docs/EXECUTION-ENGINE.md`
- Strategy engine and strategy catalog: `docs/STRATEGIES.md`
- AI decision pipeline: `docs/AI-PIPELINE.md`
- Market data: `docs/MARKET-DATA.md`
- Market intelligence: `docs/MARKET-INTELLIGENCE.md`
- Routing engine: `docs/ROUTING-ENGINE.md`
- Liquidity analysis: `docs/LIQUIDITY-ANALYSIS.md`
- Slippage model: `docs/SLIPPAGE-MODEL.md`
- Gas optimisation: `docs/GAS-OPTIMISATION.md`
- MEV protection: `docs/MEV-PROTECTION.md`
- Order management: `docs/ORDER-MANAGEMENT.md`
- Transaction lifecycle: `docs/TRANSACTION-LIFECYCLE.md`
- Portfolio management: `docs/PORTFOLIO-MANAGEMENT.md`
- Position management: `docs/POSITION-MANAGEMENT.md`
- Wallet management: `docs/WALLET-MANAGEMENT.md`
- Asset management: `docs/ASSET-MANAGEMENT.md`
- Simulation framework: `docs/SIMULATION-ENGINE.md`
- Runtime operations: `docs/RUNTIME-OPERATIONS.md`
- Monitoring and observability: `docs/MONITORING-OBSERVABILITY.md`
- Recovery and failover: `docs/ERROR-HANDLING-LOGGING.md`
- Security: `docs/SECURITY.md`
- Configuration: `docs/CONFIGURATION.md`
- Database schema: `docs/DATABASE-SCHEMA.md`
- IPC protocol: `docs/IPC-PROTOCOL.md`
- Error handling and logging: `docs/ERROR-HANDLING-LOGGING.md`
- Performance targets: `docs/PERFORMANCE-TARGETS.md`
- Non-functional requirements: `docs/NON-FUNCTIONAL-REQUIREMENTS.md`
- User workflows: `docs/USER-FLOWS.md`
- Deployment and operations: `docs/DEPLOYMENT.md`
- Windows desktop shell: `docs/WINDOWS-DESKTOP.md`
- UI component spec: `docs/UI-COMPONENT-SPEC.md`
- Designer protocols: `docs/DESIGNER-PROTOCOLS.md`
- Testing guide: `docs/TESTING-GUIDE.md`
- Cloud AI integration: `docs/CLOUD-AI-INTEGRATION.md`
- API contracts: `docs/API-CONTRACTS.md`
- API reference: `docs/API-REFERENCE.md`
- AI settings: `docs/AI-SETTINGS.md`
- Skills and agents: `docs/SKILLS.md`, `docs/AGENTS.md`

## Cross-references
- `APEX-ARCHITECTURE.md`
- `docs/ARCHITECTURE.md`
- `docs/PROJECT-STRUCTURE.md`
