#!/bin/bash
set -e

echo "Running linters..."
npm run lint
npx prettier --check "**/*.{js,ts,json,md}"
echo "Linting completed successfully"
