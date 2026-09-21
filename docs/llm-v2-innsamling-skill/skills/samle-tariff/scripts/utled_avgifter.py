#!/usr/bin/env python3
"""Utled priser uten avgifter fra priser som er oppgitt med avgifter.

Bruk (kjør fra repoets rot):

  # Energiledd (øre/kWh). Kilden oppgir 48,91 inkl. mva og avgifter, Sør-Norge:
  python3 .../utled_avgifter.py energiledd --pris 48,91 --dato 2026-10-01 --sone sor \\
      --inkl-mva --inkl-avgifter

  # Kilden oppgir 29,34 inkl. mva, men avgiftene står som egne linjer:
  python3 .../utled_avgifter.py energiledd --pris 29,34 --dato 2026-09-01 --sone sor --inkl-mva

  # Fastledd (kr/mnd i kilden -> kr/år i YAML), Nord-Norge så ingen mva:
  python3 .../utled_avgifter.py fastledd --pris 508 916 1324 --sone nord_norge

Satsene leses fra references/satser.yml. Dette skriptet gjentar dem ikke.

Utfallet for hver verdi er ett av:
  REN        Et rundt tall (heltall eller .5) gir nøyaktig samme publiserte pris tilbake.
  UAVRUNDET  Bare en verdi med 1-2 desimaler gir samme pris tilbake. Bruk den, og si fra.
  INGEN      Ingen verdi gir samme pris tilbake. STOPP, ikke gjett.
"""

import argparse
import json
import sys
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import yaml

SATSER = Path(__file__).resolve().parent.parent / "references" / "satser.yml"


def d(verdi: str) -> Decimal:
    """Les et tall med norsk eller engelsk desimaltegn, uten å miste desimaler."""
    return Decimal(str(verdi).strip().replace(" ", "").replace(" ", "").replace(",", "."))


def desimaler(verdi: str) -> int:
    """Antall desimaler kilden oppga. '48,91' gir 2, '508' gir 0."""
    ren = str(verdi).strip().replace(",", ".")
    return len(ren.split(".")[1]) if "." in ren else 0


def rund(x: Decimal, n: int) -> Decimal:
    return x.quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)


def last_satser(sti: Path) -> dict:
    with open(sti, encoding="utf-8") as f:
        return yaml.safe_load(f)


def forbruksavgift(satser: dict, dato: date) -> Decimal:
    """Sats som gjelder på datoen: den nyeste raden med fra <= dato."""
    gyldige = [r for r in satser["forbruksavgift"]["satser"] if date.fromisoformat(r["fra"]) <= dato]
    if not gyldige:
        sys.exit(f"STOPP: ingen forbruksavgift i satser.yml for {dato}. Be brukeren oppgi den.")
    return d(max(gyldige, key=lambda r: r["fra"])["ore_per_kwh"])


def mva_faktor(satser: dict, sone: str, inkl_mva: bool) -> Decimal:
    if inkl_mva and satser["soner"][sone]["mva"]:
        return Decimal(1) + d(satser["mva"]["sats"])
    return Decimal(1)


def avvik_sjekk(satser: dict, maks_alder_dager: int = 90):
    """Advar hvis satsene ikke er verifisert nylig. Satsene kan endres, se satser.yml."""
    sist = date.fromisoformat(satser["sist_verifisert"])
    alder = (date.today() - sist).days
    if alder > maks_alder_dager:
        print(
            f"ADVARSEL: satser.yml er sist verifisert {sist} ({alder} dager siden). "
            "Be brukeren bekrefte elavgiften mot Skatteetaten.",
            file=sys.stderr,
        )


