# Evals for innsamlingsskillen

Testsaker som måler om en modell følger [innsamlingsskillen](../../.agents/skills/samle-tariff/).
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
| `foie-2026-11-motsigelse` | STOPPET | Kolonnene inkl. og eks. mva stemmer ikke for trinn 8 (2062,5 mot 2450), modellen må ikke velge selv |

Sakene er valgt for å dekke ulike situasjoner, og alle KOMPLETT-sakene bygger på en gjennomgått PR
(`eksisterende.yml` er filen før, `forventet.yml` filen etter). Kildeteksten er hentet på nytt fra
netteierens side, og `verifiser_kilde.py` bekrefter at hver pris i fasiten har belegg i den.
`lysna-2026-08` følger PR #398, men med `6-21` for «kl 06-22». Det ble rettet i `tariffer/lysna.yml` i #421.

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

## Resultater

Kjøring: 2026-11-23, én kjøring per sak. «Priser uten belegg» er antall priser i svaret som
`verifiser_kilde.py` ikke finner i `input.md` (mål på hallusinasjoner). `–` betyr ikke kjørt ennå.

| Sak | Forventet | Claude Sonnet 5.5 (`claude-sonnet-5-5`) | GPT (modell og versjon: ______) |
|---|---|---|---|
| `midtnett-2026-10` | KOMPLETT | PASS (0 uten belegg) | – |
| `kystnett-2026-10` | KOMPLETT | PASS (0 uten belegg) | – |
| `lysna-2026-08` | KOMPLETT | PASS (0 uten belegg) | – |
| `glitre-2026-10` | KOMPLETT | PASS (0 uten belegg) | – |
| `mellom-2026-09` | KOMPLETT | PASS (0 uten belegg) | – |
| `midtnett-uten-priser` | STOPPET | PASS | – |
| `kystnett-naring-bilde` | STOPPET | PASS | – |
| `sae-kun-pdf` | STOPPET | PASS | – |
| `foie-2026-11-motsigelse` | STOPPET | PASS | – |
| **Totalt** | | **9 av 9 PASS** | – |

Dato for GPT-kjøringen: ______

**Kommentarer (Sonnet)**

- Alle ni sakene besto på første forsøk. Ingen feil som skillen burde ha forhindret, så ingen nye issues
  eller evalsaker kom ut av denne kjøringen.
- `foie-2026-11-motsigelse`: fant avviket i trinn 8 med `sjekk_kolonner.py`, foreslo ingen verdi selv.
- `midtnett-2026-10`: rettet de uavrundede fastleddene fra forrige periode (3964,8 og 9004,8) til 3960 og 9000, og
  sa fra om det under «Justerte verdier».
- Én kjøring per sak sier lite om variasjon mellom kjøringer. Kjør gjerne hver sak flere ganger.

### Slik kjørte vi dette (reproduserbart)

`kjor.py` kjører ikke modellen, så hver sak ble kjørt slik:

1. Lag en egen mappe per sak med bare det modellen skal se: en kopi av `.agents/` (skillen), `tariff.cue`,
   `tariff-eksempel.yml`, `.yamlfmt.yml`, `scripts/prissignal.py`, sakens `case.yml` og `input.md`, og
   `eksisterende.yml` som `tariffer/<selskap>.yml`. **Ikke** ta med `forventet.yml`, `notat.md` eller resten av
   `evals/`, ellers kan modellen lese fasiten.
2. Be modellen jobbe bare i mappen: les `SKILL.md` og referansene, gjør oppgaven i `case.yml` med `input.md` som
   kilde (ingen nettilgang), og lagre hele svaret i `svar.md`. Skriv ingen YAML til `tariffer/`, og ingen commit eller PR.
3. Vurder fra repoets rot:

```bash
venv/bin/python evals/llm-innsamling/kjor.py evals/llm-innsamling/caser/<sak> <sandkasse>/svar.md
```

Sonnet ble kjørt som subagent i Claude Code (modellvalg `sonnet`) med instruksen i steg 2. For GPT: bruk
samme mapper og samme instruks i en agent med filtilgang og shell (for eksempel Codex CLI), eller lim inn
skillen, `case.yml` og `input.md` i en chat og lagre svaret i en fil. Chat-varianten kan ikke kjøre
`valider.sh` selv, så den er strengere. Noter hvilken variant som ble brukt.

## Legge til en sak

1. Lag en mappe under `caser/` og fyll ut filene over.
2. `forventet.yml` skal være et resultat et menneske har gjennomgått, for eksempel fra en mergad PR.
3. Test saken: `kjor.py` skal gi PASS på en riktig fasit-som-svar og FAIL på et svar med en
   endret pris.

Legg gjerne til en sak hver gang en modell gjør en feil skillen burde ha forhindret.
