SHELL := /bin/bash

STAGED := $(shell git diff --cached --name-only --diff-filter=ACMR -- 'src/***.py' | sed 's| |\\ |g')

format:
	black .
	isort .

lint:
	pytest src/ --pylint --flake8

lint-all:
	pytest src/ --pylint --flake8 --cache-clear

lint-staged:
ifdef STAGED
	pytest $(STAGED) --pylint --flake8 --cache-clear
else
	@echo "No Staged Python File in the src folder"
endif

init:
	pip install -U pip
	pip install -e .
	pip install -r requirements.txt
	bash ./hooks/install.sh
