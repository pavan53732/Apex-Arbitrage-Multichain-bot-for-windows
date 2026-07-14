'use strict';

/**
 * Financial math helpers for arbitrage evaluation.
 * All percentages are expressed as numbers (e.g. 0.3 means 0.3%).
 */

function pctToFraction(pct) {
  return Number(pct) / 100;
}

/** Amount remaining after applying a taker fee (feePct in percent). */
function applyFee(amount, feePct) {
  return amount * (1 - pctToFraction(feePct));
}

/**
 * Linear slippage model: the larger the trade relative to venue liquidity
 * depth, the more price impact. Returns a fraction (0.01 = 1%).
 */
function estimateSlippage(tradeSizeUsd, liquidityDepthUsd) {
  if (!liquidityDepthUsd || liquidityDepthUsd <= 0) return 0;
  const ratio = tradeSizeUsd / liquidityDepthUsd;
  // Quadratic-ish impact: 1% of trade at 1% depth, scaled by depth factor.
  return Math.min(0.5, ratio * 0.5);
}

/**
 * Net multiplier for a sequence of legs. Each leg is:
 *   { factor, feePct, tradeSizeUsd, liquidityDepthUsd }
 * factor is the gross conversion ratio for that leg (e.g. priceFrom/priceTo).
 * Returns { multiplier, grossPct, feePctTotal, slippagePctTotal, netPct }.
 */
function evaluateLegs(legs) {
  let multiplier = 1;
  let feePctTotal = 0;
  let slippagePctTotal = 0;

  for (const leg of legs) {
    const feeFrac = pctToFraction(leg.feePct || 0);
    const slipFrac = estimateSlippage(leg.tradeSizeUsd || 0, leg.liquidityDepthUsd);
    const effective = leg.factor * (1 - feeFrac) * (1 - slipFrac);
    multiplier *= effective;
    feePctTotal += leg.feePct || 0;
    slippagePctTotal += slipFrac * 100;
  }

  const grossPct = (legs.reduce((p, l) => p * l.factor, 1) - 1) * 100;
  const netPct = (multiplier - 1) * 100;

  return { multiplier, grossPct, feePctTotal, slippagePctTotal, netPct };
}

module.exports = {
  pctToFraction,
  applyFee,
  estimateSlippage,
  evaluateLegs,
};
