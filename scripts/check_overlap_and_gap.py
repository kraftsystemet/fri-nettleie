#!/usr/bin/env python3
# A script to check for overlapping tariff intervals within each tarrif file.
# Also checks for gaps in the intervals.
import os
import dateutil.parser
import yaml

if __name__ == "__main__":
    for filename in os.listdir("tariffer"):
        if filename.endswith(".yml"):
            with open(os.path.join("tariffer", filename), "r") as f:
                data = yaml.safe_load(f)

            # Check overlap between tariffs
            intervals_household = []
            intervals_cabins = []
            intervals_business = []
            for t in data["tariffer"]:
                valid_from = dateutil.parser.parse(t["gyldig_fra"])
                valid_to = dateutil.parser.parse(t.get("gyldig_til", "2099-01-01"))

                if "husholdning" in t["kundegrupper"]:
                    intervals_household.append((valid_from, valid_to))
                if "fritid" in t["kundegrupper"]:
                    intervals_cabins.append((valid_from, valid_to))
                if "liten_næring" in t["kundegrupper"]:
                    intervals_business.append((valid_from, valid_to))

            for type, intervals in [
                ("household", intervals_household),
                ("cabins", intervals_cabins),
                ("business", intervals_business),
            ]:
                intervals.sort(key=lambda x: x[0])

                for i in range(len(intervals) - 1):
                    if intervals[i + 1][0] < intervals[i][1]:
                        print(
                            f"Overlap between {intervals[i][0]} and {intervals[i + 1][0]} in {filename} for {type}"
                        )
                    if intervals[i + 1][0] > intervals[i][1]:
                        print(
                            f"Gap between {intervals[i][1]} and {intervals[i + 1][0]} in {filename} for {type}"
                        )
