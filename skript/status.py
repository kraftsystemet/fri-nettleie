#!/usr/bin/env python3
# Skriver en liste over norske netteiere til stdout

import json
import yaml
import os
import base64
from datetime import date, datetime
import sys
import csv
import math

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


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
        if mga['dsoCode'] in dsos:
            continue

        dsos[mga["dsoCode"]] = mga['dsoName']
    return dsos

def load_status():
    files = [f for f in os.listdir("./tariffer") if f.endswith(".yml")]

    status = {}
    for f in files:
        with open("./tariffer/" + f, "r") as file:
            data = yaml.safe_load(file)

        for gln in data["gln"]:
            status[gln] = data

    return status

def load_ignores():
    """
    Yield all GLNs in .statusignore

    .statusignore is expected to contain one GLN per line. Lines can be
    commented out with a `#` and empty lines are ignored.
    """
    ignores = []
    with open('./.statusignore', 'r') as file:
        for line in file.readlines():
            l = line.strip().split('#')[0]
            if l.isdigit() and len(l) == 13:
                ignores.append(l)

    return ignores

def load_mp_count():

    total_count = 0
    mp_counts = {}

    with open('./referanse-data/elhub/grid_owner_mp_count.json') as file:
        go_mp_counts = json.load(file)

    for go in go_mp_counts:
        total_count += go['mp_count']
        mp_counts[go['gln']] = go['mp_count']

    return total_count, mp_counts


def print_status():

    dsos = load_dsos()
    dso_status = load_status()

    ignores = load_ignores()
    for dso in list(dsos.keys()):
        if dso in ignores:
            eprint(f"Ignoring {dso} - {dsos[dso]}")
            dsos.pop(dso)

    total_count, mp_counts = load_mp_count()
    collected_count = 0
    for dso in list(dso_status.keys()):
        if dso in mp_counts:
            collected_count += mp_counts[dso]

    print("")
    print(f"Vi har samlet data for {len(dso_status)} av {len(dsos)} netteiere 🥳!")
    print("")
    print(f"Dette dekker ~{math.floor(( collected_count / total_count ) * 100)}% ({collected_count}) av private husholdninger* 🎉.")
    print("")
    print("""<table>
    <tr>
        <th>Navn</th>
        <th>GLN</th>
        <th>Antall MP*</th>
        <th>Oppdatert</th>
        <th>Handling</th>
    </tr>""")

    for dso in dict(sorted(dsos.items(), key=lambda x:x[1])):

        gln = dso

        # fjerne " (tidligere xxx)" i netteiernavn ? .split('(')[0].strip()
        name = dsos[dso]
        antall_mp = mp_counts.get(gln, 0)

        oppdatert = ''
        status = ''

        data = {
            "netteier": name,
            "gln": [gln]
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
        print(f"    <td>{name}{status}</td>")
        print(f"    <td>{gln}</td>")
        print(f"    <td>{'<code>' + str(antall_mp) + '</code>*' if antall_mp > 0 else ''}</td>")
        print(f"    <td>{oppdatert}</td>")
        print(f"    <td><a href='{edit_url}' title='Samle inn data for {name}' target='_blank'>✏️</a></td>")
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
