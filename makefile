default:
	@cat makefile

env:
	python3 -m venv env
	. env/bin/activate; pip install -r requirements.txt

run:
	@python3 bin/clockdeco_param.py

.PHONY: tests
tests:
	pytest -vv tests
