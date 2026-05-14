#!/usr/bin/env python3
"""
Generate docs/llms.txt from tariffer/*.yml for fri-nettleie.

Run from the repo root:
    python scripts/generate_llms_txt.py

Produces docs/llms.txt — a machine-readable context file for LLMs.
"""

import sys
from datetime import date, datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
TARIFFER_DIR = REPO_ROOT / "tariffer"
OUTPUT_FILE = REPO_ROOT / "docs" / "llm" / "llms.txt"

ENOVA_AVGIFT = 1.0          # øre/kWh, for husholdning
MVA_SATS = 0.25             # 25%
MVA_FRITAK_FYLKER = ["Nordland", "Troms", "Finnmark"]
TILTAKSSONEN_KOMMUNER_NOTE = "Finnmark og Nord-Troms (se regjeringen.no for full liste)"
INNSAMLER_URL = "https://kraftsystemet.no/fri-nettleie/innsamler/"


def load_tariffer() -> list[dict]:
    """Load all YAML files from tariffer/ and return as list of dicts."""
    tariffer = []
    for yml_file in sorted(TARIFFER_DIR.glob("*.yml")):
        try:
            with open(yml_file, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data:
                data["_fil"] = yml_file.stem
                tariffer.append(data)
        except yaml.YAMLError as e:
            print(f"ADVARSEL: Kunne ikke lese {yml_file.name}: {e}", file=sys.stderr)
    return tariffer


def parse_date(date_str: str, context: str) -> date | None:
    """Parse a date string, returning None and printing a warning on failure."""
    try:
        return date.fromisoformat(date_str)
    except (ValueError, TypeError) as e:
        print(f"ADVARSEL: Ugyldig dato '{date_str}' i {context}: {e}", file=sys.stderr)
        return None


def find_active_tariff(tariffs: list[dict], as_of: date = None) -> list[dict]:
    """
    Return the subset of tariff periods that are active on `as_of`.
    A period is active if gyldig_fra <= as_of < gyldig_til (or no gyldig_til).
    """
    if as_of is None:
        as_of = date.today()

    active = []
    for t in tariffs:
        fra = parse_date(t.get("gyldig_fra", ""), "gyldig_fra")
        if fra is None:
            continue
        til_str = t.get("gyldig_til")
        til = parse_date(til_str, "gyldig_til") if til_str else None
        if til_str and til is None:
            continue  # invalid gyldig_til, skip
        if fra <= as_of and (til is None or as_of < til):
            active.append(t)
    return active


def format_tariff_compact(netteier_data: dict, as_of: date) -> str:
    """Format one netteier's active tariff(s) as compact text for llms.txt."""
    navn = netteier_data["netteier"].strip()
    gln = ", ".join(netteier_data.get("gln", []))
    oppdatert = netteier_data.get("sist_oppdatert", "ukjent")
    alle_tariffer = netteier_data.get("tariffer", [])
    active = find_active_tariff(alle_tariffer, as_of)

    lines = [f"## {navn}"]
    lines.append(f"GLN: {gln} | Sist oppdatert: {oppdatert}")

    if not active:
        lines.append("_Ingen aktiv tariff funnet for dagens dato._")
        return "\n".join(lines)

    for t in active:
        grupper = ", ".join(t.get("kundegrupper", []))
        lines.append(f"Kundegrupper: {grupper}")
        lines.append(f"Gyldig fra: {t['gyldig_fra']}" + (f" til {t['gyldig_til']}" if t.get("gyldig_til") else ""))

        # Fastledd
        fl = t.get("fastledd", {})
        metode = fl.get("metode", "ukjent")
        terskel_inkl = fl.get("terskel_inkludert", None)
        lines.append(f"Fastledd metode: {metode} | Terskel inkludert: {terskel_inkl}")
        lines.append("Fastledd terskler (kr/år):")
        for tr in fl.get("terskler", []):
            lines.append(f"  - Fra {tr['terskel']} kW: {tr['pris']} kr/år")

        # Energiledd
        el = t.get("energiledd", {})
        grunnpris = el.get("grunnpris")
        lines.append(f"Energiledd grunnpris: {grunnpris} øre/kWh (eks. avgifter)")

        unntak = el.get("unntak", [])
        if unntak:
            lines.append("Energiledd unntak:")
            for u in unntak:
                parts = [f"  - {u.get('navn', '?')}: {u['pris']} øre/kWh"]
                if u.get("timer"):
                    parts.append(f"timer {u['timer']}")
                if u.get("dager"):
                    parts.append(f"dager: {', '.join(u['dager'])}")
                if u.get("måneder"):
                    parts.append(f"måneder: {', '.join(u['måneder'])}")
                lines.append(" | ".join(parts))

        lines.append("")  # blank line between tariff periods

    return "\n".join(lines)


def generate_llms_txt(as_of: date = None) -> str:
    if as_of is None:
        as_of = date.today()

    tariffer = load_tariffer()
    generated_at = datetime.now().isoformat(timespec="seconds")

    sections = []

    # -----------------------------------------------------------------------
    # Header / project description
    # -----------------------------------------------------------------------
    sections.append(f"""\
# fri-nettleie — Nettleietariffer for Norge
> Generert: {generated_at} | Gyldige tariffer per: {as_of}
> Kilde: https://github.com/kraftsystemet/fri-nettleie
> Lisens: CC-BY-4.0 (navngivelse påkrevd)

fri-nettleie er en åpen dugnad som samler nettleietariffer for alle norske
netteiere (nettselskaper) i et standardisert format. Dataene oppdateres
løpende når netteiere endrer sine tariffer.

Nettleie er den delen av strømregningen som betales til det lokale nettselskapet
(ikke til strømleverandøren). Den består av to hoveddeler:
- **Energiledd**: øre/kWh — betales per kWh forbrukt
- **Fastledd** (effektledd): kr/år — basert på kundens effektuttak (kW)

Alle priser i dette datasettet er **uten avgifter** (eks. mva, elavgift, Enova).
""")

    # -----------------------------------------------------------------------
    # How to interpret the data
    # -----------------------------------------------------------------------
    sections.append("""\
# Slik tolker du dataene

## Energiledd
`grunnpris` er standardprisen i øre/kWh som gjelder når ingen unntak treffer.
`unntak` er perioder med avvikende pris. Et unntak gjelder når ALLE angitte
betingelser er oppfylt samtidig (timer OG dager OG måneder, der de er angitt).
Dersom ingen unntak treffer, brukes alltid grunnpris.
Merk: I praksis vil typisk bare ett unntak treffe om gangen, men dersom flere
skulle treffe, er det ikke definert hvilken som gjelder — bruk grunnpris som
fallback og informer brukeren om usikkerheten.

### Timer
Angis som spenn, f.eks. `6-21`. Tolkes som: fra kl 06:00 til og med 21:59:59
(dvs. [06:00, 22:00) — time 6 t.o.m. time 21 inkludert).

### Dager
Mulige verdier:
- mandag, tirsdag, onsdag, torsdag, fredag, lørdag, søndag
- ukedag = mandag–fredag
- helg = lørdag + søndag
- helligdager = bevegelige helligdager
- fridag = helg eller helligdag
- virkedag = alle dager som ikke er fridag
- alle = alle dager

### Måneder
januar, februar, mars, april, mai, juni, juli, august, september, oktober,
november, desember

## Fastledd (effektledd)
Fastleddet avhenger av kundens effektuttak (kW). Metoden bestemmer hvordan
effekten måles:

- **TRE_DØGNMAX_MND** (vanligst): gjennomsnitt av de 3 høyeste timene i ulike
  døgn i foregående måned
- **FEM_VEKTET_ÅR**: de 5 høyeste ukesmaksene siste 12 måneder, vektet for sesong
- **OV_TREFASE**: oversiktsbryter trefase — terskel er sikringsstørrelse i ampere
- **MND_MAX**: høyeste enkelttime i måneden

`terskler` angir trinnvis pris. Kunden betaler prisen for det trinnet de
befinner seg på (ikke summert). Priser oppgis i **kr/år**.

`terskel_inkludert: true` betyr at kunden havner på neste trinn dersom forbruket
er nøyaktig lik terskelgrensen. `false` betyr kunden forblir på laveste trinn
ved nøyaktig terskelverdi.

## Kundegrupper
- **husholdning**: vanlige husholdningskunder
- **fritid**: hytter og fritidshus
- **liten_næring**: lavspent næring under 100 MWh/år

VIKTIG: Dataene samles inn manuelt — vi oppfordrer ikke til automatisk scraping.
Dersom en netteier mangler `liten_næring` betyr det at vi ikke har samlet inn
den tariffen ennå, ikke at netteieren ikke tilbyr den.

## Gyldighetsperioder
`gyldig_fra` er inklusiv. `gyldig_til` er eksklusiv (dvs. perioden slutter dagen
før). Manglende `gyldig_til` betyr at tariffen er gjeldende uten sluttdato.
Dataene i denne filen gjelder per genereringsdato — for historiske spørsmål,
spesifiser datoen eksplisitt og vær oppmerksom på at eldre perioder kan mangle.

## Feil i dataene?
Dersom du oppdager feil eller mangler, kan du åpne et issue på GitHub:
https://github.com/kraftsystemet/fri-nettleie/issues

## Eksempler på spørsmål og hvordan tolke dataene
Q: "Hva er energileddet for Elvia på en fredag kveld i januar?"
A: Finn Elvia-seksjonen. Sjekk energiledd-unntak: finn unntak der dager inkluderer
   'fredag' (eller 'ukedag'/'virkedag') og timer dekker kveldstimene, og måneder
   inkluderer 'januar' (eller at måneder er utelatt = gjelder alle). Bruk den
   prisen. Ellers bruk grunnpris.

Q: "Hvilken netteier er billigst på en søndag natt?"
A: Søndag natt er typisk lavlast — sjekk grunnpris for alle netteiere (unntak
   for 'helg', 'fridag' eller 'søndag' kan gi lavere pris). Sammenlign
   grunnprisene der ingen unntak treffer.

Q: "Har Griug liten_næring-tariff?"
A: Dersom liten_næring ikke finnes i Griug sine kundegrupper er det fordi vi
   ikke har samlet inn den tariffen ennå — ikke at den ikke eksisterer.
""")


    # -----------------------------------------------------------------------
    # Avgifter
    # -----------------------------------------------------------------------
    sections.append(f"""\
# Avgifter (legges til på toppen av prisene i datasettet)

Alle priser i datasettet er UTEN avgifter. For å beregne faktisk pris må du
legge til:

## 1. Enova-avgift
{ENOVA_AVGIFT} øre/kWh for husholdning (pålagt alle, alle steder i Norge).

## 2. Forbruksavgift (elavgift)
Satsen endres ved stortingsvedtak noen ganger i året.
VIKTIG: Hent alltid gjeldende og historiske satser fra innsamleren:
  {INNSAMLER_URL}
Se seksjonen "Forbruksavgift" øverst på siden — den holdes oppdatert løpende.
Gjelder IKKE i tiltakssonen ({TILTAKSSONEN_KOMMUNER_NOTE}).

## 3. Merverdiavgift (mva)
25% på (nettleie + Enova-avgift + forbruksavgift).
Fritak for mva i: {', '.join(MVA_FRITAK_FYLKER)}.
Verken elavgift eller mva i tiltakssonen.

## Eksempel: totalberegning for husholdning (sør for Nordland)
Anta grunnpris energiledd = 20 øre/kWh og forbruksavgift = F øre/kWh (hent F fra innsamleren):
  Nettleie:        20.00 øre/kWh
  + Enova:          {ENOVA_AVGIFT:.2f} øre/kWh
  + Forbruksavgift: F øre/kWh
  = Subtotal:       (20 + {ENOVA_AVGIFT} + F) øre/kWh
  + MVA (25%):     * 1.25
  = Total:          (20 + {ENOVA_AVGIFT} + F) * 1.25 øre/kWh
""")

    # -----------------------------------------------------------------------
    # Netteier index
    # -----------------------------------------------------------------------
    netteier_index = []
    for nd in tariffer:
        navn = nd["netteier"].strip()
        gln = ", ".join(nd.get("gln", []))
        netteier_index.append(f"- {navn} (GLN: {gln})")

    sections.append("# Alle netteiere i datasettet\n" + "\n".join(netteier_index))

    # -----------------------------------------------------------------------
    # Full tariff data per netteier (active only)
    # -----------------------------------------------------------------------
    sections.append("# Tariffer per netteier (kun aktive per generert dato)\n")
    for nd in tariffer:
        sections.append(format_tariff_compact(nd, as_of))
        sections.append("---")

    return "\n\n".join(sections)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generer docs/llms.txt fra tariffer/*.yml")
    parser.add_argument("dato", nargs="?", help="Dato å generere for (YYYY-MM-DD), standard: i dag")
    parser.add_argument("--dry-run", action="store_true", help="Skriv til stdout i stedet for fil")
    args = parser.parse_args()

    as_of = date.today()
    if args.dato:
        as_of = parse_date(args.dato, "kommandolinje")
        if as_of is None:
            print("Ugyldig dato. Bruk format YYYY-MM-DD.", file=sys.stderr)
            sys.exit(1)

    print(f"Genererer llms.txt for dato: {as_of}", file=sys.stderr)
    print(f"Leser tariffer fra: {TARIFFER_DIR}", file=sys.stderr)

    content = generate_llms_txt(as_of)

    if args.dry_run:
        print(content)
    else:
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        file_size_kb = OUTPUT_FILE.stat().st_size / 1024
        tariff_count = len(load_tariffer())
        print(f"Skrev {OUTPUT_FILE} ({file_size_kb:.1f} KB, {tariff_count} netteiere)", file=sys.stderr)


if __name__ == "__main__":
    main()