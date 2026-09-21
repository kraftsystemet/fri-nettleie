# Repo og PR

Gjelder bare når du har tilgang til repoet (filer og git). Uten verktøy, se «Levering» i SKILL.md.

## Modus velges av brukeren

| Modus | Hva du gjør | Når |
|---|---|---|
| **Lokalt (standard)** | Lag gren, endre filen, valider, vis diffen. Stopp. | Alltid, med mindre brukeren ber om mer. |
| **PR** | Som over, og deretter commit, push og åpne PR etter malen under. | Bare når brukeren uttrykkelig ber om PR eller push. |

Du merger **aldri**, uansett hva du blir bedt om. Tillatelser du ikke har fått eksplisitt
(push, PR, sletting av gren) tar du ikke. Å ha fått lov til én ting gir ikke lov til neste.

## Gren og commit

- `git checkout main && git pull`, og lag gren `update-<selskap>-<åååå-mm>` fra oppdatert `main`.
- Én gren og én PR per selskap. Aldri flere selskaper i samme PR.
- Endrer du bare `tariffer/<selskap>.yml` (og evt. `kilder`), er det riktig omfang. Ikke rør
  README eller andre filer. `make` (som oppdaterer README-statusen) kjøres av vedlikeholdere.
- Formater med `yamlfmt` om det er installert (`.yamlfmt.yml` ligger i repoet). Er det ikke det,
  skriv i samme stil som filen har fra før.

## Validering

Bruk `scripts/valider.sh` (se SKILL.md). I tillegg, hvis kommandoen fungerer for filen:

```bash
python3 scripts/prissignal.py --fra <dato> --til <dato+1> --tariff-fil tariffer/<selskap>.yml
```

`prissignal.py` krasjer med `KeyError: 'unntak'` på perioder uten `unntak` (flat energipris).
Det er en kjent feil i skriptet og ikke noe du skal «fikse» med tom `unntak: []`. Skriv i
PR-en at skriptet ikke lot seg kjøre av den grunnen.

## PR-mal

Hold beskrivelsen kort. Avledninger og antakelser hører hjemme i svaret til brukeren, ikke i PR-en.

```
## Summary
- <hva som endret seg, for eksempel «Legger til <selskap> sin nye tariffperiode fra <dato>»>
- Sources:
  - <URL> (<kundegrupper>)

Closes #<issue>

## Test plan
- [x] `cue vet --schema "#Selskap" tariff.cue tariffer/<selskap>.yml` passes
- [x] `scripts/prissignal.py` picks up the new tariffer for dates after <dato>
```

Tittel: «Oppdater <selskap> med nye priser fra <dato>». Ta med `Closes #<issue>` slik at saken
lukkes ved merge. Finnes det et eget navnebytte-issue, ta med `Closes` for begge.
