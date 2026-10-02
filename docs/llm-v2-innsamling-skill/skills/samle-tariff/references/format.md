# Format

Fasit er [`tariff-eksempel.yml`](../../../../../tariff-eksempel.yml) (forklart eksempel, med
begrunnelse for reglene) og [`tariff.cue`](../../../../../tariff.cue) (schema). **Les begge ved
starten av hver innsamling.** Prosjektet sier selv at innsamlingsformatet ikke skal ansees som
stabilt: hvis nye modeller dukker opp, tilpasses formatet. Denne filen er et sammendrag. Er du uenig
med eksempelfila eller schemaet, gjelder de, og du bør si fra om uenigheten.

Formatet er laget for **manuell innsamling** og skal kunne uttrykke alle eksisterende modeller
kompakt. Å utelate et element regnes som det samme som å sette det til `null`.

## Filen

```yaml
---
netteier: 'Navn AS'
gln:
  - '7080000000000'          # liste, tom liste [] hvis ukjent, aldri null
sist_oppdatert: '2026-09-21' # når tariffene sist ble samlet inn eller kontrollert
kilder:
  - 'https://...'            # sider vi vil overvåke for endringer, minst én
tariffer:
  - ...                      # én oppføring per periode og kundegruppe-sett
```

- **`gln`** identifiserer netteieren i mange systemer. Det er en liste fordi noen nettselskaper har
  flere GLN etter sammenslåing.
- **`sist_oppdatert`** er datoen tariffene sist ble samlet inn eller kontrollert som riktige, også
  når ingenting endret seg.
- **`kilder`** er sider vi overvåker for endringer (se kilder.md).
- **`mga`** (nettavregningsområde, liste) finnes i formatet for netteiere med ulike tariffer i ulike
  områder. Utelatt betyr alle områder. Ingen aktive filer bruker det i dag (bare `tariffer/old/`),
  så ikke innfør det uten at en sak eller brukeren ber om det. Se kanttilfeller.md.

Filen starter med `---`, bruker enkle anførselstegn på tekst og maks 100 tegn per linje
(se `.yamlfmt.yml`). Tall skrives med punktum som desimaltegn, alle priser **uten avgifter**.
Skriv i samme stil som de andre filene.

## En tariff

En netteier har en liste over tariffer for å støtte ulike gyldighetsperioder (historikk), ulike
deler av nettet, og ulike kundegrupper.

| Felt | Regel |
|---|---|
| `kundegrupper` | `husholdning`, `fritid` (hytter og fritidshus), `liten_næring` (lavspente næringskunder under 100 MWh/år). Se kundegrupper.md. |
| `gyldig_fra` | Inklusiv, `YYYY-MM-DD`. |
| `gyldig_til` | Eksklusiv. Utelates på gjeldende tariff uten sluttdato. Sett den på forrige periode lik ny `gyldig_fra`. |
| `navn` | Valgfri. Brukes når en netteier har flere tariffer samtidig for ulike deler av nettet (`tensio-tn.yml`). |

Eldre perioder står urørt. Bare `gyldig_til` på den forrige endres. Ikke fyll inn manglende
mellomperioder: å vedlikeholde historiske priser er ikke et mål.

## Fastledd

Fastleddet avhenger av kundens etterspørsel etter effekt (kW). Prisene er i **kr/år**, uten avgifter.
Grunnen til kr/år er at noen netteiere oppgir årspris, og at det unngår avrundingsfeil i dataene.

| `metode` | Betyr | Eksempel |
|---|---|---|
| `TRE_DØGNMAX_MND` | Snitt av de tre høyeste timene i ulike døgn forrige måned. Vanligst. | `area-lega.yml` |
| `FEM_VEKTET_ÅR` | Fem høyeste ukesmaksene siste 12 måneder, sesongvektet. | `fjellnett.yml` |
| `OV_TREFASE` | Terskel er sikringsstørrelse i ampere (230 V). | `alut.yml` |
| `MND_MAX` | Timen i måneden med høyest gjennomsnittlig forbruk. | `soraurdalenergi.yml` |
| `UKJENT` | Brukes i én fil (`tinfos.yml`). Sett den aldri selv. | |

