# Risk Engine

## Purpose
Defines trading risk checks used before and during execution.

## Ownership
- Owns exposure limits, spread checks, liquidity checks, and leg failure protection.
- Does not own route scoring or execution transport.

## Risk checks
- Maximum loss per trade.
- Minimum liquidity threshold.
- Maximum acceptable slippage.
- Partial-fill exposure handling.
- Cross-exchange timing risk.

## Cross-references
- `TRADING-LIFECYCLE.md`
- `EXECUTION-ENGINE.md`
- `ARBITRAGE-WINDOW-MANAGER.md`
- `OPPORTUNITY-RANKING.md`

## Required details
- Define formulas, limits, and abort behavior for arb risk.

## Abort rules
- Abort if loss limit, slippage, or timing budget is exceeded.
- Abort if a leg is partially filled and recovery cannot restore limits.

## Risk rules
- Define formulas, limits, and abort behavior for arbitrage risk.
- Define partial fill and cross-leg exposure handling.
