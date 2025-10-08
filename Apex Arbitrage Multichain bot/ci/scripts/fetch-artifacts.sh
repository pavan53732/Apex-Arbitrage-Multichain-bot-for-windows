#!/bin/bash
set -e

echo "Fetching build artifacts..."
mkdir -p artifacts
curl -o artifacts/build.zip ${ARTIFACT_URL}
unzip artifacts/build.zip -d artifacts/
echo "Artifacts fetched successfully"
