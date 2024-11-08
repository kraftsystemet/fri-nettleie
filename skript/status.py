#!/usr/bin/env python3
# Skriver en liste over norske netteiere til stdout

import json
import yaml
import os

def load_dsos():

    with open('./referanse-data/elhub/grid_owners.json', 'r') as file:
        gos = json.load(file)

    go_org = {}
    for go in gos:
        go_org[go['gln']] = go["organisationNumber"]

    with open('./referanse-data/nve/konsesjonar.json', 'r') as file:
        konsesjoner = set([k["organisasjonsnr"] for k in json.load(file)])

    with open('./referanse-data/esett/metering_grid_areas.json', 'r') as file:
        mgas = json.load(file)

    dsos = {}

    for mga in mgas:
        if mga['mgaType'] != 'DISTRIBUTION':
            continue

        org = go_org[mga['dsoCode']]

        if org not in konsesjoner:
            continue

        if mga['dsoName'] in dsos:
            continue

        dsos[mga['dsoName']] = mga["dsoCode"]
    return dsos

def load_status():
    files = [f for f in os.listdir("./tariffer") if f.endswith(".yml")]

    status = {}
    for f in files:
        with open("./tariffer/" + f, "r") as file:
            data = yaml.safe_load(file)

        status[data["gln"]] = data["sist_oppdatert"]

    return status

def print_status():

    dsos = load_dsos()
    dso_status = load_status()

    print("")
    for dso in sorted(list(dsos.keys())):
        gln = dsos[dso]
        status = 'x' if gln in dso_status else ' '
        details = f' - Sist oppdatert `{dso_status[gln].strftime("%Y-%m-%d")}`' if gln in dso_status else ''

        print(f"- [{status}] {dso} - {gln}{details}")
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
