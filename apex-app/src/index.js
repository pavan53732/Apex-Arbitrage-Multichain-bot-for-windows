'use strict';

const path = require('path');
const { loadConfig } = require('./config');
const { createPriceSource } = require('./pricing');
const Store = require('./storage/store');
const Engine = require('./engine/engine');
const { buildServer } = require('./server/app');
const logger = require('./logger');

function bootstrap(configOverrides = {}) {
  const config = loadConfig();
  Object.assign(config, configOverrides);

  const dbPath = process.env.APEX_DB || path.join(__dirname, '..', 'data', 'apex.json');
  const store = new Store(dbPath);
  const priceSource = createPriceSource(config);
  const engine = new Engine({ priceSource, store, config });

  const server = buildServer({ engine, store, config, priceSource });
  return { config, store, priceSource, engine, server };
}

function main() {
  const { config, engine, server } = bootstrap();

  const port = config.server.port;
  const host = config.server.host;
  server.listen(port, host, () => {
    logger.info(`Apex Arbitrage API listening on http://${host}:${port}`);
    logger.info(`Pricing source: ${config.pricing.source} | autoExecute: ${config.engine.autoExecute}`);
  });

  if (config.engine.enabled) {
    engine.start();
  }

  const shutdown = (sig) => {
    logger.info(`Received ${sig}, shutting down...`);
    engine.stop();
    server.close(() => process.exit(0));
  };
  process.on('SIGINT', () => shutdown('SIGINT'));
  process.on('SIGTERM', () => shutdown('SIGTERM'));
}

if (require.main === module) {
  main();
}

module.exports = { bootstrap, main };
