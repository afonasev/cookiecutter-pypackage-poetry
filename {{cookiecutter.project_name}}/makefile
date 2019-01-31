.PHONY: test lint pretty

CODE = {{cookiecutter.project_name}} tests

test:
	pytest -vv --cov=$(CODE) $(args)

lint:
	flake8 --jobs 4 --statistics $(CODE)
	pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	black --py36 --skip-string-normalization --line-length=79 --check $(CODE)

pretty:
	isort --apply --recursive $(CODE)
	black --py36 --skip-string-normalization --line-length=79 $(CODE)
	unify --in-place --recursive $(CODE)
