#!/usr/bin/env bash
#
# Gets data from
# https://nve.geodataonline.no/arcgis/rest/services/Nettanlegg2/MapServer
#
# Same data as shown in https://temakart.nve.no/tema/nettanlegg
#

# go to script directory
cd $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# The result set contains polygons but we are only interested in
curl 'https://nve.geodataonline.no/arcgis/rest/services/Nettanlegg2/MapServer/6/query?where=1%3D1&outFields=*&f=json' \
    --silent \
    --compressed | jq '[.features[].attributes] | sort_by(.NAVN)' > ../referanse-data/nve/consessionaires.json
