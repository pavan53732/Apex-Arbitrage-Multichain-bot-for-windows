'use strict';

const { PriceSource, buildMarket } = require('./priceSource');
const logger = require('../logger');

class CoinGeckoSource extends PriceSource {
  constructor(config) {
    super(config);
    const cfg = config.pricing.coingecko;
    this.baseUrl = cfg.baseUrl;
    this.vsCurrency = cfg.vsCurrency;
    this.timeoutMs = cfg.timeoutMs;
    this.tokens = config.tokens;
  }

  async fetchMarket() {
    const ids = this.tokens.map((t) => t.coingeckoId).join(',');
    const url = `${this.baseUrl}/simple/price?ids=${encodeURIComponent(ids)}&vs_currencies=${this.vsCurrency}`;
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), this.timeoutMs);
    let data;
    try {
      const res = await fetch(url, { signal: controller.signal });
      if (!res.ok) throw new Error(`CoinGecko HTTP ${res.status}`);
      data = await res.json();
    } finally {
      clearTimeout(timer);
    }

    const basePrices = {};
    for (const t of this.tokens) {
      const price = data[t.coingeckoId] && data[t.coingeckoId][this.vsCurrency];
      if (typeof price !== 'number') {
        logger.warn(`No price for ${t.symbol} (${t.coingeckoId})`);
        continue;
      }
      basePrices[t.symbol] = price;
    }
    if (Object.keys(basePrices).length === 0) throw new Error('CoinGecko returned no prices');

    // CoinGecko returns a single aggregate USD price per coin; we replicate it
    // across all configured venues (offset 0). Real per-venue order-book feeds
    // would replace this distribution to surface genuine cross-venue spreads.
    return buildMarket({
      basePrices,
      venues: this.venues,
      source: 'coingecko',
    });
  }
}

module.exports = CoinGeckoSource;
