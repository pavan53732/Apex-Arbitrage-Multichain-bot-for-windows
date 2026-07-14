'use strict';

const crypto = require('crypto');

/** Simulated executor: models arbitrage trades against a paper portfolio. */
class Executor {
  constructor(config) {
    this.config = config;
    this.baseToken = config.portfolio.baseToken;
  }

  /**
   * Simulate executing an opportunity against a paper balance.
   * @returns {{ ok: boolean, reason?: string, trade?: object, newBalance?: number }}
   */
  simulate(opportunity, balanceUsd) {
    const size = opportunity.tradeSizeUsd;
    if (balanceUsd < size) {
      return { ok: false, reason: 'insufficient_balance' };
    }
    const profitUsd = opportunity.expectedProfitUsd;
    const newBalance = Math.round((balanceUsd + profitUsd) * 100) / 100;
    const trade = {
      id: crypto.randomBytes(8).toString('hex'),
      timestamp: Date.now(),
      type: opportunity.type,
      path: opportunity.path,
      legs: opportunity.legs,
      profitPct: opportunity.profitPct,
      tradeSizeUsd: size,
      profitUsd,
      baseToken: this.baseToken,
      status: 'simulated',
    };
    return { ok: true, trade, newBalance };
  }
}

module.exports = Executor;
