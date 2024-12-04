import requests
import json
import requests_cache
import csv

requests_cache.install_cache(
    'kraftsystemet-fri-nettleie',
    backend='filesystem',
    use_cache_dir=True
)

# Uses Elhub APIs

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
    
def get_mga_name():
    """
    Returns a set of grid area ids and their name
    """

    url = "https://api.elhub.no/energy-data/v0/grid-areas"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    mgas = response.json()

    return mgas

if __name__ == "__main__":
    parties = get_parties()
    mgas = get_mga_name()

    with open("./referanse-data/elhub/party_gln_eic_mga.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["PARTY_NAME, GLN, GRID_AREA_ID"])
        
        for party in parties:
            gln = party["id"]
            name = party["attributes"]["name"]
            grid_areas = party["relationships"]["grid-area"]["data"]

            for grid_area in grid_areas:
                grid_area_names = [mga["attributes"] for mga in mgas["data"] if mga["id"] == grid_area["id"]]
                for ga_name in grid_area_names:
                    writer.writerow([name, gln, grid_area["id"], ga_name["name"]])

