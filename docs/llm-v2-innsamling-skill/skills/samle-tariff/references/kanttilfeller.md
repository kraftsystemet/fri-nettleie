# Kanttilfeller

## Selskapet har byttet navn

Norske netteiere bytter navn av og til. Før du oppretter en ny fil for et selskap du ikke finner:

1. Søk på `gln` og `netteier` i `tariffer/` og i `tariffer/old/`.
2. Søk i issues etter «heter nå», «heter egentlig» og «byttet navn».
3. Er det samme juridiske enhet: `git mv tariffer/<gammel>.yml tariffer/<ny>.yml`, oppdater
   `netteier` og `kilder`, behold `gln`. Én PR kan løse både navnebyttet og prisene.

Presedenser: #403 (`telemark.yml` ble `tnett.yml`, med nye priser i samme PR) og de lukkede
sakene #325, #165, #114 og #50. Er du usikker på om det er samme enhet: STOPPET og spør.

## Selskapet er opphørt eller fusjonert

Filer for selskaper som er opphørt eller fusjonert flyttes til `tariffer/old/` i stedet for å
slettes (se `tariffer/old/README.md`). Kundene dekkes av overtakeren. Gjør ikke dette uten at
en sak eller brukeren sier det.

## Flere tariffer hos samme netteier

Noen har ulike tariffer for ulike deler av nettet (for eksempel etter sammenslåing). Formatet har
to mekanismer: `mga` (nettavregningsområde) på tariffen, og `navn` på tariffen. I dataene i dag er
det ikke brukt slik: bare de gamle filene i `tariffer/old/` bruker `mga`. Aktive filer har **én fil
per område**, med området i navnet (`area-lega.yml`, `area-nettinord.yml`, `tensio-tn.yml`), og
`tensio-*` bruker i tillegg `navn`. Gjelder kilden flere områder, må du vite hvilket område oppgaven
gjelder. Er det uklart: STOPPET. Innfør ikke `mga` uten at en sak eller brukeren ber om det.

## Sesong, helligdager og dag/natt

Bruk `unntak` med `måneder`, `dager` og `timer` (se format.md). Merk at
`scripts/prissignal.py` bare håndterer noen av kombinasjonene. Kilden avgjør, ikke skriptet.
Står helligdager i kilden og prisen skiller på dem, bruk `fridag` eller `helligdager`.

## Enhet: kr/mnd eller kr/år

Filene bruker kr/år. Konverter kr/mnd med `utled_avgifter.py fastledd` og sjekk at
**uendrede** trinn fra forrige periode gir nøyaktig samme tall. Gjør de ikke det, er enten
enheten eller tolkningen feil. STOPPET.

## Fastledd som ikke er trinn

Har kilden en fast pris uten trinn, bruk ett trinn med `terskel: 0`. Kilder som oppgir
fastleddet som fast beløp per kunde og et separat effektledd hører ikke hjemme i formatet
(effektledd samles ikke inn). Si fra og stopp hvis det er hele tariffen.

## Uendrede priser

Har forrige periode ingen `gyldig_til`, gjelder den fortsatt, og det trengs ingen ny periode.
Oppdater `sist_oppdatert` (og `kilder` om nødvendig) og si fra at prisene er uendret.
Har forrige periode en `gyldig_til` som er passert eller nådd, blir det et hull i dataene
hvis du ikke legger til en ny periode. Da er det brukeren som avgjør hva som skal gjøres.

## Priser som synker eller hopper

Store endringer er ikke feil i seg selv, men kilden må belegge dem (Midtnetts økning fra 18,86
til 26 øre hadde en forklaring på siden). Se `sammenlign_forrige.py`. Finner du ikke
begrunnelsen i kilden, og endringen er stor, er det grunn til å dobbeltsjekke transkriberingen.
