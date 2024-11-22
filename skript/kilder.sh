#!/usr/bin/env bash
set -euo pipefail

API_KEY=$(curl -s http://localhost:5000/settings | grep -oP '(?<=<span id="api-key">).*?(?=</span>)')

diff <( \
    curl --silent --header "x-api-key: ${API_KEY}" \
    localhost:5000/api/v1/watch | jq -r '.[].url' | sort | uniq
) \
<(
    yq -r '.kilder' tariffer/*.yml | grep -Eo 'http.*' | tr -d "'" | sort | uniq
)
