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


def usage():
    print(f"Usage: {sys.argv[0]} <type> <output_directory>")


if __name__ == "__main__":
    dt = date.today() + timedelta(days=14)

    while True:
        if dt.weekday() in [0, 1, 2, 3, 4] and dt not in HOLIDAYS:
            break
        dt += timedelta(days=1)

    weekday_date = dt.strftime("%Y-%m-%d")

    while True:
        if dt.weekday() == 4:
            break
        dt += timedelta(days=1)

    friday_date = dt.strftime("%Y-%m-%d")

    while True:
        if dt.weekday() == 6:
            break
        dt += timedelta(days=1)

    sunday_date = dt.strftime("%Y-%m-%d")

    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    dates = sorted(list(set([weekday_date, friday_date, sunday_date])))

    print(f"Getting data for: {', '.join(dates)}")

    type = sys.argv[1]

    if type not in ["private", "industry"]:
        usage()
        print("Type must be 'private' or 'industry'")
        sys.exit(1)

    output_dir = sys.argv[2]
    tariffGroup = (
        nve.TariffGroup.Household if type == "private" else nve.TariffGroup.Industry
    )

    consessionaires = nve.get_konsesjonarer(weekday_date)

    for org, c in consessionaires.items():
        print(f"{org}: {c}")
        nve_tariff = nve.get_summary(dates, tariffGroup, c.fylker, c.org)
        file_name = f"{output_dir}/{slugify(c.navn)}.yml".replace("//", "/")
        print(file_name)
        nve_tariff.update(dataclasses.asdict(c))
        with open(file_name, "w") as f:
            yaml.dump(nve_tariff, f)

    with open(f"{output_dir}/README.md".replace("//", "/"), "w") as f:
        f.write(
            f"""
# Tariffer er sist oppdatert {datetime.now().strftime("%Y-%m-%d %H:%M")}

Tariffene gjelder for: {", ".join(dates)}.
"""
        )
