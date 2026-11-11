#!/usr/bin/env python3
"""Sjekk at hvert pristall i en ny tariffperiode kan spores til kilden.

Dette er sperren mot oppdiktede tall. For hver pris i perioden som starter på
--fra regner skriptet fremover til hvordan prisen ville stått i kilden (med og
uten mva, elavgift og Enova, per måned og per år) og ser etter tallet i
kildeutdraget. Finnes ingen mulig kildeverdi i utdraget, mangler prisen belegg.

Bruk (kjør fra repoets rot):

  python3 .../verifiser_kilde.py tariffer/selskap.yml \\
      --kilde kilde-utdrag.md --fra 2026-10-01 --sone nord_norge

Avslutter med kode 1 hvis minst ett tall mangler belegg.

Et unntak i formatet er en erstatningspris (tillegg er summert til grunnprisen). For unntak godtas
derfor to ting: at selve prisen finnes i kilden, eller at tillegget (unntak minus grunnpris)
finnes i kilden. Da vises «tillegg» som kilden.

Begrensninger (skriv dem i rapporten, ikke skjul dem):
  * Sjekker pris, ikke terskler og datoer. Små heltall står nesten alltid et sted i en kilde.
  * Fanger ikke feil i selve transkriberingen av et bilde. Les bildet to ganger.
  * Et tall kan finnes i kilden uten å gjelde riktig trinn. Kontroller rekkefølgen selv.
"""

import argparse
import re
import sys
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import yaml

SATSER = Path(__file__).resolve().parent.parent / "references" / "satser.yml"

# Norske og engelske tall: "1 324", "1.324,50", "1324", "48,91", "48.91".
TALL = re.compile(r"\d{1,3}(?:[  .]\d{3})+(?:,\d+)?|\d+(?:[.,]\d+)?")


def rund(x: Decimal, n: int) -> Decimal:
    return x.quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)


def tall_i_tekst(tekst: str) -> set[Decimal]:
    """Alle tall i teksten som Decimal. Tolker både 1 324 og 1.324 som tusenskille."""
    funnet: set[Decimal] = set()
    for m in TALL.finditer(tekst):
        rå = m.group(0).replace(" ", " ")
        kandidater = set()
        # Tolkning 1: mellomrom/punkt er tusenskille, komma er desimal.
        kandidater.add(rå.replace(" ", "").replace(".", "").replace(",", "."))
        # Tolkning 2: punkt er desimal, komma er tusenskille eller desimal.
        kandidater.add(rå.replace(" ", "").replace(",", "."))
        for k in kandidater:
            try:
                funnet.add(Decimal(k))
            except Exception:
                pass
    return funnet


def forbruksavgift(satser: dict, dato: date) -> Decimal:
    gyldige = [r for r in satser["forbruksavgift"]["satser"] if date.fromisoformat(r["fra"]) <= dato]
    if not gyldige:
        sys.exit(f"STOPP: ingen forbruksavgift i satser.yml for {dato}.")
    return Decimal(str(max(gyldige, key=lambda r: r["fra"])["ore_per_kwh"]))


def avrundet(x: Decimal, desimaler: tuple[int, ...]) -> set[Decimal]:
    """Verdien slik kilden kan ha avrundet den. Heltall er bare tillatt der kilden pleier å bruke dem."""
    return {rund(x, n) for n in desimaler}


def kilde_kandidater_energi(pris: Decimal, avgiftssett: list[Decimal], faktorer: list[Decimal]) -> dict[Decimal, str]:
    """Alle verdier prisen kan ha stått som i kilden (øre/kWh)."""
    ut: dict[Decimal, str] = {}
    for a in avgiftssett:
        for f in faktorer:
            beskrivelse = f"({pris} + {a}) x {f}"
            # Øre/kWh oppgis med 1-2 desimaler. Heltall aksepteres bare hvis verdien er et heltall,
            # ellers ville "25" i en kilde godkjent enhver pris rundt 25.
            x = (pris + a) * f
            for v in avrundet(x, (1, 2)):
                ut.setdefault(v, beskrivelse)
    return ut


def kilde_kandidater_tillegg(pris: Decimal, grunnpris: Decimal, faktorer: list[Decimal]) -> dict[Decimal, str]:
    """Verdier et tillegg kan ha stått som i kilden (øre/kWh), når unntaket er grunnpris pluss tillegg."""
    ut: dict[Decimal, str] = {}
    diff = abs(pris - grunnpris)
    if diff == 0:
        return ut
    for f in faktorer:
        for v in avrundet(diff * f, (1, 2)):
            ut.setdefault(v, f"tillegg |{pris} - {grunnpris}| = {diff} x {f}")
    return ut


