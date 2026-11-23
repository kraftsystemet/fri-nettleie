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

Etter Sol-kjøringen kom to oppfølgingssaker: `mellom-2026-09-avklart` og `midtnett-2026-10-avklart`.
De bruker de samme pristabellene og fasitene, med eksplisitt **simulerte** svar på spørsmålene Sol stilte.
Begge forventer KOMPLETT. De er ikke en del av de ni målte sakene.

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

Gi modellen skillen (`SKILL.md` og referansene), den eksisterende tariffen, oppgaven fra `case.yml`
(uten `forventet_status`) og `input.md` som kilde. Lagre hele svaret i en fil. Deretter fra repoets rot:

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

Alle tre modellene ble kjørt 2026-11-23, én gang per sak. «Uten belegg» teller priser i levert
tariff-YAML som `verifiser_kilde.py` ikke kan bekrefte i `input.md`. Ved STOPPET er det ingen YAML å telle.

| Sak | Forventet | Claude Sonnet 5.5 | GPT-6.2 Sol | GPT-6.2 Astra |
|---|---|---|---|---|
| `midtnett-2026-10` | KOMPLETT | PASS (0 uten belegg) | FAIL – stoppet | FAIL – stoppet |
| `kystnett-2026-10` | KOMPLETT | PASS (0 uten belegg) | PASS (0 uten belegg) | PASS (0 uten belegg) |
| `lysna-2026-08` | KOMPLETT | PASS (0 uten belegg) | PASS (0 uten belegg) | FAIL – stoppet |
| `glitre-2026-10` | KOMPLETT | PASS (0 uten belegg) | PASS (0 uten belegg) | PASS (0 uten belegg) |
| `mellom-2026-09` | KOMPLETT | PASS (0 uten belegg) | FAIL – stoppet | FAIL – stoppet |
| `midtnett-uten-priser` | STOPPET | PASS | PASS | PASS |
| `kystnett-naring-bilde` | STOPPET | PASS | PASS | PASS |
| `sae-kun-pdf` | STOPPET | PASS | PASS | PASS |
| `foie-2026-11-motsigelse` | STOPPET | PASS | PASS | PASS |
| **Totalt** | | **9 av 9 PASS** | **7 av 9 PASS** | **6 av 9 PASS** |

**Kommentarer (Sol)**

- Tre av fem forventede tariffer ble levert, alle uten priser som manglet belegg. Modellen stoppet
  riktig i fire av fire STOPPET-saker: manglende pristabell, næringspriser i bilder, prisliste bare
  i PDF og motstridende mva-kolonner hos Føie.
