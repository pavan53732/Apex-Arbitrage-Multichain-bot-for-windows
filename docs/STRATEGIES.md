# Strategies

## Purpose
This document is the authoritative specification for every supported trading strategy and their implementation behavior.

## Strategy contract
Each strategy must define business objective, decision logic, market conditions, entry and exit criteria, sizing, allocation, risk, slippage, gas, MEV, chain/DEX support, market data dependencies, AI interaction, runtime flow, state machine, IPC events, persistence, monitoring, alerting, backtesting, simulation, stress testing, failure handling, recovery, performance metrics, limitations, and extension points.

## Shared lifecycle
Discover -> Score -> Validate -> Size -> Approve -> Execute -> Monitor -> Exit -> Reconcile -> Learn.

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
Capture mispricing across chains.
### Decision logic
Compare equivalent assets across supported chains with bridge/finality costs modeled.
### Market conditions
Requires bridge support and manageable finality windows.
### Entry conditions
Positive net edge after bridge, gas, and timing costs.
### Exit conditions
Edge collapse, bridge delay, or risk breach.
### Position sizing
Bound by bridge capacity and exposure tolerance.
### Capital allocation
Reserve for slower settlement and finality risk.
### Risk controls
Cap bridge exposure and cross-chain inventory.
### Stop-loss
Abort if bridge delay exceeds threshold.
### Take-profit
On fully reconciled cross-chain settlement.
### Volatility handling
Smaller size during unstable bridge or chain conditions.
### Liquidity requirements
Depth across both chains and bridge path.
### Slippage tolerance
Per chain plus bridge overhead.
### Gas optimisation rules
Model gas on both chains before entry.
### MEV considerations
Protect per-chain execution where possible.
### Supported chains
Configured supported chain pairings only.
### Supported DEXs
Configured DEX set on each chain.
### Required market data
Cross-chain quotes, bridge cost, finality, gas.
### AI interaction
AI may rank by net risk-adjusted edge.
### Runtime workflow
Detect -> verify -> bridge plan -> execute legs -> reconcile.
### State machine
Idle -> Candidate -> Approved -> Bridging -> Settled | Failed -> Reconciled.
### IPC interactions
Opportunity, bridge, execution, reconciliation events.
### Database persistence
Persist cross-chain inventory and finalized PnL.
### Monitoring metrics
Bridge latency, settlement success, reorg rate.
### Alert thresholds
Alert on settlement delays or repeated bridge failures.
### Backtesting methodology
Replay historical cross-chain spreads with delay modeling.
### Simulation scenarios
Bridge outage, reorg, delayed finality.
### Stress testing
Increase latency and reduce liquidity across both chains.
### Performance metrics
Risk-adjusted edge, completion rate.
### Failure scenarios
Bridge failure, one-chain revert, finality delay.
### Recovery behaviour
Hold inventory, reconcile later, or unwind per policy.
### Known limitations
High latency and settlement risk reduce determinism.
### Extension points
Bridge adapters and chain-specific route policies.

