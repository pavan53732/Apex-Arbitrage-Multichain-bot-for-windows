#!/bin/bash
MESSAGE=$1
WEBHOOK_URL=${SLACK_WEBHOOK_URL}

curl -X POST -H 'Content-Type: application/json' \
  -d "{\"text\":\"${MESSAGE}\"}" \
  ${WEBHOOK_URL}
