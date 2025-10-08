#!/bin/bash
set -e

echo "Updating badges for Buildkite..."
bash ci/scripts/run-badge-update.sh
echo "Badges updated successfully"
