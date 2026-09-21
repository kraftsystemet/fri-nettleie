---
name: samle-tariff
description: >
  Samle inn og oppdatere nettleietariffer i fri-nettleie (tariffer/*.yml). Bruk når en
  netteier har nye priser, et issue er merket collecting eller help wanted, eller rådata
  fra en netteiers prisside skal gjøres om til YAML. Nekter å gjette: mangler dataene,
  stopper den og ber om mer. Collects and updates Norwegian grid-tariff YAML for
  fri-nettleie; refuses to guess prices.
---

# Samle inn nettleietariffer

Du oppdaterer én netteiers tariff-fil i fri-nettleie fra deres offentlige prisside.
Prisene brukes av andre. **En manglende pris er bedre enn en gjettet pris.** Les
[usikkerhet.md](references/usikkerhet.md) før du begynner. Det finnes bare to utfall:
`KOMPLETT` eller `STOPPET`, og aldri noe delvis.

## Arbeidsflyt

Gå gjennom stegene i rekkefølge. Hopp aldri over validering.

1. **Finn saken.** Netteier, kilde-URL og filen `tariffer/<selskap>.yml`. Finnes ikke
   filen, sjekk om selskapet har byttet navn før du oppretter en ny
   ([kanttilfeller.md](references/kanttilfeller.md)).
2. **Les formatet og den eksisterende filen.** Les `tariff-eksempel.yml` og `tariff.cue`
   (fasit, og kan ha endret seg siden sist). Noter i filen kundegrupper, fastleddmetode,
   at fastledd lagres i **kr/år**, og forrige periodes `gyldig_fra`.
3. **Hent kilden og transkriber.** Skriv relevante tall og tekst ordrett til
   `kilde-utdrag.md` (i en midlertidig mappe, aldri i repoet). Se [kilder.md](references/kilder.md): bare netteierens egne
   kilder. Ligger prisene i et bilde eller dokument du ikke kan lese som tekst: **STOPPET**.
4. **Avgjør avgifter.** Finn sonen og hva kilden har med. Se
   [avgifter.md](references/avgifter.md). Er det uklart: **STOPPET**.
5. **Utled prisene** med `scripts/utled_avgifter.py`. Utfallet `INGEN`: **STOPPET**.
6. **Velg kundegrupper.** Se [kundegrupper.md](references/kundegrupper.md).
7. **Skriv den nye perioden** (se Format under). Ikke rør eldre perioder, bortsett fra
   `gyldig_til` på den forrige. Ikke fyll inn manglende mellomperioder.
8. **Valider:**
   ```bash
   docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts/valider.sh \
     tariffer/<selskap>.yml --kilde kilde-utdrag.md --fra <YYYY-MM-DD> --sone <sone>
   ```
   Retter du noe, kjør på nytt. Feiler den fortsatt uten at du kan begrunne det: **STOPPET**.
   Advarsler fra sammenligningen med forrige periode må forklares i rapporten.
9. **Lever** i svarformatet i [usikkerhet.md](references/usikkerhet.md).

## Format (kort)

Fasit er `tariff-eksempel.yml` og `tariff.cue`. Sammendrag og detaljer i
[format.md](references/format.md). Det som oftest går galt:

- **Alle priser uten avgifter.** Fastledd i **kr/år** (kilden sier ofte kr/mnd, gang med 12).
- **`grunnpris`** er den generelle prisen når ingen unntak treffer, og typisk den laveste.
  Dyrere (eller billigere) perioder er `unntak`.
- **Tillegg summeres.** Formatet har ikke tillegg. Et «+8 øre i høylast» blir en `pris` lik
  grunnpris + tillegget.
- **Timer** er inklusive: «kl 06–22» skrives `6-21`. Spenn over midnatt (`22-5`) unngås ved å
  velge natt som `grunnpris`.
- **`terskel_inkludert`:** `true` for «2 til 5» eller «2 til 4,99», `false` for «2,01 til 5».
- **`gyldig_til`** er eksklusiv. Sett den på forrige periode lik den nye `gyldig_fra`.
- **`gln`** ukjent: tom liste `[]`, aldri `null`.
- Ny fastleddmodell som ikke finnes i listen: **STOPPET**, formatet må utvides.
- Effektledd og andre næringssegmenter samles ikke inn.

## Levering

Standard er å **stoppe før noe pushes**: lag en gren, gjør endringen, valider og vis
diffen. Åpne PR eller push bare når brukeren uttrykkelig ber om det. Merge aldri. Én PR per
selskap. Se [repo-og-pr.md](references/repo-og-pr.md) for gren, valideringskommandoer og PR-mal.

Bruker du dette uten verktøy (chat): lever KOMPLETT-svaret med YAML-blokken, og la
brukeren kopiere den inn. Du kjører ikke `valider.sh` selv da, så si tydelig at
brukeren må gjøre det, og at tabellen i svaret må sjekkes mot kilden.

## Referanser

- [usikkerhet.md](references/usikkerhet.md): når du skal stoppe, forbudt atferd, svarformat
- [avgifter.md](references/avgifter.md): soner, utledning og avrundingssjekk
- [kundegrupper.md](references/kundegrupper.md): når `liten_næring` skal med
- [format.md](references/format.md): feltene, fastleddmetoder, timer og dager
- [kilder.md](references/kilder.md): tillatte kilder, bilder, PDF og transkribering
- [kanttilfeller.md](references/kanttilfeller.md): navnebytte, flere områder, enhet, uendrede priser
- [repo-og-pr.md](references/repo-og-pr.md): gren, modus, validering og PR-mal
- [satser.yml](references/satser.yml): gjeldende avgiftssatser (eneste sted de står)
