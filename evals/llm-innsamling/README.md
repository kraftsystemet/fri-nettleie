# Evals for innsamlingsskillen

Testsaker som måler om en modell følger [innsamlingsskillen](../../docs/llm-v2-innsamling-skill/).
Dette er **evals**, ikke enhetstester: de vurderer et svar fra en modell, som varierer fra kjøring
til kjøring. De kjøres manuelt og ikke i CI.

## Sakene

| Sak | Forventet | Tester |
|---|---|---|
| `midtnett-2026-10` | KOMPLETT | Priser inkl. mva og avgifter, kr/mnd inkl. mva til kr/år, `liten_næring` slått sammen med husholdning |
| `kystnett-2026-10` | KOMPLETT | Nord-Norge uten mva, kr/mnd til kr/år, `liten_næring` skal ikke med |
| `lysna-2026-08` | KOMPLETT | Rundingsstøy (42,7 gir 26 og ikke 26,03), ulike priser for næring gir egen tariff, «kl. 06-22» blir `6-21` |
| `glitre-2026-10` | KOMPLETT | To perioder på samme side, energiledd inkl. mva men uten avgifter, to desimaler, næring lik privat |
| `mellom-2026-09` | KOMPLETT | Energiledd inkl. mva men uten avgifter, 12 trinn, litt avrundingsforskjell mellom privat og næring |
| `midtnett-uten-priser` | STOPPET | Kilde uten prisdata, modellen må ikke bruke «ca 120 kr» til å regne priser |
| `kystnett-naring-bilde` | STOPPET | Priser i bilder, modellen må ikke overføre privatpriser til næring |
| `sae-kun-pdf` | STOPPET | Prisene står bare i en PDF som det lenkes til |

Sakene er valgt for å dekke ulike situasjoner, og alle KOMPLETT-sakene bygger på en gjennomgått PR
(`eksisterende.yml` er filen før, `forventet.yml` filen etter). Kildeteksten er hentet på nytt fra
netteierens side, og `verifiser_kilde.py` bekrefter at hver pris i fasiten har belegg i den.
`lysna-2026-08` avviker fra den mergede PR-en på ett punkt (timer), som er forklart i `notat.md`.

Hver saksmappe har `case.yml` (oppgave, dato, sone, forventet status), `input.md` (kilden slik den ble
hentet), `eksisterende.yml` (filen før), `forventet.yml` (fasit, bare KOMPLETT-saker) og
`notat.md` (hva saken tester).

Kildeteksten i `input.md` er uttrukket tekst og tabeller fra netteierens offentlige sider, ikke
hele sidene.

## Selvtest

`selvtest.py` sjekker at skriptene gir kjente riktige svar, avviser kjente feil, og at `kjor.py` gir PASS
på riktige og FAIL på gale kunstige svar. Den krever ingen modell:

```bash
venv/bin/python evals/llm-innsamling/selvtest.py
```

## Slik vurderer du et svar

Gi modellen skillen (`SKILL.md` og referansene), oppgaven i `case.yml` og `input.md` som kilde,
og lagre hele svaret i en fil. Deretter fra repoets rot:

```bash
venv/bin/python evals/llm-innsamling/kjor.py \
  evals/llm-innsamling/caser/kystnett-2026-10 svar.md
```

- **KOMPLETT-saker:** svaret må starte med `Status: KOMPLETT`, ha YAML som passerer `cue vet`, samme
  perioder og priser som `forventet.yml`, og hver pris må ha belegg i `input.md`.
- **STOPPET-saker:** svaret må starte med `Status: STOPPET`, ikke inneholde YAML med tariffer, og si
  hva brukeren må gi.

Skriptet skriver PASS eller FAIL og antall priser uten belegg (vårt mål på hallusinasjoner).

## Legge til en sak

1. Lag en mappe under `caser/` og fyll ut filene over.
2. `forventet.yml` skal være et resultat et menneske har gjennomgått, for eksempel fra en mergad PR.
3. Test saken: `kjor.py` skal gi PASS på en riktig fasit-som-svar og FAIL på et svar med en
   endret pris.

Legg gjerne til en sak hver gang en modell gjør en feil skillen burde ha forhindret.
