_PHONY: readme vet

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements-dev.txt

readme:
	npx markdown-toc -i README.md
	./skript/status.py | sponge README.md

vet:
	cue vet -d "#Selskap" tariff.cue tariff-eksempel.yml tariffer/*.yml
