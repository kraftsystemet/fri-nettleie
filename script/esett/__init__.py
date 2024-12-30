import requests
def get_mgas():
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


    mgas.sort(key=lambda x: x['dsoName'])

    return mgas

def get_dsos():
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
