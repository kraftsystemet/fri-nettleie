#!/usr/bin/env python3
# Skriver en liste over norske netteiere til stdout

import json
import yaml
import os
import base64
from datetime import date, datetime

# https://stackoverflow.com/a/22238613
def json_serial(obj):

    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.strftime("%Y-%m-%d")
    raise TypeError ("Type %s not serializable" % type(obj))


def atob(s):
    return base64.b64encode(s.encode()).decode()


def btoa(s):
    return base64.b64decode(s).decode()

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

def load_status():
    files = [f for f in os.listdir("./tariffer") if f.endswith(".yml")]

    status = {}
    for f in files:
        with open("./tariffer/" + f, "r") as file:
            data = yaml.safe_load(file)

        status[data["gln"]] = data

    return status

def print_status():

    dsos = load_dsos()
    dso_status = load_status()
    print("")
    print("""<table>
    <tr>
        <th>Navn</th>
        <th>GLN</th>
        <th>Oppdatert</th>
        <th>Handling</th>
    </tr>""")

    for dso in sorted(list(dsos.keys())):
        # fjerne " (tidligere xxx)" i netteiernavn
        navn = dso.split('(')[0].strip()
        gln = dsos[dso]
        oppdatert = ''
        status = ''

        data = {
            "netteier": dso,
            "gln": gln
        }

        if gln in dso_status:
            data = dso_status[gln]

            sist_oppdatert = data["sist_oppdatert"]
            if isinstance(sist_oppdatert, datetime):
                sist_oppdatert = sist_oppdatert.strftime("%Y-%m-%d")
            oppdatert = f'<code>{sist_oppdatert}</code>'

            status = ' ✅'

        edit_url = f"https://kraftsystemet.no/fri-nettleie/innsamler/?data={atob(json.dumps(data, default=json_serial))}"

        # ✏️

        print("<tr>")
        print(f"    <td>{navn}{status}</td>")
        print(f"    <td>{gln}</td>")
        print(f"    <td>{oppdatert}</td>")
        print(f"    <td><a href='{edit_url}' title='Samle inn data for {navn}' target='_blank'>✏️</a></td>")
        print("</tr>")

    print("</table>")
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
