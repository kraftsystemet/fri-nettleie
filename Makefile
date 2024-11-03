_PHONY: readme

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements-dev.txt

readme:
	npx markdown-toc -i README.md
	./skript/status.py | sponge README.md