SHELL := /bin/bash

STAGED := $(shell git diff --cached --name-only --diff-filter=ACMR -- 'src/***.py' | sed 's| |\\ |g')

format:
	black .
	isort .
	nbqa black .
	nbqa isort .

lint:
	pytest src/ --pylint --flake8 --mypy
	# nbqa pytest src/ --pylint --flake8 --mypy

lint-all:
	pytest src/ --pylint --flake8 --mypy --cache-clear
	# nbqa pytest src/ --pylint --flake8 --mypy --cache-clear

lint-staged:
ifdef STAGED
	pytest $(STAGED) --pylint --flake8 --mypy --cache-clear
	# nbqa pytest $(STAGED) --pylint --flake8 --mypy --cache-clear
else
	@echo "No Staged Python File in the src folder"
endif

init:
	pip install -U pip
	pip install -e .
	pip install -r requirements.txt
	bash ./hooks/install.sh
