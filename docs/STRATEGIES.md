# Strategies

## Purpose
This document is the authoritative specification for every supported trading strategy and their implementation behavior.

## Strategy contract
Each strategy must define business objective, decision logic, market conditions, entry and exit criteria, sizing, allocation, risk, slippage, gas, MEV, chain/DEX support, market data dependencies, AI interaction, runtime flow, state machine, IPC events, persistence, monitoring, alerting, backtesting, simulation, stress testing, failure handling, recovery, performance metrics, limitations, and extension points.

## Shared lifecycle
Discover -> Score -> Validate -> Size -> Approve -> Execute -> Monitor -> Exit -> Reconcile -> Learn.

## Common strategy requirements
- Strategies must fail closed when market data freshness, liquidity, risk, or chain health are invalid.
- Strategies may request AI assistance, but AI cannot bypass deterministic risk gates.
- Strategy state must be persisted with enough detail to resume deterministic evaluation after restart.
- Every live strategy must expose backtest and simulation scenarios before activation.
- Every strategy must define a stop condition and a recovery condition.

## Arbitrage
### Business objective
Exploit price inefficiencies between venues after gas, slippage, and MEV costs.
### Decision logic
Use route quotes, latency, and liquidity depth to compute net edge.
### Market conditions
Requires fragmented pricing and sufficient liquidity on both legs.
### Entry conditions
Net positive edge, fresh quotes, wallet ready, risk-approved.
### Exit conditions
Execution completed, edge collapses, timeout, or risk breach.
### Position sizing
Size by net edge, pool depth, gas cost, and risk budget.
### Capital allocation
Prefer lowest capital needed for atomic or near-atomic capture.
### Risk controls
Max loss per attempt, stale quote rejection, exposure cap.
### Stop-loss
Abort if edge compresses below threshold during pre-submit validation.
### Take-profit
Realize on confirmed fills only.
### Volatility handling
Reduce size when price variance increases.
### Liquidity requirements
Both sides must support the required notional with acceptable impact.
### Slippage tolerance
Bounded by route-specific policy from `SLIPPAGE-MODEL.md`.
### Gas optimisation rules
Use fee ceilings and replacement only within policy.
### MEV considerations
Prefer protected routes when sandwich risk is high.
### Supported chains
Configured chain set only.
### Supported DEXs
Configured DEX set only.
### Required market data
Quotes, liquidity depth, gas, chain health, token metadata.
### AI interaction
AI may rank but cannot bypass deterministic risk gates.
### Runtime workflow
Detect -> validate -> route -> submit -> monitor -> reconcile.
### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.
### IPC interactions
Opportunity, plan, order, and transaction events.
### Database persistence
Store opportunity scores, order ids, fills, and final PnL.
### Monitoring metrics
Edge capture rate, fill latency, slippage, failure rate.
### Alert thresholds
Alert on repeated stale quotes, high failure rate, or excessive slippage.
### Backtesting methodology
Replay historical spreads and execution constraints.
### Simulation scenarios
Thin liquidity, gas spikes, reorgs, and quote invalidation.
### Stress testing
Increase latency, reduce liquidity, and inflate gas to verify abort logic.
### Performance metrics
Net captured edge, success rate, execution latency.
### Failure scenarios
Stale quote, route failure, revert, reorg, wallet failure.
### Recovery behaviour
Reconcile receipts, update accounting, and block further attempts when thresholds exceed.
### Known limitations
Cannot guarantee fills in fast-moving or illiquid markets.
### Extension points
Additional route scorers, chain adapters, and AI ranking hooks.

## Triangular Arbitrage
### Business objective
Capture conversion inefficiencies across three assets on a venue or chain.
### Decision logic
Evaluate three-leg closed-loop edge after fees and impact.
### Market conditions
Requires sufficient depth on all three legs.
### Entry conditions
Positive closed-loop edge, all routes fresh, liquidity sufficient.
### Exit conditions
Edge loss, completion, or pre-submit invalidation.
### Position sizing
Bound by weakest leg depth and risk budget.
### Capital allocation
Reserve capital for atomic or near-atomic execution only.
### Risk controls
Reject if any leg becomes stale or illiquid.
### Stop-loss
Cancel if any leg quote drifts beyond tolerance.
### Take-profit
Recognize only when the full loop settles.
### Volatility handling
Smaller size when inter-leg variance increases.
### Liquidity requirements
All legs must meet minimum depth and impact limits.
### Slippage tolerance
Per leg, with total-loop budget enforced.
### Gas optimisation rules
Use single transaction bundle where supported.
### MEV considerations
Prefer protected bundle submission.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Three-leg quotes, gas, liquidity, fees, token metadata.
### AI interaction
AI may rank opportunities by confidence and risk.
### Runtime workflow
Loop discovery -> validation -> route build -> execution -> reconciliation.
### State machine
Idle -> Candidate -> Approved -> Submitted -> Settled | Failed -> Reconciled.
### IPC interactions
Opportunity, plan, order, transaction events.
### Database persistence
Loop quote snapshot, execution result, realized edge.
### Monitoring metrics
Loop edge, fill rate, loop latency.
### Alert thresholds
Alert on repeated loop invalidations or high failure counts.
### Backtesting methodology
Replay historical three-leg loops.
### Simulation scenarios
Depth loss, fee spike, route invalidation, partial completion.
### Stress testing
Vary liquidity and latency across all legs.
### Performance metrics
Loop success rate, average captured edge.
### Failure scenarios
One-leg revert, partial completion, stale third-leg quote.
### Recovery behaviour
Mark partial loops, reconcile, and quarantine bad routes.
### Known limitations
Atomic completion may not be available on all paths.
### Extension points
Alternative loop builders and venue adapters.

