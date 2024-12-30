#!/usr/bin/env bash
# collect.sh <yml file> is used to get a link to the collector (innsamler)
# containing the data from the specified yml file.

set -euo pipefail

yml_file=$1

if [ -z "$yml_file" ]; then
    echo "Usage: $0 <yml_file>"
    exit 1
fi


data=$(yq --output-format json --no-colors $yml_file | jq -M --ascii-output | base64 -w 0 | tr -d '=')


url='https://kraftsystemet.no/fri-nettleie/innsamler/'

# Local url used for debugging/testing
#url='http://127.0.0.1:3000/docs/innsamler/index.html'

echo Visit the following URL in a browser:
echo "${url}?data=${data}"
