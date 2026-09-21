#!/usr/bin/env python3
"""Sammenlign en ny tariffperiode med forrige periode for de samme kundegruppene.

Bruk (kjør fra repoets rot):

  python3 .../sammenlign_forrige.py tariffer/selskap.yml --fra 2026-10-01

Dette er en plausibilitetssjekk, ikke en fasit. Store endringer er ikke feil i seg selv, men
de må kunne forklares av kilden. Skriptet skriver ADVARSEL for hver ting som må forklares i
rapporten, og avslutter alltid med kode 0. En ADVARSEL du ikke kan forklare fra kilden, er
grunn til å dobbeltsjekke transkriberingen.

Advarsler for:
  * endring i en pris på mer enn 30 % (opp eller ned)
  * en pris som synker
  * færre trinn i fastleddet enn forrige periode
  * andre terskelgrenser enn forrige periode
  * andre kundegrupper enn forrige periode
"""

import argparse
import sys
from decimal import Decimal
from pathlib import Path

import yaml

GRENSE = Decimal("0.30")


def pris_liste(periode: dict) -> dict[str, Decimal]:
    """Alle priser i en periode med et lesbart navn."""
    ut = {"energiledd.grunnpris": Decimal(str(periode["energiledd"]["grunnpris"]))}
    for u in periode["energiledd"].get("unntak") or []:
        ut[f"energiledd.unntak[{u['navn']}]"] = Decimal(str(u["pris"]))
    for t in periode["fastledd"]["terskler"]:
        ut[f"fastledd.terskel[{t['terskel']}]"] = Decimal(str(t["pris"]))
    return ut


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("yaml_fil")
    p.add_argument("--fra", required=True, help="gyldig_fra for den nye perioden")
    args = p.parse_args()

    data = yaml.safe_load(Path(args.yaml_fil).read_text(encoding="utf-8"))
    alle = data["tariffer"]
    nye = [t for t in alle if str(t["gyldig_fra"]) == args.fra]
    if not nye:
        sys.exit(f"STOPP: fant ingen tariffperiode med gyldig_fra {args.fra}.")

    advarsler = 0
    for ny in nye:
        grupper = set(ny["kundegrupper"])
        # Forrige periode: den nyeste eldre perioden som deler minst én kundegruppe.
        eldre = [t for t in alle if str(t["gyldig_fra"]) < args.fra and grupper & set(t["kundegrupper"])]
        print(f"\nPeriode {args.fra} [{','.join(sorted(grupper))}]")
        if not eldre:
            print("  Ingen forrige periode for disse kundegruppene, så det er ingenting å sammenligne mot.")
            continue
        forrige = max(eldre, key=lambda t: str(t["gyldig_fra"]))
        for_denne = advarsler
        print(f"  Sammenlignet med perioden fra {forrige['gyldig_fra']} [{','.join(sorted(forrige['kundegrupper']))}]")

        if set(forrige["kundegrupper"]) != grupper:
            advarsler += 1
            print(f"  ADVARSEL kundegrupper endret: {sorted(forrige['kundegrupper'])} -> {sorted(grupper)}")

        gt, nt = forrige["fastledd"]["terskler"], ny["fastledd"]["terskler"]
        if len(nt) < len(gt):
            advarsler += 1
            print(f"  ADVARSEL færre trinn i fastleddet: {len(gt)} -> {len(nt)}")
        if [t["terskel"] for t in gt] != [t["terskel"] for t in nt]:
            advarsler += 1
            print(f"  ADVARSEL andre terskelgrenser: {[t['terskel'] for t in gt]} -> {[t['terskel'] for t in nt]}")
        if forrige["fastledd"]["metode"] != ny["fastledd"]["metode"]:
            advarsler += 1
            print(f"  ADVARSEL annen fastleddmetode: {forrige['fastledd']['metode']} -> {ny['fastledd']['metode']}")

        for navn, ny_pris in pris_liste(ny).items():
            gammel = pris_liste(forrige).get(navn)
            if gammel is None:
                advarsler += 1
                print(f"  ADVARSEL {navn} finnes ikke i forrige periode (ny: {ny_pris})")
                continue
            if gammel == ny_pris:
                continue
            endring = (ny_pris - gammel) / gammel if gammel else Decimal(1)
            merknad = []
            if abs(endring) > GRENSE:
                merknad.append(f"endring over {int(GRENSE * 100)} %")
            if ny_pris < gammel:
                merknad.append("pris synker")
            if merknad:
                advarsler += 1
                print(f"  ADVARSEL {navn}: {gammel} -> {ny_pris} ({endring:+.1%}), {', '.join(merknad)}")

        if advarsler == for_denne:
            print("  Ingen uvanlige endringer.")

    if advarsler:
        print(f"\n{advarsler} ting å forklare i rapporten (finn begrunnelsen i kilden, ellers dobbeltsjekk tallene).")


if __name__ == "__main__":
    main()
