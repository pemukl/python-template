# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## What you need

- pixi installed
  `brew install pixi`
- git installed
  `brew install git`
- pre-commit installed
  `brew install pre-commit`
- optionally docker and docker-compose installed

## Getting started

1. Clone the repository
2. Navigate to the cloned project directory: `cd {{cookiecutter.project_slug}}`
3. `pixi install`
4. `pre-commit install`
5. Copy the example env file and set your variables: `cp .env_example .env`
6. `pixi run main`
7. `pixi run lint`
8. `pixi run test`
9. `docker-compose up`

## Project structure

- `src/{{ cookiecutter.module_name }}`: The main application code
- `tests/{{ cookiecutter.module_name }}`: The test cases for the project
- `data/`: Contains the data files you don't want to commit to git.
- `.pixi/envs/default/bin/python`: Your local python binary for the project

## Hints

- We have a logger instance you can use `from {{ cookiecutter.project_slug }}.util import logger`
- We have a config files in `./config/` you can use the one accoring to your environment with `from {{ cookiecutter.project_slug }}.util import config`
- You can access the data folder from `./data/` with `from {{ cookiecutter.project_slug }}.data import DATA_DIR`.
- The root of the project can be accessed with `from {{ cookiecutter.project_slug }}.util import ROOT_DIR`.

---

generated with https://github.com/pemukl/python-template
