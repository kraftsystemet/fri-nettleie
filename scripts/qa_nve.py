#!/usr/bin/env python3
# Sjekk innsamlede verdier mot NVE referanse-data
#
# Usage: ./scripts/qa_nve.py

import cache

import sys
import os
import nve
import elhub
import yaml
import json
from datetime import datetime, timedelta
import dateutil.parser

# gln: org
GRID_OWNERS = {}

# fmt: off
KNOWN_ERRORS = {
    "979399901": ["fastledd"],  # Vestmar har avrundingfeil i NVE/på sine sider
    "924862602": ["fastledd"],  # DE Nett har enova-avgift og mangler et fastledd i NVE sine data
    "971589752": ["energiledd","fastledd"], # Hallingdal/Føie har endel rot i sine NVE data
    "923789324": ["energiledd"], # Haringnett rett og slett bare feil energiledd hos NVE
    "924527994": ["fastledd"], # Breheim har enova-avgift og feil avrunding på fastledd i NVE sine data
    "924330678": ["energiledd", "fastledd"], # SuNett våre priser er bekreftet på epost. Fastledd er vanskelig ref issue #4
    "980824586": ["fastledd"], # Nordvestnett har enova-avgift og feil i første fastledd i NVE sine data
    "923819177" : ["fastledd"], # S-NETT har enova-avgift og rot på fastledd i NVE sine data
    "925336637" : ["fastledd"], # Alut avvik på fastledd pga terskel_inkludert
    "986347801" : ["fastledd"], # Elmea rot i NVE sine fastledd
    "882783022" : ["energiledd"], # Etna sine priser har elavgift host NVE
}
# fmt: on


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
            if not (org in KNOWN_ERRORS and "energiledd" in KNOWN_ERRORS[org]):
                print(f"{name} - {org} - Energiledd not the same: {cte} != {nte}")

        if ctt != ntt:
            if not (org in KNOWN_ERRORS and "fastledd" in KNOWN_ERRORS[org]):
                print(f"{name} - {org} - Fastledd is not the same")

                all_terskler = list(ctt.keys())
                all_terskler.extend(list(ntt.keys()))
                all_terskler = sorted(list(set(all_terskler)))
                for t in all_terskler:
                    print(
                        f"    {t} - Collected: {ctt.get(t, '  ')} - NVE: {ntt.get(t, '    ')}"
                    )
