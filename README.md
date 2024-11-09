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
./skript/prissignal.py --fra 2024-10-26 --til 2024-10-28 --tariff tariffer/midtnett.yml
```

## Mål

- [x] Samle strukturdata for å identifisere alle netteier og nettområder
- [x] Definere format for innsamling
- [x] Vise at det kan genereres prissignal basert på formatet
- [ ] Samle tariffer for private husholdninger og hytter/fritidseiendom på yaml
  format for et utvalg nettselskaper (med varierende tariffer)
- [ ] Maskinlesbare filer for avgifter
- [ ] Overvåke nettselskapenes sider for å varsle ved endring
- [ ] Publisere prissignal basert på de innsamlede tariffene
- [ ] Sammenstille og publisere informasjon per netteier på et "menneskelig" format på kraftsystemet.no/fri-nettleie
- [ ] Samle tariffer for husholdninger og hytter/fritidshus for alle nettområder
- [ ] Kontinuerlig oppdatere dataene ved endring hos nettselskapene

## Anti-mål

Selv om det kan være nyttig er det følgende foreløpig ikke en del av dette
prosjektet

* tariffer for selskaper
* tariff for ikke automatisk avlesning
* brukergrensesnitt for visning eller innsamling
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
fastsetter også lavere avgift for jan-mars og ytterligere lav avgift for mange
kommuner i Troms og Finnmark.

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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJBbHV0IEFTIiwgImdsbiI6ICI3MDgwMDEwMDA0MzgzIiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAia2lsZGVyIjogWyJodHRwczovL2FsdXQubm8vbmV0dGxlaWUvIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQiLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiT1ZfVFJFRkFTRSIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDI5MS42N30sIHsidGVyc2tlbCI6IDEyNSwgInByaXMiOiAzNzV9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMS41Mn0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV19' title='Samle inn data for Alut AS' target='_blank'>✏️</a></td>
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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJGamVsbG5ldHQgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDAzMTYiLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIkZFTV9WRUtURVRfXHUwMGM1UiIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDE0MS42Njd9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDE4MC43MzN9LCB7InRlcnNrZWwiOiAzLCAicHJpcyI6IDIxOS44fSwgeyJ0ZXJza2VsIjogNCwgInByaXMiOiAyOTcuOTMzfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzMzd9LCB7InRlcnNrZWwiOiA2LCAicHJpcyI6IDM3Ni4wNjd9LCB7InRlcnNrZWwiOiA3LCAicHJpcyI6IDQxNS4xMzN9LCB7InRlcnNrZWwiOiA4LCAicHJpcyI6IDQ1NC4yfSwgeyJ0ZXJza2VsIjogOSwgInByaXMiOiA0OTMuMjY3fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNTMyLjMzM30sIHsidGVyc2tlbCI6IDExLCAicHJpcyI6IDU3MS40fSwgeyJ0ZXJza2VsIjogMTIsICJwcmlzIjogNjEwLjQ2N30sIHsidGVyc2tlbCI6IDEzLCAicHJpcyI6IDY0OS41MzN9LCB7InRlcnNrZWwiOiAxNCwgInByaXMiOiA2ODguNn0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDcyNy42Njd9LCB7InRlcnNrZWwiOiAxNiwgInByaXMiOiA3NjYuNzMzfSwgeyJ0ZXJza2VsIjogMTcsICJwcmlzIjogODA1Ljh9LCB7InRlcnNrZWwiOiAxOCwgInByaXMiOiA4NDQuODY3fSwgeyJ0ZXJza2VsIjogMTksICJwcmlzIjogODgzLjkzM30sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDkyM31dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDEwLjYwOH0sICJneWxkaWdfZnJhIjogIjIwMjQtMDEtMDEifV0sICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LmZqZWxsbmV0dC5uby9uZXR0bGVpZS9hdnRhbGVyLW9nLXZpbGthci9mZWxsZXNiZXN0ZW1tZWxzZXIvIiwgImh0dHBzOi8vd3d3LmZqZWxsbmV0dC5uby9uZXR0bGVpZXByaXNlci9wcml2YXRrdW5kZXIvIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5In0=' title='Samle inn data for Fjellnett AS' target='_blank'>✏️</a></td>
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
    <td>Glitre Nett AS</td>
    <td>7080005056069</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHbGl0cmUgTmV0dCBBUyAodGlkbGlnZXJlIEFnZGVyIEVuZXJnaSBOZXR0KSIsICJnbG4iOiAiNzA4MDAwNTA1NjA2OSJ9' title='Samle inn data for Glitre Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Griug AS ✅</td>
    <td>7080005052900</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJHcml1ZyBBUyIsICJnbG4iOiAiNzA4MDAwNTA1MjkwMCIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA5IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cuZ3JpdWcubm8vb20tbmV0dGxlaWUtb2ctcHJpc2VyL3ByaXNlci9uZXR0bGVpZXByaXNlci0yMDI0LyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTc2fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyNjR9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDM5Nn0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDUwOH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDY0MH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDc3Nn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDE0NTJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyMTMyfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjg2MH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA1Njc2fV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogOC44LCAidW5udGFrIjogW3sibmF2biI6ICJCcnVrc3RpZHN0aWxsZWdnIiwgInRpbWVyIjogIjYtMjEiLCAidGlsbGVnZyI6IDExLCAiZGFnZXIiOiBbImZyZWRhZyJdLCAibVx1MDBlNW5lZGVyIjogWyJqYW51YXIiLCAiZmVicnVhciIsICJtYXJzIiwgIm9rdG9iZXIiLCAibm92ZW1iZXIiLCAiZGVzZW1iZXIiXX1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XX0=' title='Samle inn data for Griug AS' target='_blank'>✏️</a></td>
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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJMaW5qYSBBUyIsICJnbG4iOiAiNzA4MDAwMTMxOTgzMCIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTAzIiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubGluamEubm8vbmV0dGxlaWdlIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIm5vcmQtcHJpdmF0IiwgImd5bGRpZ19mcmEiOiAiMjAyNC0wNy0wMSIsICJneWxkaWdfdGlsIjogbnVsbCwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjIwLjB9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDI3NC40fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzMjguOH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDU0OC44fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNjU5LjJ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA3NjguMH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDEwOTguNH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDEyMDguMH0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDEzMTYuOH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiAxNjQ3LjJ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAyMC40MjQsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAyNy4yMzJ9XX19LCB7ImlkIjogInNcdTAwZjhyLXByaXZhdCIsICJneWxkaWdfZnJhIjogIjIwMjQtMDctMDEiLCAiZ3lsZGlnX3RpbCI6IG51bGwsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDIyMi40fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAzMDguOH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMzk1LjJ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA1NjguMH0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDY4My4yfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogNzk5LjJ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMDE1LjJ9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAxMTMwLjR9LCB7InRlcnNrZWwiOiA3NSwgInByaXMiOiAxMjQ2LjR9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogMTUzNC40fV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTUuMzg0LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjIuMzg0fV19fV19' title='Samle inn data for Linja AS' target='_blank'>✏️</a></td>
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
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJNaWR0bmV0dCBBUyIsICJnbG4iOiAiNzA4MDAwMzg2OTAxMiIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTAzIiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cubWlkdG5ldHQubm8vbmV0dGxlaWUiLCAiaHR0cHM6Ly93d3cubWlkdG5ldHQubm8vbWVkaWEvMjkxOS9uZXR0bGVpZXByaXNlci1mcmEtMS1hcHJpbC0yMDI0LnBkZiJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICJobjIyLXByaXZhdCIsICJneWxkaWdfZnJhIjogIjIwMjQtMDQtMDEiLCAiZ3lsZGlnX3RpbCI6IG51bGwsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IHRydWUsICJ0ZXJza2xlciI6IFt7InRlcnNrZWwiOiAwLCAicHJpcyI6IDIyMH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMzMwfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNTAwfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNzUwfSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTAwMH0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDEzOTd9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyMDk2fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMjYwMH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiAzMDAwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMjYsICJ1bm50YWsiOiBbeyJuYXZuIjogIkhcdTAwZjh5bGFzdCIsICJ0aW1lciI6ICI2LTIxIiwgInByaXMiOiAzMX1dfX1dfQ==' title='Samle inn data for Midtnett AS' target='_blank'>✏️</a></td>
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
    <td>Straumnett AS</td>
    <td>7080004053632</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdHJhdW1uZXR0IEFTIiwgImdsbiI6ICI3MDgwMDA0MDUzNjMyIn0=' title='Samle inn data for Straumnett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>SuNett AS</td>
    <td>7080010003218</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTdU5ldHQgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDMyMTgifQ==' title='Samle inn data for SuNett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Sygnir AS ✅</td>
    <td>7080010009654</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTeWduaXIgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDk2NTQiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJraWxkZXIiOiBbImh0dHBzOi8vc3RhdGljMS5zcXVhcmVzcGFjZS5jb20vc3RhdGljLzYxZGZlN2IzMTk5OTU5MTk3MjI1NGRlYS90LzY1N2FmMWJjOGIzYjM1Nzk0NzE1YmVmNy8xNzAyNTU2MDk0MTE4L05ldHRsZWlnZXByaXNhcitwciswMS4wMS4yNC5wZGYiLCAiaHR0cHM6Ly93d3cuc3lnbmlyLm5vL25ldHRsZWlnZSJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjAxLjZ9LCB7InRlcnNrZWwiOiAxLCAicHJpcyI6IDI0Mi40fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyODIuNH0sIHsidGVyc2tlbCI6IDMsICJwcmlzIjogMzIzLjJ9LCB7InRlcnNrZWwiOiA0LCAicHJpcyI6IDM2My4yfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA0MjR9LCB7InRlcnNrZWwiOiA2LCAicHJpcyI6IDQ4NC44fSwgeyJ0ZXJza2VsIjogNywgInByaXMiOiA1NDQuOH0sIHsidGVyc2tlbCI6IDgsICJwcmlzIjogNjA1LjZ9LCB7InRlcnNrZWwiOiA5LCAicHJpcyI6IDY2Ni40fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogNzg3LjJ9LCB7InRlcnNrZWwiOiAxMiwgInByaXMiOiA5MDh9LCB7InRlcnNrZWwiOiAxNCwgInByaXMiOiAxMDI5LjZ9LCB7InRlcnNrZWwiOiAxNiwgInByaXMiOiAxMTUwLjR9LCB7InRlcnNrZWwiOiAxOCwgInByaXMiOiAxMjcxLjJ9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAyMjgwLjh9LCB7InRlcnNrZWwiOiA0MCwgInByaXMiOiAzMjg5LjZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOC43ODR9LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIn1dfQ==' title='Samle inn data for Sygnir AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Sør Aurdal Energi AS Nett</td>
    <td>7080005046459</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJTXHUwMGY4ciBBdXJkYWwgRW5lcmdpIEFTIE5ldHQiLCAiZ2xuIjogIjcwODAwMDUwNDY0NTkifQ==' title='Samle inn data for Sør Aurdal Energi AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Tensio TS AS ✅</td>
    <td>7080005051880</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJUZW5zaW8gVFMgQVMiLCAiZ2xuIjogIjcwODAwMDUwNTE4ODAiLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnRlbnNpby5uby9uby9rdW5kZS9uZXR0bGVpZS9uZXR0bGVpZXByaXNlci1zZXB0ZW1iZXItMjAyNC10biIsICJodHRwczovL3d3dy50ZW5zaW8ubm8vbm8va3VuZGUvbmV0dGxlaWUvbmV0dGxlaWVwcmlzZXItc2VwdGVtYmVyLXRzIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtMDctdG4iLCAia3VuZGVncnVwcGUiOiAicHJpdmF0IiwgImZhc3RsZWRkIjogeyJtZXRvZGUiOiAiVFJFX0RcdTAwZDhHTk1BWF9NTkQiLCAidGVyc2tlbF9pbmtsdWRlcnQiOiB0cnVlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAxNDh9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDI5Nn0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogNTM2fSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogODEzfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogMTA4OX0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDEzNjd9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyMzgxfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMzc2N30sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDUxNTF9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzQ1N30sIHsidGVyc2tlbCI6IDE1MCwgInByaXMiOiAxMDIyOX0sIHsidGVyc2tlbCI6IDIwMCwgInByaXMiOiAxNDg0MX0sIHsidGVyc2tlbCI6IDMwMCwgInByaXMiOiAyMDM4MX0sIHsidGVyc2tlbCI6IDQwMCwgInByaXMiOiAyNTkyMH0sIHsidGVyc2tlbCI6IDUwMCwgInByaXMiOiAzMTQ1NX1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDM5LjY4LCAidW5udGFrIjogW3sibmF2biI6ICJEYWciLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogNTcuNDN9XX0sICJneWxkaWdfZnJhIjogIjIwMjQtMDktMDEifSwgeyJpZCI6ICIyMDI0LTA5LXRzIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMTM0fSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiAyMzl9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDQwOH0sIHsidGVyc2tlbCI6IDEwLCAicHJpcyI6IDYwMX0sIHsidGVyc2tlbCI6IDE1LCAicHJpcyI6IDc5NH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDk4OX0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDE2OTl9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAyNjY3fSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogMzYzNX0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA1MjUwfSwgeyJ0ZXJza2VsIjogMTUwLCAicHJpcyI6IDcxODV9LCB7InRlcnNrZWwiOiAyMDAsICJwcmlzIjogMTA0MTF9LCB7InRlcnNrZWwiOiAzMDAsICJwcmlzIjogMTQyODh9LCB7InRlcnNrZWwiOiA0MDAsICJwcmlzIjogMTgxNTh9LCB7InRlcnNrZWwiOiA1MDAsICJwcmlzIjogMjIwMzJ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAzNS45MywgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDUwLjE4fV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTA5LTAxIn1dfQ==' title='Samle inn data for Tensio TS AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Tinfos AS Nett</td>
    <td>7080003612595</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJUaW5mb3MgQVMgTmV0dCIsICJnbG4iOiAiNzA4MDAwMzYxMjU5NSJ9' title='Samle inn data for Tinfos AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Uvdal Kraftforsyning</td>
    <td>7080005050500</td>
    <td></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJVdmRhbCBLcmFmdGZvcnN5bmluZyIsICJnbG4iOiAiNzA4MDAwNTA1MDUwMCJ9' title='Samle inn data for Uvdal Kraftforsyning' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vang Energiverk AS ✅</td>
    <td>7080010002297</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJWYW5nIEVuZXJnaXZlcmsgQVMiLCAiZ2xuIjogIjcwODAwMTAwMDIyOTciLCAic2lzdF9vcHBkYXRlcnQiOiAiMjAyNC0xMS0wOSIsICJraWxkZXIiOiBbImh0dHBzOi8vd3d3LnZhbmdlbmVyZ2kubm8vbmV0dGxlaWdlL2ZvcmJydWthcmt1bmRhci8iLCAiaHR0cHM6Ly93d3cudmFuZ2VuZXJnaS5uby9ueWhldGVyLyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogNDAwfSwgeyJ0ZXJza2VsIjogMiwgInByaXMiOiA1MDB9LCB7InRlcnNrZWwiOiA1LCAicHJpcyI6IDYwNX0sIHsidGVyc2tlbCI6IDgsICJwcmlzIjogNzEwfSwgeyJ0ZXJza2VsIjogMTIsICJwcmlzIjogODM1fSwgeyJ0ZXJza2VsIjogMTgsICJwcmlzIjogOTY1fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMTExNX1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDgsICJ1bm50YWsiOiBbeyJuYXZuIjogIkJydWtzdGlkc3RpbGxlZ2ciLCAidGltZXIiOiAiNi0yMSIsICJ0aWxsZWdnIjogMTAsICJkYWdlciI6IFsiZnJlZGFnIl0sICJtXHUwMGU1bmVkZXIiOiBbImphbnVhciIsICJmZWJydWFyIiwgIm1hcnMiLCAiYXByaWwiLCAib2t0b2JlciIsICJub3ZlbWJlciIsICJkZXNlbWJlciJdfV19LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAxLTAxIn1dfQ==' title='Samle inn data for Vang Energiverk AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vest-Telemark Kraftlag AS Nett ✅</td>
    <td>7080005051927</td>
    <td><code>2024-03-01</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJWZXN0LVRlbGVtYXJrIEtyYWZ0bGFnIEFTIE5ldHQiLCAiZ2xuIjogIjcwODAwMDUwNTE5MjciLCAia2lsZGVyIjogWyJodHRwczovL3d3dy50ZWxlbWFyay1uZXR0Lm5vL3ByaXNhci9uZXR0bGVpZ2UtMS8iXSwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMDMtMDEiLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LTAzIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjk1fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzODB9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA3MDB9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA5NTB9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiAxMTYwfSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogMjAwMH0sIHsidGVyc2tlbCI6IDUwLCAicHJpcyI6IDMyNjB9LCB7InRlcnNrZWwiOiA3NSwgInByaXMiOiA0NDMwfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMjZ9LCAiZ3lsZGlnX2ZyYSI6ICIyMDI0LTAzLTAxIn1dfQ==' title='Samle inn data for Vest-Telemark Kraftlag AS Nett' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vestall AS ✅</td>
    <td>7080005051897</td>
    <td><code>2024-11-09</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJWZXN0YWxsIEFTIiwgImdsbiI6ICI3MDgwMDA1MDUxODk3IiwgInNpc3Rfb3BwZGF0ZXJ0IjogIjIwMjQtMTEtMDkiLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0IiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogNDUyfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA3NTJ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiAxMDYzfSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogMTM3NH0sIHsidGVyc2tlbCI6IDIwLCAicHJpcyI6IDE2NzJ9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAyNTkxfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMjkyNX0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDU2NDl9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogNzk0MH1dfSwgImVuZXJnaWxlZGQiOiB7ImdydW5ucHJpcyI6IDQuMywgInVubnRhayI6IFt7Im5hdm4iOiAiRGFnIiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDguNn1dfSwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSJ9XSwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXN0YWxsLm5vL25ldHRsZWllcHJpc2VyLTIwMjQvIl19' title='Samle inn data for Vestall AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vestmar Nett AS ✅</td>
    <td>7080005054928</td>
    <td><code>2024-02-01</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJWZXN0bWFyIE5ldHQgQVMiLCAiZ2xuIjogIjcwODAwMDUwNTQ5MjgiLCAia2lsZGVyIjogWyJodHRwczovL3Zlc3RtYXItbmV0dC5uby9uZXR0LW9nLW5ldHRsZWllLyIsICJodHRwczovL3Zlc3RtYXItbmV0dC5uby93cC1jb250ZW50L3VwbG9hZHMvMjAyNC8wMS9UYXJpZmZlci0wMTAyMjQucGRmIl0sICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTAyLTAxIiwgInRhcmlmZmVyIjogW3siaWQiOiAiMjAyNC0wMi1uMTAwIiwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMzQyLjI3fSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiA2MDUuMTZ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA4NjguMDV9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiAxMTMwLjk0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogMTM5My43Mn0sIHsidGVyc2tlbCI6IDI1LCAicHJpcyI6IDIxODIuMzl9LCB7InRlcnNrZWwiOiA1MCwgInByaXMiOiAzNDk2LjczfSwgeyJ0ZXJza2VsIjogNzUsICJwcmlzIjogNDgxMS4wOH0sIHsidGVyc2tlbCI6IDEwMCwgInByaXMiOiA2NzgyLjU0fSwgeyJ0ZXJza2VsIjogMTUwLCAicHJpcyI6IDk0MTEuMjN9LCB7InRlcnNrZWwiOiAyMDAsICJwcmlzIjogMTMzNTQuMjZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxOS44Nn0sICJneWxkaWdfZnJhIjogIjIwMjQtMDItMDEifV19' title='Samle inn data for Vestmar Nett AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vevig AS ✅</td>
    <td>7080003807946</td>
    <td><code>2024-11-06</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJWZXZpZyBBUyIsICJnbG4iOiAiNzA4MDAwMzgwNzk0NiIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA2IiwgImtpbGRlciI6IFsiaHR0cHM6Ly92ZXZpZy5uby9uZXR0bGVpZS1vZy12aWxrYXIvbmV0dGxlaWUtcHJpdmF0LyJdLCAidGFyaWZmZXIiOiBbeyJpZCI6ICIyMDI0LXByaXZhdCIsICJneWxkaWdfZnJhIjogIjIwMjQtMDYtMDEiLCAiZ3lsZGlnX3RpbCI6IG51bGwsICJrdW5kZWdydXBwZSI6ICJwcml2YXQiLCAiZmFzdGxlZGQiOiB7Im1ldG9kZSI6ICJUUkVfRFx1MDBkOEdOTUFYX01ORCIsICJ0ZXJza2VsX2lua2x1ZGVydCI6IGZhbHNlLCAidGVyc2tsZXIiOiBbeyJ0ZXJza2VsIjogMCwgInByaXMiOiAxNjh9LCB7InRlcnNrZWwiOiAyLCAicHJpcyI6IDIxOH0sIHsidGVyc2tlbCI6IDUsICJwcmlzIjogMzAzfSwgeyJ0ZXJza2VsIjogMTAsICJwcmlzIjogMzg5fSwgeyJ0ZXJza2VsIjogMTUsICJwcmlzIjogNDc0fSwgeyJ0ZXJza2VsIjogMjAsICJwcmlzIjogNTU4fSwgeyJ0ZXJza2VsIjogMjUsICJwcmlzIjogNjQzfSwgeyJ0ZXJza2VsIjogMzAsICJwcmlzIjogODEzfSwgeyJ0ZXJza2VsIjogNDAsICJwcmlzIjogOTgyfSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMTQwNn0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDE4MDN9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogMjI1M30sIHsidGVyc2tlbCI6IDEyNSwgInByaXMiOiAyNjc4fSwgeyJ0ZXJza2VsIjogMTUwLCAicHJpcyI6IDM1MjZ9LCB7InRlcnNrZWwiOiAyMDAsICJwcmlzIjogNTIyMn0sIHsidGVyc2tlbCI6IDMwMCwgInByaXMiOiA2OTE3fSwgeyJ0ZXJza2VsIjogNDAwLCAicHJpcyI6IDE3MDkyfV19LCAiZW5lcmdpbGVkZCI6IHsiZ3J1bm5wcmlzIjogMTMuNCwgInVubnRhayI6IFt7Im5hdm4iOiAiSFx1MDBmOHlsYXN0IiwgInRpbWVyIjogIjYtMjEiLCAicHJpcyI6IDIxLjR9XX19XX0=' title='Samle inn data for Vevig AS' target='_blank'>✏️</a></td>
</tr>
<tr>
    <td>Vissi AS ✅</td>
    <td>7080004045743</td>
    <td><code>2024-11-06</code></td>
    <td><a href='https://kraftsystemet.no/fri-nettleie/innsamler/?data=eyJuZXR0ZWllciI6ICJWaXNzaSBBUyIsICJnbG4iOiAiNzA4MDAwNDA0NTc0MyIsICJzaXN0X29wcGRhdGVydCI6ICIyMDI0LTExLTA2IiwgImtpbGRlciI6IFsiaHR0cHM6Ly93d3cudmlzc2kubm8vcHJpc2VyLW9nLXZpbGthci9uZXR0bGVpZS1wcml2YXQvIl0sICJ0YXJpZmZlciI6IFt7ImlkIjogIjIwMjQtcHJpdmF0IiwgImd5bGRpZ19mcmEiOiAiMjAyNC0wMS0wMSIsICJneWxkaWdfdGlsIjogbnVsbCwgImt1bmRlZ3J1cHBlIjogInByaXZhdCIsICJmYXN0bGVkZCI6IHsibWV0b2RlIjogIlRSRV9EXHUwMGQ4R05NQVhfTU5EIiwgInRlcnNrZWxfaW5rbHVkZXJ0IjogdHJ1ZSwgInRlcnNrbGVyIjogW3sidGVyc2tlbCI6IDAsICJwcmlzIjogMjAwfSwgeyJ0ZXJza2VsIjogNSwgInByaXMiOiAzMzZ9LCB7InRlcnNrZWwiOiAxMCwgInByaXMiOiA0NzJ9LCB7InRlcnNrZWwiOiAxNSwgInByaXMiOiA2MDh9LCB7InRlcnNrZWwiOiAyMCwgInByaXMiOiA3NDR9LCB7InRlcnNrZWwiOiAyNSwgInByaXMiOiAxMjE2fSwgeyJ0ZXJza2VsIjogNTAsICJwcmlzIjogMTYzNn0sIHsidGVyc2tlbCI6IDc1LCAicHJpcyI6IDIwMTZ9LCB7InRlcnNrZWwiOiAxMDAsICJwcmlzIjogMjQxNn0sIHsidGVyc2tlbCI6IDE1MCwgInByaXMiOiAyNzM2fSwgeyJ0ZXJza2VsIjogMjAwLCAicHJpcyI6IDMxMzZ9XX0sICJlbmVyZ2lsZWRkIjogeyJncnVubnByaXMiOiAxMC40LCAidW5udGFrIjogW3sibmF2biI6ICJIXHUwMGY4eWxhc3QiLCAidGltZXIiOiAiNi0yMSIsICJwcmlzIjogMjAuOH1dfX1dfQ==' title='Samle inn data for Vissi AS' target='_blank'>✏️</a></td>
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
