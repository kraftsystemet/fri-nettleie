#!/usr/bin/env python3
# Download and niceify data from Elhub api

import json
from elhub import get_grid_owner_data
import cache

if __name__ == "__main__":
    with open("./referanse-data/elhub/grid_owners.json", "w") as f:
        json.dump(
            get_grid_owner_data(), f, indent=4, sort_keys=True, ensure_ascii=False
        )
