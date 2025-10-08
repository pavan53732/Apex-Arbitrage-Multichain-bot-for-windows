#!/bin/bash
set -e

echo "Running coverage tests..."
npm run test:coverage
python -m pytest --cov=backend --cov-report=html
echo "Coverage report generated"
