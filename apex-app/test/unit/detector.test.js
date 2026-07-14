'use strict';

const { detectOpportunities } = require('../../src/arbitrage/detector');
const { MockSource, DEFAULT_MOCK_PRICES } = require('../../src/pricing/mockSource');

function makeConfig(overrides = {}) {
  return {
    engine: {
      tradeSizeUsd: 1000,
      minProfitPct: 0.2,
      maxSlippagePct: 1.5,
      liquidityDepthUsd: 5_000_000,
      autoExecute: false,
    },
    portfolio: { baseToken: 'USDC', initialBalanceUsd: 10000 },
    venues: [
      { id: 'uniswap', name: 'Uniswap', feePct: 0.3, chain: 'ethereum' },
      { id: 'sushiswap', name: 'SushiSwap', feePct: 0.25, chain: 'ethereum' },
      { id: 'pancakeswap', name: 'PancakeSwap', feePct: 0.2, chain: 'bsc' },
      { id: 'quickswap', name: 'QuickSwap', feePct: 0.3, chain: 'polygon' },
      { id: 'curve', name: 'Curve', feePct: 0.04, chain: 'ethereum' },
      { id: 'traderjoe', name: 'Trader Joe', feePct: 0.3, chain: 'arbitrum' },
    ],
    ...overrides,
  };
}

function buildMarket(customPrices) {
  const source = new MockSource(makeConfig(), customPrices);
  return source.fetchMarket();
}

describe('arbitrage detector', () => {
  test('detects a direct cross-venue arbitrage on ETH', async () => {
    const market = await buildMarket(DEFAULT_MOCK_PRICES);
    const ops = detectOpportunities(market, makeConfig(), 'USDC');
    const ethDirect = ops.find((o) => o.type === 'direct' && o.path[0] === 'ETH');
    expect(ethDirect).toBeDefined();
    expect(ethDirect.profitPct).toBeGreaterThan(0);
    // buy cheap (quickswap 2998) -> sell dear (sushiswap 3030)
    const buyLeg = ethDirect.legs.find((l) => l.pair === 'USD->ETH');
    const sellLeg = ethDirect.legs.find((l) => l.pair === 'ETH->USD');
    expect(buyLeg.venueId).toBe('quickswap');
    expect(sellLeg.venueId).toBe('sushiswap');
  });

  test('detects at least one triangular arbitrage', async () => {
    const market = await buildMarket(DEFAULT_MOCK_PRICES);
    const ops = detectOpportunities(market, makeConfig(), 'USDC');
    const tri = ops.filter((o) => o.type === 'triangular');
    expect(tri.length).toBeGreaterThan(0);
    expect(tri.every((o) => o.profitPct > 0)).toBe(true);
  });

  test('does not report opportunities when all venues are fairly priced', async () => {
    const flat = {
      ETH: { uniswap: 3000, sushiswap: 3000, pancakeswap: 3000, quickswap: 3000, curve: 3000, traderjoe: 3000 },
      BTC: { uniswap: 60000, sushiswap: 60000, pancakeswap: 60000, quickswap: 60000, curve: 60000, traderjoe: 60000 },
      USDC: { uniswap: 1, sushiswap: 1, pancakeswap: 1, quickswap: 1, curve: 1, traderjoe: 1 },
      USDT: { uniswap: 1, sushiswap: 1, pancakeswap: 1, quickswap: 1, curve: 1, traderjoe: 1 },
      DAI: { uniswap: 1, sushiswap: 1, pancakeswap: 1, quickswap: 1, curve: 1, traderjoe: 1 },
      WBTC: { uniswap: 60000, sushiswap: 60000, pancakeswap: 60000, quickswap: 60000, curve: 60000, traderjoe: 60000 },
      MATIC: { uniswap: 0.8, sushiswap: 0.8, pancakeswap: 0.8, quickswap: 0.8, curve: 0.8, traderjoe: 0.8 },
      ARB: { uniswap: 1.2, sushiswap: 1.2, pancakeswap: 1.2, quickswap: 1.2, curve: 1.2, traderjoe: 1.2 },
    };
    const market = await buildMarket(flat);
    const ops = detectOpportunities(market, makeConfig(), 'USDC');
    expect(ops).toEqual([]);
  });

  test('filters out opportunities below minProfitPct', async () => {
    const market = await buildMarket(DEFAULT_MOCK_PRICES);
    const ops = detectOpportunities(market, makeConfig({ engine: { ...makeConfig().engine, minProfitPct: 50 } }), 'USDC');
    expect(ops).toEqual([]);
  });

  test('sorts opportunities by profitability descending', async () => {
    const market = await buildMarket(DEFAULT_MOCK_PRICES);
    const ops = detectOpportunities(market, makeConfig(), 'USDC');
    for (let i = 1; i < ops.length; i++) {
      expect(ops[i - 1].profitPct).toBeGreaterThanOrEqual(ops[i].profitPct);
    }
  });
});
