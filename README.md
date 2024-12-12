# Fri nettleie

> Slipp nettleien fri

En _dugnad_ for å samle nettleie-tariffer i det norske kraftsystemet.

<!-- toc -->

- [Åpen og gratis oversikt over nettleiepriser](#apen-og-gratis-oversikt-over-nettleiepriser)
- [Ta kontakt! 👋🏻](#ta-kontakt-%F0%9F%91%8B%F0%9F%8F%BB)
- [Dataene](#dataene)
  * [Prissignal](#prissignal)
- [Mål](#mal)
- [Anti-mål](#anti-mal)
- [Innsamling](#innsamling)
- [Utfordringer](#utfordringer)
  * [Ulike modeller](#ulike-modeller)
  * [Flere tariffer per netteier](#flere-tariffer-per-netteier)
  * [Priser oppgitt med og uten avgifter](#priser-oppgitt-med-og-uten-avgifter)
- [Avgifter](#avgifter)
  * [Enova-avgift](#enova-avgift)
  * [Forbruksavgift - Elavgift](#forbruksavgift---elavgift)
  * [Merverdiavgift](#merverdiavgift)
- [Bidra](#bidra)
  * [Samle data](#samle-data)
  * [Gi besked om feil eller kom med ideer](#gi-besked-om-feil-eller-kom-med-ideer)
  * [Gi oss en stjerne](#gi-oss-en-stjerne)
  * [Si at du bruker våre data](#si-at-du-bruker-vare-data)
- [Dataene i bruk](#dataene-i-bruk)
- [Netteiere](#netteiere)
- [Status](#status)
- [Forvaltere](#forvaltere)
- [Ofte stilte spørsmål](#ofte-stilte-sporsmal)
  * [Hvorfor gidder dere?](#hvorfor-gidder-dere)
  * [Bør ikke noen andre gjøre dette?](#bor-ikke-noen-andre-gjore-dette)
  * [Hva med NVE sine data?](#hva-med-nve-sine-data)
  * [Hva med Nettleie API fra Digin/Elbits?](#hva-med-nettleie-api-fra-diginelbits)
- [Lisens](#lisens)

<!-- tocstop -->

## Åpen og gratis oversikt over nettleiepriser

Nettleie er en del av [strømregningen](https://snl.no/str%C3%B8mregning) som går
til det lokale nettselskapet.
[Nettleie-tariffer skal være lett tilgjengelig for nettkundene](https://lovdata.no/forskrift/1999-03-11-302/§13-5),
men praksis i dag er at den distribueres av nettselskaper på mange ulike måter
og formater. Selv om det finnes
[gode initiativer](https://elhub.no/elhub-planlegger-a-tilby-en-felles-losning-for-distribusjon-av-nettariffer/),
[statistikk](https://api.nve.no/doc/nettleiestatistikk/),
[datasett](https://biapi.nve.no/nettleietariffer/swagger/index.html),
[kommersielle](https://docs.hark.eco/docs/developers/delivery-charge-api/)
[løsninger](https://stromradar.no/zohmapi/) og
[standarder for deling av nettleie](https://github.com/3lbits/API-nettleie-for-styring)
finnes det ikke noen åpen, gratis oversikt over nettleie på tvers av alle
nettselskaper i Norge som er oppdatert, uten feil og som inneholder både tariffmodeller og
prissignal.

Dette prosjektet bruker kraften av en nettdugnad for å samle og systematisere
nettleie-priser for hele landet. **De innsamlede dataene er gratis og åpent
tilgengelig på standardisert format her på GitHub.** Hensikten er å legge til rette for at

* privatpersoner og selskaper skal kunne lage tekniske løsninger som viser
  kostnad eller styrer strømforbruk basert på nettleie.
* alle interesserte kan analysere dataene for eksempel for å se forskjeller mellom nettselskaper.

At sluttkunder får oversikt over alle komponentene i strømregningen er viktig
for energiøkonomisering, men det er vanskelig å oppnå uten at dataene er lett
tilgjengelig for hele Norge. Lett tilgjengelige data vil legge til rette for at
nettkundene reagerer på prissignalene i nettleien og styrer sitt forbruk på en
måte som hjelper nettet samtidig som de sparer penger.

## Ta kontakt! 👋🏻

Har du bruk for nettleie-data? Da ønsker vi å snakke med deg for å lære mer om
hva du trenger og ønsker! Er det noe som mangler for at du kan ta dataene i bruk?

Kom i kontakt med oss ved å bruke vårt
[kontaktskjema på tally.so](https://tally.so/r/wol2v1) eller åpne et issue her
på GitHub.

## Dataene

Dataene finner du under [tariffer](./tariffer/) som yaml-filer. Dataene
inneholder en beskrivelse av fastledd og energiledd uten avgifter.

Vi samler inn data per netteier og vil gjøre tilgjengelig data per
nettavregningsområde.

### Prissignal

Selv om tariff-dataene kun inneholder en _beskrivelse_ av tariffen er det fullt
mulig å lage en tidsserie - prissignal - basert på dette.

Et skript som viser hvordan dette kan gjøres konseptuelt finnes i
[skript/prissignal.py](./skript/prissignal.py). Brukes slik:

```bash
./skript/prissignal.py --fra 2024-10-26 --til 2024-10-28 --tariff-fil tariffer/midtnett.yml
./skript/prissignal.py --fra 2024-10-25 --til 2024-10-28 --tariff-fil tariffer/griug.yml
```

Dette prissignalet er uten alle avgifter. Det er mulig å beregne avgift basert
på når og hvor (hvilken kommune) forbruket er. Se [avsnittet om avgifter](#avgifter).

Et annet eksempel finnes på
[visningssidene for tariffene på kraftsystemet.no](https://kraftsystemet.no/fri-nettleie/tariffer/).
Der viser vi også en forenklet bereging av avgifter.

## Mål

- [x] Samle strukturdata for å identifisere alle netteier og nettområder
- [x] Definere format for innsamling
- [x] Vise at det kan genereres prissignal basert på formatet
- [x] Samle tariffer for private husholdninger og hytter/fritidseiendom på yaml
  format for et utvalg nettselskaper (med varierende tariffer)
- [x] Overvåke nettselskapenes sider for å varsle ved endring
- [x] Sammenstille og publisere informasjon per netteier på et "menneskelig" format på kraftsystemet.no/fri-nettleie
- [x] Publisere visualisert prissignal basert på de innsamlede tariffene
- [ ] Samle tariffer for husholdninger og hytter/fritidshus for alle nettområder
- [ ] Kontinuerlig oppdatere dataene ved endring hos nettselskapene
- [ ] Maskinlesbare filer for avgifter

## Anti-mål

Selv om det kan være nyttig er det følgende foreløpig ikke en del av dette
prosjektet

* tariffer for næring
* tariff for ikke automatisk avlesning
* vedlikeholde historiske priser

## Innsamling

Dataene i dette prosjektet samles inn manuelt fra netteiers hjemmesider og
lignende. Automatisk scraping er ikke et mål og det oppfordres til å unngå bruk av
roboter for innsamling. Vi respekterer andres systemer og immatrielle rettigheter og bruker
f.eks. ikke data fra andre kommersielle aktører som leverer samme type data.

Kilde-dataene som vi henter fra netteierne er
[offentlig eiendom/allemannseie/public domain](https://no.wikipedia.org/wiki/Offentlig_eiendom).
Tariffer og vilkår gjøres tilgjengelig fra netteierne i henhold til
[Forskrift om kontroll av nettvirksomhet](https://lovdata.no/dokument/SF/forskrift/1999-03-11-302/KAPITTEL_5-1#%C2%A713-5).
Vi samler og sammenstiller tariffene på vårt format og lisensierer datasettet
under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.no) som
krever navngivelse. Det er viktig at dataene som samles inn er public domain.
Det betyr f.eks. at vi ikke kan bruke andre sammenstilte datasett, APIer eller
lignende dersom det ikke eksplisitt er angitt som public domain.

Vi har også et verktøy som kan brukes ved innsamling som finnes på på
[kraftsystemet.no/fri-nettleie/innsamler/](http://kraftsystemet.no/fri-nettleie/innsamler/).

## Utfordringer ved innsamling

Ved innsamling og struktuering av data møter vi noen (overkommelige)
utfordringer. Kort fortalt er det variasjon i både tariffene og hvordan de
presenteres som gjør det lett å gjøre feil ved innsamling.

### Ulike modeller

Det eksisterer flere ulike modeller for nettleie. Det kan for eksempel være
forskjellige priser i løpet av døgnet,
[sesonger](https://fagne.no/kunde-og-nettleie/nettleie-priser-og-vilkar/priser-privatkunder/),
[brukstidstillegg](https://www.griug.no/om-nettleie-og-priser/priser/nettleiepriser-2024/) eller
[forskjell mellom hverdag og helg/helligdager](https://www.elvia.no/nettleie/alt-om-nettleiepriser/nettleiepriser-for-privatkunder/).

For fastleddet finnes det også flere modeller. For eksempel at fastledd regnes
ut
[fem høyeste effektene, løpende siste 12 mnd](https://www.fjellnett.no/nettleie/avtaler-og-vilkar/fellesbestemmelser/)
til forskjell fra den mer vanlige
[tre timene i måneden med høyest forbruk](https://norgesnett.no/kunde/ny-nettleie/).
I tilleg er det noen som oppgir priser per år mens andre per måned, samt om de
ulike trinnene er "til og med" eller "opp til, men ikke med".

### Flere tariffer per netteier

Noen netteiere har ulike tariffer for ulike deler av sitt nett. Dette er typisk
dersom det har vært sammenslåing av konsesjonsområder.

### Priser oppgitt med og uten avgifter

Ved innsamling av tariffer er det utfordrende for innsamling når noen netteiere
gjør tilgjengelig sine priser med avgifter, mens andre ikke inkluderer avgifter.
Avgiftsnivået er forskjellig avhengig av hvor i landet en netteier er
konsesjonær - det er fort å gjøre feil.

## Avgifter

Det er tre avgifter som gjelder for nettleie:

* Enova-avgift
* Elavgift/Forbruksavgift
* Merverdiavgift

Enova-avgiften gjelder alle, men forbruk- og merverdiavgiften er avhenging av
hvor i landet forbruket er. De følgende underkapitlene beskriver de tre
avgiftene, men i praksis deles landed inn i tre deler.

* Tiltakssonen i Finnmark og Nord-Troms - hverken elavgift eller moms
* Resten av Troms og Nordland - elavgift, men ikke moms
* Alle fylker sør for Nordland - alle avgifter

### Enova-avgift

[Forskrift om Energifondet](https://lovdata.no/dokument/SF/forskrift/2001-12-10-1377)
sier at netteier skal legge et påslag på tariffen til alle sluttbrukere på alle
nettnivåer når det faktureres.

> For husholdningsbruk skal påslaget utgjøre 1 øre/kWh.

Inkludert moms blir avgiften 1,25 øre/kWh.

### Forbruksavgift - Elavgift

En avgift på strøm som betales til netteier og netteier viderefører til Skatteetaten.

[Forskrift om særavgifter](https://lovdata.no/dokument/SF/forskrift/2001-12-11-1451/KAPITTEL_3-12#KAPITTEL_3-12)
fastsetter at avgift på elektrisk kraft settes ved
[stortingsvedtak](https://lovdata.no/register/stortingsvedtak).
[Vedtaket for 2024](https://lovdata.no/dokument/STV/forskrift/2023-12-14-2075/KAPITTEL_14#KAPITTEL_14)
fastsetter også lavere avgift for jan-mars og redusert sats for en del næringer.

Personer som bor i
[tiltakssonen i Finnmark og Nord-Troms](https://www.regjeringen.no/no/tema/kommuner-og-regioner/regional--og-distriktspolitikk/Berekraftig-regional-utvikling-i-nord/virkemidler-i-tiltakssonen/id2362290/)
har fritak for el-avgift på forbruk.

### Merverdiavgift

Vanlig moms på 25% betales på nettleie, Enova-avgiften og Elavgiften.

Det er
[fritak for mva i Nord-Norge](https://www.skatteetaten.no/rettskilder/type/handboker/merverdiavgiftshandboken/2020/M-6/M-6-6/)
- Nordland, Troms og Finnmark.

## Bidra

Vi trenger all den hjelp vi kan få!

### Samle data

Status-lista under viser at det er mange nettselskaper igjen å samle data for!
Velg et nettselskap og finn fram nettleien deres. Formatet er formalisert i
filen [tariff-eksempel.yml](./tariff-eksempel.yml) og kan valideres med
[cue](https://cuelang.org/) basert på [tariff.cue](./tariff.cue). Du bør se på
noen av de allerede innsamlede tariffene for å få en følelse av formatet.

Primært ønsker vi at bidrag gjøres gjennom pull-requests. Men du kan også åpne
et issue eller levere [kontaktskjema på tally.so](https://tally.so/r/wol2v1).
Alle bidrag teller!

### Gi beskjed om feil eller kom med ideer

Dersom du ser feil i dataene, status eller annet - åpne et issue her på GitHub
eller bruk vårt [kontaktskjema på tally.so](https://tally.so/r/wol2v1)! Det
samme gjelder om du har gode ideer om hvordan vi kan samle inn og/eller
strukturere data.

### Gi oss en stjerne

Det holder oss motivert!

### Si at du bruker våre data

Se under.

## Dataene i bruk

Dette avsnittet viser et utvalg av hvor dataene er i bruk.

* [Slipper](https://slipper.no/) har brukt dataene i sin app siden desember 2024 📈

## Netteiere

Vi samler inn nettleie-tariffer per netteier. Listen over netteiere er
fra [eSett Open Data](https://opendata.esett.com/dso) som er en kontinuerlig
oppdatert liste over nåværende netteiere. Dette er ikke en statisk liste, men
endrer seg over tid. Elhub publiserer informasjon om endring av f.eks.
[navn](https://elhub.no/aktorer-og-markedsstruktur/opprette-endre-og-avslutte-aktorer/navneendringer-for-nettselskap/)
og
[nettavregningsområder](https://elhub.no/aktorer-og-markedsstruktur/opprette-endre-og-avslutte-aktorer/planlagte-strukturendringer/).

Noen netteiere er ikke med i listen
siden de ikke har private sluttkunder. Vi filtrerer ved hjelp av en
[ignoreringsliste](./.statusignore).

Netteiere i Norge identifiseres med Global Location Number (GLN). Øsnker du å
vite organisasjonsnummeret kan du se på
[referansedataene fra Elhub](./referanse-data/elhub/grid_owners.json).

I noen
tilfeller kan det være avvik mellom områdekonsesjonærer i
[NVEs kartkatalog](https://kartkatalog.nve.no/) og eSett/Elhub. Dette skyldes
oftes etterslep i registrering mellom systemene. Vi vil alltid bruke eSett som
autoritativ kilde.

## Status

<!-- statusstart -->

Vi har samlet data for 61 av 79 netteiere 🥳!

Dette dekker ~95.9% (2524371 av 2632326) av private husholdninger* 🎉.

<table>
    <tr>
        <th>Navn</th>
        <th>GLN</th>
        <th>Antall*</th>
        <th>Oppdatert</th>
        <th>Handling</th>
    </tr>
<tr>
  <td>AS Saudefaldene Nett</td>
  <td>7080003674630</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBUyBTYXVkZWZhbGRlbmUgTmV0dCIsICJnbG4iOiBbIjcwODAwMDM2NzQ2MzAiXX0=' title='Samle inn data for AS Saudefaldene Nett' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Alut AS ✅</td>
  <td>7080010004383</td>
  <td><em>10569</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDQzODMiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly9hbHV0Lm5vL25ldHRsZWllLyJdLCAibmV0dGVpZXIiOiAiQWx1dCBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTMuMX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIk9WX1RSRUZBU0UiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMzUwMCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNDUwMCwgInRlcnNrZWwiOiAxMjV9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Alut AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/alut.html" title="Se på tariffen for Alut AS" target="_blank">🔍</a>
    <a href="./tariffer/alut.yml" title="Se dataene for Alut AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Area Nett AS</td>
  <td>7080004087071</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBcmVhIE5ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDA0MDg3MDcxIl19' title='Samle inn data for Area Nett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Arva AS ✅</td>
  <td>7080005051859</td>
  <td><em>62848</em></td>
  <td><code>2024-11-27</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBcnZhIEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MTg1OSIsICI3MDgwMDA1MDUxMzYxIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI3IiwgImtpbGRlciI6IFsiaHR0cHM6Ly9hcnZhLm5vL2hqZW0vUHJpc2VyIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDEtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTAyMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjQxMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDc3Nn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDcxNDB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA5NTA0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTE4Njh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzY2NH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM1NDYwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDcyNTZ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzEzNDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMS42LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjMuMX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Arva AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/arva.html" title="Se på tariffen for Arva AS" target="_blank">🔍</a>
    <a href="./tariffer/arva.yml" title="Se dataene for Arva AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Arva AS (tidligere Nordlandsnett) ✅</td>
  <td>7080005051361</td>
  <td><em>32212</em></td>
  <td><code>2024-11-27</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBcnZhIEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MTg1OSIsICI3MDgwMDA1MDUxMzYxIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI3IiwgImtpbGRlciI6IFsiaHR0cHM6Ly9hcnZhLm5vL2hqZW0vUHJpc2VyIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDEtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTAyMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjQxMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDc3Nn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDcxNDB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA5NTA0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTE4Njh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzY2NH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM1NDYwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDcyNTZ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzEzNDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMS42LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjMuMX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Arva AS (tidligere Nordlandsnett)' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/arva.html" title="Se på tariffen for Arva AS (tidligere Nordlandsnett)" target="_blank">🔍</a>
    <a href="./tariffer/arva.yml" title="Se dataene for Arva AS (tidligere Nordlandsnett) i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Asker Nett AS ✅</td>
  <td>7080003858825</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-27</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBc2tlciBOZXR0IiwgImdsbiI6IFsiNzA4MDAwMzg1ODgyNSJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNyIsICJraWxkZXIiOiBbImh0dHBzOi8vYXNrZXJuZXR0Lm5vL25ldHRsZWllLW9nLXByaXNlci8iLCAiaHR0cHM6Ly9hc2tlcm5ldHQubm8vcHJpc2xpc3RlLWZvci1wcml2YXRrdW5kZXItaS0yMDI0LyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTAxLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDE3NzZ9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIyMDh9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDMyNjR9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA2ODE2fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogODU5Mn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDEwODQ4fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTUzNjB9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNDM4NH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDMyNDQ4fSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDUxODQwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTUuODg4LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjMuODg4fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIn1dfQ==' title='Samle inn data for Asker Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/asker-nett.html" title="Se på tariffen for Asker Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/asker-nett.yml" title="Se dataene for Asker Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>BKK AS ✅</td>
  <td>7080005051378</td>
  <td><em>221627</em></td>
  <td><code>2024-11-27</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCS0sgQVMgIiwgImdsbiI6IFsiNzA4MDAwNTA1MTM3OCJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNyIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmJray5uby9hbHQtb20tbmV0dGxlaWUvbmV0dGxlaWVwcmlzZXIiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wNC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAxNTM2fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNDk2fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0MTI4fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNTk1Mn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDc2ODB9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA5MzYwfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTc5NTJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNjQ5Nn0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDM1MDQwfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDY5MTIwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTkuNzc2LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3Qgdmlya2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjkuOTYsICJkYWdlciI6IFsidmlya2VkYWciXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNC0wMSJ9XX0=' title='Samle inn data for BKK AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/bkk.html" title="Se på tariffen for BKK AS" target="_blank">🔍</a>
    <a href="./tariffer/bkk.yml" title="Se dataene for BKK AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Barents Nett AS</td>
  <td>7080005051934</td>
  <td><em>7925</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCYXJlbnRzIE5ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDA1MDUxOTM0Il19' title='Samle inn data for Barents Nett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Bindal Kraftlag Nett</td>
  <td>7080005055963</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCaW5kYWwgS3JhZnRsYWcgTmV0dCIsICJnbG4iOiBbIjcwODAwMDUwNTU5NjMiXX0=' title='Samle inn data for Bindal Kraftlag Nett' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Breheim Nett</td>
  <td>7080010010919</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCcmVoZWltIE5ldHQiLCAiZ2xuIjogWyI3MDgwMDEwMDEwOTE5Il19' title='Samle inn data for Breheim Nett' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Bømlo Kraftnett AS</td>
  <td>7080010002327</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCXHUwMGY4bWxvIEtyYWZ0bmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMTAwMDIzMjciXX0=' title='Samle inn data for Bømlo Kraftnett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>DE Nett AS</td>
  <td>7080010003614</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJERSBOZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwMzYxNCJdfQ==' title='Samle inn data for DE Nett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Elinett AS ✅</td>
  <td>7080005053044</td>
  <td><em>23927</em></td>
  <td><code>2024-12-07</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbGluZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MzA0NCJdLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5lbGluZXR0Lm5vL2t1bmRlL25ldHRsZWllLTIiLCAiaHR0cHM6Ly93d3cuZWxpbmV0dC5uby9rdW5kZS9uZXR0bGVpZS0yL25ldHRsZWllIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTEyLTA3IiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDI0MDkuNn0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMzAxNC40fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzNjA5LjZ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA2MDE5LjJ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA3MjI4Ljh9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA4NDI4Ljh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMjAzOC40fSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMTMyMzguNH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDE0NDQ4fSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDE4MDU3LjZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNy44NCwgInVubnRhayI6IFt7Im5hdm4iOiAiVmlya2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjUuODQsICJkYWdlciI6IFsidmlya2VkYWciXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNC0wMSJ9XX0=' title='Samle inn data for Elinett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/elinett.html" title="Se på tariffen for Elinett AS" target="_blank">🔍</a>
    <a href="./tariffer/elinett.yml" title="Se dataene for Elinett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Elmea AS Nett</td>
  <td>7080005046442</td>
  <td><em>12135</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbG1lYSBBUyBOZXR0IiwgImdsbiI6IFsiNzA4MDAwNTA0NjQ0MiJdfQ==' title='Samle inn data for Elmea AS Nett' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Elvenett AS</td>
  <td>7080005052917</td>
  <td><em>9694</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbHZlbmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNTI5MTciXX0=' title='Samle inn data for Elvenett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Elvia AS ✅</td>
  <td>7080005046220</td>
  <td><em>861140</em></td>
  <td><code>2024-11-27</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbHZpYSBBUyIsICJnbG4iOiBbIjcwODAwMDUwNDYyMjAiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMjciLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5lbHZpYS5uby9uZXR0bGVpZS9hbHQtb20tbmV0dGxlaWVwcmlzZXIvbmV0dGxlaWVwcmlzZXItZm9yLXByaXZhdGt1bmRlci8iLCAiaHR0cHM6Ly93d3cuZWx2aWEubm8vbmV0dGxlaWUvYWx0LW9tLW5ldHRsZWllcHJpc2VyL3ByaXNlbi1wYS1uZXR0bGVpZS1nYXItbmVkLyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTEwLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDEzNDR9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIyMDh9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDM2MDB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA1MDQwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNjQ4MH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDc4NzJ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxNDk3Nn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDIyMDgwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjkwODh9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNTgwODB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOC41NiwgInVubnRhayI6IFt7Im5hdm4iOiAiVmlya2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJkYWdlciI6IFsidmlya2VkYWciXSwgInByaXMiOiAyNC41Nn1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0xMC0wMSIsICJneWxkaWdfdGlsIjogIjIwMjUtMDEtMDEifSwgeyJpZCI6ICIyMDI1LTAxLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDEyOTZ9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIwNjR9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDMzNjB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA0NjU2fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNTk1Mn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDcyNDh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMzY4MH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDIwMTYwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjY2NDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNTM4MDh9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiA4LjU2LCAidW5udGFrIjogW3sibmF2biI6ICJWaXJrZWRhZyIsICJ0aW1lciI6ICI2LTIxIiwgImRhZ2VyIjogWyJ2aXJrZWRhZyJdLCAicHJpcyI6IDE2LjU2fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI1LTAxLTAxIn1dfQ==' title='Samle inn data for Elvia AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/elvia.html" title="Se på tariffen for Elvia AS" target="_blank">🔍</a>
    <a href="./tariffer/elvia.yml" title="Se dataene for Elvia AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Enida AS</td>
  <td>7080003871534</td>
  <td><em>10973</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbmlkYSBBUyIsICJnbG4iOiBbIjcwODAwMDM4NzE1MzQiXX0=' title='Samle inn data for Enida AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Etna Nett AS</td>
  <td>7080005046404</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFdG5hIE5ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDA1MDQ2NDA0Il19' title='Samle inn data for Etna Nett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Everket AS</td>
  <td>7080005052825</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFdmVya2V0IEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MjgyNSJdfQ==' title='Samle inn data for Everket AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Fagne AS ✅</td>
  <td>7080003809599</td>
  <td><em>68802</em></td>
  <td><code>2024-12-07</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGYWduZSBBUyIsICJnbG4iOiBbIjcwODAwMDM4MDk1OTkiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMDciLCAia2lsZGVyIjogWyJodHRwczovL2ZhZ25lLm5vL2t1bmRlLW9nLW5ldHRsZWllL25ldHRsZWllLXByaXNlci1vZy12aWxrYXIvcHJpc2VyLXByaXZhdGt1bmRlci8iXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDM0NTZ9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDQ0MTZ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA1Mzc2fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNjMzNn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDcyOTZ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMTEyMH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDMwNzIwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDAzMjB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNDk5MjB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyMCwgInVubnRhayI6IFt7Im5hdm4iOiAiVWtlZGFnZXIiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjgsICJkYWdlciI6IFsidWtlZGFnIl19XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDQtMDEiLCAiZ3lsZGlnX3RpbCI6ICIyMDI0LTEyLTMxIn1dfQ==' title='Samle inn data for Fagne AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/fagne.html" title="Se på tariffen for Fagne AS" target="_blank">🔍</a>
    <a href="./tariffer/fagne.yml" title="Se dataene for Fagne AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Fjellnett AS ✅</td>
  <td>7080010000316</td>
  <td><em>7184</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDAzMTYiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZmplbGxuZXR0Lm5vL25ldHRsZWllL2F2dGFsZXItb2ctdmlsa2FyL2ZlbGxlc2Jlc3RlbW1lbHNlci8iLCAiaHR0cHM6Ly93d3cuZmplbGxuZXR0Lm5vL25ldHRsZWllcHJpc2VyL3ByaXZhdGt1bmRlci8iXSwgIm5ldHRlaWVyIjogIkZqZWxsbmV0dCBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTAuNjA4fSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiRkVNX1ZFS1RFVF9cdTAwYzVSIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDE3MDAuMDA0LCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiAyMTY4LjgsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDI2MzcuNiwgInRlcnNrZWwiOiAzfSwgeyJwcmlzIjogMzU3NS4yLCAidGVyc2tlbCI6IDR9LCB7InByaXMiOiA0MDQ0LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA0NTEyLjgsICJ0ZXJza2VsIjogNn0sIHsicHJpcyI6IDQ5ODEuNiwgInRlcnNrZWwiOiA3fSwgeyJwcmlzIjogNTQ1MC40LCAidGVyc2tlbCI6IDh9LCB7InByaXMiOiA1OTE5LjIsICJ0ZXJza2VsIjogOX0sIHsicHJpcyI6IDYzODgsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA2ODU2LjgsICJ0ZXJza2VsIjogMTF9LCB7InByaXMiOiA3MzI1LjYsICJ0ZXJza2VsIjogMTJ9LCB7InByaXMiOiA3Nzk0LjQsICJ0ZXJza2VsIjogMTN9LCB7InByaXMiOiA4MjYzLjIsICJ0ZXJza2VsIjogMTR9LCB7InByaXMiOiA4NzMyLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogOTIwMC44LCAidGVyc2tlbCI6IDE2fSwgeyJwcmlzIjogOTY2OS42LCAidGVyc2tlbCI6IDE3fSwgeyJwcmlzIjogMTAxMzguNCwgInRlcnNrZWwiOiAxOH0sIHsicHJpcyI6IDEwNjA3LjIsICJ0ZXJza2VsIjogMTl9LCB7InByaXMiOiAxMTA3NiwgInRlcnNrZWwiOiAyMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Fjellnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/fjellnett.html" title="Se på tariffen for Fjellnett AS" target="_blank">🔍</a>
    <a href="./tariffer/fjellnett.yml" title="Se dataene for Fjellnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Føie AS ✅</td>
  <td>7080005048415</td>
  <td><em>18675</em></td>
  <td><code>2024-12-10</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGXHUwMGY4aWUgQVMiLCAiZ2xuIjogWyI3MDgwMDA1MDQ4NDE1IiwgIjcwODAwMDQwNjc4ODIiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZm9pZS5uby9uZXR0bGVpZS9wcmlzZXItYXZ0YWxlci8iXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMTAiLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTA1IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTIzOC40fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAxNTM2fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzNzkyfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNjI5Ny42fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogODg2MC44fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTE4MDh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMzc3Nn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDE1NzQ0fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjE2MDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMSwgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInRpbWVyIjogIjctMjEiLCAicHJpcyI6IDE3LjV9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDUtMDEifV19' title='Samle inn data for Føie AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/foie.html" title="Se på tariffen for Føie AS" target="_blank">🔍</a>
    <a href="./tariffer/foie.yml" title="Se dataene for Føie AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Føie AS – Hemsedal ✅</td>
  <td>7080004067882</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-10</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGXHUwMGY4aWUgQVMiLCAiZ2xuIjogWyI3MDgwMDA1MDQ4NDE1IiwgIjcwODAwMDQwNjc4ODIiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZm9pZS5uby9uZXR0bGVpZS9wcmlzZXItYXZ0YWxlci8iXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMTAiLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTA1IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTIzOC40fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAxNTM2fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzNzkyfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNjI5Ny42fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogODg2MC44fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTE4MDh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMzc3Nn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDE1NzQ0fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjE2MDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMSwgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInRpbWVyIjogIjctMjEiLCAicHJpcyI6IDE3LjV9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDUtMDEifV19' title='Samle inn data for Føie AS – Hemsedal' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/foie.html" title="Se på tariffen for Føie AS – Hemsedal" target="_blank">🔍</a>
    <a href="./tariffer/foie.yml" title="Se dataene for Føie AS – Hemsedal i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Føre AS</td>
  <td>7080010003836</td>
  <td><em>8841</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGXHUwMGY4cmUgQVMiLCAiZ2xuIjogWyI3MDgwMDEwMDAzODM2Il19' title='Samle inn data for Føre AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Glitre Nett AS (tidl Glitre Energi Nett, Distrib.) ✅</td>
  <td>7080005052672</td>
  <td><em>83425</em></td>
  <td><code>2024-11-25</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNTYwNjkiLCAiNzA4MDAwNTA1MjY3MiIsICI3MDgwMDA1MDUzMjczIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI1IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZ2xpdHJlbmV0dC5uby9rdW5kZS9uZXR0bGVpZS1vZy1wcmlzZXIvbmV0dGxlaWVwcmlzZXItcHJpdmF0a3VuZGUiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0xMC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyMDQwfSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNTgwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0NDQwfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogOTEyMH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDExODgwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTQ4ODB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzA0MH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM2NDgwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDg2MDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzg5NjB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNS4zNiwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDI0Ljk2fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTEwLTAxIn1dfQ==' title='Samle inn data for Glitre Nett AS (tidl Glitre Energi Nett, Distrib.)' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/glitre.html" title="Se på tariffen for Glitre Nett AS (tidl Glitre Energi Nett, Distrib.)" target="_blank">🔍</a>
    <a href="./tariffer/glitre.yml" title="Se dataene for Glitre Nett AS (tidl Glitre Energi Nett, Distrib.) i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Glitre Nett AS (tidl. Glitre Energi Nett - Reg.n.) ✅</td>
  <td>7080005053273</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-25</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNTYwNjkiLCAiNzA4MDAwNTA1MjY3MiIsICI3MDgwMDA1MDUzMjczIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI1IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZ2xpdHJlbmV0dC5uby9rdW5kZS9uZXR0bGVpZS1vZy1wcmlzZXIvbmV0dGxlaWVwcmlzZXItcHJpdmF0a3VuZGUiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0xMC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyMDQwfSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNTgwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0NDQwfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogOTEyMH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDExODgwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTQ4ODB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzA0MH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM2NDgwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDg2MDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzg5NjB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNS4zNiwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDI0Ljk2fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTEwLTAxIn1dfQ==' title='Samle inn data for Glitre Nett AS (tidl. Glitre Energi Nett - Reg.n.)' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/glitre.html" title="Se på tariffen for Glitre Nett AS (tidl. Glitre Energi Nett - Reg.n.)" target="_blank">🔍</a>
    <a href="./tariffer/glitre.yml" title="Se dataene for Glitre Nett AS (tidl. Glitre Energi Nett - Reg.n.) i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Glitre Nett AS (tidligere Agder Energi Nett) ✅</td>
  <td>7080005056069</td>
  <td><em>150687</em></td>
  <td><code>2024-11-25</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNTYwNjkiLCAiNzA4MDAwNTA1MjY3MiIsICI3MDgwMDA1MDUzMjczIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI1IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZ2xpdHJlbmV0dC5uby9rdW5kZS9uZXR0bGVpZS1vZy1wcmlzZXIvbmV0dGxlaWVwcmlzZXItcHJpdmF0a3VuZGUiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0xMC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyMDQwfSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNTgwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0NDQwfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogOTEyMH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDExODgwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTQ4ODB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzA0MH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM2NDgwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDg2MDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzg5NjB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNS4zNiwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDI0Ljk2fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTEwLTAxIn1dfQ==' title='Samle inn data for Glitre Nett AS (tidligere Agder Energi Nett)' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/glitre.html" title="Se på tariffen for Glitre Nett AS (tidligere Agder Energi Nett)" target="_blank">🔍</a>
    <a href="./tariffer/glitre.yml" title="Se dataene for Glitre Nett AS (tidligere Agder Energi Nett) i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Griug AS ✅</td>
  <td>7080005052900</td>
  <td><em>5471</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTI5MDAiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZ3JpdWcubm8vb20tbmV0dGxlaWUtb2ctcHJpc2VyL3ByaXNlci9uZXR0bGVpZXByaXNlci0yMDI0LyJdLCAibmV0dGVpZXIiOiAiR3JpdWcgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDkuOCwgInVubnRhayI6IFt7ImRhZ2VyIjogWyJmcmVkYWciXSwgIm1cdTAwZTVuZWRlciI6IFsiamFudWFyIiwgImZlYnJ1YXIiLCAibWFycyIsICJva3RvYmVyIiwgIm5vdmVtYmVyIiwgImRlc2VtYmVyIl0sICJuYXZuIjogIkJydWtzdGlkc3RpbGxlZ2ciLCAicHJpcyI6IDIwLjgsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMjExMiwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMzE2OCwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNDc1MiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNjA5NiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDc2ODAsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiA5MzEyLCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMTc0MjQsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAyNTU4NCwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDM0MzIwLCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogNjgxMTIsICJ0ZXJza2VsIjogMTAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIiwgImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Griug AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/griug.html" title="Se på tariffen for Griug AS" target="_blank">🔍</a>
    <a href="./tariffer/griug.yml" title="Se dataene for Griug AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Hallingdal Kraftnett AS ✅</td>
  <td>7080005050654</td>
  <td><em>9581</em></td>
  <td><code>2024-07-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJIYWxsaW5nZGFsIEtyYWZ0bmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNTA2NTQiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMDctMDEiLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5oYWxsaW5nZGFsLWtyYWZ0bmV0dC5uby91cGxvYWRzL0hhbGxpbmdkYWwtS3JhZnRuZXR0LU5ldHRsZWllLXByLTA3LTIwMjQucGRmIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDctcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjM1Mn0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjg0NH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMzc0NH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDQ2MzJ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA1NTMyfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogNjQyMH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDczMjB9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA4MjA4fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogODQ3Mn0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA4NzEyfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogNi42OCwgInVubnRhayI6IFt7Im5hdm4iOiAiYWxsZSIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAxMC45MywgImRhZ2VyIjogWyJhbGxlIl19XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDctMDEifV19' title='Samle inn data for Hallingdal Kraftnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/hallingdalkraftnett.html" title="Se på tariffen for Hallingdal Kraftnett AS" target="_blank">🔍</a>
    <a href="./tariffer/hallingdalkraftnett.yml" title="Se dataene for Hallingdal Kraftnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Havnett AS</td>
  <td>7080010001832</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJIYXZuZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwMTgzMiJdfQ==' title='Samle inn data for Havnett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Høland og Setskog Elverk AS ✅</td>
  <td>7080004320253</td>
  <td><em>5341</em></td>
  <td><code>2024-12-08</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJIXHUwMGY4bGFuZCBvZyBTZXRza29nIEVsdmVyayBBUyIsICJnbG4iOiBbIjcwODAwMDQzMjAyNTMiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMDgiLCAia2lsZGVyIjogWyJodHRwczovL2hzZXYubm8vdXBsb2Fkcy8yMDI0LTA5LTA5LUhTRVYtbmV0dGxlaWUtbiVDMyVBNnJpbmctbWVkLWZvcmJydWstbWluZHJlLWVubi0xMDAtMDAwLWtXaC0xLW9rdG9iZXItMjAyNC5wZGYiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0xMC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyMDY0fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyODgwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0MDgwfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNTc2MH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDY5MTJ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA4ODMyfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTU1NTJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNDAwMH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDMwNzIwfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDU5NTIwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMjAsICJ1bm50YWsiOiBbeyJuYXZuIjogIlZpcmtlZGFnIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDI1LCAiZGFnZXIiOiBbInZpcmtlZGFnIl19XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMTAtMDEifV19' title='Samle inn data for Høland og Setskog Elverk AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/holandogsetskogelverk.html" title="Se på tariffen for Høland og Setskog Elverk AS" target="_blank">🔍</a>
    <a href="./tariffer/holandogsetskogelverk.yml" title="Se dataene for Høland og Setskog Elverk AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Indre Hordaland Kraftnett AS ✅</td>
  <td>7080010008367</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-07</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJJbmRyZSBIb3JkYWxhbmQgS3JhZnRuZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwODM2NyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTEwLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDIzMDR9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDI4ODB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDM4NDB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA1NzYwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNzY4MH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDk2MDB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMTUyMH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI4LjU2fSwgImd5bGRpZ19mcmEiOiAiMjAyNC0xMC0wMSJ9XSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMDciLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5paGsubm8vcHJpc2FyL25ldHRsZWlnZSIsICJodHRwczovL3d3dy5paGsubm8vaW1hZ2VzL3BkZi9OZXR0bGVpZ2VfcHJpdmF0XzAxLjEwLjIwMjQucGRmIl19' title='Samle inn data for Indre Hordaland Kraftnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/indrehordalandkraftnett.html" title="Se på tariffen for Indre Hordaland Kraftnett AS" target="_blank">🔍</a>
    <a href="./tariffer/indrehordalandkraftnett.yml" title="Se dataene for Indre Hordaland Kraftnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Jæren Everk AS ✅</td>
  <td>7080010002419</td>
  <td><em>7537</em></td>
  <td><code>2024-12-06</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJKXHUwMGU2cmVuIEV2ZXJrIEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwMjQxOSJdLCAia2lsZGVyIjogWyJodHRwczovL2pldi5uby9uZXR0bGVpZS1mb3Ita3VuZGVyLW1lZC1mb3JicnVrLXVuZGVyLTEwMC0wMDAta3doLTItMi0yLTIiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMDYiLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTAxLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDE4OTZ9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDMwNjB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDQ4OTZ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA3MjAwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogOTUxNn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDExODIwfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTg3MzJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAzMDI2NH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDQxNzk2fSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDU5MTAwfSwgeyJ0ZXJza2VsIjogMTUwLCAicHJpcyI6IDgyMTI4fSwgeyJ0ZXJza2VsIjogMjAwLCAicHJpcyI6IDEwNTE1Nn1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEzLCAidW5udGFrIjogW3sibmF2biI6ICJVa2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJkYWdlciI6IFsidWtlZGFnIl0sICJwcmlzIjogMTl9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV19' title='Samle inn data for Jæren Everk AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/jaereneverk.html" title="Se på tariffen for Jæren Everk AS" target="_blank">🔍</a>
    <a href="./tariffer/jaereneverk.yml" title="Se dataene for Jæren Everk AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>KE Nett AS ✅</td>
  <td>7080005046060</td>
  <td><em>8337</em></td>
  <td><code>2024-12-04</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLRSBOZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwNTA0NjA2MCJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMi0wNCIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMTAtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzAwMH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDY4MH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDYzNjB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA4MDQwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogOTcyMH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDE5ODAwfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMjUyMDB9LCB7InRlcnNrZWwiOiA3NSwgInByaXMiOiAzMzYwMH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA2NDY4MH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IC0yLCAidW5udGFrIjogW3sibmF2biI6ICJVa2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMTAsICJkYWdlciI6IFsidWtlZGFnIl19XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMTAtMDEifV0sICJraWxkZXIiOiBbImh0dHBzOi8va2UtbmV0dC5uby9nZXRmaWxlLnBocC8xMzIyNjUtMTczMDg4MzIyNS9Eb2t1bWVudGVyL05ldHRsZWlnZS9OZXR0bGVpZ2Vicm9zanlyZTIwMjQlMjBva3RvYmVyLnBkZiIsICJodHRwczovL2tlLW5ldHQubm8vTmV0dGxlaWVwcmlzZXIvIl19' title='Samle inn data for KE Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/kenett.html" title="Se på tariffen for KE Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/kenett.yml" title="Se dataene for KE Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Klive AS ✅</td>
  <td>7080010000132</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-03</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLbGl2ZSBBUyIsICJnbG4iOiBbIjcwODAwMTAwMDAxMzIiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly9rbGl2ZS5uby9oYXItc3Ryb20vbmV0dGxlaWVwcmlzZXIvIiwgImh0dHBzOi8va2xpdmUubm8vd3AtY29udGVudC91cGxvYWRzLzIwMjQvMTAvTmV0dGxlaWVwcmlzZXItMjAyNC0xMS0wMS0xLnBkZiJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMi0wMyIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMTEtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogNDYxNC4yNH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNTczMS4zMn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDc2MDYuMzJ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAxMDE0Ni4xMn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDEyNjg2LjA0fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMjUzNTguNjR9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAzODA0NC42OH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDUwNzMwLjZ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzYwODkuMzZ9LCB7InRlcnNrZWwiOiAxNTAsICJwcmlzIjogMTAxNDQ4fSwgeyJ0ZXJza2VsIjogMjAwLCAicHJpcyI6IDE1MjE3OC42fSwgeyJ0ZXJza2VsIjogMzAwLCAicHJpcyI6IDI1MzYyNi42fSwgeyJ0ZXJza2VsIjogNTAwLCAicHJpcyI6IDM1NTA3NC42fV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTcuNjMyfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0xMS0wMSJ9XX0=' title='Samle inn data for Klive AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/klive.html" title="Se på tariffen for Klive AS" target="_blank">🔍</a>
    <a href="./tariffer/klive.yml" title="Se dataene for Klive AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Kvam Energi Nett AS ✅</td>
  <td>7080010001276</td>
  <td><em>4567**</em></td>
  <td><code>2024-05-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLdmFtIEVuZXJnaSBOZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwMTI3NiJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0wNS0wMSIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3Lmt2YW1lbmVyZ2luZXR0Lm5vL25ldHRsZWlnZXByaXNhcjIwMjQiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wNS1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyNDAwfSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAzNjAwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA1NTIwfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogODQwMH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDEwMDgwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTIwMDB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyNDAwMH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM2MDAwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDgwMDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzIwMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNC41LCAidW5udGFrIjogW3sibmF2biI6ICJVa2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJkYWdlciI6IFsidWtlZGFnIl0sICJwcmlzIjogMjIuNX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNS0wMSJ9XX0=' title='Samle inn data for Kvam Energi Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/kvamenerginett.html" title="Se på tariffen for Kvam Energi Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/kvamenerginett.yml" title="Se dataene for Kvam Energi Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Kystnett AS ✅</td>
  <td>7080010000064</td>
  <td><em>3926</em></td>
  <td><code>2024-01-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLeXN0bmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMTAwMDAwNjQiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMDEtMDEiLCAia2lsZGVyIjogWyJodHRwczovL2t5c3RuZXR0Lm5vL05ldHRsZWllLz9BcnRpY2xlPTY4Il0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDEtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogNTkxNn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMTA2ODB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAxNTQzMn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDIwMTg0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMjQ5NDh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAzOTIxNn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDYzMDAwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogODY3NzJ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogMTIyNDQ4fSwgeyJ0ZXJza2VsIjogMTUwLCAicHJpcyI6IDE3MDAxNn1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDE4fSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Kystnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/kystnett.html" title="Se på tariffen for Kystnett AS" target="_blank">🔍</a>
    <a href="./tariffer/kystnett.yml" title="Se dataene for Kystnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Lede AS ✅</td>
  <td>7080005050975</td>
  <td><em>178069</em></td>
  <td><code>2024-12-02</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMZWRlIEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MDk3NSJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMi0wMiIsICJraWxkZXIiOiBbImh0dHBzOi8vbGVkZS5uby9nZXRmaWxlLnBocC8xMzUzMzk5LTE3MjAxNzM5MjYvTGVkZS9GaWxlci9QcmlzbGlzdGVyL1ByaXNlciUyMG5ldHRsZWllJTIwMDEuMDguMjQucGRmIiwgImh0dHBzOi8vbGVkZS5uby9wcmlzZXIvbmV0dGxlaWUtcHJpdmF0a3VuZGVyLyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTA4LXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDI4MjB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDQ4MjR9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA2NzkyfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogODc5Nn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDEwNzg4fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTY3NjR9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNjcyNH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDM2NjcyfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDUxNjEyfSwgeyJ0ZXJza2VsIjogMTUwLCAicHJpcyI6IDcxNTIwfSwgeyJ0ZXJza2VsIjogMjAwLCAicHJpcyI6IDEwMTQwMH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI0LjM4fSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wOC0wMSJ9XX0=' title='Samle inn data for Lede AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/lede.html" title="Se på tariffen for Lede AS" target="_blank">🔍</a>
    <a href="./tariffer/lede.yml" title="Se dataene for Lede AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Linea AS ✅</td>
  <td>7080003965325</td>
  <td><em>33729</em></td>
  <td><code>2024-12-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMaW5lYSBBUyIsICJnbG4iOiBbIjcwODAwMDM5NjUzMjUiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMDEiLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5saW5lYS5uby9uby9rdW5kZS9uZXR0bGVpZS9uZXR0bGVpZXByaXNlciJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTA1LXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDMxMjB9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDMxMjB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDM5NjB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA1NzYwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogODE2MH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDExMTYwfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTU5NjB9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyMzE2MH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDMwMzYwfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDQxMTYwfSwgeyJ0ZXJza2VsIjogMTUwLCAicHJpcyI6IDU1NTYwfSwgeyJ0ZXJza2VsIjogMjAwLCAicHJpcyI6IDc3MTYwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogOS43LCAidW5udGFrIjogW3sibmF2biI6ICJWaXJrZWRhZ2VyIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDE5LjcsICJkYWdlciI6IFsidmlya2VkYWciXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNS0wMSJ9XX0=' title='Samle inn data for Linea AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/linea.html" title="Se på tariffen for Linea AS" target="_blank">🔍</a>
    <a href="./tariffer/linea.yml" title="Se dataene for Linea AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Linja AS ✅</td>
  <td>7080001319830</td>
  <td><em>76992</em></td>
  <td><code>2024-11-03</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDEzMTk4MzAiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubGluamEubm8vbmV0dGxlaWdlIl0sICJuZXR0ZWllciI6ICJMaW5qYSBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTAzIiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMjAuNDI0LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDI3LjIzMiwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAyNjQwLCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiAzMjkyLjgsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDM5NDUuNiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNjU4NS42LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogNzkxMC40LCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogOTIxNiwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDEzMTgwLjgsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAxNDQ5NiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDE1ODAxLjYsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAxOTc2Ni40LCAidGVyc2tlbCI6IDEwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNy0wMSIsICJpZCI6ICJub3JkLXByaXZhdCIsICJuYXZuIjogIk5vcmQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In0sIHsiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTUuMzg0LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDIyLjM4NCwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAyNjY4LjgsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDM3MDUuNiwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNDc0Mi40LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA2ODE2LjAsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA4MTk4LjQsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiA5NTkwLjQsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAxMjE4Mi40LCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMTM1NjQuOCwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDE0OTU2LjgsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAxODQxMi44LCAidGVyc2tlbCI6IDEwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNy0wMSIsICJpZCI6ICJzXHUwMGY4ci1wcml2YXQiLCAibmF2biI6ICJTXHUwMGY4ciIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Linja AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/linja.html" title="Se på tariffen for Linja AS" target="_blank">🔍</a>
    <a href="./tariffer/linja.yml" title="Se dataene for Linja AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Lnett AS ✅</td>
  <td>7080005046053</td>
  <td><em>140237</em></td>
  <td><code>2024-11-29</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMbmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNDYwNTMiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMjkiLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5sLW5ldHQubm8vbmV0dGxlaWUvcHJpc2VyLW9nLXZpbGthci1wcml2YXQvIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDctcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjc4NH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDQ2NH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDY4NjR9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA5MjY0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTE2NjR9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMTI2NH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDMwODY0fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDA0NjR9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNjcyMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyNC41NywgInVubnRhayI6IFt7Im5hdm4iOiAiVmlya2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMzAuOTcsICJkYWdlciI6IFsidmlya2VkYWciXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNy0wMSJ9XX0=' title='Samle inn data for Lnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/lnett.html" title="Se på tariffen for Lnett AS" target="_blank">🔍</a>
    <a href="./tariffer/lnett.yml" title="Se dataene for Lnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Lucerna AS ✅</td>
  <td>7080005050661</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-02</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMdWNlcm5hIEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MDY2MSJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzEwOH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMzczMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDUxMn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDQ5ODB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA2MjI4fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogNzAwOH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDc3ODh9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA4NTU2fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogOTMzNn1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEyLjQ1LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMTguNDV9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTEyLTAyIiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubHVjZXJuYS5uby9wcmlzZXIiXX0=' title='Samle inn data for Lucerna AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/lucerna.html" title="Se på tariffen for Lucerna AS" target="_blank">🔍</a>
    <a href="./tariffer/lucerna.yml" title="Se dataene for Lucerna AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Lysna AS ✅</td>
  <td>7080010013088</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-02</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMeXNuYSBBUyIsICJnbG4iOiBbIjcwODAwMTAwMTMwODgiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMDIiLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzcyMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogNDc0MH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNTcyNH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDY5NjB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA4MjIwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogOTQyMH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI0LCAidW5udGFrIjogW3sibmF2biI6ICJEYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMzJ9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDItMDEifV0sICJraWxkZXIiOiBbImh0dHBzOi8vbHlzbmEubm8vcHJpc2FyLWZvci1wcml2YXRlLWt1bmRhci0yMDI0Il19' title='Samle inn data for Lysna AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/lysna.html" title="Se på tariffen for Lysna AS" target="_blank">🔍</a>
    <a href="./tariffer/lysna.yml" title="Se dataene for Lysna AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Mellom AS ✅</td>
  <td>7080010004369</td>
  <td><em>19101</em></td>
  <td><code>2024-12-02</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJNZWxsb20gQVMiLCAiZ2xuIjogWyI3MDgwMDEwMDA0MzY5Il0sICJraWxkZXIiOiBbImh0dHBzOi8vbWVsbG9tLm5vL25ldHRsZWllL25ldHRsZWllcHJpc2VyLyJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMi0wMiIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyNDM4LjR9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDM2NDh9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDYwNTcuNn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDgwMDYuNH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDEwMTM3LjZ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAxMjcwMC44fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTU5OTMuNn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDIxMzY5LjZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyOS4zNCwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDM3LjIxfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA4LTAxIn1dfQ==' title='Samle inn data for Mellom AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/mellom.html" title="Se på tariffen for Mellom AS" target="_blank">🔍</a>
    <a href="./tariffer/mellom.yml" title="Se dataene for Mellom AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Meløy Nett AS ✅</td>
  <td>7080003968395</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-02</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJNZWxcdTAwZjh5IE5ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDAzOTY4Mzk1Il0sICJraWxkZXIiOiBbImh0dHBzOi8vbWVsb3llbmVyZ2kubm8vYS9ha3R1ZWx0L255ZS1uZXR0bGVpZXByaXNlciIsICJodHRwczovL21lbG95ZW5lcmdpLm5vL2FjL25ldHRsZWllLWF2cmVnbmluZyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzAxM30sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMzYxNn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMzkxN30sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDQyMTh9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA0NTIwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogNTI3M30sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDU3MjV9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA2MzI3fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNjkzMH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA3NTMzfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTguMywgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDIyLjN9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTEyLTAyIn0=' title='Samle inn data for Meløy Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/meloy.html" title="Se på tariffen for Meløy Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/meloy.yml" title="Se dataene for Meløy Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Midtnett AS ✅</td>
  <td>7080003869012</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-03</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDM4NjkwMTIiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubWlkdG5ldHQubm8vbmV0dGxlaWUiLCAiaHR0cHM6Ly93d3cubWlkdG5ldHQubm8vbWVkaWEvMjkxOS9uZXR0bGVpZXByaXNlci1mcmEtMS1hcHJpbC0yMDI0LnBkZiJdLCAibmV0dGVpZXIiOiAiTWlkdG5ldHQgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wMyIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI2LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDMxLCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDI2NDAsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDM5NjAsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDYwMDAsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA5MDAwLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMTIwMDAsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAxNjc2NCwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDI1MTUyLCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogMzEyMDAsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAzNjAwMCwgInRlcnNrZWwiOiAxMDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDQtMDEiLCAiaWQiOiAiaG4yMi1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Midtnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/midtnett.html" title="Se på tariffen for Midtnett AS" target="_blank">🔍</a>
    <a href="./tariffer/midtnett.yml" title="Se dataene for Midtnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Modalen Kraftlag Nett ✅</td>
  <td>7080003816184</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-27</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJNb2RhbGVuIEtyYWZ0bGFnIE5ldHQiLCAiZ2xuIjogWyI3MDgwMDAzODE2MTg0Il0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI3IiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDYwMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogOTg4Ljh9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDE2ODB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAyMzcxLjJ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAzMDYyLjR9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAzNzQ3LjJ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAzMCwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjItMTAtMDEifV0sICJraWxkZXIiOiBbImh0dHBzOi8vd3d3Lm1vZGFsZW5rcmFmdGxhZy5uby9WaWV3RmlsZS5hc3B4P0l0ZW1JRD0xMjg0Il19' title='Samle inn data for Modalen Kraftlag Nett' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/modalen.html" title="Se på tariffen for Modalen Kraftlag Nett" target="_blank">🔍</a>
    <a href="./tariffer/modalen.yml" title="Se dataene for Modalen Kraftlag Nett i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Nettselskapet AS ✅</td>
  <td>7080004064553</td>
  <td><em>17244</em></td>
  <td><code>2024-01-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOZXR0c2Vsc2thcGV0IEFTIiwgImdsbiI6IFsiNzA4MDAwNDA2NDU1MyJdLCAia2lsZGVyIjogWyJodHRwczovL25ldHRzZWxza2FwZXQuYXMvcHJpdmF0LTIwMjQvIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTAxLTAxIiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDExMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjAwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzNDB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA1MDB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA2NTB9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA4MjB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxNDAwfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMjIwMH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEwLjcwNCwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDIxLjUwNH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Nettselskapet AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/nettselskapet.html" title="Se på tariffen for Nettselskapet AS" target="_blank">🔍</a>
    <a href="./tariffer/nettselskapet.yml" title="Se dataene for Nettselskapet AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Noranett AS ✅</td>
  <td>7080003811318</td>
  <td><em>19644</em></td>
  <td><code>2024-01-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JhbmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDM4MTEzMTgiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubm9yYW5ldHQubm8vZ2V0ZmlsZS5waHAvMTMyMzMwNi0xNzA0OTUzNzQ4L05vcmFuZXR0L0ZpbGVyL05ldHRsZWllJTIwMjAyNCUyMC0lMjBIJUMzJUE1bG9nYWxhbmQlMjBwZGYucGRmIiwgImh0dHBzOi8vd3d3Lm5vcmFuZXR0Lm5vL25ldHRsZWllcHJpc2VyL25ldHRsZWllcHJpc2VyLWhhbG9nYWxhbmQtZnJhLTEtMS0yMDI0LWFydGljbGUzODcwLTI0MTUuaHRtbCJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogNDMyMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogNjEyMH0sIHsidGVyc2tlbCI6IDQsICJwcmlzIjogNzQ0MH0sIHsidGVyc2tlbCI6IDYsICJwcmlzIjogODQwMH0sIHsidGVyc2tlbCI6IDgsICJwcmlzIjogOTM2MH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDEwMzIwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogMTIzNjB9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAxNjgwMH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDE5MjAwfSwgeyJ0ZXJza2VsIjogMzAsICJwcmlzIjogMjI4MDB9LCB7InRlcnNrZWwiOiAzNSwgInByaXMiOiAyNjQwMH0sIHsidGVyc2tlbCI6IDQwLCAicHJpcyI6IDMwMDAwfSwgeyJ0ZXJza2VsIjogNDUsICJwcmlzIjogMzI0MDB9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA0OTIwMH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDc0NDAwfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDk4NDAwfSwgeyJ0ZXJza2VsIjogMTI1LCAicHJpcyI6IDEyMzYwMH0sIHsidGVyc2tlbCI6IDE1MCwgInByaXMiOiAxNDc2MDB9LCB7InRlcnNrZWwiOiAxNzUsICJwcmlzIjogMTcyODAwfSwgeyJ0ZXJza2VsIjogMjAwLCAicHJpcyI6IDI0NzIwMH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDAuOH0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTAxLTAxIn0=' title='Samle inn data for Noranett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/noranett.html" title="Se på tariffen for Noranett AS" target="_blank">🔍</a>
    <a href="./tariffer/noranett.yml" title="Se dataene for Noranett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Noranett Andøy AS ✅</td>
  <td>7080010002433</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-29</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JhbmV0dCBBbmRcdTAwZjh5IEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwMjQzMyJdLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5ub3JhbmV0dC5uby9uZXR0bGVpZXByaXNlci9uZXR0bGVpZXByaXNlci1hbmRveS1mcmEtMS0xLTIwMjQtYXJ0aWNsZTM4NzEtMjQxNS5odG1sIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI5IiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wMSIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDM3MjB9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDQ5MjB9LCB7InRlcnNrZWwiOiA0LCAicHJpcyI6IDYyNDB9LCB7InRlcnNrZWwiOiA2LCAicHJpcyI6IDc1NjB9LCB7InRlcnNrZWwiOiA4LCAicHJpcyI6IDg3NjB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAxMTA0MH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDE0MTYwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTc0MDB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMDQwMH0sIHsidGVyc2tlbCI6IDMwLCAicHJpcyI6IDIzNzYwfSwgeyJ0ZXJza2VsIjogMzUsICJwcmlzIjogMjcxMjB9LCB7InRlcnNrZWwiOiA0MCwgInByaXMiOiAzMDQ4MH0sIHsidGVyc2tlbCI6IDQ1LCAicHJpcyI6IDMzOTYwfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogNDMyMDB9LCB7InRlcnNrZWwiOiA3NSwgInByaXMiOiA1OTQwMH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA3NjA4MH0sIHsidGVyc2tlbCI6IDEyNSwgInByaXMiOiA5Mjc2MH0sIHsidGVyc2tlbCI6IDE1MCwgInByaXMiOiAxMDk0NDB9LCB7InRlcnNrZWwiOiAxNzUsICJwcmlzIjogMTI2MjQwfSwgeyJ0ZXJza2VsIjogMjAwLCAicHJpcyI6IDE0MjkyMH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI2LjV9LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIn1dfQ==' title='Samle inn data for Noranett Andøy AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/noranett-andoy.html" title="Se på tariffen for Noranett Andøy AS" target="_blank">🔍</a>
    <a href="./tariffer/noranett-andoy.yml" title="Se dataene for Noranett Andøy AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Noranett Hadsel AS ✅</td>
  <td>7080003857989</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-29</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JhbmV0dCBIYWRzZWwgQVMiLCAiZ2xuIjogWyI3MDgwMDAzODU3OTg5Il0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI5IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubm9yYW5ldHQubm8vbmV0dGxlaWVwcmlzZXIvbmV0dGxlaWVwcmlzZXItaGFkc2VsLWZyYS0xLTEwLTIwMjQtYXJ0aWNsZTM5ODItMjQxNS5odG1sIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDEiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMzg4OCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNDg5NiwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNTkwNCwgInRlcnNrZWwiOiA0fSwgeyJwcmlzIjogNjkxMiwgInRlcnNrZWwiOiA2fSwgeyJwcmlzIjogNzkyMCwgInRlcnNrZWwiOiA4fSwgeyJwcmlzIjogOTIxNiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDExNTIwLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMTM5NjgsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAxNjQxNiwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDE4NzIwLCAidGVyc2tlbCI6IDMwfSwgeyJwcmlzIjogMjEwMjQsICJ0ZXJza2VsIjogMzV9LCB7InByaXMiOiAyMzMyOCwgInRlcnNrZWwiOiA0MH0sIHsicHJpcyI6IDI1NjMyLCAidGVyc2tlbCI6IDQ1fSwgeyJwcmlzIjogMzI0MDAsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiA0MzkyMCwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDU1NzI4LCAidGVyc2tlbCI6IDEwMH0sIHsicHJpcyI6IDY3OTY4LCAidGVyc2tlbCI6IDEyNX0sIHsicHJpcyI6IDgwMzUyLCAidGVyc2tlbCI6IDE1MH0sIHsicHJpcyI6IDkyNTkyLCAidGVyc2tlbCI6IDE3NX0sIHsicHJpcyI6IDEwNDgzMiwgInRlcnNrZWwiOiAyMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyMi44LCAidW5udGFrIjogW3sibmF2biI6ICJEYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjguOH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Noranett Hadsel AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/noranett-hadsel.html" title="Se på tariffen for Noranett Hadsel AS" target="_blank">🔍</a>
    <a href="./tariffer/noranett-hadsel.yml" title="Se dataene for Noranett Hadsel AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Nordvest Nett AS ✅</td>
  <td>7080005052801</td>
  <td><em>11996</em></td>
  <td><code>2024-09-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JkdmVzdCBOZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MjgwMSJdLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5udm4ubm8vYWt0dWVsdC9ueWUtbmV0dGxlaWVwcmlzZXItZnJhLTEtc2VwdGVtYmVyLTIwMjQvIiwgImh0dHBzOi8vd3d3Lm52bi5uby9kb3dubG9hZD9vYmplY3RQYXRoPS91cGxvYWRfaW1hZ2VzL0U0MzYxMzA4MkMyNjQ0QzdCNjdEQ0ZBMjIxNDczRkI1LnBkZiJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0wOS0wMSIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAxMzcyLjh9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDMzNjkuNn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDE1Ni44fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNjMxNi44fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNzQ5Ny42fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogODczNn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDE2NzcxLjJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNDgxNn0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDMyODUxLjJ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNjQ2MDh9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNy42MDgsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAyMy42MDh9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEifV19' title='Samle inn data for Nordvest Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/nordvestnett.html" title="Se på tariffen for Nordvest Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/nordvestnett.yml" title="Se dataene for Nordvest Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Norefjell Nett AS ✅</td>
  <td>7080010003911</td>
  <td><em>4567**</em></td>
  <td><code>2024-01-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JlZmplbGwgTmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMTAwMDM5MTEiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMDEtMDEiLCAia2lsZGVyIjogWyJodHRwOi8vd3d3Lmtyb2RzaGVyYWQtbmV0dC5uby9uZXR0amVuZXN0ZXIvaHl0dGVtYXJrZWRldC9uZXR0bGVpZXByaXNlciIsICJodHRwOi8vd3d3Lmtyb2RzaGVyYWQtbmV0dC5uby9hc3NldHMvRG9rdW1lbnRlci9OZXR0bGVpZXByaXNlciUyMDAxLjAxLjIwMjQucGRmIl0sICJ0YXJpZmZlciI6IFt7Imt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJpZCI6ICIyMDI0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAxOTY4fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNTQ0fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzNTI4fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNTMwNH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDY4NjR9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA4NDQ4fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTM3NTJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyMDYxNn0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDI3NDkyfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDM5MjY0fV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTIuNzUzLCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMTkuMDUzfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIn1dfQ==' title='Samle inn data for Norefjell Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/norefjell.html" title="Se på tariffen for Norefjell Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/norefjell.yml" title="Se dataene for Norefjell Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Norgesnett AS ✅</td>
  <td>7080005052702</td>
  <td><em>71010</em></td>
  <td><code>2024-11-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JnZXNuZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MjcwMiJdLCAia2lsZGVyIjogWyJodHRwczovL25vcmdlc25ldHQubm8va3VuZGUvbmV0dGxlaWUtcHJpdmF0LyJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wMSIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiA5ODQuMDk2fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAxNjQwLjI1Nn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMjY5Ny4zMTJ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA0Nzk4LjY1Nn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDYzNzEuNTJ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA3OTAyLjUyOH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDEyMjQ3LjI5Nn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDE5MTcyLjkyOH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDI2MDk4LjQ2NH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA0MjI5Ny4xMn1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDExLjU1MiwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDE3LjYxNn1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0xMS0wMSJ9XX0=' title='Samle inn data for Norgesnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/norgesnett.html" title="Se på tariffen for Norgesnett AS" target="_blank">🔍</a>
    <a href="./tariffer/norgesnett.yml" title="Se dataene for Norgesnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>R-Nett AS ✅</td>
  <td>7080010012852</td>
  <td><em>4567**</em></td>
  <td><code>2024-01-01</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSLU5ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDEwMDEyODUyIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTAxLTAxIiwgImtpbGRlciI6IFsiaHR0cHM6Ly9yLW5ldHQubm8vd3AtY29udGVudC91cGxvYWRzL2FwcGxpY2F0aW9uL3BkZi9OZXR0bGVpZXRhcmlmZmVyX2ZyYV8wMTAxMjAyNC5wZGYiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wMS1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAzMTk2Ljh9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDQ3OTAuNH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDcwMjcuMn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDEzNDExLjJ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAxOTc5NS4yfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMjkzNzZ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA0NTM1MC40fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNjQ1MTJ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogOTAwNTcuNn1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDE0LjU2LCAidW5udGFrIjogW3sibmF2biI6ICJhbGxlIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDIyLjU2LCAiZGFnZXIiOiBbImFsbGUiXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for R-Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/rnett.html" title="Se på tariffen for R-Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/rnett.yml" title="Se dataene for R-Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>RK Nett AS ✅</td>
  <td>7080010004017</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-10</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSSyBOZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwNDAxNyJdLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5yYXVsYW5kLW5ldHQubm8vbmV0dHByaXNhciJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMi0xMCIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDUtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzA5Nn0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogNDAyMH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNTU2OH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDcxMTZ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA4NjY0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTAyMTJ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxNzk1Mn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDI1NjkyfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMzM0MzJ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNDg5MDB9LCB7InRlcnNrZWwiOiAxNTAsICJwcmlzIjogNjQzODB9LCB7InRlcnNrZWwiOiAyMDAsICJwcmlzIjogOTI4NTZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyNC42NX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDUtMDEifV19' title='Samle inn data for RK Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/rknett.html" title="Se på tariffen for RK Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/rknett.yml" title="Se dataene for RK Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Rakkestad Energi AS Nett</td>
  <td>7080005054898</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSYWtrZXN0YWQgRW5lcmdpIEFTIE5ldHQiLCAiZ2xuIjogWyI3MDgwMDA1MDU0ODk4Il19' title='Samle inn data for Rakkestad Energi AS Nett' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Romsdalsnett AS</td>
  <td>7080010005427</td>
  <td><em>3734</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSb21zZGFsc25ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDEwMDA1NDI3Il19' title='Samle inn data for Romsdalsnett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>Røros E-verk Nett AS</td>
  <td>7080003947932</td>
  <td><em>4567**</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSXHUwMGY4cm9zIEUtdmVyayBOZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwMzk0NzkzMiJdfQ==' title='Samle inn data for Røros E-verk Nett AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>S-NETT AS</td>
  <td>7080010002464</td>
  <td><em>4389</em></td>
  <td></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTLU5FVFQgQVMiLCAiZ2xuIjogWyI3MDgwMDEwMDAyNDY0Il19' title='Samle inn data for S-NETT AS' target='_blank'>✏️</a>
  </td>
</tr>
<tr>
  <td>SkiakerNett AS ✅</td>
  <td>7080004062702</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-10</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTa2lha2VyTmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDQwNjI3MDIiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly9za2lha2VybmV0dC5uby9uZXR0bGVpZ2VwcmlzYXIiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMTAiLCAidGFyaWZmZXIiOiBbeyJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiaWQiOiAiMjAyNC0xMCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzA3Mn0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMzg0MH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDgwMH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDU5OTAuNH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDc0NzguNH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDg2NDB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMTY1NC40fSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMTQ1NDR9LCB7InRlcnNrZWwiOiA3NSwgInByaXMiOiAxODE1My42fSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDIyNjY1LjZ9LCB7InRlcnNrZWwiOiAxNTAsICJwcmlzIjogMjQwMDB9LCB7InRlcnNrZWwiOiAyMDAsICJwcmlzIjogMzAwMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyMX0sICJneWxkaWdfZnJhIjogIjIwMjQtMTAtMDEifV19' title='Samle inn data for SkiakerNett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/skiaker-nett.html" title="Se på tariffen for SkiakerNett AS" target="_blank">🔍</a>
    <a href="./tariffer/skiaker-nett.yml" title="Se dataene for SkiakerNett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Stannum AS ✅</td>
  <td>7080010003959</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-10</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdGFubnVtIEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwMzk1OSJdLCAia2lsZGVyIjogWyJodHRwczovL3N0YW5udW0ubm8vbmV0dGxlaWVwcmlzZXIiLCAiaHR0cHM6Ly9zdGFubnVtLm5vL3VwbG9hZHMvTmV0dGxlaWVwcmlzZXItMDEuMDkuMjQtVjMuMDAucGRmIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTEyLTEwIiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDMwMzN9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDM2NDB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDM5NDN9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA0NTUwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNTE1Nn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDUzMDh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiA1NzYzfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogNjM3MH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI1LjMzLCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjguMzN9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEifV19' title='Samle inn data for Stannum AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/stannum.html" title="Se på tariffen for Stannum AS" target="_blank">🔍</a>
    <a href="./tariffer/stannum.yml" title="Se dataene for Stannum AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Stram AS ✅</td>
  <td>7080003822901</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-10</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhbSBBUyIsICJnbG4iOiBbIjcwODAwMDM4MjI5MDEiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTItMTAiLCAia2lsZGVyIjogWyJodHRwczovL3N0YXRpYzEuc3F1YXJlc3BhY2UuY29tL3N0YXRpYy82NmJkZDAzNDE3ZDliZDM1NDVmODU1OWMvdC82NzNkYTAwZjMwNGQ5ZjMwNWNmZTRiZTQvMTczMjA5MTkxOTk3My9UYXJpZmZoZWZ0ZV9ub3YrMjAyNC5wZGYiLCAiaHR0cHM6Ly93d3cuc3RyYW0ubm8vbmV0dGxlaWVwcmlzIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBmYWxzZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTMyMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMzk2MH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNTI5Mn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDY2MTJ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA3OTMyfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogOTI1Mn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDIzNzg0fSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMzgzMjh9LCB7InRlcnNrZWwiOiA3NSwgInByaXMiOiA1Mjg2MH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA4MTkzNn1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDQuMTEsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAxNC4xMSwgImRhZ2VyIjogWyJ2aXJrZWRhZyJdfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTEwLTAxIn1dfQ==' title='Samle inn data for Stram AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/stram.html" title="Se på tariffen for Stram AS" target="_blank">🔍</a>
    <a href="./tariffer/stram.yml" title="Se dataene for Stram AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Straumen Nett AS ✅</td>
  <td>7080010003720</td>
  <td><em>4567**</em></td>
  <td><code>2024-12-10</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhdW1lbiBOZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAxMDAwMzcyMCJdLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5zdHJhdW1lbi1uZXR0Lm5vL25ldHRsZWlnZS9uZXR0bGVpZ2UtcHJpdmF0ZS0yMDI0LyJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMi0xMCIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyNzg0fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzMjA2LjR9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA0NzUyfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNTU4Ny4yfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogODM4MC44fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTExNjQuOH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDE4LjMwNH0sICJneWxkaWdfZnJhIjogIjIwMjQtMTAtMDEifV19' title='Samle inn data for Straumen Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/straumen-nett.html" title="Se på tariffen for Straumen Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/straumen-nett.yml" title="Se dataene for Straumen Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Straumnett AS ✅</td>
  <td>7080004053632</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-25</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhdW1uZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwNDA1MzYzMiJdLCAia2lsZGVyIjogWyJodHRwczovL3N0cmF1bW5ldHQubm8vcHJpc2FyLWZvci1uZXR0bGVpZ2UiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMjUiLCAidGFyaWZmZXIiOiBbeyJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiaWQiOiAiMjAyNCIsICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDI0MzUuMzI4fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyOTIyLjQzMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMzE2NS45ODR9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAzNDA5LjUzNn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDM2NTMuMDg4fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogNDI2MS45Mn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDQ2MjcuMn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDUxMTQuMzA0fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNTYwMS4zMTJ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNjA4OC40MTZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMS41NiwgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDE2LjU2fV19fV19' title='Samle inn data for Straumnett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/straumnett.html" title="Se på tariffen for Straumnett AS" target="_blank">🔍</a>
    <a href="./tariffer/straumnett.yml" title="Se dataene for Straumnett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>SuNett AS ✅</td>
  <td>7080010003218</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-24</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdU5ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDEwMDAzMjE4Il0sICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnN1bm5kYWxlbmVyZ2luZXR0Lm5vL25ldHRsZWllLyIsICJodHRwczovL3d3dy5zdW5uZGFsZW5lcmdpbmV0dC5uby9uZXR0bGVpZS9uZXR0YXZ0YWxlci9uZXR0bGVpZS1wcml2YXQvIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI0IiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wNC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiT1ZfVFJFRkFTRSIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDE2NDYuNH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDMyOTJ9LCB7InRlcnNrZWwiOiA2MywgInByaXMiOiA2NTg0Ljh9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNi44OCwgInVubnRhayI6IFt7Im5hdm4iOiAiVmludGVyIiwgInByaXMiOiAxOS4yOCwgIm1cdTAwZTVuZWRlciI6IFsiamFudWFyIiwgImZlYnJ1YXIiLCAibWFycyIsICJhcHJpbCIsICJub3ZlbWJlciIsICJkZXNlbWJlciJdfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA0LTAxIn1dfQ==' title='Samle inn data for SuNett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/sunett.html" title="Se på tariffen for SuNett AS" target="_blank">🔍</a>
    <a href="./tariffer/sunett.yml" title="Se dataene for SuNett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Sygnir AS ✅</td>
  <td>7080010009654</td>
  <td><em>7572</em></td>
  <td><code>2024-11-26</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDk2NTQiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly9zdGF0aWMxLnNxdWFyZXNwYWNlLmNvbS9zdGF0aWMvNjFkZmU3YjMxOTk5NTkxOTcyMjU0ZGVhL3QvNjU3YWYxYmM4YjNiMzU3OTQ3MTViZWY3LzE3MDI1NTYwOTQxMTgvTmV0dGxlaWdlcHJpc2FyK3ByKzAxLjAxLjI0LnBkZiIsICJodHRwczovL3d3dy5zeWduaXIubm8vbmV0dGxlaWdlIl0sICJuZXR0ZWllciI6ICJTeWduaXIgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNiIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDE4Ljc4NH0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDI0MjIuNCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMjkwNi40LCAidGVyc2tlbCI6IDF9LCB7InByaXMiOiAzMzkwLjQsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDM4NzUuMiwgInRlcnNrZWwiOiAzfSwgeyJwcmlzIjogNDM2MCwgInRlcnNrZWwiOiA0fSwgeyJwcmlzIjogNTA4Ni40LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA1ODEyLjgsICJ0ZXJza2VsIjogNn0sIHsicHJpcyI6IDY1MzkuMiwgInRlcnNrZWwiOiA3fSwgeyJwcmlzIjogNzI2Ni40LCAidGVyc2tlbCI6IDh9LCB7InByaXMiOiA3OTkyLjgsICJ0ZXJza2VsIjogOX0sIHsicHJpcyI6IDk0NDYuNCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDEwODk5LjIsICJ0ZXJza2VsIjogMTJ9LCB7InByaXMiOiAxMjM1Mi44LCAidGVyc2tlbCI6IDE0fSwgeyJwcmlzIjogMTM4MDUuNiwgInRlcnNrZWwiOiAxNn0sIHsicHJpcyI6IDE1MjU5LjIsICJ0ZXJza2VsIjogMTh9LCB7InByaXMiOiAyNzM2OS42LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMzk0ODAsICJ0ZXJza2VsIjogNDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Sygnir AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/sygnir.html" title="Se på tariffen for Sygnir AS" target="_blank">🔍</a>
    <a href="./tariffer/sygnir.yml" title="Se dataene for Sygnir AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Sør Aurdal Energi AS Nett ✅</td>
  <td>7080005046459</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-24</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTXHUwMGY4ciBBdXJkYWwgRW5lcmdpIEFTIE5ldHQiLCAiZ2xuIjogWyI3MDgwMDA1MDQ2NDU5Il0sICJraWxkZXIiOiBbImh0dHBzOi8vc2FlLm5vL3RhcmlmZmVyIiwgImh0dHBzOi8vc2FlLm5vL3VwbG9hZHMvS3VuZGVpbmZvcm1hc2pvbi8yMDI0XzA4X0t1bmRlaW5mb3JtYXNqb25fdGFyaWZmZXIucGRmIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI0IiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wOS1uMTAwIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIk1ORF9NQVgiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBmYWxzZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogNTQwMH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNjI0MH0sIHsidGVyc2tlbCI6IDgsICJwcmlzIjogNzQ0MH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDg2NDB9LCB7InRlcnNrZWwiOiAzMCwgInByaXMiOiA5NzIwfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMTMyMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyMS41MiwgInVubnRhayI6IFt7Im5hdm4iOiAiVmludGVyIiwgInByaXMiOiAyNS41MiwgIm1cdTAwZTVuZWRlciI6IFsiamFudWFyIiwgImZlYnJ1YXIiLCAibWFycyIsICJva3RvYmVyIiwgIm5vdmVtYmVyIiwgImRlc2VtYmVyIl19XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEifV19' title='Samle inn data for Sør Aurdal Energi AS Nett' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/sor-aurdal-energi.html" title="Se på tariffen for Sør Aurdal Energi AS Nett" target="_blank">🔍</a>
    <a href="./tariffer/sor-aurdal-energi.yml" title="Se dataene for Sør Aurdal Energi AS Nett i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Tendranett AS ✅</td>
  <td>7080003897855</td>
  <td><em>7249</em></td>
  <td><code>2024-12-02</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJUZW5kcmFuZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwMzg5Nzg1NSJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMi0wMiIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnRlbmRyYW5ldHQubm8vcHJpc2FyLW9nLXZpbGthci1mb3ItbmV0dGxlaWdlIiwgImh0dHBzOi8vd3d3LnRlbmRyYW5ldHQubm8vZmlsZXIvTmV0dGxlaWdlLnBkZiJdLCAidGFyaWZmZXIiOiBbeyJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiaWQiOiAiMjAyNCIsICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDE2MDB9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIxMDB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDI2MDB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAzNjAwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNDUwMH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDU1MDB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiA2ODAwfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogODEwMH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDk0MDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogOTcwMH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDcuMDQsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAxMi4wOH1dfX1dfQ==' title='Samle inn data for Tendranett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/tendranett.html" title="Se på tariffen for Tendranett AS" target="_blank">🔍</a>
    <a href="./tariffer/tendranett.yml" title="Se dataene for Tendranett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Tensio TN AS ✅</td>
  <td>7080005052627</td>
  <td><em>62277</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTI2MjciXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudGVuc2lvLm5vL25vL2t1bmRlL25ldHRsZWllL25ldHRsZWllcHJpc2VyLXNlcHRlbWJlci0yMDI0LXRuIiwgImh0dHBzOi8vd3d3LnRlbnNpby5uby9uby9rdW5kZS9uZXR0bGVpZS9uZXR0bGVpZXByaXNlci1zZXB0ZW1iZXItdHMiXSwgIm5ldHRlaWVyIjogIlRlbnNpbyBUUyBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMzkuNjgsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJwcmlzIjogNTcuNDMsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMTc3NiwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMzU1MiwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNjQzMiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogOTc1NiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDEzMDY4LCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMTY0MDQsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAyODU3MiwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDQ1MjA0LCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogNjE4MTIsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiA4OTQ4NCwgInRlcnNrZWwiOiAxMDB9LCB7InByaXMiOiAxMjI3NDgsICJ0ZXJza2VsIjogMTUwfSwgeyJwcmlzIjogMTc4MDkyLCAidGVyc2tlbCI6IDIwMH0sIHsicHJpcyI6IDI0NDU3MiwgInRlcnNrZWwiOiAzMDB9LCB7InByaXMiOiAzMTEwNDAsICJ0ZXJza2VsIjogNDAwfSwgeyJwcmlzIjogMzc3NDYwLCAidGVyc2tlbCI6IDUwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wOS0wMSIsICJpZCI6ICIyMDI0LTA3LXRuIiwgIm5hdm4iOiAiTm9yZCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Tensio TN AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/tensio-tn.html" title="Se på tariffen for Tensio TN AS" target="_blank">🔍</a>
    <a href="./tariffer/tensio-tn.yml" title="Se dataene for Tensio TN AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Tensio TS AS ✅</td>
  <td>7080005051880</td>
  <td><em>147146</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTE4ODAiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudGVuc2lvLm5vL25vL2t1bmRlL25ldHRsZWllL25ldHRsZWllcHJpc2VyLXNlcHRlbWJlci0yMDI0LXRuIiwgImh0dHBzOi8vd3d3LnRlbnNpby5uby9uby9rdW5kZS9uZXR0bGVpZS9uZXR0bGVpZXByaXNlci1zZXB0ZW1iZXItdHMiXSwgIm5ldHRlaWVyIjogIlRlbnNpbyBUUyBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMzUuOTMsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJwcmlzIjogNTAuMTgsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMTYwOCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMjg2OCwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNDg5NiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNzIxMiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDk1MjgsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiAxMTg2OCwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDIwMzg4LCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMzIwMDQsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiA0MzYyMCwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDYzMDAwLCAidGVyc2tlbCI6IDEwMH0sIHsicHJpcyI6IDg2MjIwLCAidGVyc2tlbCI6IDE1MH0sIHsicHJpcyI6IDEyNDkzMiwgInRlcnNrZWwiOiAyMDB9LCB7InByaXMiOiAxNzE0NTYsICJ0ZXJza2VsIjogMzAwfSwgeyJwcmlzIjogMjE3ODk2LCAidGVyc2tlbCI6IDQwMH0sIHsicHJpcyI6IDI2NDM4NCwgInRlcnNrZWwiOiA1MDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEiLCAiaWQiOiAiMjAyNC0wOS10cyIsICJuYXZuIjogIlNcdTAwZjhyIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Tensio TS AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/tensio-ts.html" title="Se på tariffen for Tensio TS AS" target="_blank">🔍</a>
    <a href="./tariffer/tensio-ts.yml" title="Se dataene for Tensio TS AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Tinfos AS Nett ✅</td>
  <td>7080003612595</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-24</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJUaW5mb3MgQVMgTmV0dCIsICJnbG4iOiBbIjcwODAwMDM2MTI1OTUiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMjQiLCAia2lsZGVyIjogWyJodHRwczovL3d3dy50aW5mb3Mubm8vdGluZm9zLW5ldHQvIiwgImh0dHBzOi8vYmlhcGkubnZlLm5vL25ldHRsZWlldGFyaWZmZXIvc3dhZ2dlci9pbmRleC5odG1sIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIm52ZSIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJVS0pFTlQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBudWxsLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAzMTU2fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0OTU2fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNjc1Nn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDg1NTZ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAxMDM1Nn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDE1NzU2fSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogNDUwMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV19' title='Samle inn data for Tinfos AS Nett' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/tinfos.html" title="Se på tariffen for Tinfos AS Nett" target="_blank">🔍</a>
    <a href="./tariffer/tinfos.yml" title="Se dataene for Tinfos AS Nett i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Uvdal Kraftforsyning ✅</td>
  <td>7080005050500</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-15</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJVdmRhbCBLcmFmdGZvcnN5bmluZyIsICJnbG4iOiBbIjcwODAwMDUwNTA1MDAiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMTUiLCAia2lsZGVyIjogWyJodHRwOi8vd3d3LnV2ZGFsa3JhZnQubm8vY29udGFjdC9uZXR0LyIsICJodHRwOi8vd3d3LnV2ZGFsa3JhZnQubm8vcGRmL1RhcmlmZmhlZnRlMDEwNTIwMjQucGRmIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDUiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBmYWxzZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzgxMS4yfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA1NzIxLjZ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA4MzkwLjR9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAxNjAyMi40fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMjM2NTQuNH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDM1MDk3LjZ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA1NDE4Mi40fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNzcwNjguOH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiAxMDc1OTYuOH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDIyLjU4LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMzAuNTh9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDUtMDEifV19' title='Samle inn data for Uvdal Kraftforsyning' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/uvdal.html" title="Se på tariffen for Uvdal Kraftforsyning" target="_blank">🔍</a>
    <a href="./tariffer/uvdal.yml" title="Se dataene for Uvdal Kraftforsyning i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Vang Energiverk AS ✅</td>
  <td>7080010002297</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDIyOTciXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudmFuZ2VuZXJnaS5uby9uZXR0bGVpZ2UvZm9yYnJ1a2Fya3VuZGFyLyIsICJodHRwczovL3d3dy52YW5nZW5lcmdpLm5vL255aGV0ZXIvIl0sICJuZXR0ZWllciI6ICJWYW5nIEVuZXJnaXZlcmsgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDgsICJ1bm50YWsiOiBbeyJkYWdlciI6IFsiZnJlZGFnIl0sICJtXHUwMGU1bmVkZXIiOiBbImphbnVhciIsICJmZWJydWFyIiwgIm1hcnMiLCAiYXByaWwiLCAib2t0b2JlciIsICJub3ZlbWJlciIsICJkZXNlbWJlciJdLCAibmF2biI6ICJCcnVrc3RpZHN0aWxsZWdnIiwgInByaXMiOiAxOCwgInRpbWVyIjogIjE2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogNDgwMCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNjAwMCwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNzI2MCwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogODUyMCwgInRlcnNrZWwiOiA4fSwgeyJwcmlzIjogMTAwMjAsICJ0ZXJza2VsIjogMTJ9LCB7InByaXMiOiAxMTU4MCwgInRlcnNrZWwiOiAxOH0sIHsicHJpcyI6IDEzMzgwLCAidGVyc2tlbCI6IDI1fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIiwgImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Vang Energiverk AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/vang.html" title="Se på tariffen for Vang Energiverk AS" target="_blank">🔍</a>
    <a href="./tariffer/vang.yml" title="Se dataene for Vang Energiverk AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Vest-Telemark Kraftlag AS Nett ✅</td>
  <td>7080005051927</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTE5MjciXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudGVsZW1hcmstbmV0dC5uby9wcmlzYXIvbmV0dGxlaWdlLTEvIl0sICJuZXR0ZWllciI6ICJWZXN0LVRlbGVtYXJrIEtyYWZ0bGFnIEFTIE5ldHQiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI2fSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMzU0MCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNDU2MCwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogODQwMCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDExNDAwLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMTM5MjAsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAyNDAwMCwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDM5MTIwLCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogNTMxNjAsICJ0ZXJza2VsIjogNzV9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDMtMDEiLCAiaWQiOiAiMjAyNC0wMyIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Vest-Telemark Kraftlag AS Nett' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/telemark.html" title="Se på tariffen for Vest-Telemark Kraftlag AS Nett" target="_blank">🔍</a>
    <a href="./tariffer/telemark.yml" title="Se dataene for Vest-Telemark Kraftlag AS Nett i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Vestall AS ✅</td>
  <td>7080005051897</td>
  <td><em>9181</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTE4OTciXSwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXN0YWxsLm5vL25ldHRsZWllcHJpc2VyLTIwMjQvIl0sICJuZXR0ZWllciI6ICJWZXN0YWxsIEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiA0LjMsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJwcmlzIjogOC42LCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDU0MjQsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDkwMjQsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDEyNzU2LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogMTY0ODgsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiAyMDA2NCwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDMxMDkyLCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMzUxMDAsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiA2Nzc4OCwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDk1MjgwLCAidGVyc2tlbCI6IDEwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vestall AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/vestall.html" title="Se på tariffen for Vestall AS" target="_blank">🔍</a>
    <a href="./tariffer/vestall.yml" title="Se dataene for Vestall AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Vestmar Nett AS ✅</td>
  <td>7080005054928</td>
  <td><em>4567**</em></td>
  <td><code>2024-11-09</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTQ5MjgiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXN0bWFyLW5ldHQubm8vbmV0dC1vZy1uZXR0bGVpZS8iLCAiaHR0cHM6Ly92ZXN0bWFyLW5ldHQubm8vd3AtY29udGVudC91cGxvYWRzLzIwMjQvMDEvVGFyaWZmZXItMDEwMjI0LnBkZiJdLCAibmV0dGVpZXIiOiAiVmVzdG1hciBOZXR0IEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOS44Nn0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDQxMDcuMjQsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDcyNjEuOTIsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDEwNDE2LjYsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiAxMzU3MS4yOCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDE2NzI0LjY0LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMjYxODguNjgsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiA0MTk2MC43NiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDU3NzMyLjk2LCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogODEzOTAuNDgsICJ0ZXJza2VsIjogMTAwfSwgeyJwcmlzIjogMTEyOTM0Ljc2LCAidGVyc2tlbCI6IDE1MH0sIHsicHJpcyI6IDE2MDI1MS4xMiwgInRlcnNrZWwiOiAyMDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDItMDEiLCAiaWQiOiAiMjAyNC0wMi1uMTAwIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vestmar Nett AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/vestmar.html" title="Se på tariffen for Vestmar Nett AS" target="_blank">🔍</a>
    <a href="./tariffer/vestmar.yml" title="Se dataene for Vestmar Nett AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Vevig AS ✅</td>
  <td>7080003807946</td>
  <td><em>8924</em></td>
  <td><code>2024-11-06</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDM4MDc5NDYiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXZpZy5uby9uZXR0bGVpZS1vZy12aWxrYXIvbmV0dGxlaWUtcHJpdmF0LyJdLCAibmV0dGVpZXIiOiAiVmV2aWcgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wNiIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEzLjQsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJwcmlzIjogMjEuNCwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IGZhbHNlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMjAxNiwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMjYxNiwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogMzYzNiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNDY2OCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDU2ODgsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiA2Njk2LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogNzcxNiwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDk3NTYsICJ0ZXJza2VsIjogMzB9LCB7InByaXMiOiAxMTc4NCwgInRlcnNrZWwiOiA0MH0sIHsicHJpcyI6IDE2ODcyLCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogMjE2MzYsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAyNzAzNiwgInRlcnNrZWwiOiAxMDB9LCB7InByaXMiOiAzMjEzNiwgInRlcnNrZWwiOiAxMjV9LCB7InByaXMiOiA0MjMxMiwgInRlcnNrZWwiOiAxNTB9LCB7InByaXMiOiA2MjY2NCwgInRlcnNrZWwiOiAyMDB9LCB7InByaXMiOiA4MzAwNCwgInRlcnNrZWwiOiAzMDB9LCB7InByaXMiOiAyMDUxMDQsICJ0ZXJza2VsIjogNDAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA2LTAxIiwgImlkIjogIjIwMjQtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vevig AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/vevig.html" title="Se på tariffen for Vevig AS" target="_blank">🔍</a>
    <a href="./tariffer/vevig.yml" title="Se dataene for Vevig AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
<tr>
  <td>Vissi AS ✅</td>
  <td>7080004045743</td>
  <td><em>4835</em></td>
  <td><code>2024-11-06</code></td>
  <td>
    <a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDQwNDU3NDMiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudmlzc2kubm8vcHJpc2VyLW9nLXZpbGthci9uZXR0bGVpZS1wcml2YXQvIl0sICJuZXR0ZWllciI6ICJWaXNzaSBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA2IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTIsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJwcmlzIjogMjUsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMjQwMCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNDAzMiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNTY2NCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDcyOTYsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiA4OTI4LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMTQ1OTIsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAxOTYzMiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDI0MTkyLCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogMjg5OTIsICJ0ZXJza2VsIjogMTAwfSwgeyJwcmlzIjogMzI4MzIsICJ0ZXJza2VsIjogMTUwfSwgeyJwcmlzIjogMzc2MzIsICJ0ZXJza2VsIjogMjAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIiwgImlkIjogIjIwMjQtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vissi AS' target='_blank'>✏️</a>
    <a href="https://kraftsystemet.no/fri-nettleie/tariffer/vissi.html" title="Se på tariffen for Vissi AS" target="_blank">🔍</a>
    <a href="./tariffer/vissi.yml" title="Se dataene for Vissi AS i YAML-format" target="_blank">📄</a>
  </td>
</tr>
</table>

<!-- statusstop -->

\* Tallet et basert på datasettet
[CONSUMPTION_PER_GROUP_MGA_HOUR](https://api.elhub.no/api/energy-data#/Grid%20area/grid_areas)
og
[CONSUMPTION_PER_GROUP_MBA_HOUR](https://api.elhub.no/api/energy-data#/Price%20area/price_areas)
fra Elhub. Datasettene inneholder ikke data for små nettavregningsområder. Derfor kan det
reelle tallet avvike noe.

\** Dette er ikke et reelt tall, men en distribusjon av differansen mellom
`CONSUMPTION_PER_GROUP_MGA_HOUR` og `CONSUMPTION_PER_GROUP_MBA_HOUR` på
netteiere hvor vi ikke har noe antall.

## Forvaltere

Forvalterne av dette prosjektet er medlemmene av
[github.com/kraftsystemet](https://github.com/kraftsystemet). Alt vi gjør på
dette prosjektet er som privatpersoner.

## Ofte stilte spørsmål

### Hvorfor gidder dere?

Vi er egentlig bare noen nørder som jobber i kraftbransjen som mener at dette
datasettet bør eksistere. Mens vi venter på at det kommer en skikkelig løsning
basert på rapporterte data fra nettselskapene er vårt forslag å invitere til
dugnad.

### Bør ikke noen andre gjøre dette?

Jo. Vi tror også at det vil komme gode løsninger på dette med tiden. Men i
mellomtiden skader det ikke med en liten dugnad. Det kan selvfølgelig være fare
for å dø av kjedsomhet når man puncher tariffer, men den risikoen tar vi 🤓.

### Hva med NVE sine data?

NVE publiserer både
[tariffer](https://biapi.nve.no/nettleietariffer/swagger/index.html) og
[statistikk](https://api.nve.no/doc/nettleiestatistikk/) basert på
innrapporterte data fra nettselskapene. Dette er gode datasett, men mangler
faktiske beskrivelser av tariffene. Noe av det kan utledes, men ikke fullt ut.
En entydig og korrekt beskrivelse er et godt grunnlag for både analyser og
generering av prissignal. Vi ser også at i noen tilfeller avviker dataene hos
NVE fra nettleien som netteierene oppgir på sine sider. Vi vet ikke hva det
skyldes men vi vet at et dugnadsbasert datasett enkelt kan fikses med en
pull-request.

### Hva med Nettleie API fra Digin/Elbits?

[API-nettleie-for-styring](https://github.com/3lbits/API-nettleie-for-styring)
fungerer knallbra 🚀, men enn så lenge er det ikke alle netteiere som har
implementert det. Et samlet datasett for hele Norge letter også tilgang og
mulighet for analyse.

## Lisens

Dataene og dokumentasjon i dette prosjektet er lisensiert under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Kreditering gjøres
til "Fri nettleie", med lenke til dette prosjektet. Vi bruker denne lisensen for
å gi deg som bruker vide rettigheter til å bruke dataene samtidig som vi ønsker
navngivelse for å sikre synlighet (og dermed bidrag) til nettdugnaden vår.

All kode er lisensiert under [MIT](https://opensource.org/license/MIT). En kopi av [lisensen](./LICENSE-MIT)
og opphavsrett må følge med programvaren.

Data i mappen `referanse-data` er lastet fra andre kilder og brukes for
status-rapportering. Disse dataene har egne lisenser.

* `esett` - Data fra [eSett](https://opendata.esett.com/) lisensiert med
  [CC0](https://creativecommons.org/publicdomain/zero/1.0/)
* `elhub` - Data fra [Elhub](https://api.elhub.no) med uspesifisert lisens
* `nve` - Data fra
  [NVE](https://biapi.nve.no/nettleietariffer/swagger/index.html) lisensiert med
  [NLOD](https://data.norge.no/nlod)
