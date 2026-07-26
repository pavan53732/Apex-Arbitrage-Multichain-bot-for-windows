# Policy Engine

## Purpose
Defines the central source of truth for all user-configurable policies.

## Scope
Trading, AI, security, recovery, failover, and operational thresholds.

## Content
- Max daily loss.
- Position size.
- Budget caps.
- Model selection.
- Plugin permissions.
- Secret rotation.
- Retry limits.
- Failover behavior.

## Governance
Policies load from a central config file and can be hot-reloaded. Policy changes require approval and are versioned.

## Cross-references
- `CONFIGURATION.md`
- `SECURITY-CONTRACTS.md`
- `RISK-ENGINE.md`
- `AI-COST-MANAGEMENT.md`

## Governance Rules
Defines policy evaluation, priority ordering, overrides, and final decision selection.

## Example
A routing policy blocks execution when cost exceeds target.

## Arbitrage policies
- Must define spread, latency, and loss-limit policies.

## Required details
- Define policy inputs, limits, and enforcement.

## Policy rules
- Define policy inputs, limits, enforcement, and override behavior.
- Define how policy failures block execution.
