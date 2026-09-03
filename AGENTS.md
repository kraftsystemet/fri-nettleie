# AGENTS.md


# Project structure

* Scripts go in the `scripts` directory

# General guidelines

* NEVER add new tools or dependencies before asking the user for confirmation

# Python development

* When working with python, use the virtual environment in the venv directory
* Run scripts with `venv/bin/python`
* If new requirements are needed, add them to `requirements-dev.txt`. Install
  in the virtual environment using `venv/bin/pip install -r requirements-dev.txt`
* Use the CLI tool `ruff` to lint python code. Use `ruff check --fix <filename>`
