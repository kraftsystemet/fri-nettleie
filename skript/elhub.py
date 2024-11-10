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

    return gos
