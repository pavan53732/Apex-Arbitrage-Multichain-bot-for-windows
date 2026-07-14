'use strict';

const { PriceSource, buildMarket } = require('./priceSource');

// Default deterministic market with guaranteed cross-venue mispricing so the
// app (and tests) always surface real arbitrage opportunities.
const DEFAULT_MOCK_PRICES = {
  ETH: { uniswap: 3000, sushiswap: 3030, pancakeswap: 3000, quickswap: 2998, curve: 3000, traderjoe: 3005 },
  BTC: { uniswap: 60000, sushiswap: 60000, pancakeswap: 59800, quickswap: 60100, curve: 60600, traderjoe: 60000 },
  USDC: { uniswap: 1, sushiswap: 1, pancakeswap: 1, quickswap: 1, curve: 1, traderjoe: 1 },
  USDT: { uniswap: 1.0, sushiswap: 1.0, pancakeswap: 1.0, quickswap: 1.0, curve: 1.02, traderjoe: 1.0 },
  DAI: { uniswap: 1, sushiswap: 1, pancakeswap: 1, quickswap: 1, curve: 1, traderjoe: 1 },
  WBTC: { uniswap: 60000, sushiswap: 60600, pancakeswap: 60000, quickswap: 60000, curve: 60000, traderjoe: 60000 },
  MATIC: { uniswap: 0.8, sushiswap: 0.8, pancakeswap: 0.8, quickswap: 0.8, curve: 0.8, traderjoe: 0.8 },
  ARB: { uniswap: 1.2, sushiswap: 1.2, pancakeswap: 1.2, quickswap: 1.2, curve: 1.2, traderjoe: 1.2 },
};

class MockSource extends PriceSource {
  constructor(config, customPrices) {
    super(config);
    this.prices = customPrices || DEFAULT_MOCK_PRICES;
  }

  async fetchMarket() {
    const basePrices = {};
    const venueIds = this.venues.map((v) => v.id);
    for (const token of Object.keys(this.prices)) {
      const byVenue = this.prices[token];
      basePrices[token] = {};
      for (const vId of venueIds) {
        basePrices[token][vId] = byVenue[vId] != null ? byVenue[vId] : 1;
      }
    }
    return {
      timestamp: Date.now(),
      source: 'mock',
      prices: basePrices,
      venues: this.venues.reduce((acc, v) => {
        acc[v.id] = { id: v.id, name: v.name, feePct: v.feePct, chain: v.chain };
        return acc;
      }, {}),
    };
  }
}

module.exports = { MockSource, DEFAULT_MOCK_PRICES };
