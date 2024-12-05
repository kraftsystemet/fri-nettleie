import requests
import cache
import csv

from elhub import get_mga_name, get_parties

if __name__ == "__main__":
    parties = get_parties()
    mgas = get_mga_name()

    with open(
        "./referanse-data/elhub/party_gln_eic_mga.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["GRID_OWNER", "GLN", "GRID_AREA_ID", "GRID_AREA_NAME"])

        for party in parties:
            gln = party["id"]
            name = party["attributes"]["name"]
            grid_areas = party["relationships"]["grid-area"]["data"]

            for grid_area in grid_areas:
                grid_area_names = [
                    mga["attributes"]
                    for mga in mgas["data"]
                    if mga["id"] == grid_area["id"]
                ]
                for ga_name in grid_area_names:
                    writer.writerow([name, gln, grid_area["id"], ga_name["name"]])