## Flash Loan Arbitrage
### Business objective
Exploit price inefficiency using atomic borrowed capital.
### Decision logic
Validate atomic profitability after fee, gas, and repayment costs.
### Market conditions
Requires flash-loan liquidity and atomic execution support.
### Entry conditions
Positive atomic PnL under worst-case gas and slippage.
### Exit conditions
Atomic completion or full revert.
### Position sizing
Bound by flash liquidity and atomic risk policy.
### Capital allocation
No persistent capital commitment beyond atomic transaction.
### Risk controls
Strict repayment and revert enforcement.
### Stop-loss
Not applicable beyond atomic revert.
### Take-profit
Confirmed only on successful atomic settlement.
### Volatility handling
More conservative edge threshold in volatile markets.
### Liquidity requirements
Enough liquidity for both borrowed size and exit route.
### Slippage tolerance
Atomic bundle tolerance only.
### Gas optimisation rules
Use fee-aware atomic bundles and avoid underpricing.
### MEV considerations
Protect bundle when exposed to searchers.
### Supported chains
Configured flash-loan-supported chains only.
### Supported DEXs
Configured DEX set.
### Required market data
Flash liquidity availability, route depth, gas.
### AI interaction
AI may rank but cannot bypass atomic profit validation.
### Runtime workflow
Construct bundle -> validate -> submit -> either settle or revert.
### State machine
Idle -> Candidate -> Approved -> Submitted -> Settled | Reverted -> Reconciled.
### IPC interactions
Opportunity, bundle, transaction, reconciliation events.
### Database persistence
Record bundle result, realized profit, and revert reason.
### Monitoring metrics
Atomic success rate, revert rate, edge captured.
### Alert thresholds
Alert on repeated non-profitable bundle generation.
### Backtesting methodology
Replay historical flash-loan conditions.
### Simulation scenarios
Revert, fee spike, liquidity removal mid-bundle.
### Stress testing
Raise gas and shrink liquidity thresholds.
### Performance metrics
Atomic success, profit per bundle.
### Failure scenarios
Repayment failure, route failure, revert.
### Recovery behaviour
No partial recovery; record failure and block repeated bad configs.
### Known limitations
Atomicity depends on protocol and chain support.
### Extension points
New bundle builders and liquidity sources.

## Statistical Arbitrage
### Business objective
Capture mean-reversion or divergence opportunities statistically.
### Decision logic
Use spread z-scores, regime filters, and confidence thresholds.
### Market conditions
Requires stable historical relationships.
### Entry conditions
Signal exceeds threshold with acceptable risk score.
### Exit conditions
Signal normalizes, stop-loss, or time exit.
### Position sizing
By volatility, confidence, and correlation.
### Capital allocation
Dynamically allocated by regime quality.
### Risk controls
Correlation break detection and drawdown cap.
### Stop-loss
Exit on adverse divergence or regime change.
### Take-profit
Exit on target normalization.
### Volatility handling
Reduce exposure when volatility expands.
### Liquidity requirements
Sufficient depth for entry and exit.
### Slippage tolerance
Model-based and conservative.
### Gas optimisation rules
Only trade if expected edge clears execution cost.
### MEV considerations
Prefer low-visibility routes when needed.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Historical series, spreads, liquidity, gas.
### AI interaction
AI may tune thresholds or rank candidates.
### Runtime workflow
Score -> validate -> size -> execute -> monitor -> exit.
### State machine
Idle -> Candidate -> Approved -> Open -> Closing -> Closed -> Reconciled.
### IPC interactions
Signal, plan, order, position, accounting events.
### Database persistence
Store signals, positions, outcomes.
### Monitoring metrics
Hit rate, PnL, drawdown, regime-break rate.
### Alert thresholds
Alert on drawdown and correlation breakouts.
### Backtesting methodology
Use historical replay and regime segmentation.
### Simulation scenarios
Volatility spikes, correlation collapse, stale data.
### Stress testing
Broaden volatility bands and reduce liquidity.
### Performance metrics
Sharpe-like metrics, drawdown, win rate.
### Failure scenarios
False positive, regime shift, stale inputs.
### Recovery behaviour
Reduce size, pause, or reparameterize per policy.
### Known limitations
Historical relationships may not persist.
### Extension points
Alternate statistics engines and regime detectors.

