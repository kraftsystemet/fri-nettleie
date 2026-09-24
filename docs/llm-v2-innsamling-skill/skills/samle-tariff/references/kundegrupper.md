# Kundegrupper

Vi samler inn tre kundegrupper: `husholdning`, `fritid` og `liten_næring`.
`fritid` er hytter og fritidshus. `liten_næring` er lavspente næringskunder med årlig forbruk
under 100 000 kWh (100 MWh). Andre
næringssegmenter (over 100 000 kWh, høyspent, effekttariffer med effektledd)
samles ikke inn og ignoreres.

For liten næring under 100 000 kWh/år er prisen i praksis den samme som for
husholdning. Denne filen sier når det skal stå i dataene.

## Regel: når skal liten_næring med?

Ta `liten_næring` med i samme tariff som `husholdning` (og `fritid`, hvis den har
samme priser) når ett av disse gjelder:

1. **Kilden sier det uttrykkelig.** For eksempel «samme priser for privat- og
   næringskunder under 100 000 kWh».
2. **Kilden oppgir egne priser for liten næring**, og prisene er like etter
   normalisering (se under).

Oppgir kilden egne priser for liten næring som *avviker* fra husholdning, samles
de i en egen tariff med `kundegrupper: [liten_næring]`.

Sier kilden ingenting om næring og har ingen egne næringspriser: ikke legg til
`liten_næring`. Ikke anta at prisene er like.

Har forrige periode en kundegruppe som kilden fortsatt dekker, skal den ikke fjernes
uten grunn. Sier kilden at den er avviklet, si fra i rapporten.

## Normalisering før sammenligning

Sammenlign med samme avgiftsbasis (alt uten avgifter, se avgifter.md) og samme
enhet (kr/år for fastledd). Vanlige falske forskjeller:

- **Enova i fastleddet.** Næring betaler Enova som 800 kr/år, privat 1 øre/kWh.
  Noen netteiere legger de 800 kr/år inn i fastleddet (66,67 kr/mnd). Trekk fra
  før sammenligning.
- **Mva.** Privatkunder i Nord-Norge betaler ikke mva, og næringspriser oppgis
  ofte ekskl. mva. Regn begge til uten avgifter.
- **Redusert elavgift** for enkelte næringskoder (0,6 øre) hører ikke hjemme i tariffen.
- **Avrunding i kilden.** Kilder oppgir kr/mnd i hele kroner. Avvik på inntil ±0,5
  kr/mnd (±6 kr/år) er avrunding, ikke en reell forskjell. Priser er «like» innenfor
  dette. Bruk verdiene fra husholdning i den sammenslåtte tariffen.

## Når prisene er like

Én tariff med alle relevante grupper og alle trinn fra kilden:

```yaml
kundegrupper:
  - husholdning
  - fritid
  - liten_næring
```

Har næring flere trinn øverst enn husholdning, tas alle trinnene med.

## Rapportering

Skriv i svaret hvilken av de to reglene som ga `liten_næring`, og hvilke
justeringer som ble gjort før prisene ble sammenlignet.
