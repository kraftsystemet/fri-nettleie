#!/usr/bin/env python3
# Dump tariffer fra NVE sitt api

import cache

import sys
import nve
import yaml
import dataclasses

def slugify(s):
    return s.lower().replace(" ", "-").replace("æ", "ae").replace("ø", "oe").replace("å", "a")

if __name__ == '__main__':

    # Dato å hente data fra NVE
    dato = "2024-12-31"

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_directory>")
        sys.exit(1)

    output_dir = sys.argv[1]

    konsesjonarer = nve.get_konsesjonarer(dato)

    for org, k in konsesjonarer.items():
        print(f"{org}: {k}")
        nve_tariff = nve.get_oppsummering(dato, k.fylker, k.org)
        file_name = f"{output_dir}/{slugify(k.navn)}.yml".replace("//", "/")
        print(file_name)
        nve_tariff.update(dataclasses.asdict(k))
        nve_tariff["dato"] = dato
        with open(file_name, 'w') as f:
            yaml.dump(
                nve_tariff
            , f)
