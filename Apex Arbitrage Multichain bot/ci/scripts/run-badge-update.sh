#!/bin/bash
set -e

echo "Updating all CI badges..."
node ci/workflows/badge-updater.yml
cp ci/badges/*.svg docs/badges/
echo "All badges updated"