## Cross-DEX Arbitrage
### Business objective
Capture spread across DEX venues.
### Decision logic
Compare normalized quotes across routers and pools.
### Market conditions
Requires multiple venues with non-overlapping pricing.
### Entry conditions
Positive net edge after fees and slippage.
### Exit conditions
Fill, edge collapse, timeout.
### Position sizing
Size by depth and route quality.
### Capital allocation
Use lowest-risk venue pair first.
### Risk controls
Reject stale, shallow, or MEV-exposed routes.
### Stop-loss
Abort if route score drops below threshold.
### Take-profit
Settle on confirmed fills only.
### Volatility handling
Reduce size when price dispersion is unstable.
### Liquidity requirements
Sufficient depth on both venues.
### Slippage tolerance
Route-level tolerance only.
### Gas optimisation rules
Optimize for venue-specific fees and transaction counts.
### MEV considerations
Use protection when route visibility is high.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
DEX quotes, depth, gas, chain health.
### AI interaction
AI may identify candidate pairs and rank confidence.
### Runtime workflow
Detect -> compare -> validate -> execute -> reconcile.
### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed -> Reconciled.
### IPC interactions
Opportunity, routing, execution, transaction, accounting events.
### Database persistence
Store pair scores, route, fill, and PnL.
### Monitoring metrics
Spread capture, fill time, invalidation rate.
### Alert thresholds
Alert on repeated failed routes or stale input data.
### Backtesting methodology
Replay cross-DEX spread histories.
### Simulation scenarios
MEV attack, router outage, shallow pools.
### Stress testing
Increase spread churn and reduce liquidity.
### Performance metrics
Net edge, execution success, average slippage.
### Failure scenarios
Revert, quote drift, sandwich attack.
### Recovery behaviour
Reprice, abandon, reconcile exposures.
### Known limitations
Sensitive to chain congestion and MEV.
### Extension points
Additional router adapters and protected execution paths.

## Cross-Chain Arbitrage
### Business objective
Capture spread between equivalent assets on different chains.
### Decision logic
Compare net edge after bridge cost, latency, and finality risk.
### Market conditions
Requires stable bridge routes and finality confidence.
### Entry conditions
Positive edge after bridge, gas, and transfer costs.
### Exit conditions
Edge collapse, bridge failure, or finality breach.
### Position sizing
Constrained by bridge liquidity and transfer limits.
### Capital allocation
Use capital only when bridge and destination liquidity both satisfy policy.
### Risk controls
Reject if bridge latency, reorg risk, or destination liquidity exceed limits.
### Stop-loss
Abort when bridge delay invalidates profitability.
### Take-profit
Settle after verified arrival and hedge completion.
### Volatility handling
Prefer smaller size under high volatility or finality uncertainty.
### Liquidity requirements
Bridge capacity and destination venue depth must both pass.
### Slippage tolerance
Combined chain-and-bridge budget enforced.
### Gas optimisation rules
Budget both source and destination transaction cost.
### MEV considerations
Use protected submission on both sides if available.
### Supported chains
Configured source and destination chain set.
### Supported DEXs
Configured source and destination DEX set.
### Required market data
Bridge quotes, finality metrics, destination depth, fees.
### AI interaction
AI may rank chains by relative execution confidence.
### Runtime workflow
Source validation -> bridge initiation -> destination validation -> completion -> reconcile.
### State machine
Idle -> Candidate -> Bridging -> Confirming -> Settled | Failed -> Reconciled.
### IPC interactions
Bridge status, execution, confirmation, and reconciliation events.
### Database persistence
Source tx, bridge id, destination tx, final outcome.
### Monitoring metrics
Bridge success, finality delay, profit capture, failure rate.
### Alert thresholds
Alert on repeated bridge stalls or transfer failures.
### Backtesting methodology
Replay bridge latency and cross-chain spread history.
### Simulation scenarios
Bridge outage, delayed finality, chain reorg, destination liquidity loss.
### Stress testing
Increase latency and reduce finality assumptions.
### Performance metrics
Net cross-chain edge, completion success, realized duration.
### Failure scenarios
Bridge timeout, reorg, destination reject, price collapse.
### Recovery behaviour
Reconcile both sides and quarantine unsettled transfers.
### Known limitations
Cross-chain execution is slower and finality-sensitive.
### Extension points
Additional bridge adapters and chain-finality heuristics.

