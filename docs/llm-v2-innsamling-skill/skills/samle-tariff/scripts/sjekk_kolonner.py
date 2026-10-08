#!/usr/bin/env python3
"""Sjekk at to kolonner i kilden stemmer med hverandre (med og uten avgifter).

Mange netteiere oppgir samme pris både inkl. og eks. avgifter. Da skal de to tallene henge
sammen. Gjør de ikke det, motsier kilden seg selv (skrivefeil hos netteier eller i transkriberingen),
og utfallet er STOPPET, se usikkerhet.md.

Bruk (kjør fra repoets rot). Hvert par er INKL:EKS, nøyaktig slik de står i kilden:

  # Fastledd kr/mnd, sør (mva). Føie 2026-11:
  python3 .../sjekk_kolonner.py --sone sor --par 237,5:190 293,8:235 2062,5:2450

  # Energiledd øre/kWh der kolonnen «inkl.» også har elavgift og Enova:
  python3 .../sjekk_kolonner.py --sone sor --inkl-avgifter --dato 2026-11-01 --par 30,79:16,5

Satsene leses fra references/satser.yml. Avslutter med kode 1 hvis et par ikke stemmer.
"""

import argparse
import sys
from datetime import date
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utled_avgifter import SATSER, d, desimaler, forbruksavgift, last_satser, mva_faktor, rund  # noqa: E402


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--par", nargs="+", required=True, help="INKL:EKS, for eksempel 293,8:235")
    p.add_argument("--sone", required=True)
    p.add_argument("--inkl-avgifter", action="store_true", help="«Inkl.» har også elavgift og Enova (øre/kWh)")
    p.add_argument("--dato", help="Første gyldighetsdato, kreves med --inkl-avgifter")
    p.add_argument("--satser", type=Path, default=SATSER)
    args = p.parse_args()

    satser = last_satser(args.satser)
    if args.sone not in satser["soner"]:
        sys.exit(f"Ukjent sone {args.sone}. Gyldige: {', '.join(satser['soner'])}")
    faktor = mva_faktor(satser, args.sone, True)
    avgifter = Decimal(0)
    if args.inkl_avgifter:
        if not args.dato:
            sys.exit("--inkl-avgifter krever --dato")
        if satser["soner"][args.sone]["forbruksavgift"]:
            avgifter += forbruksavgift(satser, date.fromisoformat(args.dato))
        avgifter += d(satser["enova"]["husholdning_ore_per_kwh"])

    feil = 0
    for par in args.par:
        try:
            inkl_tekst, eks_tekst = par.split(":")
        except ValueError:
            sys.exit(f"Ugyldig par «{par}», bruk INKL:EKS")
        n = desimaler(inkl_tekst)
        forventet = rund((d(eks_tekst) + avgifter) * faktor, n)
        ok = forventet == rund(d(inkl_tekst), n)
        print(f"{'OK    ' if ok else 'AVVIK '} inkl {inkl_tekst} / eks {eks_tekst}: ({eks_tekst} + {avgifter}) x {faktor} = {forventet}")
        feil += not ok

    if feil:
        print(f"\nSTOPP: {feil} par stemmer ikke. Kilden motsier seg selv. Ikke velg en av dem selv.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
