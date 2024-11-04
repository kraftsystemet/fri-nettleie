#!/usr/bin/env python3
# Download and niceify data from Elhub api

import requests
import json

# Cache is used to do local iterations on scripts w/o putting load on the external APIs.
# Clear cache with `rm -rf ~/.cache/raftsystemet-fri-nettleie`
import requests_cache
requests_cache.install_cache(
    'kraftsystemet-fri-nettleie',
    backend='filesystem',
    use_cache_dir=True
)




if __name__ == '__main__':

    url = 'https://api.elhub.no/energy-data/v0/parties'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    parties = response.json()

    gos = []
    for party in parties['data']:
        if 'GridOwner' in party['attributes']['partyTypes']:
            gos.append({
                'name': party['attributes']['name'],
                'gln': party['attributes']['gln'],
                'organisationNumber': party['attributes']['organisationNumber']
            })

    with open('./referanse-data/elhub/grid_owners.json', 'w') as f:
        json.dump(gos, f, indent=4, sort_keys=True)
