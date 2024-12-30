#!/usr/bin/bash
set -euxo pipefail

# go to script directory
cd $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


RAW_FILE=../referanse-data/nve/.nettleie-per-omrade-pr-maned-husholdning-fritid-effekttariffer.json

# download raw file if not exists
if [ ! -f $RAW_FILE ]; then
  curl -X 'GET' \
    'https://biapi.nve.no/nettleietariffer/api/NettleiePerOmradePrManedHusholdningFritidEffekttariffer?FraDato=2024-11-01&Tariffgruppe=Husholdning&Kundegruppe=2' \
    -H 'accept: application/json' > $RAW_FILE
fi

clickhouse local --output-format JSON \
-q 'SELECT DISTINCT replaceOne(organisasjonsnr, '"'"'*'"'"', '"''"') as organisasjonsnr, replaceOne(konsesjonar, '"'"'*'"'"', '"''"') as konsesjonar, fylkeNr, fylke FROM '"'"$RAW_FILE"'"' ORDER BY konsesjonar, fylkeNr' \
| jq -r -M '.data' > ../referanse-data/nve/konsesjonar_fylke.json

clickhouse local --output-format JSON \
-q 'SELECT DISTINCT organisasjonsnr, konsesjonar FROM '"'"'../referanse-data/nve/konsesjonar_fylke.json'"'"' ORDER BY konsesjonar' \
| jq -r -M '.data' > ../referanse-data/nve/konsesjonar.json
