.PHONY: format
format:
	black .

poetry.lock: pyproject.toml
	poetry lock

requirements.txt: poetry.lock
	poetry install $(POETRY_EXTRA)
	poetry show | awk '{print $$1"=="$$2}' > $@
