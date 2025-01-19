#!/usr/bin/env python3
# Skriver en liste over norske netteiere til stdout

import json
import yaml
import os
import base64
from datetime import date, datetime
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# https://stackoverflow.com/a/22238613
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.strftime("%Y-%m-%d")
    raise TypeError("Type %s not serializable" % type(obj))


def atob(s):
    return base64.b64encode(s.encode()).decode()


def btoa(s):
    return base64.b64decode(s).decode()


def load_tariffs():
    files = [f for f in os.listdir("./tariffer") if f.endswith(".yml")]

    tariffs = []
    for f in files:
        with open("./tariffer/" + f, "r") as file:
            data = yaml.safe_load(file)
            data.update({"file_name": f})
            tariffs.append(data)

    tariffs.sort(key=lambda x: x["netteier"])

    return tariffs


def print_status():
    tariffs = load_tariffs()

    print("""<table>
    <tr>
        <th>Navn</th>
        <th>GLN</th>
        <th>Oppdatert</th>
        <th>Handling</th>
    </tr>""")

    for tariff in tariffs:
        gln = tariff["gln"]
        name = tariff["netteier"]

        last_updated = tariff["sist_oppdatert"]
        if isinstance(last_updated, datetime):
            last_updated = last_updated.strftime("%Y-%m-%d")

        file_name = tariff["file_name"]
        tariff.pop("file_name")

        inspect_url = f"https://kraftsystemet.no/fri-nettleie/tariffer/{file_name.replace('.yml', '.html')}"
        inspect_link = f'<a href="{inspect_url}" title="Se på tariffen for {name}" target="_blank">🔍</a>'

        yaml_link = f'<a href="./tariffer/{file_name}" title="Se dataene for {name} i YAML-format" target="_blank">📄</a>'

        edit_url = f"https://kraftsystemet.no/fri-nettleie/innsamler/?data={atob(json.dumps(tariff, default=json_serial))}"
        edit_link = f"<a href='{edit_url}' title='Samle inn data for {name}' target='_blank'>✏️</a>"

        print("<tr>")
        print(f"  <td>{name}</td>")
        print(f"  <td>{', '.join(gln)}</td>")
        print(f"  <td>{last_updated}</td>")
        print(f"  <td>\n    {inspect_link}\n    {yaml_link}\n    {edit_link}\n  </td>")
        print("</tr>")

    print("</table>")
    print("")


if __name__ == "__main__":
    with open("README.md", "r") as f:
        readme = f.readlines()

    in_status = False
    for line in readme:
        if not in_status:
            print(line, end="")

            if line.startswith("<!-- statusstart"):
                in_status = True
                print_status()

        else:  # in status
            if line.startswith("<!-- statusstop"):
                print(line, end="")
                in_status = False
