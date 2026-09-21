#!/usr/bin/env bash
# Valider en tariff-fil før den leveres.
#
#   scripts/valider.sh tariffer/<selskap>.yml \
#       --kilde kilde-utdrag.md --fra YYYY-MM-DD --sone <sone>
#
# Kilde, dato og sone er påkrevd for å levere KOMPLETT. Uten dem kjøres bare de
# strukturelle kontrollene, og resultatet skal ikke rapporteres som KOMPLETT.
#
# Avslutter med kode 1 ved første feil.

set -uo pipefail

fil="${1:-}"
[ -n "$fil" ] || { echo "Bruk: valider.sh tariffer/<selskap>.yml [--kilde F --fra D --sone S]"; exit 2; }
shift

kilde="" fra="" sone=""
while [ $# -gt 0 ]; do
  case "$1" in
    --kilde) kilde="$2"; shift 2 ;;
    --fra) fra="$2"; shift 2 ;;
    --sone) sone="$2"; shift 2 ;;
    *) echo "Ukjent argument: $1"; exit 2 ;;
  esac
done

cd "$(git rev-parse --show-toplevel)"
skill="docs/llm-v2-innsamling-skill/skills/samle-tariff/scripts"
py="${PYTHON:-python3}"
[ -x venv/bin/python ] && py="venv/bin/python"
navn="$(basename "$fil")"
feil=0

echo "1/5 cue vet (schema)"
if cue vet --schema "#Selskap" tariff.cue "$fil"; then echo "    OK"; else feil=1; fi

echo "2/5 økende terskler og priser"
ut="$($py scripts/check_increasing_levels.py 2>&1 | grep -F "$navn" || true)"
if [ -z "$ut" ]; then echo "    OK"; else echo "$ut"; feil=1; fi

echo "3/5 overlapp og hull i perioder"
ut="$($py scripts/check_overlap_and_gap.py 2>&1 | grep -F "$navn" || true)"
if [ -z "$ut" ]; then echo "    OK"; else echo "$ut"; feil=1; fi

echo "4/5 belegg i kilden"
if [ -n "$kilde" ] && [ -n "$fra" ] && [ -n "$sone" ]; then
  if $py "$skill/verifiser_kilde.py" "$fil" --kilde "$kilde" --fra "$fra" --sone "$sone" | tail -3; then :; else feil=1; fi
else
  echo "    HOPPET OVER (mangler --kilde, --fra eller --sone). Kan ikke rapporteres som KOMPLETT."
  feil=1
fi

echo "5/5 sammenlign med forrige periode (advarsler skal forklares i rapporten, feiler ikke)"
if [ -n "$fra" ]; then
  $py "$skill/sammenlign_forrige.py" "$fil" --fra "$fra" | sed 's/^/    /'
else
  echo "    HOPPET OVER (mangler --fra)"
fi

[ "$feil" -eq 0 ] && echo "VALIDERING OK" || echo "VALIDERING FEILET"
exit "$feil"
