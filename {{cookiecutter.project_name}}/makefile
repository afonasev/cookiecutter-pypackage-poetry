.PHONY: test lint pretty

CODE = {{cookiecutter.project_name}}

test:
	pytest -vv --cov=$(CODE) $(args)

lint:
	flake8 --jobs 4 --statistics $(CODE) tests
	pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	black --py36 --skip-string-normalization --line-length=79 --check $(CODE) tests

pretty:
	isort --apply --recursive $(CODE) tests
	black --py36 --skip-string-normalization --line-length=79 $(CODE) tests
	unify --in-place --recursive $(CODE) tests
