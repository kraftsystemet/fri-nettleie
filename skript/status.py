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
            status[gln] = { "data" : data }
            status[gln]["file"] = f

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

def load_go_mp_count():

    total_count = 0
    go_mp_counts = {}

    with open('./referanse-data/elhub/grid_owner_mp_count.json') as file:
        data = json.load(file)

    for go in data:
        if go['mp_count'] == 0:
            continue
        total_count += go['mp_count']
        go_mp_counts[go['gln']] = go['mp_count']

    return total_count, go_mp_counts

def load_total_mp_count():
    with open('./referanse-data/elhub/price_area_mp_count.json') as file:
        pa_mp_counts = json.load(file)

    total_count = 0
    for pa in pa_mp_counts:
        total_count += pa['mp_count']

    return total_count

def print_status():

    dsos = load_dsos()
    dso_status = load_status()

    ignores = load_ignores()
    for dso in list(dsos.keys()):
        if dso in ignores:
            eprint(f"Ignoring {dso} - {dsos[dso]}")
            dsos.pop(dso)

    go_total_mp_count, go_mp_counts = load_go_mp_count()
    total_mp_count = load_total_mp_count()

    # distribute the difference between the total mp count and the grid owner count on the remaining dsos
    mp_count_diff = total_mp_count - go_total_mp_count
    default_mp_count = math.floor(mp_count_diff / (len(dsos)-len(go_mp_counts)))

    collected_count = 0
    for dso in list(dso_status.keys()):
        collected_count += go_mp_counts.get(dso, default_mp_count)

    print("")
    print(f"Vi har samlet data for {len(dso_status)} av {len(dsos)} netteiere 🥳!")
    print("")
    print(f"Dette dekker ~{round(( collected_count / total_mp_count ) * 100, 1)}% ({collected_count} av {total_mp_count}) av private husholdninger* 🎉.")
    print("")
    print("""<table>
    <tr>
        <th>Navn</th>
        <th>GLN</th>
        <th>Antall*</th>
        <th>Oppdatert</th>
        <th>Handling</th>
    </tr>""")

    for dso in dict(sorted(dsos.items(), key=lambda x:x[1])):

        gln = dso

        # fjerne " (tidligere xxx)" i netteiernavn ? .split('(')[0].strip()
        name = dsos[dso]
        antall_mp = go_mp_counts.get(gln, default_mp_count)

        oppdatert = ''
        status = ''
        inspect_link = ''
        yaml_link = ''

        data = {
            "netteier": name,
            "gln": [gln]
        }

        if gln in dso_status:
            data = dso_status[gln]['data']
            file = dso_status[gln]['file']

            sist_oppdatert = data["sist_oppdatert"]
            if isinstance(sist_oppdatert, datetime):
                sist_oppdatert = sist_oppdatert.strftime("%Y-%m-%d")
            oppdatert = f'<code>{sist_oppdatert}</code>'

            status = ' ✅'

            inspect_href = f"https://kraftsystemet.no/fri-nettleie/tariffer/{file.replace('.yml', '.html')}"
            inspect_link = f'<a href="{inspect_href}" title="Se på tariffen for {name}" target="_blank">🔍</a>'
            yaml_link = f'<a href="./tariffer/{file}" title="Se dataene for {name} i YAML-format" target="_blank">📄</a>'

        edit_url = f"https://kraftsystemet.no/fri-nettleie/innsamler/?data={atob(json.dumps(data, default=json_serial))}"

        print("<tr>")
        print(f"  <td>{name}{status}</td>")
        print(f"  <td>{gln}</td>")
        print(f"  <td><em>{antall_mp}{ '**' if antall_mp == default_mp_count else '' }</em></td>")
        print(f"  <td>{oppdatert}</td>")
        print(f"  <td>")
        print(f"    <a href='{edit_url}' title='Samle inn data for {name}' target='_blank'>✏️</a>")
        if inspect_link: print(f"    {inspect_link}")
        if yaml_link: print(f"    {yaml_link}")
        print(f"  </td>")
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