Viser kilden en **ny modell** som ikke passer i listen, skal du ikke presse den inn i en metode som
nesten passer. Formatet utvides i stedet (`tariff.cue` og `tariff-eksempel.yml`). Gjør STOPPET og
forklar modellen for brukeren.

`terskler` er en liste av `terskel` (nedre grense) og `pris`, gjerne sortert stigende. Kunden betaler
prisen for trinnet den befinner seg på, ikke en sum.

**`terskel_inkludert`** sier om en kunde som havner nøyaktig på terskelverdien får det høyere trinnet:

- `true` når netteier oppgir trinn som «2 til 5» eller «2 til 4,99». Nøyaktig 5 havner på neste trinn.
- `false` når netteier oppgir «2,01 til 5». Nøyaktig 5 hører til trinnet under.

(`null` brukes i én fil (`tinfos.yml`) for ukjent. Bruk den ikke, spør i stedet.)

## Energiledd

`grunnpris` (øre/kWh) er den generelle prisen når ingen unntak treffer, og **typisk den laveste**
(lavlast, natt). Unntak kan også være billigere (sommer-lavlast i `area-lega.yml`). Har alle timer
samme pris, utelates `unntak` helt (se `barentsnett.yml`).

Et `unntak` beskriver perioder med avvikende pris: brukstidstillegg, høylast, sesongvariasjon eller
lignende. Hvert unntak har et `navn` (for å forenkle kontroll av innsamling), en `pris` og valgfritt
`timer`, `dager` og `måneder`. Det gjelder når **alle** oppgitte betingelser treffer samtidig.
Utelatt betyr alle timer, alle dager og alle måneder.

**Tillegg summeres.** Kilden oppgir ofte et unntak som et tillegg («+8 øre i høylast»). Formatet
modellerer ikke tillegg, så du må regne ut erstatningsprisen: `pris` = grunnpris + tillegg. Vis
utregningen i rapporten (`vang.yml`: grunnpris 8 og `Brukstidstillegg` 18, altså et tillegg på 10). Legg merke til at tillegg
kan stå med mva i kilden, så fjern mva før du summerer.

- **`timer`** er tall fra 0 til 23. Et spenn har **inklusiv øvre grense**: `16-21` gjelder fra 16:00
  til og med 21:59:59. «kl 06–22» betyr til, men ikke med, time 22 og skrives `6-21`. Ved skifte
  mellom sommer- og vintertid regnes siste time i døgnet fortsatt som 23.
  Spenn som går over midnatt («kl 22–06») er skrevet `22-5` i dataene, men eksempelfila beskriver
  dem ikke, og `scripts/prissignal.py` tolker dem som tom liste, så unntaket vises ikke der. Velg
  derfor helst natt som `grunnpris` slik at du slipper spennet. Må du bruke det, skriv `22-5` og si
  fra i rapporten.
- **`dager`:** `mandag` … `søndag`, `ukedag` (man–fre), `helg`, `helligdager` (bevegelige helligdager),
  `fridag` (helg eller helligdag), `virkedag` (alt som ikke er fridag), `alle`. Flere verdier
  tolkes som ELLER.
- **`måneder`:** `januar` … `desember` med små bokstaver.

Sesongpriser: `area-lega.yml`. Virkedag: `bkk.yml`. (Ingen filer bruker `fridag` eller `helligdager` i dag.)

## Ikke samle inn

Effektledd i en modell med både fastledd, energiledd og effektledd, kunder over 100 000 kWh,
høyspent, produksjon/innmating og umålte veilys. Nevn i rapporten at du har ignorert dem.
