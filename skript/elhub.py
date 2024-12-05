import requests

def get_grid_owner_data():
    url = "https://api.elhub.no/energy-data/v0/parties"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    parties = response.json()

    gos = []
    for party in parties["data"]:
        if "GridOwner" in party["attributes"]["partyTypes"]:
            gos.append(
                {
                    "name": party["attributes"]["name"],
                    "gln": party["attributes"]["gln"],
                    "organisationNumber": party["attributes"]["organisationNumber"],
                }
            )

    gos.sort(key=lambda x: x["name"])

    return gos


def get_mga_name():
    """
    Returns a set of grid area ids and their name
    """

    url = "https://api.elhub.no/energy-data/v0/grid-areas"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    mgas = response.json()

    return mgas


def get_parties():
    """
    Returns a set of GLNs, their attributes and relationships (MGAs)
    """

    url = "https://api.elhub.no/energy-data/v0/parties"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    parties = response.json()["data"]

    for p in reversed(range(len(parties))):
        if not "GridOwner" in parties[p]["attributes"]["partyTypes"]:
            parties.pop(p)
            continue

    return parties
