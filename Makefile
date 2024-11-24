_PHONY: readme vet fmt changedetection qa kilder bygg
.DEFAULT_GOAL := ci

ci: fmt kilder readme bygg

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements-dev.txt

readme: vet
	npx markdown-toc -i README.md
	./skript/status.py | sponge README.md

vet:
	cue vet -d "#Selskap" tariff.cue tariff-eksempel.yml tariffer/*.yml

fmt:
	yamlfmt tariff-eksempel.yml tariffer/*.yml referanse-data/nve/tariffer/*.yml

qa:
	ls -1 tariffer/ | xargs -I% ./skript/qa_nve.py ./tariffer/%

changedetection:
	docker compose up -d
	echo "Visit http://localhost:5000"

kilder:
	./skript/kilder.sh

bygg:
	#rm -f docs/tariffer/*
	./skript/template.py
	npx prettier docs/tariffer/*.html --write