def kilde_kandidater_fastledd(pris_ar: Decimal, enova_ar: Decimal, faktorer: list[Decimal]) -> dict[Decimal, str]:
    """Alle verdier fastleddet kan ha stått som i kilden (kr/år og kr/mnd)."""
    ut: dict[Decimal, str] = {}
    for e in (Decimal(0), enova_ar):
        for f in faktorer:
            ar = (pris_ar + e) * f
            for v in avrundet(ar, (0, 1, 2)):
                ut.setdefault(v, f"({pris_ar} + {e}) x {f} kr/år")
            for v in avrundet(ar / 12, (0, 1, 2)):
                ut.setdefault(v, f"({pris_ar} + {e}) x {f} / 12 kr/mnd")
    return ut


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("yaml_fil")
    p.add_argument("--kilde", type=Path, required=True, help="Ordrett utdrag av kilden (tekst)")
    p.add_argument("--fra", required=True, help="gyldig_fra for perioden som sjekkes")
    p.add_argument("--sone", required=True)
    p.add_argument("--satser", type=Path, default=SATSER)
    args = p.parse_args()

    satser = yaml.safe_load(args.satser.read_text(encoding="utf-8"))
    if args.sone not in satser["soner"]:
        sys.exit(f"Ukjent sone {args.sone}. Gyldige: {', '.join(satser['soner'])}")
    sone = satser["soner"][args.sone]
    dato = date.fromisoformat(args.fra)

    data = yaml.safe_load(Path(args.yaml_fil).read_text(encoding="utf-8"))
    perioder = [t for t in data["tariffer"] if str(t["gyldig_fra"]) == args.fra]
    if not perioder:
        sys.exit(f"STOPP: fant ingen tariffperiode med gyldig_fra {args.fra} i {args.yaml_fil}.")

    kilde_tall = tall_i_tekst(args.kilde.read_text(encoding="utf-8"))
    if not kilde_tall:
        sys.exit("STOPP: fant ingen tall i kildeutdraget. Utdraget er tomt eller uleselig.")

    mva = Decimal(str(satser["mva"]["sats"]))
    faktorer = [Decimal(1)] + ([Decimal(1) + mva] if sone["mva"] else [])
    elavgift = forbruksavgift(satser, dato) if sone["forbruksavgift"] else Decimal(0)
    enova_ore = Decimal(str(satser["enova"]["husholdning_ore_per_kwh"]))
    enova_ar = Decimal(str(satser["enova"]["naring_kr_per_ar"]))

    mangler = 0
    totalt = 0
    for t in perioder:
        grupper = ",".join(t["kundegrupper"])
        privat = any(g in ("husholdning", "fritid") for g in t["kundegrupper"])
        # Kilden kan oppgi prisen uten avgifter, med kun elavgift, eller med alt.
        avgiftssett = sorted({Decimal(0), elavgift, elavgift + (enova_ore if privat else Decimal(0))})

        print(f"\nPeriode {args.fra} [{grupper}]")

        e = t["energiledd"]
        grunnpris = Decimal(str(e["grunnpris"]))
        priser = [("energiledd.grunnpris", grunnpris, False)]
        for u in e.get("unntak", []) or []:
            priser.append((f"energiledd.unntak[{u['navn']}]", Decimal(str(u["pris"])), True))
        for navn, pris, er_unntak in priser:
            totalt += 1
            kandidater = kilde_kandidater_energi(pris, avgiftssett, faktorer)
            if er_unntak:
                for v, b in kilde_kandidater_tillegg(pris, grunnpris, faktorer).items():
                    kandidater.setdefault(v, b)
            treff = next(((v, b) for v, b in kandidater.items() if v in kilde_tall), None)
            if treff:
                print(f"  OK       {navn} = {pris}  (kilde: {treff[0]} via {treff[1]})")
            else:
                mangler += 1
                print(f"  MANGLER  {navn} = {pris}  (ingen mulig kildeverdi finnes i utdraget)")

        for tr in t["fastledd"]["terskler"]:
            navn = f"fastledd.terskel[{tr['terskel']}]"
            pris = Decimal(str(tr["pris"]))
            totalt += 1
            treff = next(
                ((v, b) for v, b in kilde_kandidater_fastledd(pris, enova_ar, faktorer).items() if v in kilde_tall),
                None,
            )
            if treff:
                print(f"  OK       {navn} = {pris}  (kilde: {treff[0]} via {treff[1]})")
            else:
                mangler += 1
                print(f"  MANGLER  {navn} = {pris}  (ingen mulig kildeverdi finnes i utdraget)")

    print(f"\n{totalt - mangler} av {totalt} priser har belegg i kilden.")
    if mangler:
        print("STOPP: minst én pris mangler belegg. Ikke lever YAML. Se usikkerhet.md.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
