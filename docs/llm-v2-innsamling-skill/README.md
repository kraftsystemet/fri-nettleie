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
    ├── sjekk_kolonner.py     sjekker at inkl.- og eks.-kolonner i kilden stemmer med hverandre
    ├── sammenlign_forrige.py plausibilitet mot forrige periode
    └── valider.sh            kjører alt over pluss cue vet og eksisterende check_*-skript
```

Tester for skillen ligger i [`evals/llm-innsamling/`](../../evals/llm-innsamling/).

## Slik bruker du skillen til innsamling

Du trenger repoet lokalt, `make venv` (PyYAML m.m.) og `cue`.

**Med Claude Code eller en annen agent som kan lese repoet (anbefalt):**

1. Gi agenten skillen. `.claude/` er gitignorert, så den oppdages ikke automatisk. Enten lenker du
   den inn i din egen skills-mappe:

   ```bash
   ln -s "$PWD/docs/llm-v2-innsamling-skill/skills/samle-tariff" ~/.claude/skills/samle-tariff
   ```

   eller du skriver i prompten: «Les `docs/llm-v2-innsamling-skill/skills/samle-tariff/SKILL.md`
   og følg den».
2. Gi oppgaven med issue, dato og kilde, for eksempel: «Samle nye priser fra 2026-11-01 for
   Romsdalsnett (issue #435). Kilden står under.» Ligger prisene i et bilde eller en PDF, må du
   lime inn teksten selv. Agenten stopper ellers.
3. Agenten jobber lokalt som standard: lager en gren, endrer `tariffer/<selskap>.yml`, kjører
   `valider.sh` og viser diffen. Den pusher eller åpner PR bare hvis du ber om det.
4. Svaret er **KOMPLETT** (tabell med kilde per verdi, antakelser og YAML) eller **STOPPET** (hva
   som mangler og hva du må oppgi). Les antakelsene og sjekk tabellen mot kilden før du går videre.
5. Åpne PR etter malen i [`repo-og-pr.md`](skills/samle-tariff/references/repo-og-pr.md): tittel
   «Selskap åååå-mm», `Closes #N` og en kort beskrivelse. Ingen PR merges før en annen i repoet har
   reviewet den.

**Uten agent**, de samme sjekkene kan kjøres for hånd (fra repoets rot):

```bash
S=docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts

# Fjern mva og avgifter, med avrundingssjekk (kr/mnd i kilden gir kr/år)
venv/bin/python $S/utled_avgifter.py fastledd --pris 305 367 --sone sor --inkl-mva

# Stemmer inkl.- og eks.-kolonnene i kilden med hverandre? (INKL:EKS)
venv/bin/python $S/sjekk_kolonner.py --sone sor --par 293,8:235

# Alle kontrollene på den ferdige filen
PYTHON=venv/bin/python $S/valider.sh tariffer/<selskap>.yml \
  --kilde kilde-utdrag.md --fra 2026-11-01 --sone sor
```

`kilde-utdrag.md` er et ordrett utdrag av kilden som du lager selv, utenfor repoet. Alle tall som
står i den nye perioden må kunne spores til det.

**Husk:** skillen fanger oppdiktede tall og inkonsistente kolonner, men ikke feil i transkribering av
bilder, og den sjekker ikke terskler og datoer. Se over disse selv.

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
- `sammenlign_forrige.py` bruker en fast grense på 30 %. Høsten 2026 gir flere netteiere økninger
  rundt og over dette (Føie +30 til +35 %), og advarselen er da reell. Den skal forklares med kilden,
  ikke dempes. Justér grensen hvis den gir for mye støy.
- Bare en skive er laget. Mangler: `index.html`, en chat-variant (én fil), peker fra
  `docs/llm/innsamling-prompt.txt` og automatisk oppdagelse i Claude Code (`.claude/` er
  gitignorert). Skriptene har en selvtest, men ikke egne enhetstester.
- Enova-satsene (1 øre/kWh og 800 kr/år) er ikke kontrollert mot Forskrift om Energifondet.

## Hva jeg ønsker tilbakemelding på

1. Er reglene i `kundegrupper.md` og `usikkerhet.md` slik dere vil ha dem?
2. Er «stopp og spør» riktig standard, eller er det steder der det blir for strengt?
3. Bør evalene ligge på toppnivå (`evals/`), eller et annet sted?
4. Skal norsk være språk for hele skillen?