## Grid Trading
### Business objective
Capture bounded oscillations with structured buy/sell levels.
### Decision logic
Place grid levels around a reference price and rebalance on fills.
### Market conditions
Works best in range-bound markets.
### Entry conditions
Range validity, liquidity, and risk approval.
### Exit conditions
Grid completion, risk breach, or trend break.
### Position sizing
Split capital across grid levels.
### Capital allocation
Reserve capital across both buy and sell sides.
### Risk controls
Max inventory, grid width, and max drawdown.
### Stop-loss
Exit when trend invalidates the range.
### Take-profit
Profit from cycle completion and rebalancing.
### Volatility handling
Wider grids in high volatility; narrower grids in calm regimes.
### Liquidity requirements
Every level must have sufficient fill probability.
### Slippage tolerance
Level-specific tolerance per grid step.
### Gas optimisation rules
Minimize update frequency and batch when possible.
### MEV considerations
Prefer protected updates if grid visibility is exploitable.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Reference price, volatility, depth, gas.
### AI interaction
AI may suggest range width or grid density.
### Runtime workflow
Initialize grid -> monitor fills -> rebalance -> exit.
### State machine
Idle -> Candidate -> Active -> Rebalancing -> Closed -> Reconciled.
### IPC interactions
Strategy, order, execution, portfolio events.
### Database persistence
Persist grid levels, fills, and realized PnL.
### Monitoring metrics
Fill cadence, inventory drift, grid efficiency.
### Alert thresholds
Alert on repeated range breaks or inventory drift.
### Backtesting methodology
Replay range-bound historical windows.
### Simulation scenarios
Range breakout, volatility spike, liquidity removal.
### Stress testing
Expand volatility and slash depth.
### Performance metrics
Grid efficiency and realized cycle returns.
### Failure scenarios
Trend breakout, missed rebalance, stale grid.
### Recovery behaviour
Recenter or disable grid per policy.
### Known limitations
Underperforms in strong trends.
### Extension points
Dynamic grid spacing and adaptive bands.

## Scalping
### Business objective
Capture very small short-lived inefficiencies.
### Decision logic
Use short horizon signals and fast cancellation logic.
### Market conditions
Low latency, tight spread, high liquidity.
### Entry conditions
Micro-edge plus fresh data and low execution risk.
### Exit conditions
Quick fill, edge loss, or timeout.
### Position sizing
Very small by design.
### Capital allocation
Minimal inventory at risk.
### Risk controls
Hard timeout, strict slippage ceiling.
### Stop-loss
Immediate abort on adverse move.
### Take-profit
Capture micro-edge only.
### Volatility handling
Reduce or disable when volatility destabilizes fills.
### Liquidity requirements
Very high liquidity and rapid orderability.
### Slippage tolerance
Extremely tight.
### Gas optimisation rules
Use only when gas cost is dominated by edge.
### MEV considerations
Use protection where search risk is material.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Ultra-fresh quotes, gas, depth, spread.
### AI interaction
AI may prioritize venues but not override latency policy.
### Runtime workflow
Detect -> validate -> submit -> cancel/close quickly.
### State machine
Idle -> Candidate -> Submitted -> Filled | Cancelled | Failed -> Reconciled.
### IPC interactions
High-frequency opportunity and execution events.
### Database persistence
Record every attempt and result for analytics.
### Monitoring metrics
Latency, fill speed, win rate.
### Alert thresholds
Alert on latency and failure bursts.
### Backtesting methodology
Tick-replay and execution-delay modeling.
### Simulation scenarios
Latency spike, stale quotes, gas surge.
### Stress testing
Increase latency and widen spread noise.
### Performance metrics
Net micro-edge and fill latency.
### Failure scenarios
Missed fills, stale order, stale data.
### Recovery behaviour
Pause if latency or stale data exceeds threshold.
### Known limitations
Highly sensitive to latency and fees.
### Extension points
Latency-aware routers and faster venues.

## Momentum
### Business objective
Ride directional continuation after confirmation.
### Decision logic
Use trend, volume, and momentum confirmation signals.
### Market conditions
Directional trend with supportive volume.
### Entry conditions
Trend confirmation and risk approval.
### Exit conditions
Trend weakness, stop-loss, or target hit.
### Position sizing
By trend strength and volatility.
### Capital allocation
Prefer staged entries.
### Risk controls
Regime failure detection and trailing stop.
### Stop-loss
Use trailing or fixed risk stop.
### Take-profit
On target or momentum decay.
### Volatility handling
Use volatility-adjusted sizing.
### Liquidity requirements
Enough depth to enter and exit cleanly.
### Slippage tolerance
Adjusted by trend strength and market depth.
### Gas optimisation rules
Trade only when expected trend edge clears costs.
### MEV considerations
Normal route protections as needed.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Trend, volume, volatility, liquidity.
### AI interaction
AI may rank trend quality and confidence.
### Runtime workflow
Signal -> size -> execute -> trail -> exit.
### State machine
Idle -> Candidate -> Open -> Managing -> Closed -> Reconciled.
### IPC interactions
Signal, order, execution, portfolio events.
### Database persistence
Persist signals, entries, exits, and outcome.
### Monitoring metrics
Trend hit rate, average hold time.
### Alert thresholds
Alert on repeated stop-outs or trend failure.
### Backtesting methodology
Replay trend regimes.
### Simulation scenarios
Fake breakout, reversal, volume drop.
### Stress testing
Degrade trend quality and raise noise.
### Performance metrics
Profit factor and trend capture rate.
### Failure scenarios
False breakout and regime reversal.
### Recovery behaviour
Reduce size or pause strategy.
### Known limitations
Performs poorly in sideways markets.
### Extension points
Adaptive trend filters and confirmations.

