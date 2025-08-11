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

nve-data:
	mkdir -p referanse-data/nve/tariffer/privat referanse-data/nve/tariffer/naring
	rm -f referanse-data/nve/tariffer/privat/*.yml referanse-data/nve/tariffer/naring/*.yml
	./scripts/get_nve_price_data.py private referanse-data/nve/tariffer/privat/
	./scripts/get_nve_price_data.py industry referanse-data/nve/tariffer/naring/
	yamlfmt referanse-data/nve/tariffer/**/*.yml

changedetection:
	docker compose up -d
	echo "Visit http://localhost:5000"

stop:
	docker compose stop

kilder:
	./scripts/kilder.sh

bygg:
	rm docs/tariffer/*.html
	./scripts/template.py
	npx prettier docs/tariffer/*.html --write

refdata:
	./scripts/get_grid_owner_data.py
	./scripts/get_mga_data.py
