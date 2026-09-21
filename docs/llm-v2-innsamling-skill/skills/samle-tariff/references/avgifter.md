# Avgifter: alle priser skal være uten avgifter

Prisene i datasettet er nettleie **uten** mva, elavgift (forbruksavgift) og Enova.
Mange netteiere oppgir priser med avgifter. Da må avgiftene fjernes riktig.

Satsene står bare i [satser.yml](satser.yml). Ikke skriv satser fra hukommelsen,
og ikke kopier dem inn i andre filer.

## Steg

1. **Finn sonen** til netteierens konsesjonsområde (ikke der du selv er):

   | Sone | Område | Elavgift | Mva |
   |---|---|---|---|
   | `tiltakssonen` | Finnmark og Nord-Troms | nei | nei |
   | `nord_norge` | Resten av Troms og Nordland | ja | nei |
   | `sor` | Sør for Nordland | ja | ja |

   Er du usikker på sonen: STOPPET og spør (se usikkerhet.md).

2. **Finn ut hva kilden har med.** Se etter «inkl. avgifter», «eks. mva», «inkl. mva» eller en
   avgiftstabell. Mva og avgifter (elavgift og Enova) er to uavhengige spørsmål, og alle fire
   kombinasjoner finnes i praksis:

   | Kilden oppgir energileddet | Flagg til skriptet | Eksempel |
   |---|---|---|
   | inkl. mva og avgifter | `--inkl-mva --inkl-avgifter` | Midtnett, Lysna privat |
   | inkl. mva, men avgiftene er egne linjer | `--inkl-mva` | Glitre privat, Mellom privat |
   | ekskl. mva, men inkl. avgifter | `--inkl-avgifter` | Kystnett (Nord-Norge har ikke mva) |
   | ekskl. mva og avgifter | ingen flagg | Glitre og Mellom næring |

   Vær særlig oppmerksom på varianten «inkl. mva, men avgiftene er egne linjer». Da skal du ikke
   trekke fra avgiftene en gang til. Sier ikke kilden noe, og det ikke kan avgjøres av andre
   opplysninger: STOPPET. «Eks. avgifter» i en tabelloverskrift stemmer av og til ikke med
   tallene (Midtnetts næringstabell). Kontroller mot en pris som er oppgitt begge veier.

3. **Regn ut med skriptet, ikke i hodet:**

   ```bash
   # øre/kWh, kilden oppgir 48,91 inkl. mva og avgifter
   python3 docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts/utled_avgifter.py \
     energiledd --pris 48,91 42,66 --dato 2026-10-01 --sone sor --inkl-mva --inkl-avgifter

   # øre/kWh, kilden oppgir 29,34 inkl. mva og har avgiftene som egne linjer
   python3 docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts/utled_avgifter.py \
     energiledd --pris 29,34 --dato 2026-09-01 --sone sor --inkl-mva

   # fastledd: kr/mnd i kilden, kr/år i YAML
   python3 docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts/utled_avgifter.py \
     fastledd --pris 508 916 1324 --sone nord_norge
   ```

   Oppgi prisene nøyaktig slik de står i kilden, med desimalene. Skriptet bruker
   antall desimaler til å sjekke avrundingen.

4. **Les utfallet:**
   - `REN`: et rundt tall gir nøyaktig samme publiserte pris tilbake. Bruk det.
   - `UAVRUNDET`: bare en verdi med desimaler gir prisen tilbake. Bruk den, og si
     fra om det under «Justerte verdier».
   - `INGEN`: ingen verdi gir prisen tilbake. **STOPPET.** Ikke velg noe selv.

## Hvorfor avrundingssjekken

Kilder oppgir priser med 1–2 desimaler. Å dele på 1,25 og trekke fra avgifter
forsterker avrundingen til støy: en riktig pris på 26 kan bli 26,03. Ekte tariffer
settes nesten alltid i runde øre eller kroner. Skriptet prøver derfor de groveste
verdiene først og sjekker at de gir kildens tall tilbake.

## Fallgruver

- **Fastledd er kr/mnd i kilden, kr/år i filene.** Ganger med 12. Bekreft med at
  uendrede trinn fra forrige periode gir samme tall.
- **Enova for næring er 800 kr/år**, ikke øre/kWh. Noen netteiere legger den inn i
  fastleddet (66,67 kr/mnd). Bruk `--trekk-enova-naring` når det gjelder næringspriser.
- **Redusert elavgift** (0,6 øre) for enkelte næringskoder hører ikke hjemme i tariffen.
- **Elavgiften har endret seg flere ganger i året** (2025: 9,79, 16,93, 12,53, og 7,13
  fra 2026). Bruk satsen som gjelder på periodens startdato, ikke dagens.