## Mean Reversion
### Business objective
Profit from returns to a mean after overextension.
### Decision logic
Use deviation and reversion confidence.
### Market conditions
Stable, oscillating markets.
### Entry conditions
Overextension beyond threshold with risk approval.
### Exit conditions
Mean reached or stop-loss.
### Position sizing
Smaller when volatility rises.
### Capital allocation
Allocate according to reversion confidence.
### Risk controls
Cap exposure and time-based exits.
### Stop-loss
Exit on continued divergence.
### Take-profit
Exit at mean or target band.
### Volatility handling
Widen thresholds when volatility is high.
### Liquidity requirements
Sufficient to enter and exit around mean.
### Slippage tolerance
Must remain below expected reversion edge.
### Gas optimisation rules
Only if expected reversion edge exceeds cost.
### MEV considerations
Use protected route when needed.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Deviation, historical mean, volatility, liquidity.
### AI interaction
AI may help classify regime and confidence.
### Runtime workflow
Detect -> enter -> monitor -> exit.
### State machine
Idle -> Candidate -> Open -> Closing -> Closed -> Reconciled.
### IPC interactions
Signal, order, execution, accounting events.
### Database persistence
Signals, positions, exits, PnL.
### Monitoring metrics
Reversion rate, stop-out rate.
### Alert thresholds
Alert on persistent divergence.
### Backtesting methodology
Replay mean-reverting regimes.
### Simulation scenarios
Breakout, false mean, volatility spike.
### Stress testing
Widen deviations and reduce liquidity.
### Performance metrics
Win rate, drawdown, payoff ratio.
### Failure scenarios
Trend continuation, stale inputs.
### Recovery behaviour
Pause or reparameterize on regime change.
### Known limitations
Regime shifts can invalidate the model.
### Extension points
Alternate mean estimators and regime filters.

## Market Making
### Business objective
Provide two-sided quotes while controlling inventory and spread capture.
### Decision logic
Quote bid/ask based on inventory, spread, and risk.
### Market conditions
High liquidity and stable spreads.
### Entry conditions
Inventory policy, spread policy, and risk approval.
### Exit conditions
Inventory breach, spread invalidation, or stop.
### Position sizing
Inventory-aware and symmetric by policy.
### Capital allocation
Reserve capital for both sides and adverse movement.
### Risk controls
Inventory caps, quote fade rules, and cancel rules.
### Stop-loss
Reduce or cancel quotes when inventory risk grows.
### Take-profit
Captured spread and inventory rebalance profit.
### Volatility handling
Wider spreads and smaller quotes when volatility rises.
### Liquidity requirements
High enough to maintain continuous quoting.
### Slippage tolerance
Use tight tolerance because quoting is continuous.
### Gas optimisation rules
Batch quote updates and avoid wasteful churn.
### MEV considerations
Protect when quotes are externally exploitable.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Inventory, spread, depth, volatility, gas.
### AI interaction
AI may tune spread bands or inventory bias.
### Runtime workflow
Quote -> monitor -> adjust -> rebalance -> stop.
### State machine
Idle -> Quoting -> Managing -> Rebalancing -> Stopped -> Reconciled.
### IPC interactions
Market data, order, execution, risk events.
### Database persistence
Quotes, fills, inventory, PnL.
### Monitoring metrics
Spread capture, inventory drift, quote hit rate.
### Alert thresholds
Alert on inventory breach or quote churn.
### Backtesting methodology
Replay continuous market making windows.
### Simulation scenarios
Adverse selection, inventory shock, liquidity drain.
### Stress testing
Expand volatility and inventory pressure.
### Performance metrics
Spread capture and inventory-adjusted PnL.
### Failure scenarios
Inventory imbalance, quote poisoning.
### Recovery behaviour
Widen spread, reduce size, or stop quoting.
### Known limitations
Adverse selection risk in fast markets.
### Extension points
Dynamic spread engines and inventory controllers.

