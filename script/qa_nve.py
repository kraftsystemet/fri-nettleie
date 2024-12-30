#!/usr/bin/env python3
# Sjekk innsamlede verdier mot NVE sitt api
#
# Usage: ./script/qa_nve.py tariffer/<netteier>.yml

import cache

import sys
import nve
import elhub
import yaml

if __name__ == '__main__':

    # Dato å hente data fra NVE
    dato = "2024-11-01"

    if len(sys.argv) != 2:
        print("Usage: python script.py <yml_file>")
        sys.exit(1)

    tariff_fil = sys.argv[1]

    with open(tariff_fil, 'r') as f:
        data = yaml.safe_load(f)

    tariffer = data["tariffer"]

    for gln in data["gln"]:
        print(f"\nSjekker tariffer for {gln} - {data['netteier']}")

        gos = { g["gln"] : g["organisationNumber"] for g in elhub.get_grid_owner_data() }

        if gln not in gos:
            print(f'Gln {gln} not found in Elhub Grid Owner Data')
            sys.exit(1)

        org = gos[gln]
        print("Organisasjonsnummer:", org)

        konsesjonarer = nve.get_konsesjonarer_fylker(dato)

        if org not in konsesjonarer:
            print(f'Organisasjonsnummer {org} not found in NVE data')
            sys.exit(1)

        fylker = konsesjonarer[org]

        nve_tariff = nve.get_oppsummering(dato, fylker, org)


        for t in tariffer:
            if t["energiledd"]["grunnpris"] not in nve_tariff["priser"]:
                print(f"Tariff {t['id']} har ikke-eksisterende grunnpris {t['energiledd']['grunnpris']} - NVE => {nve_tariff['priser']}")
            else:
                print("Grunnpris OK")

            if t["fastledd"]["terskler"] != nve_tariff["terskler"]:
                print(f"Tariff {t['id']} har ikke-eksisterende terskler {t['fastledd']['terskler']} - NVE => {nve_tariff['terskler']}")
            else:
                print("Terskler OK")
