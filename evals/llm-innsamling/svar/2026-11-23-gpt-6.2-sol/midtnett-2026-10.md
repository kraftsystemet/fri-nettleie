Status: STOPPET

**Midtnett AS – nye nettleiepriser fra 2026-10-01 (sak #414).** Prisgrunnlaget er `input.md`, et utdrag fra [Midtnetts prisside](https://midtnett.no/nettleie-informasjon-og-priser/) hentet 2026-09-21. Den eksisterende tariffen er bare brukt til kontroll mot forrige periode.

### Hva jeg ikke kan bekrefte

- **Fritid, kapasitetsledd trinn 6 (25,00–49,99 kW).** `input.md` oppgir 2 096 kr/mnd og sier at kapasitetsleddet er uendret. Forrige periodes 20 112 kr/år ekskl. mva gir derimot `20 112 / 12 × 1,25 = 2 095` kr/mnd inkl. mva. Avrundingssjekken kan gjenskape 2 096 fra 20 124 kr/år, men ikke fra den registrerte uendrede verdien.
- **Mindre næringskunder, avgiftsgrunnlaget.** Energileddet er merket «eks forbruksavgift og enovaavgift», mens teksten under sier at prisene inkluderer disse avgiftene. `sjekk_kolonner.py` bekreftet at 25 % mva alene forklarer begge energiparene (39,13 → 48,91 dag og 34,13 → 42,66 natt) og alle ni fastleddsparene. Det viser hva som skiller kolonnene, men ikke om 7,13 øre/kWh i forbruksavgift ligger i begge energikolonnene eller faktureres separat. Det er heller ikke klart om Enova på 800 kr/år ligger i begge fastleddskolonnene eller kommer i tillegg. Like publiserte tall for husholdning og næring er derfor ikke nok til å slå sammen gruppene.

### Hva jeg trenger fra deg

- Bekreft med Midtnett hvilket kapasitetsledd som gjelder for fritid på trinn 6 fra 1. oktober 2026, helst i kr/mnd ekskl. mva, og om «uendret» eller den tidligere registrerte verdien må korrigeres.
- Lim inn en presisering fra Midtnett som viser om forbruksavgiften ligger i næringens energiledd og om Enova ligger i fastleddet, eller om disse faktureres separat. Entydige dag-, natt- og trinnpriser uten avgifter for mindre næringskunder vil også avklare dette.

Kolonnekontrollen og avrundingssjekken er kjørt. Full tariffvalidering (`valider.sh`) er ikke kjørt fordi avvikene må avklares før det kan skrives en ny periode. Ingen tariff-YAML er endret.
