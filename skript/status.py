#!/usr/bin/env python3
# Skriver en liste over norske netteiere til stdout

import json

def load_dsos():

    with open('./referanse-data/esett/metering_grid_areas.json', 'r') as file:
        mgas = json.load(file)

    dsos = {}

    for mga in mgas:
        if mga['mgaType'] != 'DISTRIBUTION':
            continue

        if mga['dsoName'] in dsos:
            continue

        dsos[mga['dsoName']] = mga["dsoCode"]
    return dsos

def print_status():

    dsos = load_dsos()

    print("")
    for dso in sorted(list(dsos.keys())):
        print(f"- [ ] {dso} - {dsos[dso]}")
    print("")

if __name__ == '__main__':

    with open("README.md", "r") as f:
        readme = f.readlines()

    in_status = False
    for line in readme:

        if not in_status:
            print(line, end="")

            if line.startswith("<!-- statusstart"):
                in_status = True
                print_status()

        else: # in status
            if line.startswith("<!-- statusstop"):
                print(line, end="")
                in_status = False
