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

Vi jobber med verktøy som kan brukes ved manuell innsamling som hostes på
[kraftsystemet.no/fri-nettleie/](http://kraftsystemet.no/fri-nettleie/).

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

* Bli den første på denne lista! Åpne en pull request eller git beskjed i et
  issue.

## Status

Den følgende listen viser status på innsamlede data.

<!-- statusstart -->

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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAxMDAwNDM4MyIsICJraWxkZXIiOiBbImh0dHBzOi8vYWx1dC5uby9uZXR0bGVpZS8iXSwgIm5ldHRlaWVyIjogIkFsdXQgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEzLjF9LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJPVl9UUkVGQVNFIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDM1MDAsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDQ1MDAsICJ0ZXJza2VsIjogMTI1fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIiwgImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Alut AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Arva AS</td>
    <td>7080005051859</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBcnZhIEFTIiwgImdsbiI6ICI3MDgwMDA1MDUxODU5In0=' title='Samle inn data for Arva AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Arva AS</td>
    <td>7080005051361</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBcnZhIEFTICh0aWRsaWdlcmUgTm9yZGxhbmRzbmV0dCkiLCAiZ2xuIjogIjcwODAwMDUwNTEzNjEifQ==' title='Samle inn data for Arva AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Asker Nett AS</td>
    <td>7080003858825</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBc2tlciBOZXR0IEFTIiwgImdsbiI6ICI3MDgwMDAzODU4ODI1In0=' title='Samle inn data for Asker Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>BKK AS</td>
    <td>7080005051378</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJCS0sgQVMiLCAiZ2xuIjogIjcwODAwMDUwNTEzNzgifQ==' title='Samle inn data for BKK AS' target='_blank'>✏️</a></td>
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
    <td>Elvia AS</td>
    <td>7080005046220</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJFbHZpYSBBUyIsICJnbG4iOiAiNzA4MDAwNTA0NjIyMCJ9' title='Samle inn data for Elvia AS' target='_blank'>✏️</a></td>
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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAxMDAwMDMxNiIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmZqZWxsbmV0dC5uby9uZXR0bGVpZS9hdnRhbGVyLW9nLXZpbGthci9mZWxsZXNiZXN0ZW1tZWxzZXIvIiwgImh0dHBzOi8vd3d3LmZqZWxsbmV0dC5uby9uZXR0bGVpZXByaXNlci9wcml2YXRrdW5kZXIvIl0sICJuZXR0ZWllciI6ICJGamVsbG5ldHQgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEwLjYwOH0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIkZFTV9WRUtURVRfXHUwMGM1UiIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAxNzAwLjAwNCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMjE2OC44LCAidGVyc2tlbCI6IDJ9LCB7InByaXMiOiAyNjM3LjYsICJ0ZXJza2VsIjogM30sIHsicHJpcyI6IDM1NzUuMiwgInRlcnNrZWwiOiA0fSwgeyJwcmlzIjogNDA0NCwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNDUxMi44LCAidGVyc2tlbCI6IDZ9LCB7InByaXMiOiA0OTgxLjYsICJ0ZXJza2VsIjogN30sIHsicHJpcyI6IDU0NTAuNCwgInRlcnNrZWwiOiA4fSwgeyJwcmlzIjogNTkxOS4yLCAidGVyc2tlbCI6IDl9LCB7InByaXMiOiA2Mzg4LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogNjg1Ni44LCAidGVyc2tlbCI6IDExfSwgeyJwcmlzIjogNzMyNS42LCAidGVyc2tlbCI6IDEyfSwgeyJwcmlzIjogNzc5NC40LCAidGVyc2tlbCI6IDEzfSwgeyJwcmlzIjogODI2My4yLCAidGVyc2tlbCI6IDE0fSwgeyJwcmlzIjogODczMiwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDkyMDAuOCwgInRlcnNrZWwiOiAxNn0sIHsicHJpcyI6IDk2NjkuNiwgInRlcnNrZWwiOiAxN30sIHsicHJpcyI6IDEwMTM4LjQsICJ0ZXJza2VsIjogMTh9LCB7InByaXMiOiAxMDYwNy4yLCAidGVyc2tlbCI6IDE5fSwgeyJwcmlzIjogMTEwNzYsICJ0ZXJza2VsIjogMjB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Fjellnett AS' target='_blank'>✏️</a></td>
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
    <td>Glitre Nett AS</td>
    <td>7080005052672</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyAodGlkbCBHbGl0cmUgRW5lcmdpIE5ldHQsIERpc3RyaWIuKSIsICJnbG4iOiAiNzA4MDAwNTA1MjY3MiJ9' title='Samle inn data for Glitre Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Glitre Nett AS ✅</td>
    <td>7080005056069</td>
    <td><code>2024-11-25</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyIsICJnbG4iOiAiNzA4MDAwNTA1NjA2OSIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI1IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZ2xpdHJlbmV0dC5uby9rdW5kZS9uZXR0bGVpZS1vZy1wcmlzZXIvbmV0dGxlaWVwcmlzZXItcHJpdmF0a3VuZGUiXSwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0xMC1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyMDQwfSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNTgwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0NDQwfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogOTEyMH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDExODgwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTQ4ODB9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzA0MH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDM2NDgwfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDg2MDB9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzg5NjB9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxNS4zNiwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDI0Ljk2fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTEwLTAxIn1dfQ==' title='Samle inn data for Glitre Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Griug AS ✅</td>
    <td>7080005052900</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwNTA1MjkwMCIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmdyaXVnLm5vL29tLW5ldHRsZWllLW9nLXByaXNlci9wcmlzZXIvbmV0dGxlaWVwcmlzZXItMjAyNC8iXSwgIm5ldHRlaWVyIjogIkdyaXVnIEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiA5LjgsICJ1bm50YWsiOiBbeyJkYWdlciI6IFsiZnJlZGFnIl0sICJtXHUwMGU1bmVkZXIiOiBbImphbnVhciIsICJmZWJydWFyIiwgIm1hcnMiLCAib2t0b2JlciIsICJub3ZlbWJlciIsICJkZXNlbWJlciJdLCAibmF2biI6ICJCcnVrc3RpZHN0aWxsZWdnIiwgInRpbGxlZ2ciOiAxMSwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAyMTEyLCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiAzMTY4LCAidGVyc2tlbCI6IDJ9LCB7InByaXMiOiA0NzUyLCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA2MDk2LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogNzY4MCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDkzMTIsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAxNzQyNCwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDI1NTg0LCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogMzQzMjAsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiA2ODExMiwgInRlcnNrZWwiOiAxMDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Griug AS' target='_blank'>✏️</a></td>
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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwMTMxOTgzMCIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmxpbmphLm5vL25ldHRsZWlnZSJdLCAibmV0dGVpZXIiOiAiTGluamEgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wMyIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDIwLjQyNCwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInByaXMiOiAyNy4yMzIsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMjY0MCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMzI5Mi44LCAidGVyc2tlbCI6IDJ9LCB7InByaXMiOiAzOTQ1LjYsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDY1ODUuNiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDc5MTAuNCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDkyMTYsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAxMzE4MC44LCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMTQ0OTYsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiAxNTgwMS42LCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogMTk3NjYuNCwgInRlcnNrZWwiOiAxMDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDctMDEiLCAiZ3lsZGlnX3RpbCI6IG51bGwsICJpZCI6ICJub3JkLXByaXZhdCIsICJuYXZuIjogIk5vcmQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In0sIHsiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTUuMzg0LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDIyLjM4NCwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAyNjY4LjgsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDM3MDUuNiwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNDc0Mi40LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA2ODE2LjAsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA4MTk4LjQsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiA5NTkwLjQsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAxMjE4Mi40LCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMTM1NjQuOCwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDE0OTU2LjgsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiAxODQxMi44LCAidGVyc2tlbCI6IDEwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNy0wMSIsICJneWxkaWdfdGlsIjogbnVsbCwgImlkIjogInNcdTAwZjhyLXByaXZhdCIsICJuYXZuIjogIlNcdTAwZjhyIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Linja AS' target='_blank'>✏️</a></td>
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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwMzg2OTAxMiIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3Lm1pZHRuZXR0Lm5vL25ldHRsZWllIiwgImh0dHBzOi8vd3d3Lm1pZHRuZXR0Lm5vL21lZGlhLzI5MTkvbmV0dGxlaWVwcmlzZXItZnJhLTEtYXByaWwtMjAyNC5wZGYiXSwgIm5ldHRlaWVyIjogIk1pZHRuZXR0IEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDMiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyNiwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInByaXMiOiAzMSwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAyNjQwLCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiAzOTYwLCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiA2MDAwLCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogOTAwMCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDEyMDAwLCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMTY3NjQsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAyNTE1MiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDMxMjAwLCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogMzYwMDAsICJ0ZXJza2VsIjogMTAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA0LTAxIiwgImd5bGRpZ190aWwiOiBudWxsLCAiaWQiOiAiaG4yMi1wcml2YXQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Midtnett AS' target='_blank'>✏️</a></td>
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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhdW1uZXR0IEFTIiwgImdsbiI6ICI3MDgwMDA0MDUzNjMyIiwgImtpbGRlciI6IFsiaHR0cHM6Ly9zdHJhdW1uZXR0Lm5vL3ByaXNhci1mb3ItbmV0dGxlaWdlIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI1IiwgInRhcmlmZmVyIjogW3sia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImlkIjogIjIwMjQiLCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAyNDM1LjMyOH0sIHsidGVyc2tlbCI6IDIsICJwcmlzIjogMjkyMi40MzJ9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDMxNjUuOTg0fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogMzQwOS41MzZ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAzNjUzLjA4OH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDQyNjEuOTJ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiA0NjI3LjJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiA1MTE0LjMwNH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDU2MDEuMzEyfSwgeyJ0ZXJza2VsIjogMTAwLCAicHJpcyI6IDYwODguNDE2fV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTEuNTYsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAxNi41Nn1dfX1dfQ==' title='Samle inn data for Straumnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>SuNett AS ✅</td>
    <td>7080010003218</td>
    <td><code>2024-11-24</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdU5ldHQgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDMyMTgiLCAia2lsZGVyIjogWyJodHRwczovL3d3dy5zdW5uZGFsZW5lcmdpbmV0dC5uby9uZXR0bGVpZS8iLCAiaHR0cHM6Ly93d3cuc3VubmRhbGVuZXJnaW5ldHQubm8vbmV0dGxlaWUvbmV0dGF2dGFsZXIvbmV0dGxlaWUtcHJpdmF0LyJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNCIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDQtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIk9WX1RSRUZBU0UiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAxNjQ2LjR9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAzMjkyfSwgeyJ0ZXJza2VsIjogNjMsICJwcmlzIjogNjU4NC44fV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTYuODgsICJ1bm50YWsiOiBbeyJuYXZuIjogIlZpbnRlciIsICJwcmlzIjogMTkuMjgsICJtXHUwMGU1bmVkZXIiOiBbImphbnVhciIsICJmZWJydWFyIiwgIm1hcnMiLCAiYXByaWwiLCAibm92ZW1iZXIiLCAiZGVzZW1iZXIiXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNC0wMSJ9XX0=' title='Samle inn data for SuNett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Sygnir AS ✅</td>
    <td>7080010009654</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAxMDAwOTY1NCIsICJraWxkZXIiOiBbImh0dHBzOi8vc3RhdGljMS5zcXVhcmVzcGFjZS5jb20vc3RhdGljLzYxZGZlN2IzMTk5OTU5MTk3MjI1NGRlYS90LzY1N2FmMWJjOGIzYjM1Nzk0NzE1YmVmNy8xNzAyNTU2MDk0MTE4L05ldHRsZWlnZXByaXNhcitwciswMS4wMS4yNC5wZGYiLCAiaHR0cHM6Ly93d3cuc3lnbmlyLm5vL25ldHRsZWlnZSJdLCAibmV0dGVpZXIiOiAiU3lnbmlyIEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOC43ODR9LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiAyNDE5LjIsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDI5MDguOCwgInRlcnNrZWwiOiAxfSwgeyJwcmlzIjogMzM4OC44LCAidGVyc2tlbCI6IDJ9LCB7InByaXMiOiAzODc4LjQsICJ0ZXJza2VsIjogM30sIHsicHJpcyI6IDQzNTguNCwgInRlcnNrZWwiOiA0fSwgeyJwcmlzIjogNTA4OCwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNTgxNy42LCAidGVyc2tlbCI6IDZ9LCB7InByaXMiOiA2NTM3LjYsICJ0ZXJza2VsIjogN30sIHsicHJpcyI6IDcyNjcuMiwgInRlcnNrZWwiOiA4fSwgeyJwcmlzIjogNzk5Ni44LCAidGVyc2tlbCI6IDl9LCB7InByaXMiOiA5NDQ2LjQ0LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogMTA4OTYsICJ0ZXJza2VsIjogMTJ9LCB7InByaXMiOiAxMjM1NS4yLCAidGVyc2tlbCI6IDE0fSwgeyJwcmlzIjogMTM4MDQuOCwgInRlcnNrZWwiOiAxNn0sIHsicHJpcyI6IDE1MjU0LjQsICJ0ZXJza2VsIjogMTh9LCB7InByaXMiOiAyNzM2OS42LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMzk0NzUuMiwgInRlcnNrZWwiOiA0MH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Sygnir AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Sør Aurdal Energi AS Nett ✅</td>
    <td>7080005046459</td>
    <td><code>2024-11-24</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTXHUwMGY4ciBBdXJkYWwgRW5lcmdpIEFTIE5ldHQiLCAiZ2xuIjogIjcwODAwMDUwNDY0NTkiLCAia2lsZGVyIjogWyJodHRwczovL3NhZS5uby90YXJpZmZlciIsICJodHRwczovL3NhZS5uby91cGxvYWRzL0t1bmRlaW5mb3JtYXNqb24vMjAyNF8wOF9LdW5kZWluZm9ybWFzam9uX3RhcmlmZmVyLnBkZiJdLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0yNCIsICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDktbjEwMCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJNTkRfTUFYIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogZmFsc2UsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDU0MDB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDYyNDB9LCB7InRlcnNrZWwiOiA4LCAicHJpcyI6IDc0NDB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA4NjQwfSwgeyJ0ZXJza2VsIjogMzAsICJwcmlzIjogOTcyMH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDEzMjAwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMjEuNTIsICJ1bm50YWsiOiBbeyJuYXZuIjogIlZpbnRlciIsICJwcmlzIjogMjUuNTIsICJtXHUwMGU1bmVkZXIiOiBbImphbnVhciIsICJmZWJydWFyIiwgIm1hcnMiLCAib2t0b2JlciIsICJub3ZlbWJlciIsICJkZXNlbWJlciJdfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA5LTAxIn1dfQ==' title='Samle inn data for Sør Aurdal Energi AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Tensio TS AS ✅</td>
    <td>7080005051880</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwNTA1MTg4MCIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnRlbnNpby5uby9uby9rdW5kZS9uZXR0bGVpZS9uZXR0bGVpZXByaXNlci1zZXB0ZW1iZXItMjAyNC10biIsICJodHRwczovL3d3dy50ZW5zaW8ubm8vbm8va3VuZGUvbmV0dGxlaWUvbmV0dGxlaWVwcmlzZXItc2VwdGVtYmVyLXRzIl0sICJuZXR0ZWllciI6ICJUZW5zaW8gVFMgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDM5LjY4LCAidW5udGFrIjogW3sibmF2biI6ICJEYWciLCAicHJpcyI6IDU3LjQzLCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDE3NzYsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDM1NTIsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDY0MzIsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDk3NTYsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiAxMzA2OCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDE2NDA0LCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMjg1NzIsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiA0NTIwNCwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDYxODEyLCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogODk0ODQsICJ0ZXJza2VsIjogMTAwfSwgeyJwcmlzIjogMTIyNzQ4LCAidGVyc2tlbCI6IDE1MH0sIHsicHJpcyI6IDE3ODA5MiwgInRlcnNrZWwiOiAyMDB9LCB7InByaXMiOiAyNDQ1NzIsICJ0ZXJza2VsIjogMzAwfSwgeyJwcmlzIjogMzExMDQwLCAidGVyc2tlbCI6IDQwMH0sIHsicHJpcyI6IDM3NzQ2MCwgInRlcnNrZWwiOiA1MDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEiLCAiaWQiOiAiMjAyNC0wNy10biIsICJuYXZuIjogIk5vcmQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In0sIHsiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMzUuOTMsICJ1bm50YWsiOiBbeyJuYXZuIjogIkRhZyIsICJwcmlzIjogNTAuMTgsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJwcmlzIjogMTYwOCwgInRlcnNrZWwiOiAwfSwgeyJwcmlzIjogMjg2OCwgInRlcnNrZWwiOiAyfSwgeyJwcmlzIjogNDg5NiwgInRlcnNrZWwiOiA1fSwgeyJwcmlzIjogNzIxMiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDk1MjgsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiAxMTg2OCwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDIwMzg4LCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMzIwMDQsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiA0MzYyMCwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDYzMDAwLCAidGVyc2tlbCI6IDEwMH0sIHsicHJpcyI6IDg2MjIwLCAidGVyc2tlbCI6IDE1MH0sIHsicHJpcyI6IDEyNDkzMiwgInRlcnNrZWwiOiAyMDB9LCB7InByaXMiOiAxNzE0NTYsICJ0ZXJza2VsIjogMzAwfSwgeyJwcmlzIjogMjE3ODk2LCAidGVyc2tlbCI6IDQwMH0sIHsicHJpcyI6IDI2NDM4NCwgInRlcnNrZWwiOiA1MDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEiLCAiaWQiOiAiMjAyNC0wOS10cyIsICJuYXZuIjogIlNcdTAwZjhyIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Tensio TS AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Tinfos AS Nett ✅</td>
    <td>7080003612595</td>
    <td><code>2024-11-24</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJUaW5mb3MgQVMgTmV0dCIsICJnbG4iOiAiNzA4MDAwMzYxMjU5NSIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTI0IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudGluZm9zLm5vL3RpbmZvcy1uZXR0LyIsICJodHRwczovL2JpYXBpLm52ZS5uby9uZXR0bGVpZXRhcmlmZmVyL3N3YWdnZXIvaW5kZXguaHRtbCJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICJudmUiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVUtKRU5UIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogbnVsbCwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzE1Nn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNDk1Nn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDY3NTZ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA4NTU2fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTAzNTZ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxNTc1Nn0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDQ1MDAwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTl9LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIn1dfQ==' title='Samle inn data for Tinfos AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Uvdal Kraftforsyning ✅</td>
    <td>7080005050500</td>
    <td><code>2024-11-15</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJVdmRhbCBLcmFmdGZvcnN5bmluZyIsICJnbG4iOiAiNzA4MDAwNTA1MDUwMCIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTE1IiwgImtpbGRlciI6IFsiaHR0cDovL3d3dy51dmRhbGtyYWZ0Lm5vL2NvbnRhY3QvbmV0dC8iLCAiaHR0cDovL3d3dy51dmRhbGtyYWZ0Lm5vL3BkZi9UYXJpZmZoZWZ0ZTAxMDUyMDI0LnBkZiJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTA1IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogZmFsc2UsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDM4MTEuMn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNTcyMS42fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogODM5MC40fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogMTYwMjIuNH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDIzNjU0LjR9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAzNTA5Ny42fSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogNTQxODIuNH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDc3MDY4Ljh9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogMTA3NTk2Ljh9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyMi41OCwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDMwLjU4fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA1LTAxIn1dfQ==' title='Samle inn data for Uvdal Kraftforsyning' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vang Energiverk AS ✅</td>
    <td>7080010002297</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAxMDAwMjI5NyIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnZhbmdlbmVyZ2kubm8vbmV0dGxlaWdlL2ZvcmJydWthcmt1bmRhci8iLCAiaHR0cHM6Ly93d3cudmFuZ2VuZXJnaS5uby9ueWhldGVyLyJdLCAibmV0dGVpZXIiOiAiVmFuZyBFbmVyZ2l2ZXJrIEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiA4LCAidW5udGFrIjogW3siZGFnZXIiOiBbImZyZWRhZyJdLCAibVx1MDBlNW5lZGVyIjogWyJqYW51YXIiLCAiZmVicnVhciIsICJtYXJzIiwgImFwcmlsIiwgIm9rdG9iZXIiLCAibm92ZW1iZXIiLCAiZGVzZW1iZXIiXSwgIm5hdm4iOiAiQnJ1a3N0aWRzdGlsbGVnZyIsICJ0aWxsZWdnIjogMTAsICJ0aW1lciI6ICIxNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDQ4MDAsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDYwMDAsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDcyNjAsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDg1MjAsICJ0ZXJza2VsIjogOH0sIHsicHJpcyI6IDEwMDIwLCAidGVyc2tlbCI6IDEyfSwgeyJwcmlzIjogMTE1ODAsICJ0ZXJza2VsIjogMTh9LCB7InByaXMiOiAxMzM4MCwgInRlcnNrZWwiOiAyNX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vang Energiverk AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vest-Telemark Kraftlag AS Nett ✅</td>
    <td>7080005051927</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwNTA1MTkyNyIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnRlbGVtYXJrLW5ldHQubm8vcHJpc2FyL25ldHRsZWlnZS0xLyJdLCAibmV0dGVpZXIiOiAiVmVzdC1UZWxlbWFyayBLcmFmdGxhZyBBUyBOZXR0IiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyNn0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDM1NDAsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDQ1NjAsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDg0MDAsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiAxMTQwMCwgInRlcnNrZWwiOiAxNX0sIHsicHJpcyI6IDEzOTIwLCAidGVyc2tlbCI6IDIwfSwgeyJwcmlzIjogMjQwMDAsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiAzOTEyMCwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDUzMTYwLCAidGVyc2tlbCI6IDc1fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAzLTAxIiwgImlkIjogIjIwMjQtMDMiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0In1dfQ==' title='Samle inn data for Vest-Telemark Kraftlag AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vestall AS ✅</td>
    <td>7080005051897</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwNTA1MTg5NyIsICJraWxkZXIiOiBbImh0dHBzOi8vdmVzdGFsbC5uby9uZXR0bGVpZXByaXNlci0yMDI0LyJdLCAibmV0dGVpZXIiOiAiVmVzdGFsbCBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogNC4zLCAidW5udGFrIjogW3sibmF2biI6ICJEYWciLCAicHJpcyI6IDguNiwgInRpbWVyIjogIjYtMjEifV19LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiA1NDI0LCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiA5MDI0LCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiAxMjc1NiwgInRlcnNrZWwiOiAxMH0sIHsicHJpcyI6IDE2NDg4LCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogMjAwNjQsICJ0ZXJza2VsIjogMjB9LCB7InByaXMiOiAzMTA5MiwgInRlcnNrZWwiOiAyNX0sIHsicHJpcyI6IDM1MTAwLCAidGVyc2tlbCI6IDUwfSwgeyJwcmlzIjogNjc3ODgsICJ0ZXJza2VsIjogNzV9LCB7InByaXMiOiA5NTI4MCwgInRlcnNrZWwiOiAxMDB9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEiLCAiaWQiOiAiMjAyNCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Vestall AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vestmar Nett AS ✅</td>
    <td>7080005054928</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwNTA1NDkyOCIsICJraWxkZXIiOiBbImh0dHBzOi8vdmVzdG1hci1uZXR0Lm5vL25ldHQtb2ctbmV0dGxlaWUvIiwgImh0dHBzOi8vdmVzdG1hci1uZXR0Lm5vL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI0LzAxL1RhcmlmZmVyLTAxMDIyNC5wZGYiXSwgIm5ldHRlaWVyIjogIlZlc3RtYXIgTmV0dCBBUyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgInRhcmlmZmVyIjogW3siZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTkuODZ9LCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InByaXMiOiA0MTA3LjI0LCAidGVyc2tlbCI6IDB9LCB7InByaXMiOiA3MjYxLjkyLCAidGVyc2tlbCI6IDV9LCB7InByaXMiOiAxMDQxNi42LCAidGVyc2tlbCI6IDEwfSwgeyJwcmlzIjogMTM1NzEuMjgsICJ0ZXJza2VsIjogMTV9LCB7InByaXMiOiAxNjcyNC42NCwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDI2MTg4LjY4LCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogNDE5NjAuNzYsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiA1NzczMi45NiwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDgxMzkwLjQ4LCAidGVyc2tlbCI6IDEwMH0sIHsicHJpcyI6IDExMjkzNC43NiwgInRlcnNrZWwiOiAxNTB9LCB7InByaXMiOiAxNjAyNTEuMTIsICJ0ZXJza2VsIjogMjAwfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAyLTAxIiwgImlkIjogIjIwMjQtMDItbjEwMCIsICJrdW5kZWdydXBwZSI6ICJwcml2YXQifV19' title='Samle inn data for Vestmar Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vevig AS ✅</td>
    <td>7080003807946</td>
    <td><code>2024-11-06</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwMzgwNzk0NiIsICJraWxkZXIiOiBbImh0dHBzOi8vdmV2aWcubm8vbmV0dGxlaWUtb2ctdmlsa2FyL25ldHRsZWllLXByaXZhdC8iXSwgIm5ldHRlaWVyIjogIlZldmlnIEFTIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDYiLCAidGFyaWZmZXIiOiBbeyJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMy40LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDIxLjQsICJ0aW1lciI6ICI2LTIxIn1dfSwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiBmYWxzZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDIwMTYsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDI2MTYsICJ0ZXJza2VsIjogMn0sIHsicHJpcyI6IDM2MzYsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDQ2NjgsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA1Njg4LCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogNjY5NiwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDc3MTYsICJ0ZXJza2VsIjogMjV9LCB7InByaXMiOiA5NzU2LCAidGVyc2tlbCI6IDMwfSwgeyJwcmlzIjogMTE3ODQsICJ0ZXJza2VsIjogNDB9LCB7InByaXMiOiAxNjg3MiwgInRlcnNrZWwiOiA1MH0sIHsicHJpcyI6IDIxNjM2LCAidGVyc2tlbCI6IDc1fSwgeyJwcmlzIjogMjcwMzYsICJ0ZXJza2VsIjogMTAwfSwgeyJwcmlzIjogMzIxMzYsICJ0ZXJza2VsIjogMTI1fSwgeyJwcmlzIjogNDIzMTIsICJ0ZXJza2VsIjogMTUwfSwgeyJwcmlzIjogNjI2NjQsICJ0ZXJza2VsIjogMjAwfSwgeyJwcmlzIjogODMwMDQsICJ0ZXJza2VsIjogMzAwfSwgeyJwcmlzIjogMjA1MTA0LCAidGVyc2tlbCI6IDQwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNi0wMSIsICJneWxkaWdfdGlsIjogbnVsbCwgImlkIjogIjIwMjQtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vevig AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vissi AS ✅</td>
    <td>7080004045743</td>
    <td><code>2024-11-06</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJnbG4iOiAiNzA4MDAwNDA0NTc0MyIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnZpc3NpLm5vL3ByaXNlci1vZy12aWxrYXIvbmV0dGxlaWUtcHJpdmF0LyJdLCAibmV0dGVpZXIiOiAiVmlzc2kgQVMiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wNiIsICJ0YXJpZmZlciI6IFt7ImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEyLCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAicHJpcyI6IDI1LCAidGltZXIiOiAiNi0yMSJ9XX0sICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sicHJpcyI6IDI0MDAsICJ0ZXJza2VsIjogMH0sIHsicHJpcyI6IDQwMzIsICJ0ZXJza2VsIjogNX0sIHsicHJpcyI6IDU2NjQsICJ0ZXJza2VsIjogMTB9LCB7InByaXMiOiA3Mjk2LCAidGVyc2tlbCI6IDE1fSwgeyJwcmlzIjogODkyOCwgInRlcnNrZWwiOiAyMH0sIHsicHJpcyI6IDE0NTkyLCAidGVyc2tlbCI6IDI1fSwgeyJwcmlzIjogMTk2MzIsICJ0ZXJza2VsIjogNTB9LCB7InByaXMiOiAyNDE5MiwgInRlcnNrZWwiOiA3NX0sIHsicHJpcyI6IDI4OTkyLCAidGVyc2tlbCI6IDEwMH0sIHsicHJpcyI6IDMyODMyLCAidGVyc2tlbCI6IDE1MH0sIHsicHJpcyI6IDM3NjMyLCAidGVyc2tlbCI6IDIwMH1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJneWxkaWdfdGlsIjogbnVsbCwgImlkIjogIjIwMjQtcHJpdmF0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCJ9XX0=' title='Samle inn data for Vissi AS' target='_blank'>✏️</a></td>
</tr>
</table>

<!-- statusstop -->

## Forvaltere

Forvalterne av dette prosjektet er medlemmene av
[github.com/kraftsystemet](https://github.com/kraftsystemet). Alt vi gjør på
dette prosjektet er som privatpersoner.

## Lisens

Dataene i dette prosjektet er lisensiert under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Kreditering gjøres
til "Fri nettleie", med lenke til dette prosjektet.

Vi bruker denne lisensen for å gi deg som bruker vide rettigheter til å bruke dataene samtidig som vi ønsker navngivelse for å sikre synlighet (og dermed bidrag) til nettdugnaden vår.

Data i mappen `referanse-data` er lastet fra andre kilder og brukes for status-rapportering.

* `esett` - Data fra [eSett](https://opendata.esett.com/) lisensiert med [CC0](https://creativecommons.org/publicdomain/zero/1.0/)
* `elhub` - Data fra [Elhub](https://api.elhub.no) med uspesifisert lisens
* `nve` - Data fra [NVE](https://biapi.nve.no/nettleietariffer/swagger/index.html) lisensiert med [NLOD](https://data.norge.no/nlod)
