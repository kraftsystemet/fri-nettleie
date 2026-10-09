# Glitre Nett, priser fra 2026-10-01

Tester
- Siden viser to perioder side om side (fra 1. juli og fra 1. oktober 2026). Modellen skal bruke
  bare oktober-kolonnen, og ikke blande inn julipriser.
- Privat oppgir energiledd **inkl. mva men uten avgifter** (34,84 og 19,84, og avgiftene er egne
  linjer). Riktig utledning er 34,84 / 1,25 = 27,87 og 19,84 / 1,25 = 15,87. Modellen må ikke trekke
  fra avgiftene en gang til, og må ikke bruke summen 45,00 og 30,00 som energiledd.
- Verdiene har to desimaler (`UAVRUNDET`). Avrundingssjekken gir ingen rund verdi, og det er riktig.
- Kapasitetsledd er kr/mnd inkl. mva for privat: 165 kr/mnd blir 1584 kr/år ekskl. mva.
- Næring (under 100 000 kWh) oppgir ekskl. mva-priser som er identiske med privat etter at mva er
  fjernet (132 kr/mnd mot 165 / 1,25). Det er regel 2 i kundegrupper.md, så `liten_næring` slås
  sammen med `husholdning` og `fritid`.
- Timer «kl. 06:00 - kl. 22:00» skrives `6-21`.
