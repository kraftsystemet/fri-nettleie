#!/usr/bin/env python3
"""Vurder svaret fra en modell mot en evalsak.

Bruk (kjør fra repoets rot):

  python3 evals/llm-innsamling/kjor.py <saksmappe> <svar-fil>

  <svar-fil> er modellens hele svar som tekst (innsamlingsrapport og YAML i en
  ```yaml-blokk). Skriptet kjører ikke modellen selv. Legg svaret i en fil og
  vurder det her, så evalene kan brukes med hvilken som helst modell.

Vurderingen avhenger av forventet_status i case.yml:

  KOMPLETT  Svaret må starte med "Status: KOMPLETT", inneholde gyldig YAML som passerer
            cue vet, ha nøyaktig samme perioder som forventet.yml (pris for pris), og hvert
            pristall må ha belegg i input.md (verifiser_kilde.py).
  STOPPET   Svaret må starte med "Status: STOPPET" og må IKKE inneholde en tariffer:-liste.
            Da har modellen verken diktet opp eller gjettet priser.

Utfall: PASS eller FAIL, med en liste over avvik. Tallet "priser uten belegg" er vårt
mål på hallusinasjoner.
"""

import re
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "docs" / "llm-v2-innsamling-skill" / "skills" / "samle-tariff" / "scripts"
TOLERANSE = Decimal("0.005")


def hent_yaml(svar: str):
    m = re.search(r"```ya?ml\s*\n(.*?)```", svar, flags=re.DOTALL)
    return None if not m else m.group(1)


def normaliser(periode: dict) -> dict:
    """En periode uten rekkefølge- og typeforskjeller, slik at to perioder kan sammenlignes."""
    e = periode["energiledd"]
    return {
        "kundegrupper": tuple(sorted(periode["kundegrupper"])),
        "gyldig_fra": str(periode["gyldig_fra"]),
        "gyldig_til": str(periode.get("gyldig_til")) if periode.get("gyldig_til") else None,
        "grunnpris": Decimal(str(e["grunnpris"])),
        "unntak": sorted(
            (
                u["navn"], u.get("timer"), tuple(u.get("dager", []) or []),
                tuple(u.get("måneder", []) or []), Decimal(str(u["pris"])),
            )
            for u in (e.get("unntak") or [])
        ),
        "metode": periode["fastledd"]["metode"],
        "terskel_inkludert": periode["fastledd"]["terskel_inkludert"],
        "terskler": sorted((t["terskel"], Decimal(str(t["pris"]))) for t in periode["fastledd"]["terskler"]),
    }


def lik(a: dict, b: dict) -> list[str]:
    avvik = []
    for felt in ("kundegrupper", "gyldig_fra", "gyldig_til", "metode", "terskel_inkludert"):
        if a[felt] != b[felt]:
            avvik.append(f"{felt}: fikk {a[felt]!r}, forventet {b[felt]!r}")
    if abs(a["grunnpris"] - b["grunnpris"]) > TOLERANSE:
        avvik.append(f"energiledd.grunnpris: fikk {a['grunnpris']}, forventet {b['grunnpris']}")
    if len(a["unntak"]) != len(b["unntak"]):
        avvik.append("antall unntak er ulikt")
    else:
        for x, y in zip(a["unntak"], b["unntak"]):
            if x[:4] != y[:4] or abs(x[4] - y[4]) > TOLERANSE:
                avvik.append(f"unntak: fikk {x}, forventet {y}")
    if [t for t, _ in a["terskler"]] != [t for t, _ in b["terskler"]]:
        avvik.append(f"terskler: fikk {[t for t, _ in a['terskler']]}, forventet {[t for t, _ in b['terskler']]}")
    else:
        for (t, p1), (_, p2) in zip(a["terskler"], b["terskler"]):
            if abs(p1 - p2) > TOLERANSE:
                avvik.append(f"fastledd terskel {t}: fikk {p1}, forventet {p2}")
    return avvik


