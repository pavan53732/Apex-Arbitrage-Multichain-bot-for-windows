'use strict';

const { applyFee, estimateSlippage, evaluateLegs, pctToFraction } = require('../../src/arbitrage/profit');

describe('profit math', () => {
  test('pctToFraction converts percent to fraction', () => {
    expect(pctToFraction(100)).toBe(1);
    expect(pctToFraction(0.3)).toBeCloseTo(0.003);
  });

  test('applyFee deducts the taker fee', () => {
    expect(applyFee(1000, 0.3)).toBeCloseTo(997);
    expect(applyFee(500, 0)).toBe(500);
  });

  test('estimateSlippage scales with trade size vs depth', () => {
    expect(estimateSlippage(0, 1e6)).toBe(0);
    const small = estimateSlippage(1000, 5_000_000);
    expect(small).toBeCloseTo(0.0001);
    const capped = estimateSlippage(1e12, 1);
    expect(capped).toBe(0.5);
  });

  test('estimateSlippage returns 0 with no depth', () => {
    expect(estimateSlippage(1000, 0)).toBe(0);
  });

  test('evaluateLegs computes net multiplier and percentages', () => {
    const legs = [
      { factor: 1 / 3000, feePct: 0.3, tradeSizeUsd: 1000, liquidityDepthUsd: 5_000_000 },
      { factor: 3030, feePct: 0.25, tradeSizeUsd: 1000, liquidityDepthUsd: 5_000_000 },
    ];
    const r = evaluateLegs(legs);
    // gross ratio 3030/3000 = 1.01
    expect(r.grossPct).toBeCloseTo(1.0, 2);
    expect(r.multiplier).toBeGreaterThan(1);
    expect(r.netPct).toBeGreaterThan(0);
    expect(r.feePctTotal).toBeCloseTo(0.55, 5);
  });

  test('evaluateLegs returns multiplier <= 1 when no edge', () => {
    const legs = [
      { factor: 1 / 3000, feePct: 0.3, tradeSizeUsd: 1000, liquidityDepthUsd: 5_000_000 },
      { factor: 3000, feePct: 0.3, tradeSizeUsd: 1000, liquidityDepthUsd: 5_000_000 },
    ];
    const r = evaluateLegs(legs);
    // ratio 1, fees make it a loss
    expect(r.multiplier).toBeLessThan(1);
    expect(r.netPct).toBeLessThan(0);
  });
});
