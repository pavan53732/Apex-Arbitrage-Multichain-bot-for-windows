'use strict';

const EventEmitter = require('events');
const { detectOpportunities } = require('../arbitrage/detector');
const Executor = require('./executor');
const logger = require('../logger');

const MAX_EXEC_PER_SCAN = 3;

class Engine extends EventEmitter {
  constructor({ priceSource, store, config }) {
    super();
    this.priceSource = priceSource;
    this.store = store;
    this.config = config;
    this.executor = new Executor(config);
    this.baseToken = config.portfolio.baseToken;
    this.timer = null;
    this.latestMarket = null;

    if (this.store.getBalance() === 0) {
      this.store.setBalance(config.portfolio.initialBalanceUsd);
    }
  }

  isRunning() {
    return this.timer !== null;
  }

  async scanOnce() {
    let market;
    try {
      market = await this.priceSource.fetchMarket();
    } catch (err) {
      this.emit('error', err);
      logger.error('Price fetch failed:', err.message);
      return { opportunities: [], market: null };
    }
    this.latestMarket = market;
    this.store.updateStats({ lastScanAt: Date.now(), scans: this.store.getStats().scans + 1 });

    const opportunities = detectOpportunities(market, this.config, this.baseToken);
    if (opportunities.length > 0) {
      this.store.addOpportunities(opportunities);
      this.emit('opportunities', opportunities);
    }
    this.emit('scan', market);

    if (this.config.engine.autoExecute) {
      await this._executeTop(opportunities);
    }
    return { opportunities, market };
  }

  async _executeTop(opportunities) {
    const candidates = opportunities
      .filter((o) => o.profitPct >= this.config.engine.minProfitPct)
      .sort((a, b) => b.profitPct - a.profitPct)
      .slice(0, MAX_EXEC_PER_SCAN);

    for (const op of candidates) {
      const balance = this.store.getBalance();
      const result = this.executor.simulate(op, balance);
      if (!result.ok) {
        logger.warn(`Skip exec ${op.id}: ${result.reason}`);
        continue;
      }
      this.store.recordTrade(result.trade);
      this.store.setBalance(result.newBalance);
      this.emit('trade', result.trade);
      logger.info(`Executed ${op.type} ${op.path.join('>')} profit=$${result.trade.profitUsd}`);
    }
  }

  start() {
    if (this.isRunning()) return;
    this.timer = setInterval(() => {
      this.scanOnce().catch((e) => this.emit('error', e));
    }, this.config.engine.scanIntervalMs);
    this.store.updateStats({ running: true, startedAt: Date.now() });
    this.emit('status', true);
    logger.info(`Engine started (interval ${this.config.engine.scanIntervalMs}ms)`);
  }

  stop() {
    if (!this.isRunning()) return;
    clearInterval(this.timer);
    this.timer = null;
    this.store.updateStats({ running: false });
    this.emit('status', false);
    logger.info('Engine stopped');
  }
}

module.exports = Engine;
