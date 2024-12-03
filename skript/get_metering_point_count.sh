#!/usr/bin/env bash
set -euo pipefail

# go to script directory
cd $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

RAW_FILE='../referanse-data/elhub/.CONSUMPTION_PER_GROUP_MGA_HOUR.json'
OUT_FILE='../referanse-data/elhub/grid_owner_mp_count.csv'

# download raw file if not exists
if [ ! -f $RAW_FILE ]; then
  curl -X 'GET' \
    'https://api.elhub.no/energy-data/v0/grid-areas?dataset=CONSUMPTION_PER_GROUP_MGA_HOUR&startDate=2024-11-01T00:00:00%2B01:00&endDate=2024-11-01T00:01:00%2B01:00&consumptionGroup=household' \
    -H 'accept: application/json' > $RAW_FILE
fi

# {
#       "attributes": {
#         "consumptionPerGroupMgaHour": [
#           {
#             "consumptionGroup": "household",
#             "endTime": "2024-11-01T01:00:00+01:00",
#             "gridArea": "50YWO-6UUIJ4BF1D",
#             "lastUpdatedTime": "2024-11-09T16:04:36+01:00",
#             "meteringPointCount": 140210,
#             "quantityKwh": 219350.92,
#             "startTime": "2024-11-01T00:00:00+01:00"
#           }
#         ],
#         "eic": "50YWO-6UUIJ4BF1D",
#         "name": "EIDSIVA-D",
#         "status": "Active"
#       },
#       "id": "50YWO-6UUIJ4BF1D",
#       "relationships": {
#         "grid-owner": {
#           "data": {
#             "id": "7080005046220",
#             "type": "parties"
#           }
#         },
#         "price-area": {
#           "data": {
#             "id": "NO1",
#             "type": "price-areas"
#           }
#         }
#       },
#       "type": "grid-areas"
#     },

echo "GLN,METERING_POINT_COUNT" > $OUT_FILE

jq < $RAW_FILE -r '[.data[] | { gln:.relationships."grid-owner".data.id, mpCount: .attributes.consumptionPerGroupMgaHour[0].meteringPointCount} ] | group_by(.gln) | map([
      first.gln,
      (map(.mpCount) | add)
    ]) | .[] |@csv' >> $OUT_FILE
