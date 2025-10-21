#!/usr/bin/env python3
# A script to check that tariff levels are strictly increasing
import os
import yaml

if __name__ == "__main__":
    for filename in os.listdir("tariffer"):
        if filename.endswith(".yml"):
            with open(os.path.join("tariffer", filename), "r") as f:
                data = yaml.safe_load(f)

            for t in data["tariffer"]:
                valid_from = t["gyldig_fra"]
                levels = t["fastledd"]["terskler"]

                levels.sort(key=lambda x: x["terskel"])

                for i in range(len(levels) - 1):
                    level = levels[i]["terskel"]
                    next_level = levels[i + 1]["terskel"]

                    price = levels[i]["pris"]
                    next_price = levels[i + 1]["pris"]

                    if next_level <= level:
                        print(
                            f"Level {next_level} in {filename} - {valid_from} is lower or equal to level {level}"
                        )

                    if next_price < price:
                        print(
                            f"Price {next_price} on level {next_level} in {filename} - {valid_from} is lower or equal to price {price} on level {level}"
                        )
