# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## What you need

- python3.11 installed
  `brew install python3.11`
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
4. `pixi run main`
5. `pixi run lint`
6. `pixi run test`
7. `pre-commit install`
8. `docker-compose up`

---

generated with https://github.com/pemukl/python-template
