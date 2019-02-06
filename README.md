# cookiecutter-pypackage-poetry

Cookicutter python package template with poetry, travis, etc.

## Usage

### Create project

```bash
$ cookiecutter gh/Afonasev/cookiecutter-pypackage-poetry
project_name []: my_project
full_name []: Vasiliy Petrov
email []: vp@gmail.com
github_username []: vp_username
```

### Create virtualenv and install requirements

    make init

### Run autoformat

    make pretty

### Run linters

    make lint

### Run tests

    make test

### Add precommit hook

    make precommit_install