## Liquidity Provision
### Business objective
Supply capital to pools for yield while controlling impermanent loss and exposure.
### Decision logic
Compare yield, fee generation, and loss risk.
### Market conditions
Stable pools with acceptable reward/risk balance.
### Entry conditions
Pool approval, capital availability, risk approval.
### Exit conditions
Reward decay, pool risk, or policy trigger.
### Position sizing
By pool depth, IL risk, and capital limits.
### Capital allocation
Conservative and diversified.
### Risk controls
Pool caps, IL controls, exit triggers.
### Stop-loss
Exit on pool risk or reward collapse.
### Take-profit
Collect yield and favorable fee revenue.
### Volatility handling
Reduce exposure as volatility rises.
### Liquidity requirements
Pool depth and acceptable concentration.
### Slippage tolerance
Must fit pool withdrawal/addition limits.
### Gas optimisation rules
Enter/exit only when net yield remains positive.
### MEV considerations
Avoid visible rebalancing when exploitable.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Pool APY, depth, volatility, fees.
### AI interaction
AI may rank pools by risk-adjusted yield.
### Runtime workflow
Evaluate pool -> enter -> monitor -> exit.
### State machine
Idle -> Candidate -> Active -> Exiting -> Closed -> Reconciled.
### IPC interactions
Opportunity, position, accounting events.
### Database persistence
Pool positions, yield, and exit reason.
### Monitoring metrics
Yield, IL, capital efficiency.
### Alert thresholds
Alert on IL or reward collapse.
### Backtesting methodology
Replay historical pool data and reward regimes.
### Simulation scenarios
Reward decay, volatility spike, pool drain.
### Stress testing
Increase impermanent loss and reduce fees.
### Performance metrics
Net yield after IL and gas.
### Failure scenarios
Pool risk event, withdrawal failure.
### Recovery behaviour
Exit and reconcile pool position.
### Known limitations
Yield can be offset by IL and gas.
### Extension points
Alternative pool selectors and yield optimizers.

## Yield Farming
### Business objective
Optimize reward-bearing deployments with controlled risk.
### Decision logic
Compare incentive rate against risk and cost.
### Market conditions
Reward programs with acceptable security risk.
### Entry conditions
Program approval and risk acceptance.
### Exit conditions
Reward decay, risk change, or policy trigger.
### Position sizing
By reward stability and capital limits.
### Capital allocation
Conservative and monitored.
### Risk controls
Program risk cap and withdrawal thresholds.
### Stop-loss
Exit on security or reward deterioration.
### Take-profit
Harvest rewards when policy permits.
### Volatility handling
Reduce exposure when market or reward volatility rises.
### Liquidity requirements
Enough liquidity to enter and exit without excess impact.
### Slippage tolerance
Bounded by exit policy.
### Gas optimisation rules
Harvest only when net reward remains positive.
### MEV considerations
Protect harvest or rebalance if needed.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Reward schedule, liquidity, volatility, gas.
### AI interaction
AI may rank by risk-adjusted reward.
### Runtime workflow
Select -> deploy -> monitor -> harvest -> exit.
### State machine
Idle -> Candidate -> Active -> Harvesting -> Closed -> Reconciled.
### IPC interactions
Opportunity, position, accounting events.
### Database persistence
Reward accrual and exit records.
### Monitoring metrics
Reward rate, net yield, risk score.
### Alert thresholds
Alert on reward collapse or program risk.
### Backtesting methodology
Replay historical reward schedules.
### Simulation scenarios
Reward drop, contract risk, gas spike.
### Stress testing
Increase gas and lower reward payouts.
### Performance metrics
Net reward after costs.
### Failure scenarios
Program failure, claim failure.
### Recovery behaviour
Exit and reconcile or block further participation.
### Known limitations
Protocol and reward risk can dominate returns.
### Extension points
Reward calculators and program adapters.

