#!/usr/bin/env python3
# Downloads data from eSett APIs faciliate status reporting

import requests
import json

import cache
import esett


if __name__ == "__main__":
    dsos = esett.get_dsos()
    mgas = esett.get_mgas()

    with open("./referanse-data/esett/metering_grid_areas.json", "w") as f:
        for m in range(len(mgas)):
            mgas[m]["dsoCode"] = dsos[mgas[m]["dsoName"]]["dsoCode"]
            mgas[m]["dsoCodingScheme"] = dsos[mgas[m]["dsoName"]]["codingScheme"]

        json.dump(mgas, f, indent=4, sort_keys=True, ensure_ascii=False)
