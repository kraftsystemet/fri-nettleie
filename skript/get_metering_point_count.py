#!/usr/bin/env python3
import os
import requests
import json

import cache
import elhub

if __name__ == '__main__':

    grid_owners_mp_count = elhub.get_metering_point_count()
    grid_owners = elhub.get_grid_owner_data()

    gompc = []
    for go in grid_owners:
        gln = go['gln']

        if gln in grid_owners_mp_count:
            gompc.append({
                'gln' : gln,
                'name' : go['name'],
                'mp_count' : grid_owners_mp_count[gln]
            })


    gompc.sort(key=lambda x: x['name'])

    with open('./referanse-data/elhub/grid_owner_mp_count.json', 'w') as f:
        json.dump(gompc, f, indent=4, sort_keys=True, ensure_ascii=False)