## Dollar-Cost Averaging
### Business objective
Accumulate exposure on a schedule.
### Decision logic
Execute periodic buys under budget and risk policy.
### Market conditions
Any supported market with budget availability.
### Entry conditions
Schedule due, budget available, risk approved.
### Exit conditions
Budget completion, policy stop, or manual halt.
### Position sizing
Fixed or schedule-based.
### Capital allocation
Predefined budget slices.
### Risk controls
Budget cap and pause rules.
### Stop-loss
Pause on policy breach.
### Take-profit
Not primary; accumulate cost basis.
### Volatility handling
Continue under schedule with optional size adjustments.
### Liquidity requirements
Sufficient to execute scheduled orders.
### Slippage tolerance
Moderate but bounded.
### Gas optimisation rules
Batch if schedule permits.
### MEV considerations
Normal route protection if necessary.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Price, liquidity, gas.
### AI interaction
AI may propose schedule adjustments.
### Runtime workflow
Wait -> execute schedule -> record -> repeat.
### State machine
Idle -> Scheduled -> Executing -> Waiting -> Completed -> Reconciled.
### IPC interactions
Schedule, order, execution, accounting events.
### Database persistence
Schedules, fills, cost basis.
### Monitoring metrics
Schedule adherence, average cost.
### Alert thresholds
Alert on missed executions or budget breach.
### Backtesting methodology
Replay scheduled purchase histories.
### Simulation scenarios
Gas spike, missed schedule, price gap.
### Stress testing
Simulate prolonged drawdown and gas spikes.
### Performance metrics
Average cost and schedule completion.
### Failure scenarios
Missed execution, insufficient balance.
### Recovery behaviour
Retry next window or notify operator.
### Known limitations
Not designed for rapid market timing.
### Extension points
Adaptive schedules and budget controllers.

## Swing Trading
### Business objective
Capture multi-session directional swings.
### Decision logic
Use trend, momentum, and regime confirmation.
### Market conditions
Directional moves with manageable noise.
### Entry conditions
Trend confirmation and acceptable risk score.
### Exit conditions
Trend exhaustion, stop-loss, or target.
### Position sizing
By volatility and conviction.
### Capital allocation
Staged by confidence.
### Risk controls
Trailing stop and max hold rules.
### Stop-loss
Defined by regime and ATR-like policy.
### Take-profit
Target or trend exhaustion.
### Volatility handling
Size down in high volatility.
### Liquidity requirements
Enough for entry and planned exit.
### Slippage tolerance
Bounded by expected swing profit.
### Gas optimisation rules
Prefer fewer, higher-conviction trades.
### MEV considerations
Use protective routing when needed.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Trend, momentum, volatility, liquidity.
### AI interaction
AI may rank conviction and regime quality.
### Runtime workflow
Analyze -> size -> enter -> manage -> exit.
### State machine
Idle -> Candidate -> Open -> Managing -> Closed -> Reconciled.
### IPC interactions
Signal, order, position, accounting events.
### Database persistence
Entry, exit, and PnL records.
### Monitoring metrics
Hold time, drawdown, trend capture.
### Alert thresholds
Alert on repeated stop-outs.
### Backtesting methodology
Replay swing regimes.
### Simulation scenarios
Trend reversal, gap move, liquidity drain.
### Stress testing
Increase noise and reduce liquidity.
### Performance metrics
Profit factor and average hold return.
### Failure scenarios
Gap against position, false trend.
### Recovery behaviour
Tighten stops or pause on regime failure.
### Known limitations
Slow response to sudden reversals.
### Extension points
Adaptive exits and volatility-aware sizing.

