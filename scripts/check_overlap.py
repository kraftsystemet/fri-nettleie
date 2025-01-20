#!/usr/bin/env python3
# A script to check for overlapping tariff intervals within each tarrif file.
import os
import dateutil.parser
import yaml

if __name__ == "__main__":
    for filename in os.listdir("tariffer"):
        if filename.endswith(".yml"):
            with open(os.path.join("tariffer", filename), "r") as f:
                data = yaml.safe_load(f)

            # Check overlap between tariffs
            intervals = []
            for t in data["tariffer"]:
                valid_from = dateutil.parser.parse(t["gyldig_fra"])
                valid_to = dateutil.parser.parse(t.get("gyldig_til", "2099-01-01"))

                intervals.append((valid_from, valid_to))

            intervals.sort(key=lambda x: x[0])

            for i in range(len(intervals) - 1):
                if intervals[i + 1][0] < intervals[i][1]:
                    print(
                        f"Overlap between {intervals[i][0]} and {intervals[i + 1][0]} in {filename}"
                    )
