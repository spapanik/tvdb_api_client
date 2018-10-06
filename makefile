.PHONY: black

black:
	black .

pyproject.lock: pyproject.toml
	poetry lock

requirements.txt: pyproject.lock
	pip install -U poetry
	poetry install ${DEV}
	poetry show | awk '{print $$1"=="$$2}' > $@
