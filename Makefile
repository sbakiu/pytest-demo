python_m:
	python -m pytest tests/

pytest:
	pytest tests/

pytest-cov:
	pytest --cov-report term-missing --cov=src tests

fixtures:
	pytest --fixtures

capture:
	pytest --capture=tee-sys

markers:
	pytest --markers