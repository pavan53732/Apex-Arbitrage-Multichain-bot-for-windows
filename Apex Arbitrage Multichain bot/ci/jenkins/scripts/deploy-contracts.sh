#!/bin/bash
set -e

echo "Deploying contracts..."
cd contracts
npx hardhat compile
npx hardhat deploy --network ${NETWORK:-mainnet}
echo "Contracts deployed successfully"
