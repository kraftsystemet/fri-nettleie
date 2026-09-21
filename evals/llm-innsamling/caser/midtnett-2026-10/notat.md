# Midtnett, priser fra 2026-10-01

Tester
- Avgifter fjernes riktig: 48,91 og 42,66 blir 31 og 26 (mva 25 %, elavgift 7,13, Enova 1).
- Kapasitetsledd er kr/mnd inkl. mva i kilden, men kr/år ekskl. mva i YAML.
- `liten_næring` slås sammen med `husholdning` fordi kilden oppgir egne næringspriser som er
  like. Se kundegrupper.md. `fritid` har egne (høyere) kapasitetsledd og får egen blokk.
- Næringstabellens energiledd er merket «eks forbruksavgift og enovaavgift», men tallene
  er de samme som husholdningens priser med avgifter. Riktig tolkning er ekskl. mva, og de
  er like som husholdning. En modell som tar 39,13 som ren nettleie har feil.
