#!/usr/bin/env python3
# Downloads data from eSett APIs faciliate status reporting

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

def get_esett_mgas():
    """
    Return a set of Norwegian distribution system operators from eSett API
    """

    url = 'https://api.opendata.esett.com/EXP03/MeteringGridAreas'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    mgas = response.json()

    for m in reversed(range(len(mgas))):
        if mgas[m]['country'] != 'NO':
            mgas.pop(m)
            continue

    return mgas

def get_esett_dsos():
    """
    Return a set of Norwegian distribution system operators from eSett API
    """

    url = 'https://api.opendata.esett.com/EXP01/DistributionSystemOperators?country=NO'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    dsos = {}
    for dso in response.json():

        if dso['dsoName'] in dsos:
            raise ValueError(f"Duplicate dsoName: {dso['dsoName']}")

        dsos[dso['dsoName']] = dso

    return dsos

if __name__ == "__main__":

    dsos = get_esett_dsos()

    with open('./referanse-data/esett/metering_grid_areas.json', 'w') as f:

        mgas = get_esett_mgas()
        for m in range(len(mgas)):
            mgas[m]['dsoCode'] = dsos[mgas[m]['dsoName']]['dsoCode']
            mgas[m]['dsoCodingScheme'] = dsos[mgas[m]['dsoName']]['codingScheme']

        json.dump(mgas, f, indent=4, sort_keys=True)