## AI-assisted Strategies
### Business objective
Use AI to rank, select, or parameterize strategies while preserving deterministic safety rules.
### Decision logic
AI may recommend but risk and execution gates decide final action.
### Market conditions
Any market where AI confidence is sufficiently high.
### Entry conditions
AI confidence and risk approval meet policy.
### Exit conditions
Model confidence drops, risk breach, or strategy failure.
### Position sizing
Constrained by deterministic policy, not AI alone.
### Capital allocation
Allocated only after explicit risk checks.
### Risk controls
AI cannot override safety limits.
### Stop-loss
Same as the underlying strategy policy.
### Take-profit
Same as the underlying strategy policy.
### Volatility handling
AI may lower confidence under unstable conditions.
### Liquidity requirements
Inherited from the underlying strategy.
### Slippage tolerance
Inherited from underlying strategy policy.
### Gas optimisation rules
Inherited from execution policy.
### MEV considerations
Inherited from execution policy.
### Supported chains
Configured chain set.
### Supported DEXs
Configured DEX set.
### Required market data
Strategy inputs plus AI context and memory.
### AI interaction
Directly owned by `AI-PIPELINE.md` but consumed here.
### Runtime workflow
AI ranks -> validate -> strategy executes if approved.
### State machine
Delegates to underlying strategy plus AI approval state.
### IPC interactions
AI recommendation, validation, execution events.
### Database persistence
Prompt version, confidence, decision, outcome.
### Monitoring metrics
Confidence calibration, override rate, success rate.
### Alert thresholds
Alert on model drift or override bursts.
### Backtesting methodology
Replay AI decisions against historical opportunities.
### Simulation scenarios
Bad model output, low confidence, stale memory.
### Stress testing
Degrade model confidence and increase noise.
### Performance metrics
Decision precision, approved win rate.
### Failure scenarios
Provider failure, hallucinated signal, stale context.
### Recovery behaviour
Fallback model, human review, or no-trade.
### Known limitations
AI output is advisory and bounded by deterministic control planes.
### Extension points
Additional models, prompt templates, and memory sources.

## Hybrid Strategies
### Business objective
Compose multiple strategy primitives into one coordinated policy.
### Decision logic
Use component strategy rules plus composition constraints.
### Market conditions
Only when all component strategies are valid or a coordinator can manage mixed states.
### Entry conditions
All mandatory components approved.
### Exit conditions
Any critical component invalidates or stop criteria trigger.
### Position sizing
Allocated across component strategies by policy.
### Capital allocation
Partitioned to preserve component risk limits.
### Risk controls
The tightest component rule wins.
### Stop-loss
Any component stop-loss may trigger global exit depending on policy.
### Take-profit
Aggregated or component-based per configuration.
### Volatility handling
Route volatility to the most conservative component.
### Liquidity requirements
All active sub-strategies must remain valid.
### Slippage tolerance
Minimum of component tolerances.
### Gas optimisation rules
Aggregate execution cost must remain profitable.
### MEV considerations
Protect the most exposed component path.
### Supported chains
Union of component-supported chains under policy.
### Supported DEXs
Union of component-supported DEXs under policy.
### Required market data
All component inputs plus orchestration data.
### AI interaction
AI may coordinate ranking but not bypass component rules.
### Runtime workflow
Coordinate -> validate -> execute components -> reconcile -> learn.
### State machine
Composite state machine with per-component substates.
### IPC interactions
Composite strategy events and component status events.
### Database persistence
Persist component mapping, aggregate result, and outcomes.
### Monitoring metrics
Component success, coordination latency, aggregate PnL.
### Alert thresholds
Alert on component divergence or coordination failure.
### Backtesting methodology
Replay each component and the coordinator.
### Simulation scenarios
One component failing, asymmetric market changes.
### Stress testing
Break each component independently and jointly.
### Performance metrics
Aggregate return and coordination efficiency.
### Failure scenarios
Mixed-state inconsistency, component stop mismatch.
### Recovery behaviour
Fail closed or degrade per policy.
### Known limitations
Complexity increases with each component added.
### Extension points
New components and coordinator policies.

