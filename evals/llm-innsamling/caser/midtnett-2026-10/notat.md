# Midtnett, priser fra 2026-10-01

Tester
- Avgifter fjernes riktig: 48,91 og 42,66 blir 31 og 26 (mva 25 %, elavgift 7,13, Enova 1).
- Kapasitetsledd er kr/mnd inkl. mva i kilden, men kr/år ekskl. mva i YAML.
- `liten_næring` slås sammen med `husholdning` fordi kilden oppgir egne næringspriser som er
  like. Se kundegrupper.md. `fritid` har egne (høyere) kapasitetsledd og får egen blokk.
- Næringstabellens energiledd er merket «eks forbruksavgift og enovaavgift», men tallene
  er de samme som husholdningens priser med avgifter. Riktig tolkning er ekskl. mva, og de
  er like som husholdning. En modell som tar 39,13 som ren nettleie har feil.

Oppdatering: fastledd-trinn 5, 15 og 25 kW for husholdning/liten_næring var opprinnelig 3964,8/9004,8/16761,6 (avledet fra privatprisen inkl. mva delt på 1,25, uten avrundingssjekk). Næringstabellen oppgir 330/750/1397 kr/mnd ekskl. mva direkte, og disse reproduserer privatprisene eksakt. Fasiten bruker nå 3960/9000/16764. Samme for fritid trinn 25 kW: 1677 kr/mnd (20124 kr/år) i stedet for 1676,8 (20121,6), valgt fordi det er det eneste hele kronebeløpet som reproduserer kildens 2096 kr/mnd og stemmer med at alle andre fritid-trinn er hele kr/mnd. Se PR #417.