## Flash Loan Arbitrage
### Business objective
Capture one-block or one-transaction spread using borrowed capital.
### Decision logic
Evaluate net edge after loan premium, gas, and MEV costs.
### Market conditions
Requires atomic execution and borrowable liquidity.
### Entry conditions
Positive edge exceeding loan fee and all execution costs.
### Exit conditions
Atomic fill, revert, or validation failure.
### Position sizing
Limited by borrow capacity and route depth.
### Capital allocation
No permanent capital allocation; temporary borrow only.
### Risk controls
Atomicity required; any validation failure aborts before borrow.
### Stop-loss
Not applicable after borrow; pre-borrow checks are mandatory.
### Take-profit
Only realized on full atomic settlement.
### Volatility handling
Reject unstable markets with high quote churn.
### Liquidity requirements
Borrow liquidity and route liquidity both required.
### Slippage tolerance
Very tight; bounded by atomic execution policy.
### Gas optimisation rules
Optimize for single-transaction cost and revert risk.
### MEV considerations
Use highest available execution protection.
### Supported chains
Configured chains with flash-loan support.
### Supported DEXs
Configured DEXs with atomic routing support.
### Required market data
Borrow rates, liquidity, quotes, gas, chain health.
### AI interaction
AI may identify opportunities but cannot alter atomic safety checks.
### Runtime workflow
Detect -> validate -> borrow -> route -> repay -> reconcile.
### State machine
Idle -> Candidate -> Approved -> Borrowing -> Submitted -> Settled | Reverted -> Reconciled.
### IPC interactions
Opportunity, approval, execution, borrow, repayment, reconciliation events.
### Database persistence
Loan id, route plan, repayment status, realized PnL.
### Monitoring metrics
Atomic success rate, revert rate, loan cost variance.
### Alert thresholds
Alert on failed pre-borrow validation or repeated reverts.
### Backtesting methodology
Replay atomic spreads with historical borrow and gas assumptions.
### Simulation scenarios
Revert-on-second-leg, slippage surge, gas spike, borrow rejection.
### Stress testing
Increase fee and gas volatility.
### Performance metrics
Atomic net edge, revert rate, approval latency.
### Failure scenarios
Loan rejection, revert, route failure, repayment invalidation.
### Recovery behaviour
Quarantine the failed route and reconcile accounting.
### Known limitations
Dependent on atomic on-chain behavior and borrow availability.
### Extension points
New loan venues and atomic route builders.

## Statistical Arbitrage
### Business objective
Exploit statistically significant mean reversion between correlated assets.
### Decision logic
Use spread z-score, correlation stability, and regime filters.
### Market conditions
Requires stable correlation and sufficient liquidity.
### Entry conditions
Spread threshold exceeded and confidence above policy threshold.
### Exit conditions
Spread reverts, correlation breaks, or holding-time limit reached.
### Position sizing
Scale by z-score, volatility, and estimated half-life.
### Capital allocation
Risk-budgeted allocation per pair or basket.
### Risk controls
Correlation break, drawdown cap, and regime filter.
### Stop-loss
Exit on spread overshoot or model invalidation.
### Take-profit
Exit when spread mean reverts to target band.
### Volatility handling
Reduce size when realized volatility or model error increases.
### Liquidity requirements
Sufficient depth for both legs under slippage budget.
### Slippage tolerance
Pair-specific tolerance with aggregate cap.
### Gas optimisation rules
Prefer fewer rebalances and avoid unnecessary churn.
### MEV considerations
Prefer protected paths where leg visibility is high.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Historical spreads, correlation metrics, depth, gas, volatility.
### AI interaction
AI may summarize regime signals but not replace statistical rules.
### Runtime workflow
Signal -> validate -> size -> execute -> monitor -> exit -> reconcile.
### State machine
Idle -> Candidate -> Approved -> Active -> Exiting -> Reconciled.
### IPC interactions
Signal, approval, execution, exit, reconciliation events.
### Database persistence
Signal history, parameters, realized PnL, exit reason.
### Monitoring metrics
Signal hit rate, holding time, drawdown, convergence quality.
### Alert thresholds
Alert on correlation collapse or excessive drawdown.
### Backtesting methodology
Replay historical pair spreads and regime filters.
### Simulation scenarios
Correlation break, volatility spike, lagged fills.
### Stress testing
Perturb correlation, latency, and liquidity simultaneously.
### Performance metrics
Sharpe proxy, drawdown, capture rate, turnover.
### Failure scenarios
Model drift, execution lag, spread blowout.
### Recovery behaviour
Reduce size, pause the strategy, or retire the pair.
### Known limitations
Performance depends on stable regimes and quality market data.
### Extension points
Additional pair selectors and regime classifiers.

## Cross-references
- `docs/SLIPPAGE-MODEL.md`
- `docs/GAS-OPTIMISATION.md`
- `docs/MEV-PROTECTION.md`
- `docs/OPPORTUNITY-RANKING.md`
- `docs/EXECUTION-ENGINE.md`
