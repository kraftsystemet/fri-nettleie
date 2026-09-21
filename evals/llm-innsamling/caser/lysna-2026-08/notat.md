# Lysna, priser fra 2026-08-01

Dette er saken som ga oss avrundingsregelen (PR #398): kilden oppgir 42,7 øre inkl. mva og
avgifter, og å dele på 1,25 og trekke fra 8,13 gir 26,03. Riktig verdi er 26.

Tester
- Avrundingssjekk: 42,7 og 50,2 blir 26 og 32 (ikke 26,03 og 32,03).
- Privat og næring har **ulike** priser (26 mot 25 øre natt), så `liten_næring` får egen tariff
  (regel 2, avvikende priser, i kundegrupper.md), og `husholdning` og `fritid` deler en annen.
- Kapasitetsledd: privat oppgis inkl. mva (kr/mnd og kr/år), næring ekskl. mva. Begge skal ut som
  kr/år ekskl. mva.
- «Dag (kl. 06-22)» skal skrives `timer: 6-21`.

Avvik fra den mergede PR-en: PR #398 har `timer: 6-22`. Det bryter regelen i format.md og avviker
fra 53 andre filer som bruker `6-21` for «kl 06-22». Fasiten her følger regelen. En modell som
skriver `6-22` skal feile. Det samme avviket finnes i `elvenett.yml` og `norefjell.yml`.
