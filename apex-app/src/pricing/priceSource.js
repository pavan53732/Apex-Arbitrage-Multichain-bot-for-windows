'use strict';

/**
 * Pricing abstraction. A PriceSource produces a `market` snapshot:
 *   { timestamp, source, prices: { TOKEN: { venueId: usdPrice } }, venues: { venueId: meta } }
 *
 * The CoinGecko source derives a single aggregate USD price per token, then
 * distributes it across venues with a small, deterministic per-venue offset so
 * that cross-venue arbitrage opportunities can be detected (real per-venue
 * order-book feeds would replace this distribution in production).
 */

function buildVenueMeta(venues) {
  const meta = {};
  for (const v of venues) meta[v.id] = { id: v.id, name: v.name, feePct: v.feePct, chain: v.chain };
  return meta;
}

/**
 * Distribute base USD prices across venues. `offsetFor(venueId, token)` returns
 * a fractional offset (e.g. 0.01 = +1%) applied to that venue's price.
 */
function buildMarket({ basePrices, venues, offsetFor, source }) {
  const prices = {};
  for (const token of Object.keys(basePrices)) {
    prices[token] = {};
    for (const v of venues) {
      const offset = offsetFor ? offsetFor(v.id, token) : 0;
      prices[token][v.id] = basePrices[token] * (1 + offset);
    }
  }
  return {
    timestamp: Date.now(),
    source,
    prices,
    venues: buildVenueMeta(venues),
  };
}

class PriceSource {
  constructor(config) {
    this.config = config;
    this.venues = config.venues;
  }
  // eslint-disable-next-line no-unused-vars
  async fetchMarket() {
    throw new Error('fetchMarket() not implemented');
  }
}

module.exports = { PriceSource, buildMarket, buildVenueMeta };
