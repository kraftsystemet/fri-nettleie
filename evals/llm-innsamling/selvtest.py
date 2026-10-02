#!/usr/bin/env python3
"""Selvtest for innsamlingsskillens skript og evalskriptet. Krever ingen modell.

Bruk (kjør fra repoets rot, med `cue` og PyYAML installert):

  venv/bin/python evals/llm-innsamling/selvtest.py

Tester at skriptene gir kjente riktige svar, at de avviser kjente feil, og at
kjor.py gir PASS på riktige og FAIL på gale kunstige svar. Avslutter med kode 1
hvis noe feiler.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "docs" / "llm-v2-innsamling-skill" / "skills" / "samle-tariff"
SCRIPTS = SKILL / "scripts"
CASER = REPO / "evals" / "llm-innsamling" / "caser"
KJOR = REPO / "evals" / "llm-innsamling" / "kjor.py"

feil: list[str] = []
antall = 0


def kjør(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, cwd=REPO)


def sjekk(navn: str, ok: bool, detalj: str = ""):
    global antall
    antall += 1
    print(f"  {'OK   ' if ok else 'FEIL '} {navn}")
    if not ok:
        feil.append(f"{navn}: {detalj}".strip())


def svar_med_yaml(status: str, yaml_tekst: str) -> str:
    return f"Status: {status}\n\n```yaml\n{yaml_tekst}```\n"


print("utled_avgifter.py")
u = SCRIPTS / "utled_avgifter.py"
for pris, sone, flagg, forventet, klasse in [
    ("48,91", "sor", ["--inkl-mva", "--inkl-avgifter"], "verdi=31.0", "REN"),
    ("42,66", "sor", ["--inkl-mva", "--inkl-avgifter"], "verdi=26.0", "REN"),
    ("25,13", "nord_norge", ["--inkl-avgifter"], "verdi=17.0", "REN"),
    ("42,7", "sor", ["--inkl-mva", "--inkl-avgifter"], "verdi=26.0", "REN"),       # Lysna: rundingsstøy 26,03 blir 26
    ("34,84", "sor", ["--inkl-mva"], "verdi=27.87", "UAVRUNDET"),                     # Glitre: inkl. mva, avgifter separat
]:
    r = kjør(u, "energiledd", "--pris", pris, "--dato", "2026-10-01", "--sone", sone, *flagg)
    sjekk(f"energiledd {pris} i {sone} {' '.join(flagg)} gir {forventet}", forventet in r.stdout and f"utfall={klasse}" in r.stdout, r.stdout + r.stderr)
r = kjør(u, "energiledd", "--pris", "37,21", "29,34", "--dato", "2026-09-01", "--sone", "sor", "--inkl-mva")
sjekk("Mellom: 37,21 og 29,34 inkl. mva (avgifter separat) gir 29,77 og 23,47", "verdi=29.77" in r.stdout and "verdi=23.47" in r.stdout, r.stdout)
r = kjør(u, "energiledd", "--pris", "48,37", "--dato", "2026-10-01", "--sone", "sor", "--inkl-mva", "--inkl-avgifter")
sjekk("umulig pris gir INGEN og feilkode 2", r.returncode == 2 and "utfall=INGEN" in r.stdout, r.stdout)
r = kjør(u, "fastledd", "--pris", "508", "--sone", "nord_norge")
sjekk("fastledd 508 kr/mnd gir 6096 kr/år", "verdi_kr_ar=6096.0" in r.stdout, r.stdout)
# 575 - 800/12 = 508,33 kr/mnd presist, men det runde kandidatet 508 kr/mnd (avvik 0,33, innenfor
# +-0,5 kr/mnd-grensen i kundegrupper.md) reverserer også til 575 og velges derfor — det er
# faktisk riktig svar for det ekte Kystnett-tilfellet: næring blir da lik privats 508 kr/mnd.
r = kjør(u, "fastledd", "--pris", "575", "--sone", "nord_norge", "--trekk-enova-naring")
sjekk("næringsfastledd 575 uten Enova gir 6096 kr/år (508 kr/mnd, matcher privat)", "verdi_kr_ar=6096.0" in r.stdout and "utfall=REN" in r.stdout, r.stdout)
r = kjør(u, "energiledd", "--pris", "24,13", "--dato", "2026-10-01", "--sone", "nord_norge", "--inkl-avgifter", "--gruppe", "liten_naring")
sjekk("næring eks. mva med elavgift gir 17", "verdi=17.0" in r.stdout, r.stdout)

print("verifiser_kilde.py")
v = SCRIPTS / "verifiser_kilde.py"
kyst = CASER / "kystnett-2026-10"
r = kjør(v, kyst / "forventet.yml", "--kilde", kyst / "input.md", "--fra", "2026-10-01", "--sone", "nord_norge")
sjekk("Kystnett-fasit har belegg i kilden for alle priser", r.returncode == 0 and "11 av 11" in r.stdout, r.stdout)
with tempfile.TemporaryDirectory() as tmp:
    dikta = Path(tmp) / "dikta.yml"
    dikta.write_text((kyst / "forventet.yml").read_text(encoding="utf-8").replace("pris: 10992", "pris: 11111"), encoding="utf-8")
    r = kjør(v, dikta, "--kilde", kyst / "input.md", "--fra", "2026-10-01", "--sone", "nord_norge")
    sjekk("oppdiktet pris avvises", r.returncode == 1 and "MANGLER  fastledd.terskel[5] = 11111" in r.stdout, r.stdout)
midt = CASER / "midtnett-2026-10"
r = kjør(v, midt / "forventet.yml", "--kilde", midt / "input.md", "--fra", "2026-10-01", "--sone", "sor")
sjekk("Midtnett-fasit har belegg i kilden for alle priser", r.returncode == 0 and "22 av 22" in r.stdout, r.stdout)

# Tillegg summeres til erstatningspris (vang.yml: grunnpris 8, Brukstidstillegg 18 = 8 + 10)
def tillegg_yaml(unntak_pris: str) -> str:
    return (
        "---\nnetteier: 'Test AS'\ngln: []\nsist_oppdatert: '2026-09-21'\nkilder:\n  - 'https://example.com'\n"
        "tariffer:\n  - kundegrupper:\n      - husholdning\n    gyldig_fra: '2026-10-01'\n    fastledd:\n"
        "      metode: TRE_DØGNMAX_MND\n      terskel_inkludert: true\n      terskler:\n        - terskel: 0\n          pris: 1200\n"
        f"    energiledd:\n      grunnpris: 8\n      unntak:\n        - navn: Brukstidstillegg\n          timer: 16-21\n          pris: {unntak_pris}\n"
    )


with tempfile.TemporaryDirectory() as tmp:
    kilde = Path(tmp) / "kilde.md"
    kilde.write_text("Energiledd 8 øre/kWh. Brukstidstillegg fredag kl 16-22: +10 øre/kWh. Fastledd 100 kr/mnd.\n", encoding="utf-8")
    ok_fil, dikta_fil = Path(tmp) / "ok.yml", Path(tmp) / "dikta.yml"
    ok_fil.write_text(tillegg_yaml("18"), encoding="utf-8")
    dikta_fil.write_text(tillegg_yaml("19"), encoding="utf-8")
    r = kjør(v, ok_fil, "--kilde", kilde, "--fra", "2026-10-01", "--sone", "nord_norge")
    sjekk("unntak 18 = grunnpris 8 + tillegg 10 (som står i kilden) godkjennes", r.returncode == 0 and "via tillegg" in r.stdout, r.stdout)
    r = kjør(v, dikta_fil, "--kilde", kilde, "--fra", "2026-10-01", "--sone", "nord_norge")
    sjekk("unntak 19 (tillegg 11 står ikke i kilden) avvises", r.returncode == 1 and "MANGLER  energiledd.unntak[Brukstidstillegg] = 19" in r.stdout, r.stdout)

print("sammenlign_forrige.py")
r = kjør(SCRIPTS / "sammenlign_forrige.py", midt / "forventet.yml", "--fra", "2026-10-01")
sjekk("Midtnett: varsler om +37,9 % på energiledd", "18.86 -> 26" in r.stdout and "endring over 30" in r.stdout, r.stdout)
sjekk("avslutter alltid med kode 0", r.returncode == 0)

print("satser.yml")
import yaml  # noqa: E402

satser = yaml.safe_load((SKILL / "references" / "satser.yml").read_text(encoding="utf-8"))
sjekk("har sist_verifisert, soner, mva, forbruksavgift og enova",
      all(k in satser for k in ("sist_verifisert", "soner", "mva", "forbruksavgift", "enova")), str(sorted(satser)))
sjekk("elavgift 2026 er 7,13", any(str(x["fra"]) == "2026-01-01" and float(x["ore_per_kwh"]) == 7.13 for x in satser["forbruksavgift"]["satser"]))

print("kjor.py (kunstige svar)")
with tempfile.TemporaryDirectory() as tmp:
    svar = Path(tmp) / "svar.md"

    def vurder(sak: str, tekst: str) -> subprocess.CompletedProcess:
        svar.write_text(tekst, encoding="utf-8")
        return kjør(KJOR, CASER / sak, svar)

    fasit = (kyst / "forventet.yml").read_text(encoding="utf-8")
    sjekk("KOMPLETT-sak: riktig svar gir PASS", vurder("kystnett-2026-10", svar_med_yaml("KOMPLETT", fasit)).returncode == 0)
    r = vurder("kystnett-2026-10", svar_med_yaml("KOMPLETT", fasit.replace("pris: 10992", "pris: 11111")))
    sjekk("KOMPLETT-sak: endret pris gir FAIL og teller pris uten belegg", r.returncode == 1 and "uten belegg i kilden: 1" in r.stdout, r.stdout)
    ekstra = fasit.replace("      - fritid\n    fastledd:", "      - fritid\n      - liten_næring\n    fastledd:")
    r = vurder("kystnett-2026-10", svar_med_yaml("KOMPLETT", ekstra))
    sjekk("KOMPLETT-sak: ekstra kundegruppe gir FAIL", r.returncode == 1 and "uventet periode" in r.stdout, r.stdout)
    r = vurder("kystnett-2026-10", fasit)
    sjekk("KOMPLETT-sak: manglende statuslinje gir FAIL", r.returncode == 1 and "Status: KOMPLETT" in r.stdout, r.stdout)

    stopp = "Status: STOPPET\n\nHva jeg ikke kan bekrefte:\n- ingen priser\n\nHva jeg trenger fra deg:\n- lim inn tabellen\n"
    for sak in ("midtnett-uten-priser", "kystnett-naring-bilde"):
        sjekk(f"STOPPET-sak {sak}: riktig svar gir PASS", vurder(sak, stopp).returncode == 0)
    gjettet = svar_med_yaml("KOMPLETT", (CASER / "midtnett-uten-priser" / "eksisterende.yml").read_text(encoding="utf-8"))
    r = vurder("midtnett-uten-priser", gjettet)
    sjekk("STOPPET-sak: gjettet YAML gir FAIL", r.returncode == 1 and "gjettet" in r.stdout, r.stdout)
    r = vurder("midtnett-uten-priser", "Status: STOPPET\n\nJeg mangler priser.\n")
    sjekk("STOPPET-sak: mangler spørsmål til brukeren gir FAIL", r.returncode == 1 and "trenger fra deg" in r.stdout, r.stdout)

print("alle evalsaker")
STOPP = "Status: STOPPET\n\nHva jeg ikke kan bekrefte:\n- ingen priser\n\nHva jeg trenger fra deg:\n- lim inn tabellen\n"
with tempfile.TemporaryDirectory() as tmp:
    svar = Path(tmp) / "svar.md"
    for sak in sorted(p for p in CASER.iterdir() if p.is_dir()):
        meta = yaml.safe_load((sak / "case.yml").read_text(encoding="utf-8"))
        if meta["forventet_status"] == "STOPPET":
            svar.write_text(STOPP, encoding="utf-8")
            sjekk(f"{sak.name}: STOPPET-svar gir PASS", kjør(KJOR, sak, svar).returncode == 0)
            continue
        fasit = (sak / "forventet.yml").read_text(encoding="utf-8")
        svar.write_text(svar_med_yaml("KOMPLETT", fasit), encoding="utf-8")
        sjekk(f"{sak.name}: fasit som svar gir PASS", kjør(KJOR, sak, svar).returncode == 0, kjør(KJOR, sak, svar).stdout)
        # Endre første fastledd-pris i den nye perioden: må gi FAIL
        # Bytt første pris i blokken for den nye perioden (gyldig_fra står etter fastledd)
        blokker = fasit.split("  - kundegrupper:")
        endret = [b for b in blokker]
        idx = next(i for i, b in enumerate(blokker) if f"gyldig_fra: '{meta['fra']}'" in b)
        endret[idx] = re.sub(r"(pris: )([0-9.]+)", r"\g<1>12345", blokker[idx], count=1)
        svar.write_text(svar_med_yaml("KOMPLETT", "  - kundegrupper:".join(endret)), encoding="utf-8")
        r = kjør(KJOR, sak, svar)
        sjekk(f"{sak.name}: endret pris gir FAIL", r.returncode == 1, r.stdout)

lysna = CASER / "lysna-2026-08"
fasit = (lysna / "forventet.yml").read_text(encoding="utf-8")
with tempfile.TemporaryDirectory() as tmp:
    svar = Path(tmp) / "svar.md"
    svar.write_text(svar_med_yaml("KOMPLETT", fasit.replace("timer: 6-21", "timer: 6-22")), encoding="utf-8")
    r = kjør(KJOR, lysna, svar)
    sjekk("Lysna: timer 6-22 for «kl. 06-22» gir FAIL", r.returncode == 1 and "unntak" in r.stdout, r.stdout)
    svar.write_text(svar_med_yaml("KOMPLETT", fasit.replace("grunnpris: 26", "grunnpris: 26.03")), encoding="utf-8")
    r = kjør(KJOR, lysna, svar)
    sjekk("Lysna: rundingsstøy 26,03 i stedet for 26 gir FAIL", r.returncode == 1, r.stdout)

print(f"\n{antall - len(feil)} av {antall} sjekker OK")
if feil:
    print("\nFEIL:")
    for f in feil:
        print(" -", re.sub(r"\s+", " ", f)[:300])
    sys.exit(1)
