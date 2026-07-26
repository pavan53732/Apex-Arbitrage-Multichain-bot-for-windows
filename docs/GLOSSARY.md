# GLOSSARY.md

## Purpose
Canonical terminology for APEX. All documentation and code should use these terms consistently.

## Product Terms
- **APEX**: the Windows desktop arbitrage application and supporting architecture.
- **Agent**: an AI-assisted subsystem that plans, analyzes, or assists operator workflows.
- **Skill**: a capability bundle or specialized toolset available to an agent.
- **Strategy**: a formal profit-seeking algorithm or execution plan governed by risk controls.

## Trading Terms
- **Arbitrage**: capturing price discrepancies across venues or paths.
- **Slippage**: execution price deterioration relative to quote.
- **Spread**: price difference between buy and sell legs.
- **Position Size**: capital allocated to a specific execution opportunity.
- **Circuit Breaker**: automatic risk halt triggered by threshold breach.

## Blockchain Terms
- **RPC**: remote procedure call endpoint for chain access.
- **Mempool**: pending transaction set not yet finalized on-chain.
- **Gas**: execution fee unit on EVM-compatible chains.
- **Nonce**: per-account transaction sequence number.
- **Chain Adapter**: code that normalizes access to a specific blockchain network.

## AI Terms
- **Provider**: cloud AI backend such as OpenAI, Anthropic, or Gemini.
- **Model**: a specific AI model identifier under a provider.
- **Structured Output**: AI response constrained to a machine-validated schema.
- **Tool Call**: delegated invocation of a capability exposed to the AI orchestrator.

## Internal Naming Rules
- Use **main process** and **renderer** for Electron runtime layers.
- Use **IPC contract** for typed message definitions.
- Use **safe config** for renderer-exposable settings.
- Use **secret config** for sensitive runtime values.

## Cross-References
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)
- [`PROJECT-STRUCTURE.md`](./PROJECT-STRUCTURE.md)
- [`STRATEGIES.md`](./STRATEGIES.md)
- [`RISK-ENGINE.md`](./RISK-ENGINE.md)
