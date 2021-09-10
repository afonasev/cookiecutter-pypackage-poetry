# cookiecutter-pypackage-poetry

The cookicutter template of a python package with poetry, travis, etc.

## Usage

### Create project

```bash
$ cookiecutter gh/Afonasev/cookiecutter-pypackage-poetry
project_name []: my_project
full_name []: John Doe
email []: john_doe@gmail.com
github_username []: john_doe
...
```

## In project directory

### Show help

    make help

### Create venv and install deps

    make init

### Run linters, autoformat, tests etc.

    make pretty lint test

### Bump new version

    make bump_major
    make bump_minor
    make bump_patch

### Install git precommit hook

    make precommit
