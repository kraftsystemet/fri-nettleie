#!/usr/bin/env python3
# Sjekk innsamlede /tariffer mot referanse-data/nve/tariffer/privat
#
# Bruker data fra Elhub til å mappe gln til organisasjonsnummer.
#
# Sjekken mot NVE sine data er litt "fuzzy". Det er en veldig forenklet sjekk på flere måter.
#
#   * vi avrunder verdier på begge sider - energiledd til to desimaler, fastledd til hel krone
#   * vi sjekker kun om vi finner de samme energiledd-prisene på begge sider, uten vurdering av når prisene er
#   * energiledd i NVE innholder ca 50/50 enova-avgift og ikke. Sjekken for energiledd er derfor +-1 øre
#
# Sjekken håndterer også konsesjonærer med flere GLN dårlig, siden NVE-data er på organisasjonsnummer, ikke GLN.
#
# Usage: ./scripts/qa_nve.py

import cache

import os
import yaml
import json
from datetime import datetime, timedelta
import dateutil.parser

# gln: org
GRID_OWNERS = {}


def org_from_gln(gln):
    global GRID_OWNERS

    if len(GRID_OWNERS.keys()) == 0:
        with open("./referanse-data/elhub/grid_owners.json", "r") as f:
            gos = json.load(f)
            for go in gos:
                GRID_OWNERS[go["gln"]] = go["organisationNumber"]

    return GRID_OWNERS.get(gln)


def load_collected_tariffs():
    """
    Loads the collected tariffs on a format that can be compared to the ones collected from NVE
    """
    files = [f for f in os.listdir("./tariffer") if f.endswith(".yml")]

    tariffs = {}

    for f in files:
        with open("./tariffer/" + f, "r") as file:
            data = yaml.safe_load(file)
            tariff = None
            for t in data["tariffer"]:
                # TODO better time sync between collected and NVE
                if dateutil.parser.parse(
                    t["gyldig_fra"]
                ) <= datetime.today() + timedelta(days=14) and dateutil.parser.parse(
                    t.get("gyldig_til", "2099-01-01")
                ) > datetime.today() + timedelta(days=14):
                    energiledd = []
                    energiledd.append(t["energiledd"]["grunnpris"])

                    for u in t["energiledd"].get("unntak", []):
                        energiledd.append(u["pris"])

                    energiledd.sort()
                    energiledd = [round(p, 2) for p in energiledd]

                    tariff = {
                        "name": data["netteier"],
                        "data": {
                            "energiledd": energiledd,
                            "terskler": {
                                t["terskel"]: round(t["pris"])
                                for t in t["fastledd"]["terskler"]
                            },
                        },
                    }

            if tariff is None:
                print(f"Could not find current tariff for {f}")
                continue

            for gln in data["gln"]:
                org = org_from_gln(gln)
                if org is None:
                    print(f"Could not find org for gln {gln}")
                    continue

                if org not in tariffs:
                    tariffs[org] = tariff

    return tariffs


def load_nve_tariffs():
    files = [
        f
        for f in os.listdir("./referanse-data/nve/tariffer/privat")
        if f.endswith(".yml")
    ]
    tariffs = {}
    for f in files:
        with open("./referanse-data/nve/tariffer/privat/" + f, "r") as file:
            data = yaml.safe_load(file)
            tariffs[data["org"]] = {
                "energiledd": sorted([round(p, 2) for p in data["energiledd"]]),
                "terskler": {t["terskel"]: round(t["pris"]) for t in data["terskler"]},
            }

    return tariffs


def energiledd_equal(collected, nve):
    if len(collected) != len(nve):
        return False

    for i in range(len(collected)):
        # we are doing a fuzzy match here since NVE has some prices with Enova tarrifs
        # and some without

        if abs(collected[i] - nve[i]) > 1:
            return False

    return True


if __name__ == "__main__":
    collected_tariffs = load_collected_tariffs()
    nve_tariffs = load_nve_tariffs()

    for org in collected_tariffs:
        name = collected_tariffs[org]["name"]

        if org not in nve_tariffs:
            print(f"{name} - {org} - Missing in NVE data")
            continue

        ct = collected_tariffs[org]["data"]
        cte = ct["energiledd"]
        ctt = ct["terskler"]

        nt = nve_tariffs[org]
        nte = nt["energiledd"]
        ntt = nt["terskler"]

        if not energiledd_equal(cte, nte):
            print(f"{name} - {org} - Energiledd not the same: {cte} != {nte}")

        if ctt != ntt:
            print(f"{name} - {org} - Fastledd is not the same")

            all_terskler = list(ctt.keys())
            all_terskler.extend(list(ntt.keys()))
            all_terskler = sorted(list(set(all_terskler)))
            for t in all_terskler:
                print(
                    f"    {t} - Collected: {ctt.get(t, '  ')} - NVE: {ntt.get(t, '    ')}"
                )
