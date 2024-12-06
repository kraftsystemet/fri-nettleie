import requests

def get_grid_owner_data():
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

    gos.sort(key=lambda x: x['name'])

    return gos

def get_metering_point_count():
    url = 'https://api.elhub.no/energy-data/v0/grid-areas'
    headers = {'accept': 'application/json'}
    params = {
        'dataset': 'CONSUMPTION_PER_GROUP_MGA_HOUR',
        'startDate': '2024-11-01T00:00:00+01:00',
        'endDate': '2024-11-01T00:01:00+01:00',
        'consumptionGroup': 'household'
    }

    response = requests.get(url, params=params, headers=headers)

    grid_areas = response.json()['data']
    go_mp_counts = {}
    for grid_area in grid_areas:
        gln = grid_area['relationships']['grid-owner']['data']['id']
        if gln not in go_mp_counts:
            go_mp_counts[gln] = 0
        if len(grid_area['attributes']['consumptionPerGroupMgaHour']) > 0:
            go_mp_counts[gln] += grid_area['attributes']['consumptionPerGroupMgaHour'][0]['meteringPointCount']

    return go_mp_counts
