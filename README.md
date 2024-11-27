# Fri nettleie

> Slipp nettleien fri

En _dugnad_ for å samle nettleie-tariffer i det norske kraftsystemet.

<!-- toc -->

- [Bakgrunn](#bakgrunn)
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
- [Status](#status)
- [Forvaltere](#forvaltere)
- [Lisens](#lisens)

<!-- tocstop -->

## Bakgrunn

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
nettleie-priser for hele landet. De innsamlede dataene
gjøres tilgengelig på standardisert format. Hensikten er å legge til rette for

* at privatpersoner og selskaper skal kunne lage tekniske løsninger som viser
  eller styrer strømforbruk basert på nettleie
* at alle interesserte kan analysere dataene for eksempel for å se forskjeller mellom nettselskaper

At sluttkunder får oversikt over alle komponentene i strømregningen er viktig
for energiøkonomisering, men det er vanskelig å oppnå uten at dataene er lett
tilgjengelig for hele Norge. Lett tilgjengelige data vil også legge til rette
for at nettkundene reagerer på prissignalene i nettleien og styrer sitt forbruk
på en måte som hjelper nettet samtidig som de sparer penger.

## Dataene

Tariff-dataene inkluderer:

* fastledd
* energiledd

Selve tariff-dataene inkluderer ikke avgifter, men prosjektet vil inkludere
maskinlesbare definisjoner av relevante avgifter.

Vi samler inn data per netteier og gjør tilgjengelig data per nettavregningsområde.

### Prissignal

Tariff-dataene inneholder en _beskrivelse_ av tariffen. I tillegg er det et mål
å genererer pris-signal basert på de innsamlede dataene.

Et skript som viser hvordan dette kan gjøres konseptuelt finnes i
[skript/prissignal.py](./skript/prissignal.py). Brukes slik:

```bash
./skript/prissignal.py --fra 2024-10-26 --til 2024-10-28 --tariff-fil tariffer/midtnett.yml
./skript/prissignal.py --fra 2024-10-25 --til 2024-10-28 --tariff-fil tariffer/griug.yml
```

## Mål

- [x] Samle strukturdata for å identifisere alle netteier og nettområder
- [x] Definere format for innsamling
- [x] Vise at det kan genereres prissignal basert på formatet
- [x] Samle tariffer for private husholdninger og hytter/fritidseiendom på yaml
  format for et utvalg nettselskaper (med varierende tariffer)
- [x] Overvåke nettselskapenes sider for å varsle ved endring
- [x] Sammenstille og publisere informasjon per netteier på et "menneskelig" format på kraftsystemet.no/fri-nettleie
- [ ] Samle tariffer for husholdninger og hytter/fritidshus for alle nettområder
- [ ] Koble tariffer til nettavregningsområder
- [ ] Kontinuerlig oppdatere dataene ved endring hos nettselskapene
- [ ] Publisere prissignal basert på de innsamlede tariffene
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

## Utfordringer

Ved innsamling og struktuering av data er det flere utfordringer.

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
I tilleg er det noen som oppgir priser per år mens andre per måned.


### Flere tariffer per netteier

Noen netteiere har ulike tariffer for ulike deler av sitt nett. Dette er typisk
dersom det har vært sammenslåing av konsesjonsområder.

### Priser oppgitt med og uten avgifter

Ved innsamling av tariffer er det utfordrende når noen netteiere gjør
tilgjengelig sine priser med avgifter, mens andre ikke inkluderer avgifter.
Avgiftsnivået er forskjellig avhengig av hvor i landet en netteier er
konsesjonær - det er fort å gjøre feil.

## Avgifter

Det er tre avgifter som gjelder for nettleie:

* Enova-avgift
* Elavgift
* Merverdiavgift

### Enova-avgift

[Forskrift om Energifondet](https://lovdata.no/dokument/SF/forskrift/2001-12-10-1377)
sier at netteier skal legge et påslag på tariffen til alle sluttbrukere på alle
nettnivåer når det faktureres.

> For husholdningsbruk skal påslaget utgjøre 1 øre/kWh. For andre sluttbrukere
> enn husholdninger skal påslaget utgjøre 800 kroner/år per målepunkt-ID.

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

Vanlig moms på 25% betales på nettleie, Enova-avgiften og elavgiften.

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
et issue og lime inn data i yaml-format som en del av beskrivelsen. Alle bidrag
teller!

### Gi besked om feil eller kom med ideer

Dersom du ser feil i dataene, status eller annet - åpne et issue her på GitHub!
Det samme gjelder om du har gode ideer om hvordan vi kan samle inn og/eller
strukturere data.

### Gi oss en stjerne

Det holder oss motivert!

### Si at du bruker våre data

Se under.

## Dataene i bruk

Dette avsnittet viser et utvalg av hvor dataene er i bruk.

* Bli den første på denne lista! Åpne en pull request eller gi beskjed i et
  issue.

## Status

Den følgende listen viser status på innsamlede data.

<!-- statusstart -->

Vi har samlet data for 25 av 66 netteiere 🥳!

<table>
    <tr>
        <th>Navn</th>
        <th>GLN</th>
        <th>Oppdatert</th>
        <th>Handling</th>
    </tr>
<tr>
    <td>Alut AS ✅</td>
    <td>7080010004383</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDQzODMiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly9hbHV0Lm5vL25ldHRsZWllLyJdLCAibmV0dGVpZXIiOiAiQWx1dCBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTMuMX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIk9WX1RSRUZBU0UiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMzUwMCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNDUwMCwgInRlcnNrZWwiOiAxMjV9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Alut AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Arva AS ✅</td>
    <td>7080005051859</td>
    <td><code>2024-11-27</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBcnZhIEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MTg1OSIsICI3MDgwMDA1MDUxMzYxIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI3IiwgImtpbGRlciI6IFsiaHR0cHM6Ly9hcnZhLm5vL2hqZW0vUHJpc2VyIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDEtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTAyMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjQxMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDc3Nn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDcxNDB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA5NTA0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTE4Njh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzY2NH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM1NDYwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDcyNTZ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzEzNDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMS42LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjMuMX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Arva AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Arva AS ✅</td>
    <td>7080005051361</td>
    <td><code>2024-11-27</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBcnZhIEFTIiwgImdsbiI6IFsiNzA4MDAwNTA1MTg1OSIsICI3MDgwMDA1MDUxMzYxIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI3IiwgImtpbGRlciI6IFsiaHR0cHM6Ly9hcnZhLm5vL2hqZW0vUHJpc2VyIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDEtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTAyMH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjQxMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDc3Nn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDcxNDB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA5NTA0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTE4Njh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzY2NH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM1NDYwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDcyNTZ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzEzNDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMS42LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjMuMX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Arva AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Asker Nett AS ✅</td>
    <td>7080003858825</td>
    <td><code>2024-11-27</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBc2tlciBOZXR0IiwgImdsbiI6IFsiNzA4MDAwMzg1ODgyNSJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNyIsICJraWxkZXIiOiBbImh0dHBzOi8vYXNrZXJuZXR0Lm5vL25ldHRsZWllLW9nLXByaXNlci8iLCAiaHR0cHM6Ly9hc2tlcm5ldHQubm8vcHJpc2xpc3RlLWZvci1wcml2YXRrdW5kZXItaS0yMDI0LyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTAxLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDE3NzZ9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIyMDh9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDMyNjR9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA2ODE2fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogODU5Mn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDEwODQ4fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTUzNjB9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNDM4NH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDMyNDQ4fSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDUxODQwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogOC45NiwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDE1Ljg4OH0sIHsibmF2biI6ICJWaW50ZXJsYXN0IiwgIm1cdTAwZTVuZWRlciI6IFsiamFudWFyIiwgImZlYnJ1YXIiLCAibWFycyJdLCAidGlsbGVnZyI6IDh9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV19' title='Samle inn data for Asker Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>BKK AS ✅</td>
    <td>7080005051378</td>
    <td><code>2024-11-27</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCS0sgQVMgIiwgImdsbiI6IFsiNzA4MDAwNTA1MTM3OCJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNyIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmJray5uby9hbHQtb20tbmV0dGxlaWUvbmV0dGxlaWVwcmlzZXIiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wNC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAxNTM2fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNDk2fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0MTI4fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNTk1Mn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDc2ODB9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA5MzYwfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTc5NTJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNjQ5Nn0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDM1MDQwfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDY5MTIwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTkuNzc2LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3Qgdmlya2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjkuOTYsICJkYWdlciI6IFsidmlya2VkYWciXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNC0wMSJ9XX0=' title='Samle inn data for BKK AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Bindal Kraftlag Nett</td>
    <td>7080005055963</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCaW5kYWwgS3JhZnRsYWcgTmV0dCIsICJnbG4iOiAiNzA4MDAwNTA1NTk2MyJ9' title='Samle inn data for Bindal Kraftlag Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Breheim Nett</td>
    <td>7080010010919</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCcmVoZWltIE5ldHQiLCAiZ2xuIjogIjcwODAwMTAwMTA5MTkifQ==' title='Samle inn data for Breheim Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Bømlo Kraftnett AS</td>
    <td>7080010002327</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCXHUwMGY4bWxvIEtyYWZ0bmV0dCBBUyIsICJnbG4iOiAiNzA4MDAxMDAwMjMyNyJ9' title='Samle inn data for Bømlo Kraftnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>DE Nett AS</td>
    <td>7080010003614</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJERSBOZXR0IEFTIiwgImdsbiI6ICI3MDgwMDEwMDAzNjE0In0=' title='Samle inn data for DE Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Elinett AS</td>
    <td>7080005053044</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbGluZXR0IEFTIiwgImdsbiI6ICI3MDgwMDA1MDUzMDQ0In0=' title='Samle inn data for Elinett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Elvenett AS</td>
    <td>7080005052917</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbHZlbmV0dCBBUyIsICJnbG4iOiAiNzA4MDAwNTA1MjkxNyJ9' title='Samle inn data for Elvenett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Elvia AS ✅</td>
    <td>7080005046220</td>
    <td><code>2024-11-27</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbHZpYSBBUyIsICJnbG4iOiBbIjcwODAwMDUwNDYyMjAiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMjciLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5lbHZpYS5uby9uZXR0bGVpZS9hbHQtb20tbmV0dGxlaWVwcmlzZXIvbmV0dGxlaWVwcmlzZXItZm9yLXByaXZhdGt1bmRlci8iLCAiaHR0cHM6Ly93d3cuZWx2aWEubm8vbmV0dGxlaWUvYWx0LW9tLW5ldHRsZWllcHJpc2VyL3ByaXNlbi1wYS1uZXR0bGVpZS1nYXItbmVkLyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTEwLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDEzNDR9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIyMDh9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDM2MDB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA1MDQwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNjQ4MH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDc4NzJ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxNDk3Nn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDIyMDgwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjkwODh9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNTgwODB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOC41NiwgInVubnRhayI6IFt7Im5hdm4iOiAiVmlya2VkYWciLCAidGltZXIiOiAiNi0yMSIsICJkYWdlciI6IFsidmlya2VkYWciXSwgInByaXMiOiAyNC4xNn1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0xMC0wMSIsICJneWxkaWdfdGlsIjogIjIwMjUtMDEtMDEifSwgeyJpZCI6ICIyMDI1LTAxLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDEyOTZ9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIwNjR9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDMzNjB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA0NjU2fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNTk1Mn0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDcyNDh9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMzY4MH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDIwMTYwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjY2NDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNTM4MDh9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiA4LjU2LCAidW5udGFrIjogW3sibmF2biI6ICJWaXJrZWRhZyIsICJ0aW1lciI6ICI2LTIxIiwgImRhZ2VyIjogWyJ2aXJrZWRhZyJdLCAicHJpcyI6IDE2LjU2fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI1LTAxLTAxIn1dfQ==' title='Samle inn data for Elvia AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Enida AS</td>
    <td>7080003871534</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbmlkYSBBUyIsICJnbG4iOiAiNzA4MDAwMzg3MTUzNCJ9' title='Samle inn data for Enida AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Etna Nett AS</td>
    <td>7080005046404</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFdG5hIE5ldHQgQVMiLCAiZ2xuIjogIjcwODAwMDUwNDY0MDQifQ==' title='Samle inn data for Etna Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Everket AS</td>
    <td>7080005052825</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFdmVya2V0IEFTIiwgImdsbiI6ICI3MDgwMDA1MDUyODI1In0=' title='Samle inn data for Everket AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Fagne AS</td>
    <td>7080003809599</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGYWduZSBBUyIsICJnbG4iOiAiNzA4MDAwMzgwOTU5OSJ9' title='Samle inn data for Fagne AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Fjellnett AS ✅</td>
    <td>7080010000316</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDAzMTYiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZmplbGxuZXR0Lm5vL25ldHRsZWllL2F2dGFsZXItb2ctdmlsa2FyL2ZlbGxlc2Jlc3RlbW1lbHNlci8iLCAiaHR0cHM6Ly93d3cuZmplbGxuZXR0Lm5vL25ldHRsZWllcHJpc2VyL3ByaXZhdGt1bmRlci8iXSwgIm5ldHRlaWVyIjogIkZqZWxsbmV0dCBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTAuNjA4fSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiRkVNX1ZFS1RFVF9cdTAwYzVSIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDE3MDAuMDA0LCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiAyMTY4LjgsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDI2MzcuNiwgInRlcnNrZWwiOiAzfSwgeyJwcmlzIjogMzU3NS4yLCAidGVyc2tlbCI6IDR9LCB7InByaXMiOiA0MDQ0LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA0NTEyLjgsICJ0ZXJza2VsIjogNn0sIHsicHJpcyI6IDQ5ODEuNiwgInRlcnNrZWwiOiA3fSwgeyJwcmlzIjogNTQ1MC40LCAidGVyc2tlbCI6IDh9LCB7InByaXMiOiA1OTE5LjIsICJ0ZXJza2VsIjogOX0sIHsicHJpcyI6IDYzODgsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA2ODU2LjgsICJ0ZXJza2VsIjogMTF9LCB7InByaXMiOiA3MzI1LjYsICJ0ZXJza2VsIjogMTJ9LCB7InByaXMiOiA3Nzk0LjQsICJ0ZXJza2VsIjogMTN9LCB7InByaXMiOiA4MjYzLjIsICJ0ZXJza2VsIjogMTR9LCB7InByaXMiOiA4NzMyLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogOTIwMC44LCAidGVyc2tlbCI6IDE2fSwgeyJwcmlzIjogOTY2OS42LCAidGVyc2tlbCI6IDE3fSwgeyJwcmlzIjogMTAxMzguNCwgInRlcnNrZWwiOiAxOH0sIHsicHJpcyI6IDEwNjA3LjIsICJ0ZXJza2VsIjogMTl9LCB7InByaXMiOiAxMTA3NiwgInRlcnNrZWwiOiAyMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Fjellnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Føie AS</td>
    <td>7080005048415</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGXHUwMGY4aWUgQVMiLCAiZ2xuIjogIjcwODAwMDUwNDg0MTUifQ==' title='Samle inn data for Føie AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Føre AS</td>
    <td>7080010003836</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGXHUwMGY4cmUgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDM4MzYifQ==' title='Samle inn data for Føre AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Glitre Nett AS ✅</td>
    <td>7080005052672</td>
    <td><code>2024-11-25</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNTYwNjkiLCAiNzA4MDAwNTA1MjY3MiJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNSIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmdsaXRyZW5ldHQubm8va3VuZGUvbmV0dGxlaWUtb2ctcHJpc2VyL25ldHRsZWllcHJpc2VyLXByaXZhdGt1bmRlIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMTAtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjA0MH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjU4MH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDQ0MH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDkxMjB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAxMTg4MH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDE0ODgwfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMjMwNDB9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAzNjQ4MH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDQ4NjAwfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDc4OTYwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTUuMzYsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAyNC45Nn1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0xMC0wMSJ9XX0=' title='Samle inn data for Glitre Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Glitre Nett AS ✅</td>
    <td>7080005056069</td>
    <td><code>2024-11-25</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyIsICJnbG4iOiBbIjcwODAwMDUwNTYwNjkiLCAiNzA4MDAwNTA1MjY3MiJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNSIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmdsaXRyZW5ldHQubm8va3VuZGUvbmV0dGxlaWUtb2ctcHJpc2VyL25ldHRsZWllcHJpc2VyLXByaXZhdGt1bmRlIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMTAtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjA0MH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjU4MH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDQ0MH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDkxMjB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAxMTg4MH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDE0ODgwfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMjMwNDB9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAzNjQ4MH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDQ4NjAwfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDc4OTYwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTUuMzYsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAyNC45Nn1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0xMC0wMSJ9XX0=' title='Samle inn data for Glitre Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Griug AS ✅</td>
    <td>7080005052900</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTI5MDAiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZ3JpdWcubm8vb20tbmV0dGxlaWUtb2ctcHJpc2VyL3ByaXNlci9uZXR0bGVpZXByaXNlci0yMDI0LyJdLCAibmV0dGVpZXIiOiAiR3JpdWcgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDkuOCwgInVubnRhayI6IFt7ImRhZ2VyIjogWyJmcmVkYWciXSwgIm1cdTAwZTVuZWRlciI6IFsiamFudWFyIiwgImZlYnJ1YXIiLCAibWFycyIsICJva3RvYmVyIiwgIm5vdmVtYmVyIiwgImRlc2VtYmVyIl0sICJuYXZuIjogIkJydWtzdGlkc3RpbGxlZ2ciLCAidGlsbGVnZyI6IDExLCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDIxMTIsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDMxNjgsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDQ3NTIsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDYwOTYsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA3NjgwLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogOTMxMiwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDE3NDI0LCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMjU1ODQsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiAzNDMyMCwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDY4MTEyLCAidGVyc2tlbCI6IDEwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Griug AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Havnett AS</td>
    <td>7080010001832</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJIYXZuZXR0IEFTIiwgImdsbiI6ICI3MDgwMDEwMDAxODMyIn0=' title='Samle inn data for Havnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Hydro Energi AS nett</td>
    <td>7080005052818</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJIeWRybyBFbmVyZ2kgQVMgbmV0dCIsICJnbG4iOiAiNzA4MDAwNTA1MjgxOCJ9' title='Samle inn data for Hydro Energi AS nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Høland og Setskog Elverk AS</td>
    <td>7080004320253</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJIXHUwMGY4bGFuZCBvZyBTZXRza29nIEVsdmVyayBBUyIsICJnbG4iOiAiNzA4MDAwNDMyMDI1MyJ9' title='Samle inn data for Høland og Setskog Elverk AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Indre Hordaland Kraftnett AS</td>
    <td>7080010008367</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJJbmRyZSBIb3JkYWxhbmQgS3JhZnRuZXR0IEFTIiwgImdsbiI6ICI3MDgwMDEwMDA4MzY3In0=' title='Samle inn data for Indre Hordaland Kraftnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Jæren Everk AS</td>
    <td>7080010002419</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJKXHUwMGU2cmVuIEV2ZXJrIEFTIiwgImdsbiI6ICI3MDgwMDEwMDAyNDE5In0=' title='Samle inn data for Jæren Everk AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>KE Nett AS</td>
    <td>7080005046060</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLRSBOZXR0IEFTIiwgImdsbiI6ICI3MDgwMDA1MDQ2MDYwIn0=' title='Samle inn data for KE Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Klive AS</td>
    <td>7080010000132</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLbGl2ZSBBUyIsICJnbG4iOiAiNzA4MDAxMDAwMDEzMiJ9' title='Samle inn data for Klive AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Kvam Energi Nett AS</td>
    <td>7080010001276</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLdmFtIEVuZXJnaSBOZXR0IEFTIiwgImdsbiI6ICI3MDgwMDEwMDAxMjc2In0=' title='Samle inn data for Kvam Energi Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Kystnett AS</td>
    <td>7080010000064</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJLeXN0bmV0dCBBUyIsICJnbG4iOiAiNzA4MDAxMDAwMDA2NCJ9' title='Samle inn data for Kystnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Lede AS</td>
    <td>7080005050975</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMZWRlIEFTIiwgImdsbiI6ICI3MDgwMDA1MDUwOTc1In0=' title='Samle inn data for Lede AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Linja AS ✅</td>
    <td>7080001319830</td>
    <td><code>2024-11-03</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDEzMTk4MzAiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubGluamEubm8vbmV0dGxlaWdlIl0sICJuZXR0ZWllciI6ICJMaW5qYSBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTAzIiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMjAuNDI0LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDI3LjIzMiwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAyNjQwLCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiAzMjkyLjgsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDM5NDUuNiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNjU4NS42LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogNzkxMC40LCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogOTIxNiwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDEzMTgwLjgsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAxNDQ5NiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDE1ODAxLjYsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAxOTc2Ni40LCAidGVyc2tlbCI6IDEwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNy0wMSIsICJneWxkaWdfdGlsIjogbnVsbCwgImlkIjogIm5vcmQtcHJpdmF0IiwgIm5hdm4iOiAiTm9yZCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifSwgeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNS4zODQsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJwcmlzIjogMjIuMzg0LCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDI2NjguOCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMzcwNS42LCAidGVyc2tlbCI6IDJ9LCB7InByaXMiOiA0NzQyLjQsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDY4MTYuMCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDgxOTguNCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDk1OTAuNCwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDEyMTgyLjQsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAxMzU2NC44LCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogMTQ5NTYuOCwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDE4NDEyLjgsICJ0ZXJza2VsIjogMTAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA3LTAxIiwgImd5bGRpZ190aWwiOiBudWxsLCAiaWQiOiAic1x1MDBmOHItcHJpdmF0IiwgIm5hdm4iOiAiU1x1MDBmOHIiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Linja AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Lucerna AS</td>
    <td>7080005050661</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMdWNlcm5hIEFTIiwgImdsbiI6ICI3MDgwMDA1MDUwNjYxIn0=' title='Samle inn data for Lucerna AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Lyse Produksjon AS Nett</td>
    <td>7080003307231</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMeXNlIFByb2R1a3Nqb24gQVMgTmV0dCIsICJnbG4iOiAiNzA4MDAwMzMwNzIzMSJ9' title='Samle inn data for Lyse Produksjon AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Lysna AS</td>
    <td>7080010013088</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMeXNuYSBBUyIsICJnbG4iOiAiNzA4MDAxMDAxMzA4OCJ9' title='Samle inn data for Lysna AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Meløy Nett AS</td>
    <td>7080003968395</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJNZWxcdTAwZjh5IE5ldHQgQVMiLCAiZ2xuIjogIjcwODAwMDM5NjgzOTUifQ==' title='Samle inn data for Meløy Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Midtnett AS ✅</td>
    <td>7080003869012</td>
    <td><code>2024-11-03</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDM4NjkwMTIiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubWlkdG5ldHQubm8vbmV0dGxlaWUiLCAiaHR0cHM6Ly93d3cubWlkdG5ldHQubm8vbWVkaWEvMjkxOS9uZXR0bGVpZXByaXNlci1mcmEtMS1hcHJpbC0yMDI0LnBkZiJdLCAibmV0dGVpZXIiOiAiTWlkdG5ldHQgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wMyIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI2LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDMxLCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDI2NDAsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDM5NjAsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDYwMDAsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA5MDAwLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMTIwMDAsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAxNjc2NCwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDI1MTUyLCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogMzEyMDAsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAzNjAwMCwgInRlcnNrZWwiOiAxMDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDQtMDEiLCAiZ3lsZGlnX3RpbCI6IG51bGwsICJpZCI6ICJobjIyLXByaXZhdCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Midtnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Modalen Kraftlag Nett</td>
    <td>7080003816184</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJNb2RhbGVuIEtyYWZ0bGFnIE5ldHQiLCAiZ2xuIjogIjcwODAwMDM4MTYxODQifQ==' title='Samle inn data for Modalen Kraftlag Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Nettselskapet AS</td>
    <td>7080004064553</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOZXR0c2Vsc2thcGV0IEFTIiwgImdsbiI6ICI3MDgwMDA0MDY0NTUzIn0=' title='Samle inn data for Nettselskapet AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Noranett AS</td>
    <td>7080003811318</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JhbmV0dCBBUyIsICJnbG4iOiAiNzA4MDAwMzgxMTMxOCJ9' title='Samle inn data for Noranett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Nordvest Nett AS</td>
    <td>7080005052801</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JkdmVzdCBOZXR0IEFTIiwgImdsbiI6ICI3MDgwMDA1MDUyODAxIn0=' title='Samle inn data for Nordvest Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Norefjell Nett AS</td>
    <td>7080010003911</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JlZmplbGwgTmV0dCBBUyIsICJnbG4iOiAiNzA4MDAxMDAwMzkxMSJ9' title='Samle inn data for Norefjell Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Norgesnett AS</td>
    <td>7080005052702</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJOb3JnZXNuZXR0IEFTIiwgImdsbiI6ICI3MDgwMDA1MDUyNzAyIn0=' title='Samle inn data for Norgesnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>R-Nett AS</td>
    <td>7080010012852</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSLU5ldHQgQVMiLCAiZ2xuIjogIjcwODAwMTAwMTI4NTIifQ==' title='Samle inn data for R-Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Rakkestad Energi AS Nett</td>
    <td>7080005054898</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSYWtrZXN0YWQgRW5lcmdpIEFTIE5ldHQiLCAiZ2xuIjogIjcwODAwMDUwNTQ4OTgifQ==' title='Samle inn data for Rakkestad Energi AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Romsdalsnett AS</td>
    <td>7080010005427</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSb21zZGFsc25ldHQgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDU0MjcifQ==' title='Samle inn data for Romsdalsnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Røros E-verk Nett AS</td>
    <td>7080003947932</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJSXHUwMGY4cm9zIEUtdmVyayBOZXR0IEFTIiwgImdsbiI6ICI3MDgwMDAzOTQ3OTMyIn0=' title='Samle inn data for Røros E-verk Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>S-NETT AS</td>
    <td>7080010002464</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTLU5FVFQgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDI0NjQifQ==' title='Samle inn data for S-NETT AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>SkiakerNett AS</td>
    <td>7080004062702</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTa2lha2VyTmV0dCBBUyIsICJnbG4iOiAiNzA4MDAwNDA2MjcwMiJ9' title='Samle inn data for SkiakerNett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Stannum AS</td>
    <td>7080010003959</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdGFubnVtIEFTIiwgImdsbiI6ICI3MDgwMDEwMDAzOTU5In0=' title='Samle inn data for Stannum AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Stram AS</td>
    <td>7080003822901</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhbSBBUyIsICJnbG4iOiAiNzA4MDAwMzgyMjkwMSJ9' title='Samle inn data for Stram AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Straumen Nett AS</td>
    <td>7080010003720</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhdW1lbiBOZXR0IEFTIiwgImdsbiI6ICI3MDgwMDEwMDAzNzIwIn0=' title='Samle inn data for Straumen Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Straumnett AS ✅</td>
    <td>7080004053632</td>
    <td><code>2024-11-25</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhdW1uZXR0IEFTIiwgImdsbiI6IFsiNzA4MDAwNDA1MzYzMiJdLCAia2lsZGVyIjogWyJodHRwczovL3N0cmF1bW5ldHQubm8vcHJpc2FyLWZvci1uZXR0bGVpZ2UiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMjUiLCAidGFyaWZmZXIiOiBbeyJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiaWQiOiAiMjAyNCIsICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDI0MzUuMzI4fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyOTIyLjQzMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMzE2NS45ODR9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAzNDA5LjUzNn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDM2NTMuMDg4fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogNDI2MS45Mn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDQ2MjcuMn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDUxMTQuMzA0fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNTYwMS4zMTJ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNjA4OC40MTZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMS41NiwgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDE2LjU2fV19fV19' title='Samle inn data for Straumnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>SuNett AS ✅</td>
    <td>7080010003218</td>
    <td><code>2024-11-24</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdU5ldHQgQVMiLCAiZ2xuIjogWyI3MDgwMDEwMDAzMjE4Il0sICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnN1bm5kYWxlbmVyZ2luZXR0Lm5vL25ldHRsZWllLyIsICJodHRwczovL3d3dy5zdW5uZGFsZW5lcmdpbmV0dC5uby9uZXR0bGVpZS9uZXR0YXZ0YWxlci9uZXR0bGVpZS1wcml2YXQvIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI0IiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wNC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiT1ZfVFJFRkFTRSIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDE2NDYuNH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDMyOTJ9LCB7InRlcnNrZWwiOiA2MywgInByaXMiOiA2NTg0Ljh9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNi44OCwgInVubnRhayI6IFt7Im5hdm4iOiAiVmludGVyIiwgInByaXMiOiAxOS4yOCwgIm1cdTAwZTVuZWRlciI6IFsiamFudWFyIiwgImZlYnJ1YXIiLCAibWFycyIsICJhcHJpbCIsICJub3ZlbWJlciIsICJkZXNlbWJlciJdfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA0LTAxIn1dfQ==' title='Samle inn data for SuNett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Sygnir AS ✅</td>
    <td>7080010009654</td>
    <td><code>2024-11-26</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDk2NTQiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly9zdGF0aWMxLnNxdWFyZXNwYWNlLmNvbS9zdGF0aWMvNjFkZmU3YjMxOTk5NTkxOTcyMjU0ZGVhL3QvNjU3YWYxYmM4YjNiMzU3OTQ3MTViZWY3LzE3MDI1NTYwOTQxMTgvTmV0dGxlaWdlcHJpc2FyK3ByKzAxLjAxLjI0LnBkZiIsICJodHRwczovL3d3dy5zeWduaXIubm8vbmV0dGxlaWdlIl0sICJuZXR0ZWllciI6ICJTeWduaXIgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNiIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDE4Ljc4NH0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDI0MjIuNCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMjkwNi40LCAidGVyc2tlbCI6IDF9LCB7InByaXMiOiAzMzkwLjQsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDM4NzUuMiwgInRlcnNrZWwiOiAzfSwgeyJwcmlzIjogNDM2MCwgInRlcnNrZWwiOiA0fSwgeyJwcmlzIjogNTA4Ni40LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA1ODEyLjgsICJ0ZXJza2VsIjogNn0sIHsicHJpcyI6IDY1MzkuMiwgInRlcnNrZWwiOiA3fSwgeyJwcmlzIjogNzI2Ni40LCAidGVyc2tlbCI6IDh9LCB7InByaXMiOiA3OTkyLjgsICJ0ZXJza2VsIjogOX0sIHsicHJpcyI6IDk0NDYuNCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDEwODk5LjIsICJ0ZXJza2VsIjogMTJ9LCB7InByaXMiOiAxMjM1Mi44LCAidGVyc2tlbCI6IDE0fSwgeyJwcmlzIjogMTM4MDUuNiwgInRlcnNrZWwiOiAxNn0sIHsicHJpcyI6IDE1MjU5LjIsICJ0ZXJza2VsIjogMTh9LCB7InByaXMiOiAyNzM2OS42LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMzk0ODAsICJ0ZXJza2VsIjogNDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Sygnir AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Sør Aurdal Energi AS Nett ✅</td>
    <td>7080005046459</td>
    <td><code>2024-11-24</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTXHUwMGY4ciBBdXJkYWwgRW5lcmdpIEFTIE5ldHQiLCAiZ2xuIjogWyI3MDgwMDA1MDQ2NDU5Il0sICJraWxkZXIiOiBbImh0dHBzOi8vc2FlLm5vL3RhcmlmZmVyIiwgImh0dHBzOi8vc2FlLm5vL3VwbG9hZHMvS3VuZGVpbmZvcm1hc2pvbi8yMDI0XzA4X0t1bmRlaW5mb3JtYXNqb25fdGFyaWZmZXIucGRmIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI0IiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wOS1uMTAwIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIk1ORF9NQVgiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBmYWxzZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogNTQwMH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNjI0MH0sIHsidGVyc2tlbCI6IDgsICJwcmlzIjogNzQ0MH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDg2NDB9LCB7InRlcnNrZWwiOiAzMCwgInByaXMiOiA5NzIwfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMTMyMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyMS41MiwgInVubnRhayI6IFt7Im5hdm4iOiAiVmludGVyIiwgInByaXMiOiAyNS41MiwgIm1cdTAwZTVuZWRlciI6IFsiamFudWFyIiwgImZlYnJ1YXIiLCAibWFycyIsICJva3RvYmVyIiwgIm5vdmVtYmVyIiwgImRlc2VtYmVyIl19XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEifV19' title='Samle inn data for Sør Aurdal Energi AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Tensio TS AS ✅</td>
    <td>7080005051880</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTE4ODAiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudGVuc2lvLm5vL25vL2t1bmRlL25ldHRsZWllL25ldHRsZWllcHJpc2VyLXNlcHRlbWJlci0yMDI0LXRuIiwgImh0dHBzOi8vd3d3LnRlbnNpby5uby9uby9rdW5kZS9uZXR0bGVpZS9uZXR0bGVpZXByaXNlci1zZXB0ZW1iZXItdHMiXSwgIm5ldHRlaWVyIjogIlRlbnNpbyBUUyBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMzkuNjgsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJwcmlzIjogNTcuNDMsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMTc3NiwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMzU1MiwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNjQzMiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogOTc1NiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDEzMDY4LCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMTY0MDQsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAyODU3MiwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDQ1MjA0LCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogNjE4MTIsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiA4OTQ4NCwgInRlcnNrZWwiOiAxMDB9LCB7InByaXMiOiAxMjI3NDgsICJ0ZXJza2VsIjogMTUwfSwgeyJwcmlzIjogMTc4MDkyLCAidGVyc2tlbCI6IDIwMH0sIHsicHJpcyI6IDI0NDU3MiwgInRlcnNrZWwiOiAzMDB9LCB7InByaXMiOiAzMTEwNDAsICJ0ZXJza2VsIjogNDAwfSwgeyJwcmlzIjogMzc3NDYwLCAidGVyc2tlbCI6IDUwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wOS0wMSIsICJpZCI6ICIyMDI0LTA3LXRuIiwgIm5hdm4iOiAiTm9yZCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifSwgeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAzNS45MywgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInByaXMiOiA1MC4xOCwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAxNjA4LCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiAyODY4LCAidGVyc2tlbCI6IDJ9LCB7InByaXMiOiA0ODk2LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA3MjEyLCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogOTUyOCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDExODY4LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMjAzODgsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAzMjAwNCwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDQzNjIwLCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogNjMwMDAsICJ0ZXJza2VsIjogMTAwfSwgeyJwcmlzIjogODYyMjAsICJ0ZXJza2VsIjogMTUwfSwgeyJwcmlzIjogMTI0OTMyLCAidGVyc2tlbCI6IDIwMH0sIHsicHJpcyI6IDE3MTQ1NiwgInRlcnNrZWwiOiAzMDB9LCB7InByaXMiOiAyMTc4OTYsICJ0ZXJza2VsIjogNDAwfSwgeyJwcmlzIjogMjY0Mzg0LCAidGVyc2tlbCI6IDUwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wOS0wMSIsICJpZCI6ICIyMDI0LTA5LXRzIiwgIm5hdm4iOiAiU1x1MDBmOHIiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Tensio TS AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Tinfos AS Nett ✅</td>
    <td>7080003612595</td>
    <td><code>2024-11-24</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJUaW5mb3MgQVMgTmV0dCIsICJnbG4iOiBbIjcwODAwMDM2MTI1OTUiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMjQiLCAia2lsZGVyIjogWyJodHRwczovL3d3dy50aW5mb3Mubm8vdGluZm9zLW5ldHQvIiwgImh0dHBzOi8vYmlhcGkubnZlLm5vL25ldHRsZWlldGFyaWZmZXIvc3dhZ2dlci9pbmRleC5odG1sIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIm52ZSIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJVS0pFTlQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBudWxsLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAzMTU2fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0OTU2fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNjc1Nn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDg1NTZ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAxMDM1Nn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDE1NzU2fSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogNDUwMDB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV19' title='Samle inn data for Tinfos AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Uvdal Kraftforsyning ✅</td>
    <td>7080005050500</td>
    <td><code>2024-11-15</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJVdmRhbCBLcmFmdGZvcnN5bmluZyIsICJnbG4iOiBbIjcwODAwMDUwNTA1MDAiXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMTUiLCAia2lsZGVyIjogWyJodHRwOi8vd3d3LnV2ZGFsa3JhZnQubm8vY29udGFjdC9uZXR0LyIsICJodHRwOi8vd3d3LnV2ZGFsa3JhZnQubm8vcGRmL1RhcmlmZmhlZnRlMDEwNTIwMjQucGRmIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDUiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBmYWxzZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzgxMS4yfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA1NzIxLjZ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA4MzkwLjR9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAxNjAyMi40fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMjM2NTQuNH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDM1MDk3LjZ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA1NDE4Mi40fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNzcwNjguOH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiAxMDc1OTYuOH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDIyLjU4LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMzAuNTh9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDUtMDEifV19' title='Samle inn data for Uvdal Kraftforsyning' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vang Energiverk AS ✅</td>
    <td>7080010002297</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMTAwMDIyOTciXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudmFuZ2VuZXJnaS5uby9uZXR0bGVpZ2UvZm9yYnJ1a2Fya3VuZGFyLyIsICJodHRwczovL3d3dy52YW5nZW5lcmdpLm5vL255aGV0ZXIvIl0sICJuZXR0ZWllciI6ICJWYW5nIEVuZXJnaXZlcmsgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDgsICJ1bm50YWsiOiBbeyJkYWdlciI6IFsiZnJlZGFnIl0sICJtXHUwMGU1bmVkZXIiOiBbImphbnVhciIsICJmZWJydWFyIiwgIm1hcnMiLCAiYXByaWwiLCAib2t0b2JlciIsICJub3ZlbWJlciIsICJkZXNlbWJlciJdLCAibmF2biI6ICJCcnVrc3RpZHN0aWxsZWdnIiwgInRpbGxlZ2ciOiAxMCwgInRpbWVyIjogIjE2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogNDgwMCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNjAwMCwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNzI2MCwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogODUyMCwgInRlcnNrZWwiOiA4fSwgeyJwcmlzIjogMTAwMjAsICJ0ZXJza2VsIjogMTJ9LCB7InByaXMiOiAxMTU4MCwgInRlcnNrZWwiOiAxOH0sIHsicHJpcyI6IDEzMzgwLCAidGVyc2tlbCI6IDI1fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIiwgImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Vang Energiverk AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vest-Telemark Kraftlag AS Nett ✅</td>
    <td>7080005051927</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTE5MjciXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudGVsZW1hcmstbmV0dC5uby9wcmlzYXIvbmV0dGxlaWdlLTEvIl0sICJuZXR0ZWllciI6ICJWZXN0LVRlbGVtYXJrIEtyYWZ0bGFnIEFTIE5ldHQiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDI2fSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMzU0MCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNDU2MCwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogODQwMCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDExNDAwLCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMTM5MjAsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAyNDAwMCwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDM5MTIwLCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogNTMxNjAsICJ0ZXJza2VsIjogNzV9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDMtMDEiLCAiaWQiOiAiMjAyNC0wMyIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Vest-Telemark Kraftlag AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vestall AS ✅</td>
    <td>7080005051897</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTE4OTciXSwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXN0YWxsLm5vL25ldHRsZWllcHJpc2VyLTIwMjQvIl0sICJuZXR0ZWllciI6ICJWZXN0YWxsIEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiA0LjMsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJwcmlzIjogOC42LCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDU0MjQsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDkwMjQsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDEyNzU2LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogMTY0ODgsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiAyMDA2NCwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDMxMDkyLCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMzUxMDAsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiA2Nzc4OCwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDk1MjgwLCAidGVyc2tlbCI6IDEwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vestall AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vestmar Nett AS ✅</td>
    <td>7080005054928</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDUwNTQ5MjgiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXN0bWFyLW5ldHQubm8vbmV0dC1vZy1uZXR0bGVpZS8iLCAiaHR0cHM6Ly92ZXN0bWFyLW5ldHQubm8vd3AtY29udGVudC91cGxvYWRzLzIwMjQvMDEvVGFyaWZmZXItMDEwMjI0LnBkZiJdLCAibmV0dGVpZXIiOiAiVmVzdG1hciBOZXR0IEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOS44Nn0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDQxMDcuMjQsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDcyNjEuOTIsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDEwNDE2LjYsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiAxMzU3MS4yOCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDE2NzI0LjY0LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMjYxODguNjgsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiA0MTk2MC43NiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDU3NzMyLjk2LCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogODEzOTAuNDgsICJ0ZXJza2VsIjogMTAwfSwgeyJwcmlzIjogMTEyOTM0Ljc2LCAidGVyc2tlbCI6IDE1MH0sIHsicHJpcyI6IDE2MDI1MS4xMiwgInRlcnNrZWwiOiAyMDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDItMDEiLCAiaWQiOiAiMjAyNC0wMi1uMTAwIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vestmar Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vevig AS ✅</td>
    <td>7080003807946</td>
    <td><code>2024-11-06</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDM4MDc5NDYiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXZpZy5uby9uZXR0bGVpZS1vZy12aWxrYXIvbmV0dGxlaWUtcHJpdmF0LyJdLCAibmV0dGVpZXIiOiAiVmV2aWcgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wNiIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEzLjQsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJwcmlzIjogMjEuNCwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IGZhbHNlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMjAxNiwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMjYxNiwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogMzYzNiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNDY2OCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDU2ODgsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiA2Njk2LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogNzcxNiwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDk3NTYsICJ0ZXJza2VsIjogMzB9LCB7InByaXMiOiAxMTc4NCwgInRlcnNrZWwiOiA0MH0sIHsicHJpcyI6IDE2ODcyLCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogMjE2MzYsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAyNzAzNiwgInRlcnNrZWwiOiAxMDB9LCB7InByaXMiOiAzMjEzNiwgInRlcnNrZWwiOiAxMjV9LCB7InByaXMiOiA0MjMxMiwgInRlcnNrZWwiOiAxNTB9LCB7InByaXMiOiA2MjY2NCwgInRlcnNrZWwiOiAyMDB9LCB7InByaXMiOiA4MzAwNCwgInRlcnNrZWwiOiAzMDB9LCB7InByaXMiOiAyMDUxMDQsICJ0ZXJza2VsIjogNDAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA2LTAxIiwgImd5bGRpZ190aWwiOiBudWxsLCAiaWQiOiAiMjAyNC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Vevig AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vissi AS ✅</td>
    <td>7080004045743</td>
    <td><code>2024-11-06</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiBbIjcwODAwMDQwNDU3NDMiXSwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudmlzc2kubm8vcHJpc2VyLW9nLXZpbGthci9uZXR0bGVpZS1wcml2YXQvIl0sICJuZXR0ZWllciI6ICJWaXNzaSBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA2IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTIsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJwcmlzIjogMjUsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMjQwMCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogNDAzMiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNTY2NCwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDcyOTYsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiA4OTI4LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMTQ1OTIsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAxOTYzMiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDI0MTkyLCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogMjg5OTIsICJ0ZXJza2VsIjogMTAwfSwgeyJwcmlzIjogMzI4MzIsICJ0ZXJza2VsIjogMTUwfSwgeyJwcmlzIjogMzc2MzIsICJ0ZXJza2VsIjogMjAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIiwgImd5bGRpZ190aWwiOiBudWxsLCAiaWQiOiAiMjAyNC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Vissi AS' target='_blank'>✏️</a></td>
</tr>
</table>

<!-- statusstop -->

## Forvaltere

Forvalterne av dette prosjektet er medlemmene av
[github.com/kraftsystemet](https://github.com/kraftsystemet). Alt vi gjør på
dette prosjektet er som privatpersoner.

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
