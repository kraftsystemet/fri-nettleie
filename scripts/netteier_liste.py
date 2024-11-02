#!/usr/bin/env python3
# Skriver en liste over norske netteiere til stdout

import requests

url = 'https://api.opendata.esett.com/EXP03/MeteringGridAreas'
headers = {'accept': 'application/json'}

response = requests.get(url, headers=headers)

data = response.json()

dsos = set()

for mga in data:
    if mga['country'] != 'NO':
        continue
    if mga["mgaType"] != 'DISTRIBUTION':
        continue

    dsos.add(mga['dsoName'])

for dso in sorted(list(dsos)):
    print(f"- [ ] {dso}")