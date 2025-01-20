#!/usr/bin/env bash
# Diff sources in tariffer with sources in local dockerized Changedetection
# If the source is not in Changedetection, it will be added.
set -euo pipefail

API_KEY=$(curl -s http://localhost:5000/settings | grep -oP '(?<=<span id="api-key">).*?(?=</span>)')
echo API Key: $API_KEY
TMP_FILE=$(mktemp)
echo Temp file: $TMP_FILE

diff <( \
    curl --silent --header "x-api-key: ${API_KEY}" \
    localhost:5000/api/v1/watch | jq -r '.[].url' | sort | uniq
) \
<(
    yq -r '.kilder' tariffer/*.yml | grep -Eo 'http.*' | tr -d "'" | sort | uniq
) | cat > $TMP_FILE && true


echo
echo "In Changedetection, but not in tariffer:"
echo

cat $TMP_FILE |  grep -E '^<' | grep -Eo 'http.*' | cat || true


echo
echo "In tariffer, but not in Changedetection:"
echo

for SRC in  $(cat $TMP_FILE | grep -E '^>' | grep -Eo 'http.*' | cat); do

    echo $SRC

    curl --request POST \
    --silent \
    --header "x-api-key: ${API_KEY}" \
    --header "Content-Type: application/json" \
    localhost:5000/api/v1/watch --data '{"url": "'$SRC'" }'

    echo Added

done
