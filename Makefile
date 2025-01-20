_PHONY: readme vet fmt changedetection qa kilder bygg
.DEFAULT_GOAL := ci

ci: fmt kilder readme bygg

clear-cache:
	rm -rf ~/.cache/kraftsystemet-fri-nettleie

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements-dev.txt

readme: vet toc status

status:
	./scripts/status.py | sponge README.md

toc:
	npx markdown-toc -i README.md

vet:
	cue vet --schema "#Selskap" tariff.cue tariff-eksempel.yml tariffer/*.yml

fmt:
	yamlfmt tariff-eksempel.yml tariffer/*.yml referanse-data/nve/tariffer/*.yml

qa:
	ls -1 tariffer/ | xargs -I% ./scripts/qa_nve.py ./tariffer/%

nve-data:
	rm -f referanse-data/nve/tariffer/*.yml
	./scripts/get_nve_price_data.py referanse-data/nve/tariffer/
	yamlfmt referanse-data/nve/tariffer/*.yml

changedetection:
	docker compose up -d
	echo "Visit http://localhost:5000"

stop:
	docker compose stop

kilder:
	./scripts/kilder.sh

bygg:
	./scripts/template.py
	npx prettier docs/tariffer/*.html --write
