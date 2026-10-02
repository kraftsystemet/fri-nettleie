# Mellom, priser fra 2026-09-01

Tester
- Privat oppgir energiledd **inkl. mva men uten avgifter** (avgiftene står som egne linjer). 37,21 og
  29,34 / 1,25 = 29,77 og 23,47. Modellen må ikke trekke fra 8,91 og 1,25 en gang til.
- Næring oppgir de samme energileddene ekskl. mva (29,77 og 23,47), så prisene er like og
  `liten_næring` slås sammen med `husholdning` og `fritid` (regel 2, kundegrupper.md).
- Kapasitetsleddet er litt ulikt (privat 281 / 1,25 = 224,8 mot næring 224,40). Avviket er
  avrunding i kilden (under 0,5 kr/mnd) og regnes som likt. Fasiten bruker privat-verdiene.
- 12 trinn, «Over 200 kW» blir terskel 200.
- «Dag (kl. 06-22)» skrives `timer: 6-21`.
