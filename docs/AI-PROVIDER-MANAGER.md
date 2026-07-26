# AI Provider Manager

## Purpose
Defines provider abstraction, capability detection, configuration, retry policy, and test-connection behavior.

## Coverage
OpenAI-compatible, Anthropic-compatible, Gemini, OpenRouter, Groq, and custom endpoints.

## Cross-references
- `AI-ORCHESTRATION.md`
- `AI-CONSENSUS.md`
- `METRICS.md`
- `CONFIGURATION.md`

## Governance Rules
Defines provider inventory, capability detection, health monitoring, failover, and cost-aware selection.

## Example
A degraded provider is demoted until capability and latency checks recover.

## Selection and failover
- Select providers by capability, health, latency, cost, and policy priority.
- Demote providers that fail health or capability checks until recovery succeeds.
- Failover remains synchronous for critical flows and must preserve auditability.
- Capability negotiation detail remains owned by `MODEL-CAPABILITY-NEGOTIATION.md`.
