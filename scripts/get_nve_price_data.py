#!/usr/bin/env python3
# Dump tarrifs from NVE API in a simplified format.

import cache

import sys
import nve
import yaml
import dataclasses
import holidays
from datetime import date, datetime, timedelta

HOLIDAYS = holidays.Norway()


def slugify(s):
    return (
        s.lower()
        .replace(" ", "-")
        .replace("æ", "ae")
        .replace("ø", "oe")
        .replace("å", "a")
    )


if __name__ == "__main__":
    dt = date.today() + timedelta(days=14)

    while True:
        if dt.weekday() in [0, 1, 2, 3, 4] and dt not in HOLIDAYS:
            break
        dt += timedelta(days=1)

    weekday_date = dt.strftime("%Y-%m-%d")

    while True:
        if dt.weekday() == 6:
            break
        dt += timedelta(days=1)

    sunday_date = dt.strftime("%Y-%m-%d")

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_directory>")
        sys.exit(1)

    output_dir = sys.argv[1]

    consessionaires = nve.get_konsesjonarer(weekday_date)

    for org, c in consessionaires.items():
        print(f"{org}: {c}")
        nve_tariff = nve.get_summary([weekday_date, sunday_date], c.fylker, c.org)
        file_name = f"{output_dir}/{slugify(c.navn)}.yml".replace("//", "/")
        print(file_name)
        nve_tariff.update(dataclasses.asdict(c))
        with open(file_name, "w") as f:
            yaml.dump(nve_tariff, f)

    with open(f"{output_dir}/README.md".replace("//", "/"), "w") as f:
        f.write(
            f"""
# Tariffer er sist oppdatert {datetime.now().strftime("%Y-%m-%d %H:%M")}

Tariffene gjelder for {weekday_date} og {sunday_date}.
"""
        )