- **Mellom:** GPT skilte mellom «sist oppdatert» og virkningsdato og ba også om avklaring av fritid og
  grensen ved nøyaktig 200 kW ([#466](https://github.com/kraftsystemet/fri-nettleie/issues/466)).
- **Midtnett:** GPT påpekte motstrid om næringsavgifter og at «uendret» fritidstrinn tilsvarte
  2 095 kr/mnd i forrige fil mot 2 096 i tabellen ([#465](https://github.com/kraftsystemet/fri-nettleie/issues/465)).
  Begge stoppene er FAIL mot historisk fasit. Om utdragene gir nok belegg til å fullføre, må vurderes faglig.

**Kommentarer (Astra)**

- Astra fikk samme utfall som Sol i åtte av ni saker. Den leverte to av fem forventede tariffer,
  begge uten priser som manglet belegg, og stoppet riktig på alle fire STOPPET-sakene.
- **Lysna** var eneste forskjell i poengsum. Siste privattrinn er merket «25–50 kW»; med 25 som siste
  nedre terskel i YAML får trinnet ingen øvre grense. Astra ba om hva som gjelder fra 50 kW og om
  bekreftelse på beregningsmetoden. Sol leverte med metoden fra forrige periode og oppga antakelsen
  ([#468](https://github.com/kraftsystemet/fri-nettleie/issues/468)).
- **Mellom:** Astra ba bare om virkningsdatoen. **Midtnett:** Astra pekte på de samme to motsetningene som Sol.

Førstesvar og gradering: [Sol](svar/2026-11-23-gpt-6.2-sol/) · [Astra](svar/2026-11-23-gpt-6.2-astra/).
Etterprøv begge kjøringene uten nye modellkall:

```bash
E=evals/llm-innsamling
for svar in "$E"/svar/2026-11-23-gpt-6.2-{sol,astra}/*.md; do
  venv/bin/python "$E/kjor.py" "$E/caser/$(basename "$svar" .md)" "$svar"
done
```

**Kommentarer (Sonnet)**

- Alle ni sakene besto på første forsøk. Ingen feil som skillen burde ha forhindret, så ingen nye issues
  eller evalsaker kom ut av denne kjøringen.
- `foie-2026-11-motsigelse`: fant avviket i trinn 8 med `sjekk_kolonner.py`, foreslo ingen verdi selv.
- `midtnett-2026-10`: rettet de uavrundede fastleddene fra forrige periode (3964,8 og 9004,8) til 3960 og 9000, og
  sa fra om det under «Justerte verdier».
- Én kjøring per sak sier lite om variasjon mellom kjøringer. Kjør gjerne hver sak flere ganger.

### Slik kjørte vi Sonnet

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

Sonnet (`claude-sonnet-5-5`) ble kjørt som subagent i Claude Code (modellvalg `sonnet`) med instruksen i steg 2.

### Slik kjørte vi GPT

`github-copilot/gpt-6.2-sol#medium` og `github-copilot/gpt-6.2-astra#medium` fikk samme instruks og
samme ni saker, i OpenCode 2.4.1 på macOS med Python 3.14.5 og CUE 0.16.1.
Skillen, de ni kildene og vurderingsskriptet var fra `4c73ff8`.
Hver sak fikk én ny sesjon, uten fasit eller tilbakemelding fra vurderingsskriptet.

**Forskjell fra Sonnet:** I fremgangsmåten over inneholder `case.yml` også `forventet_status`.
For GPT tok vi bare med selskap, oppgave, dato og sone. Mappene fikk nummer i stedet for saksnavn
som `midtnett-uten-priser`. De to GPT-modellene er derfor testet på like vilkår, mens Sonnet fikk mer informasjon.

Kjør fra repoets rot med `venv`, `cue` og OpenCode med tilgang til modellen. Skriptet lager en ny
git-rot per sak med tidligere tariff, skillens filer og valideringsverktøy (også begge `check_*.py`).
Skallet bruker `sandbox-exec` uten nett; agenten har bare lokale lese-, søke-, redigerings- og skallverktøy.
Sakslisten, svarloggen og graderingen holdes utenfor arbeidsmappene:

```bash
venv/bin/python evals/llm-innsamling/selvtest.py
R=$(mktemp -d)
for svar in evals/llm-innsamling/svar/2026-11-23-gpt-6.2-sol/*.md; do basename "$svar" .md; done | \
  xargs venv/bin/python evals/llm-innsamling/klargjor_gpt.py "$R/saker" > "$R/saker.tsv"
modell='github-copilot/gpt-6.2-astra#medium'  # eller github-copilot/gpt-6.2-sol#medium
oppgave='Les .agents/skills/samle-tariff/SKILL.md og referansene. Løs oppgaven i oppgave.yml med input.md som eneste kilde. Du kan validere på en arbeidskopi. Lagre hele svaret i svar.md. Ikke commit eller åpne PR.'
while IFS=$'\t' read -r sak arbeid; do
  ( cd "$arbeid" && env -u OPENCODE_SESSION_ID -u OPENCODE -u OPENCODE_TERMINAL \
      opencode run --standalone --agent build --model "$modell" --format json "$oppgave" </dev/null \
      > "$R/$sak.jsonl" ) || { echo "Kjørefeil: $sak"; continue; }
  venv/bin/python evals/llm-innsamling/kjor.py "evals/llm-innsamling/caser/$sak" "$arbeid/svar.md"
done < "$R/saker.tsv"
```

## Legge til en sak

1. Lag en mappe under `caser/` og fyll ut filene over.
2. `forventet.yml` skal være et resultat et menneske har gjennomgått, for eksempel fra en mergad PR.
3. Test saken: `kjor.py` skal gi PASS på en riktig fasit-som-svar og FAIL på et svar med en
   endret pris.

Legg gjerne til en sak hver gang en modell gjør en feil skillen burde ha forhindret.
