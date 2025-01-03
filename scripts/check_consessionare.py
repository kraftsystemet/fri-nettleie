#!/usr/bin/env python3
# A script to check if Elhub grid owners are NVE consessionares

import cache
import elhub
import esett
import nve
import sys

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

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if __name__ == "__main__":
    grid_owners = elhub.get_grid_owner_data()
    go_org = { go['gln'] : go['organisationNumber'] for go in grid_owners }

    active_dsos_by_name = esett.get_dsos()
    active_dsos = {d['dsoCode']: d['dsoName'] for d in active_dsos_by_name.values()}

    consessionares = nve.get_consessionares()

    nve_has_tarrif_data = nve.get_konsesjonarer("2024-11-01").keys()

    ignores = load_ignores()

    for gln in active_dsos.keys():

        name = active_dsos[gln]
        if gln not in go_org:
            print(f"{gln} - {name} not found in Elhub Grid Owner Data")
            continue

        org = go_org[gln]

        if gln not in active_dsos:
            eprint(f"{gln} - {org} - {name} is not an active DSO in eSett")
            continue

        if gln in ignores:
            eprint(f"{gln} - {org} - {name} is ignored")
            continue

        if org in consessionares:
            eprint(f"{gln} - {org} - {name} is a consessionare")
        else:
            print(f"{gln} - {org} - {name} is NOT a consessionare")

        if org in nve_has_tarrif_data:
            eprint(f"{gln} - {org} - {name} has tarrif data")
        else:
            print(f"{gln} - {org} - {name} does NOT have tarrif data")