def utled_energiledd(args, satser: dict) -> list[dict]:
    dato = date.fromisoformat(args.dato)
    sone = args.sone
    if sone not in satser["soner"]:
        sys.exit(f"Ukjent sone {sone}. Gyldige: {', '.join(satser['soner'])}")
    avvik_sjekk(satser)

    avgifter = Decimal(0)
    if args.inkl_avgifter:
        if satser["soner"][sone]["forbruksavgift"]:
            avgifter += forbruksavgift(satser, dato)
        # Enova per kWh gjelder husholdning. Næring betaler kr/år, som ikke er en del av øre/kWh.
        if args.gruppe == "husholdning":
            avgifter += d(satser["enova"]["husholdning_ore_per_kwh"])

    faktor = mva_faktor(satser, sone, args.inkl_mva)

    resultater = []
    for publisert in args.pris:
        n = desimaler(publisert)
        pris = d(publisert)
        rå = pris / faktor - avgifter

        # Prøv de grovest mulige verdiene først: heltall, halve, en desimal, to desimaler.
        kandidater = [
            (rund(rå, 0), "REN"),
            (rund(rå * 2, 0) / 2, "REN"),
            (rund(rå, 1), "UAVRUNDET"),
            (rund(rå, 2), "UAVRUNDET"),
        ]
        valgt, utfall = None, "INGEN"
        for kandidat, klasse in kandidater:
            tilbake = rund((kandidat + avgifter) * faktor, n)
            if tilbake == rund(pris, n):
                valgt, utfall = kandidat, klasse
                break

        resultater.append({
            "publisert": publisert,
            "avgifter_ore": str(avgifter),
            "mva_faktor": str(faktor),
            "rå_utledet": str(rund(rå, 4)),
            "verdi": None if valgt is None else float(valgt),
            "utfall": utfall,
            "kontroll": (
                None if valgt is None
                else f"({valgt} + {avgifter}) x {faktor} = {rund((valgt + avgifter) * faktor, n)}"
            ),
        })
    return resultater


def utled_fastledd(args, satser: dict) -> list[dict]:
    sone = args.sone
    if sone not in satser["soner"]:
        sys.exit(f"Ukjent sone {sone}. Gyldige: {', '.join(satser['soner'])}")
    faktor = mva_faktor(satser, sone, args.inkl_mva)
    enova_per_ar = d(satser["enova"]["naring_kr_per_ar"]) if args.trekk_enova_naring else Decimal(0)

    resultater = []
    for publisert in args.pris:
        n = desimaler(publisert)
        pris = d(publisert)
        # Kilden oppgir kr/mnd, men filene lagrer kr/år.
        per_ar = pris * 12 / faktor - enova_per_ar
        verdi = rund(per_ar, 2)
        tilbake = rund(((verdi + enova_per_ar) * faktor) / 12, n)
        ok = tilbake == rund(pris, n)
        resultater.append({
            "publisert_kr_mnd": publisert,
            "verdi_kr_ar": float(verdi) if ok else None,
            "utfall": "REN" if ok and verdi == verdi.to_integral_value() else ("UAVRUNDET" if ok else "INGEN"),
            "kontroll": f"({verdi} + {enova_per_ar}) x {faktor} / 12 = {tilbake}",
        })
    return resultater


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--satser", type=Path, default=SATSER, help="Sti til satser.yml")
    p.add_argument("--json", action="store_true", help="Skriv resultatet som JSON")
    sub = p.add_subparsers(dest="kommando", required=True)

    e = sub.add_parser("energiledd", help="øre/kWh med avgifter -> uten avgifter")
    e.add_argument("--pris", nargs="+", required=True, help="Publisert(e) pris(er) i øre/kWh")
    e.add_argument("--dato", required=True, help="Første gyldighetsdato, YYYY-MM-DD")
    e.add_argument("--sone", required=True)
    e.add_argument("--inkl-mva", action="store_true", help="Prisen er oppgitt inkl. mva")
    e.add_argument(
        "--inkl-avgifter", action="store_true",
        help="Prisen inkluderer elavgift og Enova (øre/kWh). Utelat hvis avgiftene står som egne linjer.",
    )
    e.add_argument("--gruppe", choices=["husholdning", "liten_naring"], default="husholdning")

    f = sub.add_parser("fastledd", help="kr/mnd -> kr/år (og fjern mva og evt. Enova)")
    f.add_argument("--pris", nargs="+", required=True, help="Publisert(e) pris(er) i kr/mnd")
    f.add_argument("--sone", required=True)
    f.add_argument("--inkl-mva", action="store_true", help="Prisene er oppgitt inkl. mva")
    f.add_argument(
        "--trekk-enova-naring", action="store_true",
        help="Næringens Enova (kr/år) ligger inne i fastleddet. Trekk den fra.",
    )

    args = p.parse_args()
    satser = last_satser(args.satser)
    resultater = utled_energiledd(args, satser) if args.kommando == "energiledd" else utled_fastledd(args, satser)

    if args.json:
        print(json.dumps(resultater, ensure_ascii=False, indent=2))
    else:
        for r in resultater:
            print(" | ".join(f"{k}={v}" for k, v in r.items() if v is not None))

    if any(r["utfall"] == "INGEN" for r in resultater):
        print("\nSTOPP: minst én verdi lot seg ikke utlede rent. Ikke gjett en verdi.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
