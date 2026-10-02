# Innsamlingsskill v2 (utkast til review)

Dette er et forslag til en ny versjon av LLM-hjelpen for innsamling av nettleietariffer.
Den skal på sikt erstatte [`docs/llm/innsamling-prompt.txt`](../llm/innsamling-prompt.txt). Den
gamle prompten og `llms.txt` er ikke endret.

## Hva er nytt sammenlignet med v1

v1 er én prompt som limes inn i en chat. v2 er en **skill** i
Agent Skills-format (`SKILL.md` +
referansefiler + skript). Den kan brukes av en agent med tilgang til repoet, og innholdet kan senere
bygges om til én fil for vanlig chat.

Hovedidéen er at en agent aldri skal gjette en pris:

- Det finnes to utfall, **KOMPLETT** eller **STOPPET**. Mangler eller er noe uklart, stopper
  agenten og ber om det den trenger. Det finnes ikke noe «delvis».
- Hver pris må kunne spores til kilden. `verifiser_kilde.py` sjekker mekanisk at hvert tall i den
  nye perioden finnes i et ordrett kildeutdrag (direkte, eller ved å regne fremover med avgifter).
- Avgifter fjernes med et skript (`utled_avgifter.py`) med avrundingssjekk, ikke i hodet.
- Satsene står ett sted (`references/satser.yml`), datert og kontrollert mot Skatteetaten.

## Innhold

```
skills/samle-tariff/
├── SKILL.md              arbeidsflyt (start her)
├── references/
│   ├── usikkerhet.md     når agenten skal stoppe, forbudt atferd, svarformat
│   ├── avgifter.md       avgiftssoner, utledning, avrundingssjekk
│   ├── kundegrupper.md   når liten_næring skal med
│   ├── format.md         feltene i YAML, fastleddmetoder, timer og dager
│   ├── kilder.md         tillatte kilder, bilder og PDF, transkribering
│   ├── kanttilfeller.md  navnebytte, flere områder, enhet, uendrede priser
│   ├── repo-og-pr.md     gren, modus (lokalt/PR), validering, PR-mal
│   └── satser.yml        gjeldende avgiftssatser (eneste sted de står)
└── scripts/
    ├── utled_avgifter.py     fjerner avgifter, med avrundingssjekk
    ├── verifiser_kilde.py    sjekker at prisene har belegg i kilden
    ├── sammenlign_forrige.py plausibilitet mot forrige periode
    └── valider.sh            kjører alt over pluss cue vet og eksisterende check_*-skript
```

Tester for skillen ligger i [`evals/llm-innsamling/`](../../evals/llm-innsamling/).

## Slik kan du teste (uten API-nøkkel)

Fra repoets rot, med repoets Python-miljø (`make venv`) og `cue` installert:

```bash
# Kjør alle sjekkene av skriptene og evalskriptet (42 stk, tar noen sekunder)
venv/bin/python evals/llm-innsamling/selvtest.py

# Valider en fasit fra evalene med alle kontrollene
PYTHON=venv/bin/python docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts/valider.sh \
  evals/llm-innsamling/caser/kystnett-2026-10/forventet.yml \
  --kilde evals/llm-innsamling/caser/kystnett-2026-10/input.md \
  --fra 2026-10-01 --sone nord_norge

# Regn ut priser uten avgifter (Midtnett: 48,91 og 42,66 øre inkl. avgifter, Sør-Norge)
venv/bin/python docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts/utled_avgifter.py \
  energiledd --pris 48,91 42,66 --dato 2026-10-01 --sone sor
```

Se [evals/llm-innsamling/README.md](../../evals/llm-innsamling/README.md) for hvordan et modellsvar
vurderes.

## Kjente svakheter og det som mangler

- **Ikke testet med en ekte modell ennå.** Skriptene og evalskriptet er testet med kunstige svar,
  men ingen modell har vært kjørt mot evalsakene. Det er neste steg etter review.
- Sperren i `verifiser_kilde.py` fanger oppdiktede tall, men ikke feil i selve transkriberingen av
  et bilde, og den sjekker ikke terskler og datoer.
- `sammenlign_forrige.py` bruker en fast grense på 30 %. Justér den hvis den gir for mye støy.
- Bare en skive er laget. Mangler: `index.html`, en chat-variant (én fil), peker fra
  `docs/llm/innsamling-prompt.txt` og automatisk oppdagelse i Claude Code (`.claude/` er
  gitignorert). Skriptene har en selvtest, men ikke egne enhetstester.
- Enova-satsene (1 øre/kWh og 800 kr/år) er ikke kontrollert mot Forskrift om Energifondet.

## Hva jeg ønsker tilbakemelding på

1. Er reglene i `kundegrupper.md` og `usikkerhet.md` slik dere vil ha dem?
2. Er «stopp og spør» riktig standard, eller er det steder der det blir for strengt?
3. Bør evalene ligge på toppnivå (`evals/`), eller et annet sted?
4. Skal norsk være språk for hele skillen?
