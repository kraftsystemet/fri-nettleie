Status: KOMPLETT

Kystnett AS, sak #413. Tariffen gjelder fra 1. oktober 2026. Eneste kilde til de nye prisene er `input.md`, utdraget fra [Kystnetts prisside for privatkunder](https://kystnett.no/Nettleie/?Article=68) hentet 21. september 2026.

| Verdi | Kilde (sitat eller tabellrad) | Type |
|---|---|---|
| `gyldig_fra`: 2026-10-01 | «Alle tariffer gjelder fra 01.10.2026.» | Bekreftet |
| `fastledd.metode`: `TRE_DØGNMAX_MND` | «gjennomsnittet av de tre høyeste døgnmaksene i forrige måned» | Bekreftet |
| Fastledd 0–5 kW: 6 096 kr/år | «508» kr/mnd × 12 | Utledet |
| Fastledd 5–10 kW: 10 992 kr/år | «916» kr/mnd × 12 | Utledet |
| Fastledd 10–15 kW: 15 888 kr/år | «1 324» kr/mnd × 12 | Utledet |
| Fastledd 15–20 kW: 20 796 kr/år | «1 733» kr/mnd × 12 | Utledet |
| Fastledd 20–25 kW: 25 692 kr/år | «2 141» kr/mnd × 12 | Utledet |
| Fastledd 25–50 kW: 40 392 kr/år | «3 366» kr/mnd × 12 | Utledet |
| Fastledd 50–75 kW: 64 884 kr/år | «5 407» kr/mnd × 12 | Utledet |
| Fastledd 75–100 kW: 89 376 kr/år | «7 448» kr/mnd × 12 | Utledet |
| Fastledd 100–150 kW: 126 120 kr/år | «10 510» kr/mnd × 12 | Utledet |
| Fastledd 150–200 kW: 175 116 kr/år | «14 593» kr/mnd × 12 | Utledet |
| `energiledd.grunnpris`: 17 øre/kWh | «25,13» − 7,13 øre/kWh elavgift − 1 øre/kWh Enova | Utledet |

**Antakelser:** Den ene oppgitte energiprisen gjelder hele NT4-tabellen; kilden viser ingen andre energipriser eller tidsunntak. Felles trinngrenser følger formatregelen og forrige periode: nøyaktig på en terskel gjelder det høyere trinnet (`terskel_inkludert: true`). Formatet lagrer bare nedre grenser, så 200 kW er ikke en egen terskel. `sist_oppdatert` er datoen kildeutdraget ble hentet. Parentesprisene gjelder før 1. oktober og er ikke brukt som nye priser. Forrige registrerte periode får eksklusiv sluttdato 2026-10-01; ingen mellomperiode opprettes.

**Justerte verdier:** Ingen avrundingsjusteringer. `utled_avgifter.py` ga `REN` for alle elleve priser. I sonen `nord_norge` er det ingen mva. for privatkunder, og de to oppgitte avgiftene per kWh trekkes bare fra energileddet.

**Kundegrupper:** `husholdning` og `fritid`, som begge er uttrykkelig dekket. Ingen av de to reglene for å ta med `liten_næring` er oppfylt: omtalen av bestemte næringskoder i privatkundedefinisjonen dokumenterer ikke samme tariff for lavspente næringskunder under 100 MWh/år, og utdraget gir ingen egen næringstabell.

**Validering:** `valider.sh` ga `VALIDERING OK` med den foreslåtte tariffen på en arbeidskopi, `--fra 2026-10-01`, `--sone nord_norge` og et ordrett kildeutdrag. Alle 11 priser hadde belegg. Kildesjekken matcher tall, ikke riktig tabellrad, terskel eller dato; disse ble kontrollert separat mot `input.md`. Kontrollene for økende trinn og sammenhengende perioder ble også kjørt direkte på arbeidskopien. `prissignal.py` valgte den nye perioden og viste 17 øre/kWh uten tidsunntak.

**Advarsel fra periodesammenligningen:** Energileddet synker fra 18 til 17 øre/kWh (−5,6 %). Den nye verdien er kontrollert mot den publiserte prisen: 17 + 7,13 + 1 = 25,13 øre/kWh. Kilden oppgir ingen årsak til nedgangen. Alle ti fastledd øker; parentesprisene ganger 12 stemmer med de registrerte fastleddene i forrige periode.

**Full foreslått `tariffer/kystnett.yml`:**

```yaml
---
netteier: 'Kystnett AS'
gln:
  - '7080010000064'
sist_oppdatert: '2026-09-21'
kilder:
  - 'https://kystnett.no/Nettleie'
  - 'https://kystnett.no/Nettleie/?Article=68'
tariffer:
  - kundegrupper:
      - husholdning
      - fritid
    fastledd:
      metode: TRE_DØGNMAX_MND
      terskel_inkludert: true
      terskler:
        - terskel: 0
          pris: 5916
        - terskel: 5
          pris: 10680
        - terskel: 10
          pris: 15432
        - terskel: 15
          pris: 20184
        - terskel: 20
          pris: 24948
        - terskel: 25
          pris: 39216
        - terskel: 50
          pris: 63000
        - terskel: 75
          pris: 86772
        - terskel: 100
          pris: 122448
        - terskel: 150
          pris: 170016
    energiledd:
      grunnpris: 18
    gyldig_fra: '2024-01-01'
    gyldig_til: '2026-10-01'
  - kundegrupper:
      - husholdning
      - fritid
    fastledd:
      metode: TRE_DØGNMAX_MND
      terskel_inkludert: true
      terskler:
        - terskel: 0
          pris: 6096
        - terskel: 5
          pris: 10992
        - terskel: 10
          pris: 15888
        - terskel: 15
          pris: 20796
        - terskel: 20
          pris: 25692
        - terskel: 25
          pris: 40392
        - terskel: 50
          pris: 64884
        - terskel: 75
          pris: 89376
        - terskel: 100
          pris: 126120
        - terskel: 150
          pris: 175116
    energiledd:
      grunnpris: 17
    gyldig_fra: '2026-10-01'
```
