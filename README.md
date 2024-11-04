# Fri nettleie

> Slipp nettleien fri

En _dugnad_ for å samle nettleie-tariffer i det norske kraftsystemet.

<!-- toc -->

- [Bakgrunn](#bakgrunn)
- [Dataene](#dataene)
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

* kapasitet-ledd eller effekt-ledd
* energi-ledd

Selve tariff-dataene inkluderer ikke avgifter, men prosjektet inkluderer
maskinlesbare definisjoner av relevante avgifter.

Vi samler inn data per netteier og gjør tilgjengelig data per nettavregningsområde.

## Mål

- [x] Samle strukturdata for å identifisere alle netteier og nettområder
- [ ] Samle tariffer for private husholdninger og hytter/fritidseiendom på yaml
  format for et utvalg nettselskaper (med varierende tariffer)
- [ ] Formalisere skjema for utveksling av tariffer
- [ ] Overvåke nettselskapenes sider for å varsle ved endring
- [ ] Publisere fil-sett for dataene
- [ ] Publisere tidsserier (prissignal) basert på tariffene
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

For fastleddet finnes det også flere modeller samt at noen oppgir priser per år
mens andre per måned.


### Flere tariffer per netteier

Noen netteiere har ulike tariffer for ulike deler av sitt nett. Dette er typisk
dersom det har vært sammenslåing av konsesjonsområder.

### Priser oppgitt med og uten avgifter

Ved innsamling av tariffer er det utfordrende når noen netteiere gjør
tilgjengelig sine priser med avgifter, mens andre ikke inkluderer avgifter.

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
Velg et nettselskap og finn fram nettleien deres. Vi har ikke formalisert
formatet på data, men du kan se på filene i mappen `tariffer` for å få en
følelse av formatet. Husk at alle priser skal være uten avgifter.

Primært ønsker vi at bidrag gjøres gjennom pull-requests. Men du kan også åpne
et issue og paste data i yaml-format som en del av beskrivelsen.

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

- [ ] Alut AS - 7080010004383
- [ ] Arva AS - 7080005051859
- [ ] Arva AS (tidligere Nordlandsnett) - 7080005051361
- [ ] Asker Nett AS - 7080003858825
- [ ] BKK AS - 7080005051378
- [ ] Bindal Kraftlag Nett - 7080005055963
- [ ] Breheim Nett - 7080010010919
- [ ] Bømlo Kraftnett AS - 7080010002327
- [ ] DE Nett AS - 7080010003614
- [ ] Elinett AS - 7080005053044
- [ ] Elvenett AS - 7080005052917
- [ ] Elvia AS - 7080005046220
- [ ] Enida AS - 7080003871534
- [ ] Etna Nett AS - 7080005046404
- [ ] Everket AS - 7080005052825
- [ ] Fagne AS - 7080003809599
- [ ] Fjellnett AS - 7080010000316
- [ ] Føie AS - 7080005048415
- [ ] Føre AS - 7080010003836
- [ ] Glitre Nett AS (tidl Glitre Energi Nett, Distrib.) - 7080005052672
- [ ] Glitre Nett AS (tidligere Agder Energi Nett) - 7080005056069
- [ ] Griug AS - 7080005052900
- [ ] Havnett AS - 7080010001832
- [ ] Hydro Energi AS nett - 7080005052818
- [ ] Høland og Setskog Elverk AS - 7080004320253
- [ ] Indre Hordaland Kraftnett AS - 7080010008367
- [ ] Jæren Everk AS - 7080010002419
- [ ] KE Nett AS - 7080005046060
- [ ] Klive AS - 7080010000132
- [ ] Kvam Energi Nett AS - 7080010001276
- [ ] Kystnett AS - 7080010000064
- [ ] Lede AS - 7080005050975
- [x] Linja AS - 7080001319830 - Sist oppdatert `2024-11-03`
- [ ] Lucerna AS - 7080005050661
- [ ] Lyse Produksjon AS Nett - 7080003307231
- [ ] Lysna AS - 7080010013088
- [ ] Meløy Nett AS - 7080003968395
- [x] Midtnett AS - 7080003869012 - Sist oppdatert `2024-11-03`
- [ ] Modalen Kraftlag Nett - 7080003816184
- [ ] Nettselskapet AS - 7080004064553
- [ ] Noranett AS - 7080003811318
- [ ] Nordvest Nett AS - 7080005052801
- [ ] Norefjell Nett AS - 7080010003911
- [ ] Norgesnett AS - 7080005052702
- [ ] R-Nett AS - 7080010012852
- [ ] Rakkestad Energi AS Nett - 7080005054898
- [ ] Romsdalsnett AS - 7080010005427
- [ ] Røros E-verk Nett AS - 7080003947932
- [ ] S-NETT AS - 7080010002464
- [ ] SkiakerNett AS - 7080004062702
- [ ] Stannum AS - 7080010003959
- [ ] Stram AS - 7080003822901
- [ ] Straumen Nett AS - 7080010003720
- [ ] Straumnett AS - 7080004053632
- [ ] SuNett AS - 7080010003218
- [ ] Sygnir AS - 7080010009654
- [ ] Sør Aurdal Energi AS Nett - 7080005046459
- [ ] Tensio TS AS - 7080005051880
- [ ] Tinfos AS Nett - 7080003612595
- [ ] Uvdal Kraftforsyning - 7080005050500
- [ ] Vang Energiverk AS - 7080010002297
- [ ] Vest-Telemark Kraftlag AS Nett - 7080005051927
- [ ] Vestall AS - 7080005051897
- [ ] Vestmar Nett AS - 7080005054928
- [ ] Vevig AS - 7080003807946
- [ ] Vissi AS - 7080004045743

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
