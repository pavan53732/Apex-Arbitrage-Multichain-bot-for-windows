'use strict';

const { MockSource } = require('../../src/pricing/mockSource');
const CoinGeckoSource = require('../../src/pricing/coingeckoSource');

function makeConfig() {
  return {
    pricing: {
      coingecko: { baseUrl: 'https://api.coingecko.com/api/v3', vsCurrency: 'usd', timeoutMs: 5000 },
      mock: { jitterPct: 0.4 },
    },
    venues: [
      { id: 'uniswap', name: 'Uniswap', feePct: 0.3, chain: 'ethereum' },
      { id: 'sushiswap', name: 'SushiSwap', feePct: 0.25, chain: 'ethereum' },
    ],
    tokens: [
      { symbol: 'ETH', name: 'Ethereum', coingeckoId: 'ethereum' },
      { symbol: 'BTC', name: 'Bitcoin', coingeckoId: 'bitcoin' },
    ],
  };
}

describe('MockSource', () => {
  test('returns prices distributed across all configured venues', async () => {
    const cfg = makeConfig();
    const src = new MockSource(cfg, { ETH: { uniswap: 3000, sushiswap: 3030 }, BTC: { uniswap: 60000, sushiswap: 60000 } });
    const market = await src.fetchMarket();
    expect(market.source).toBe('mock');
    expect(market.prices.ETH.uniswap).toBe(3000);
    expect(market.prices.ETH.sushiswap).toBe(3030);
    expect(market.venues.uniswap.feePct).toBe(0.3);
  });
});

describe('CoinGeckoSource', () => {
  const cfg = makeConfig();

  afterEach(() => jest.restoreAllMocks());

  test('parses simple price response into per-venue prices', async () => {
    const fakeJson = { ethereum: { usd: 3000 }, bitcoin: { usd: 60000 } };
    jest.spyOn(global, 'fetch').mockResolvedValue({
      ok: true,
      json: async () => fakeJson,
    });

    const src = new CoinGeckoSource(cfg);
    const market = await src.fetchMarket();
    expect(market.source).toBe('coingecko');
    expect(market.prices.ETH.uniswap).toBeCloseTo(3000, 0);
    expect(market.prices.BTC.sushiswap).toBeCloseTo(60000, 0);
  });

  test('throws when the HTTP response is not ok', async () => {
    jest.spyOn(global, 'fetch').mockResolvedValue({ ok: false, status: 429, json: async () => ({}) });
    const src = new CoinGeckoSource(cfg);
    await expect(src.fetchMarket()).rejects.toThrow(/HTTP 429/);
  });

  test('throws when no prices are returned', async () => {
    jest.spyOn(global, 'fetch').mockResolvedValue({ ok: true, json: async () => ({}) });
    const src = new CoinGeckoSource(cfg);
    await expect(src.fetchMarket()).rejects.toThrow(/no prices/);
  });
});
