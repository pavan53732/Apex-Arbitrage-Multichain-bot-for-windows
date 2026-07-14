'use strict';

const crypto = require('crypto');
const { evaluateLegs } = require('./profit');

function round(n, d = 6) {
  const f = Math.pow(10, d);
  return Math.round(n * f) / f;
}

/** Stable id derived from opportunity shape (so duplicates are de-duplicated). */
function makeId(type, path) {
  return crypto.createHash('sha1').update(`${type}:${path.join('>')}`).digest('hex').slice(0, 12);
}

/** Common venues that quote both tokens, with the best conversion factor. */
function bestConversion(tokenFrom, tokenTo, prices, venues) {
  let best = null;
  const fromMap = prices[tokenFrom] || {};
  const toMap = prices[tokenTo] || {};
  for (const venueId of Object.keys(fromMap)) {
    if (!(venueId in toMap)) continue;
    const factor = fromMap[venueId] / toMap[venueId]; // units of `to` per unit of `from`
    const feePct = venues[venueId] ? venues[venueId].feePct : 0;
    if (!best || factor > best.factor) {
      best = { venueId, factor, feePct };
    }
  }
  return best;
}

function bestSellPrice(token, prices, venues) {
  let best = null;
  const map = prices[token] || {};
  for (const venueId of Object.keys(map)) {
    const feePct = venues[venueId] ? venues[venueId].feePct : 0;
    if (!best || map[venueId] > best.price) {
      best = { venueId, price: map[venueId], feePct };
    }
  }
  return best;
}

function bestBuyPrice(token, prices, venues) {
  let best = null;
  const map = prices[token] || {};
  for (const venueId of Object.keys(map)) {
    const feePct = venues[venueId] ? venues[venueId].feePct : 0;
    if (!best || map[venueId] < best.price) {
      best = { venueId, price: map[venueId], feePct };
    }
  }
  return best;
}

function finalize(opportunity, config, timestamp) {
  const tradeSizeUsd = config.engine.tradeSizeUsd;
  const { multiplier, grossPct, feePctTotal, slippagePctTotal, netPct } = evaluateLegs(
    opportunity.legs.map((l) => ({ ...l, tradeSizeUsd, liquidityDepthUsd: config.engine.liquidityDepthUsd }))
  );
  if (multiplier <= 1) return null;
  const profitPct = round(netPct, 4);
  if (profitPct < config.engine.minProfitPct) return null;
  if (slippagePctTotal > config.engine.maxSlippagePct) return null;

  return {
    id: makeId(opportunity.type, opportunity.path),
    type: opportunity.type,
    path: opportunity.path,
    legs: opportunity.legs,
    grossPct: round(grossPct, 4),
    feePctTotal: round(feePctTotal, 4),
    slippagePctTotal: round(slippagePctTotal, 4),
    profitPct,
    tradeSizeUsd,
    expectedProfitUsd: round((tradeSizeUsd * netPct) / 100, 2),
    timestamp,
  };
}

function detectDirect(market, config, timestamp) {
  const { prices, venues } = market;
  const results = [];
  for (const token of Object.keys(prices)) {
    const buy = bestBuyPrice(token, prices, venues);
    const sell = bestSellPrice(token, prices, venues);
    if (!buy || !sell || buy.venueId === sell.venueId) continue;
    const legs = [
      { factor: 1 / buy.price, feePct: buy.feePct, venueId: buy.venueId, pair: `USD->${token}` },
      { factor: sell.price, feePct: sell.feePct, venueId: sell.venueId, pair: `${token}->USD` },
    ];
    const op = finalize({ type: 'direct', path: [token], legs }, config, timestamp);
    if (op) results.push(op);
  }
  return results;
}

function detectTriangular(market, config, timestamp, baseToken) {
  const { prices, venues } = market;
  const symbols = Object.keys(prices).filter((s) => s !== baseToken);
  const results = [];
  const seen = new Set();

  for (let i = 0; i < symbols.length; i++) {
    for (let j = 0; j < symbols.length; j++) {
      for (let k = 0; k < symbols.length; k++) {
        if (i === j || j === k || i === k) continue;
        const A = symbols[i];
        const B = symbols[j];
        const C = symbols[k];
        const key = [A, B, C].sort().join('-');
        if (seen.has(key)) continue;
        seen.add(key);

        // Two cyclic directions.
        for (const order of [[A, B, C], [A, C, B]]) {
          const [x, y, z] = order;
          const l1 = bestBuyPrice(x, prices, venues); // USD -> x
          const l2 = bestConversion(x, y, prices, venues); // x -> y
          const l3 = bestConversion(y, z, prices, venues); // y -> z
          const l4 = bestSellPrice(z, prices, venues); // z -> USD
          if (!l1 || !l2 || !l3 || !l4) continue;
          const legs = [
            { factor: 1 / l1.price, feePct: l1.feePct, venueId: l1.venueId, pair: `USD->${x}` },
            { factor: l2.factor, feePct: l2.feePct, venueId: l2.venueId, pair: `${x}->${y}` },
            { factor: l3.factor, feePct: l3.feePct, venueId: l3.venueId, pair: `${y}->${z}` },
            { factor: l4.price, feePct: l4.feePct, venueId: l4.venueId, pair: `${z}->USD` },
          ];
          const op = finalize({ type: 'triangular', path: [x, y, z], legs }, config, timestamp);
          if (op) results.push(op);
        }
      }
    }
  }
  return results;
}

/**
 * Detect all arbitrage opportunities in a market snapshot.
 * @param {object} market - { timestamp, source, prices:{}, venues:{} }
 * @param {object} config - application config
 * @param {string} baseToken - portfolio base symbol (e.g. 'USDC')
 */
function detectOpportunities(market, config, baseToken) {
  const timestamp = market.timestamp || Date.now();
  const direct = detectDirect(market, config, timestamp);
  const triangular = detectTriangular(market, config, timestamp, baseToken);
  const all = [...direct, ...triangular].sort((a, b) => b.profitPct - a.profitPct);
  return all;
}

module.exports = {
  detectOpportunities,
  detectDirect,
  detectTriangular,
};
