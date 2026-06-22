#!/usr/bin/env python3
# A script to check that energiledd grunnpris is higher than every unntakspris
import os
import yaml

if __name__ == "__main__":
    for filename in os.listdir("tariffer"):
        if filename.endswith(".yml"):
            path = os.path.join("tariffer", filename)
            with open(path, "r") as f:
                data = yaml.safe_load(f)
            for t in data.get("tariffer", []):
                energiledd = t.get("energiledd")
                if not energiledd:
                    continue
                grunnpris = energiledd.get("grunnpris")
                unntak = energiledd.get("unntak", [])
                if grunnpris is None or not isinstance(unntak, list):
                    continue
                for u in unntak:
                    unntakspris = u.get("pris")
                    if unntakspris is not None and grunnpris > unntakspris:
                        print(
                            f"grunnpris ({grunnpris}) is HIGHER than unntakspris ({unntakspris}) "
                            f"in {filename}, tariff starting {t.get('gyldig_fra', '?')} "
                            f"for unntak '{u.get('navn', '?')}'"
                        )