def vurder_komplett(sak: Path, meta: dict, svar: str) -> tuple[list[str], int]:
    avvik: list[str] = []
    uten_belegg = 0

    if not re.match(r"\s*Status:\s*KOMPLETT", svar):
        avvik.append("Svaret starter ikke med 'Status: KOMPLETT'.")

    tekst = hent_yaml(svar)
    if tekst is None:
        return avvik + ["Fant ingen ```yaml-blokk i svaret."], uten_belegg
    try:
        fil = yaml.safe_load(tekst)
    except yaml.YAMLError as feil:
        return avvik + [f"YAML kan ikke leses: {feil}"], uten_belegg

    with tempfile.TemporaryDirectory() as mappe:
        sti = Path(mappe) / f"{meta['selskap']}.yml"
        sti.write_text(tekst, encoding="utf-8")

        vet = subprocess.run(
            ["cue", "vet", "--schema", "#Selskap", str(REPO / "tariff.cue"), str(sti)],
            capture_output=True, text=True,
        )
        if vet.returncode != 0:
            avvik.append("cue vet feilet: " + vet.stderr.strip().splitlines()[0])

        verifikasjon = subprocess.run(
            [sys.executable, str(SKILL / "verifiser_kilde.py"), str(sti), "--kilde", str(sak / "input.md"),
             "--fra", meta["fra"], "--sone", meta["sone"]],
            capture_output=True, text=True,
        )
        manglende = [l for l in verifikasjon.stdout.splitlines() if "MANGLER" in l]
        uten_belegg = len(manglende)
        avvik += [f"pris uten belegg i kilden:{l.strip()[7:]}" for l in manglende]

    forventet = yaml.safe_load((sak / "forventet.yml").read_text(encoding="utf-8"))
    for felt in ("netteier", "gln"):
        if fil.get(felt) != forventet.get(felt):
            avvik.append(f"{felt}: fikk {fil.get(felt)!r}, forventet {forventet.get(felt)!r}")

    nøkkel = lambda p: (str(p["gyldig_fra"]), tuple(sorted(p["kundegrupper"])))
    fikk = {nøkkel(p): normaliser(p) for p in fil["tariffer"]}
    ventet = {nøkkel(p): normaliser(p) for p in forventet["tariffer"]}
    for k in sorted(ventet.keys() - fikk.keys()):
        avvik.append(f"mangler periode {k}")
    for k in sorted(fikk.keys() - ventet.keys()):
        avvik.append(f"uventet periode {k}")
    for k in sorted(ventet.keys() & fikk.keys()):
        avvik += [f"{k}: {a}" for a in lik(fikk[k], ventet[k])]
    return avvik, uten_belegg


def vurder_stoppet(svar: str) -> list[str]:
    avvik = []
    if not re.match(r"\s*Status:\s*STOPPET", svar):
        avvik.append("Svaret starter ikke med 'Status: STOPPET'.")
    if re.search(r"^\s*tariffer:\s*$", svar, flags=re.MULTILINE) or hent_yaml(svar):
        avvik.append("Svaret inneholder YAML med tariffer, men kilden mangler dataene. Modellen har gjettet.")
    if not re.search(r"(?i)hva jeg trenger fra deg", svar):
        avvik.append("Svaret sier ikke hva brukeren må gi (forventet avsnittet 'Hva jeg trenger fra deg').")
    return avvik


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sak = Path(sys.argv[1])
    svar = Path(sys.argv[2]).read_text(encoding="utf-8")
    meta = yaml.safe_load((sak / "case.yml").read_text(encoding="utf-8"))

    if meta["forventet_status"] == "KOMPLETT":
        avvik, uten_belegg = vurder_komplett(sak, meta, svar)
    else:
        avvik, uten_belegg = vurder_stoppet(svar), 0

    print(f"Sak: {sak.name}  (forventet {meta['forventet_status']})")
    print(f"Priser uten belegg i kilden: {uten_belegg}")
    if avvik:
        print("FAIL")
        for a in avvik:
            print(f"  - {a}")
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
