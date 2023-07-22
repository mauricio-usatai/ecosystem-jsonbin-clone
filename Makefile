install:
	pip install -r requirements.txt

flake8:
	git ls-files '*.py' | flake8 --count

pylint:
	git ls-files '*.py' | xargs pylint --disable=duplicate-code --fail-under=10

black:
	git ls-files '*.py' | black --check .

pytest:
	pytest --no-cov-on-fail --cov-fail-under=70 --cov-branch --cov-report=term --cov-report=html:htmlcov --cov=apps --cov=src
