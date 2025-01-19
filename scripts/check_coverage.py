#!/usr/bin/env python3
# Checks the coverage of collected GLNs.
# Uses eSett data for reference.
import yaml
import json
import os


def get_collected_glns():
    files = [f for f in os.listdir("./tariffer") if f.endswith(".yml")]

    glns = []
    for f in files:
        with open("./tariffer/" + f, "r") as file:
            data = yaml.safe_load(file)

        glns.extend(data["gln"])

    return set(glns)


def get_ignored_glns():
    glns = []
    with open("./.statusignore", "r") as file:
        for line in file.readlines():
            clean_line = line.strip().split("#")[0]
            if clean_line.isdigit() and len(clean_line) == 13:
                glns.append(clean_line)
    return set(glns)


def get_grid_owners():
    glns = []
    with open("./referanse-data/esett/metering_grid_areas.json", "r") as file:
        mgas = json.load(file)
        for mga in mgas:
            glns.append(mga["dsoCode"])

    return set(glns)


if __name__ == "__main__":
    collected = get_collected_glns()
    ignored = get_ignored_glns()
    existing = get_grid_owners()

    print(f"Collected: {len(collected)}")
    print(f"Ignored: {len(ignored)}")
    print(f"Existing: {len(existing)}")

    missing = existing - (ignored | collected)
    print(f"Missing (existing but not ignored/collected): {len(missing)}")
    for gln in missing:
        print(f"Missing: {gln}")

    non_existing = (collected | ignored) - existing
    print(f"Non-existing (collected or ignored but not existing): {len(non_existing)}")
    for gln in non_existing:
        print(f"Non-existing: {gln}")
