# Fri nettleie

> Slipp nettleien fri

En _dugnad_ for å samle nettleie-tariffer i det norske kraftsystemet.

## Bakgrunn

Nettleie er en del av [strømregningen](https://snl.no/str%C3%B8mregning) som går
til det lokale nettselskapet.
[Nettleie-tariffer skal være lett tilgjengelig for nettkundene](https://lovdata.no/forskrift/1999-03-11-302/§13-5),
men praksis i dag er at den distribueres av nettselskaper på mange ulike måter
og formater. Selv om det finnes gode initiativer og
[standarder](https://github.com/3lbits/API-nettleie-for-styring) for deling av
nettleie finnes det ikke noen åpen, gratis oversikt over nettleie på tvers av
alle nettselskaper i Norge.

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

* ~~fastledd~~
* kapasitet/effekt-ledd
* energi-ledd

Dataene inkluderer ikke avgifter, men i tillegg maskinlesbare data dette tilgjengelig:

* Elavgift
* Enova-avgift
* ~~Elsertifikater~~
* Merverdiavgift

## Mål

- [ ] Samle strukturdata for å identifisere alle netteier og nettområder
- [ ] Samle tariffer for private husholdninger på YAML format for alle netteiere/områder
- [ ] Formalisere skjema for utveksling av tariffer
- [ ] Publisere fil-sett for dataene
- [ ] Overvåke nettselskapenes sider for å varsle ved endring
- [ ] Kontinuerlig oppdatere dataene ved endring hos nettselskapene

## Anti-mål

Selv om det kan være nyttig er det følgende foreløpig ikke en del av dette
prosjektet

* tariffer for selskaper
* tariff for ikke automatisk avlesning
* brukergrensesnitt for visning eller innsamling

## Innsamling

Dataene i dette prosjektet samles inn manuelt fra netteiers hjemmesider og
lignende. Automatisk scraping er ikke et mål og det oppfordres til å unngå bruk av
roboter for innsamling. Vi respekterer andres systemer og immatrielle rettigheter og bruker
f.eks. ikke data fra andre kommersielle aktører som leverer samme type data.

## Bidra

Vi trenger hjelp, men er foreløpig i startgropa! Enn så lenge kan du melde
interesse ved å
[følge dette prosjektet på GitHub](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/managing-subscriptions-for-activity-on-github/managing-your-subscriptions)
slik at du for eksempel får beskjed når vi oppgretter issues.

Senere vil bidrag være svært velkomne som issues og pull-requests her på GitHub.
Vi vurderer også skjema-innsending via en eller annen tjeneste. Vi håper på
bidrag fra privatpersoner og selskaper som har nytte av dataene.

## Lisens

Dataene i dette prosjektet er lisensiert under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Kreditering gjøres
til "Fri nettleie", med lenke til dette prosjektet.

Vi bruker denne lisensen for å gi deg som bruker vide rettigheter til å bruke dataene samtidig som vi ønsker navngivelse for å sikre synlighet (og dermed bidrag) til nettdugnaden vår.
