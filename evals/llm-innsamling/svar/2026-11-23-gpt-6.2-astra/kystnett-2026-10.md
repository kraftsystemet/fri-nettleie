Status: KOMPLETT

Kystnett AS, sak #413: Fra 1. oktober 2026 er energileddet for husholdninger og fritidsboliger **17 øre/kWh uten avgifter** hele døgnet. Fastleddet øker på alle ti trinn.

Kilde: `input.md`, utdrag fra [Kystnetts prisside for privatkunder](https://kystnett.no/Nettleie/?Article=68), hentet 21. september 2026. I tabellen gjelder beløpene før parentesen fra 1. oktober. Beløpene i parentes gjelder januar–september 2026.

| Verdi uten avgifter | Kilde og utregning | Type |
|---|---|---|
| Energiledd: 17 øre/kWh | 25,13 − 7,13 i elavgift − 1 i Enovaavgift; ingen mva. | Utledet |
| Fastledd 0–5 kWh/t: 6 096 kr/år | «508 (493)»: 508 kr/mnd × 12 | Utledet |
| Fastledd 5–10 kWh/t: 10 992 kr/år | «916 (890)»: 916 kr/mnd × 12 | Utledet |
| Fastledd 10–15 kWh/t: 15 888 kr/år | «1 324 (1 286)»: 1 324 kr/mnd × 12 | Utledet |
| Fastledd 15–20 kWh/t: 20 796 kr/år | «1 733 (1 682)»: 1 733 kr/mnd × 12 | Utledet |
| Fastledd 20–25 kWh/t: 25 692 kr/år | «2 141 (2 079)»: 2 141 kr/mnd × 12 | Utledet |
| Fastledd 25–50 kWh/t: 40 392 kr/år | «3 366 (3 268)»: 3 366 kr/mnd × 12 | Utledet |
| Fastledd 50–75 kWh/t: 64 884 kr/år | «5 407 (5 250)»: 5 407 kr/mnd × 12 | Utledet |
| Fastledd 75–100 kWh/t: 89 376 kr/år | «7 448 (7 231)»: 7 448 kr/mnd × 12 | Utledet |
| Fastledd 100–150 kWh/t: 126 120 kr/år | «10 510 (10 204)»: 10 510 kr/mnd × 12 | Utledet |
| Fastledd 150–200 kWh/t: 175 116 kr/år | «14 593 (14 168)»: 14 593 kr/mnd × 12 | Utledet |

Fastleddmetode: «gjennomsnittet av de tre høyeste døgnmaksene i forrige måned» gir `TRE_DØGNMAX_MND`. «Trinn fra kWh/t» angir inkludert nedre grense: Nøyaktig 5 kWh/t gir for eksempel 10 992 kr/år.

Antakelser: ingen.  
Justerte verdier: ingen. Alle elleve utregningene ga `REN`.  
Kundegrupper: `husholdning` og `fritid` er uttrykkelig omfattet. Kilden oppgir verken at liten næring har samme tariff eller egne priser for gruppen. `liten_næring` er derfor utelatt.

Validering: `valider.sh` godkjente arbeidskopien for `2026-10-01` i sonen `nord_norge`. Alle 11 priser har kildebelegg. Sammenligningen varslet at energileddet synker fra 18 til 17 øre/kWh (−5,6 %). Den nye prisen er dobbeltsjekket: 17 + 7,13 + 1 = 25,13 øre/kWh, nøyaktig som publisert. `prissignal.py` viste 17 øre/kWh i alle timer på startdatoen.

**Hele `tariffer/kystnett.yml`:**

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
