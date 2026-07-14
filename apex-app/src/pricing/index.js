'use strict';

const CoinGeckoSource = require('./coingeckoSource');
const { MockSource } = require('./mockSource');

function createPriceSource(config, overrides = {}) {
  if (overrides.source) return overrides.source;
  const kind = config.pricing.source;
  if (kind === 'mock') return new MockSource(config, overrides.mockPrices);
  if (kind === 'coingecko') return new CoinGeckoSource(config);
  throw new Error(`Unknown pricing source: ${kind}`);
}

module.exports = { createPriceSource, CoinGeckoSource, MockSource };
