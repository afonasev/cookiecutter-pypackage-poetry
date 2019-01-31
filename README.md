# package_template

Cookicutter python package template with travis, poetry, linters, black etc.

## Usage

### Create project

```bash
$ cookiecutter gh/Afonasev/package_template
project_name []: my_project
full_name []: Vasiliy Petrov
email []: vp@gmail.com
github_username []: vp_username
```

### Create virtualenv and install requirements

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ poetry install
```

### Run autoformat

    make pretty

### Run linters

    make lint

### Run tests

    make test
