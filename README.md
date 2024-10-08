![Python Version](https://img.shields.io/badge/python-3.11-blue)
![GitHub Repo stars](https://img.shields.io/github/stars/pemukl/python-template?style=social)

# Marc's Python Template 🐍

## What you get

A fresh python project nicely set up with git, pre-commit code formatting, a docker config and pixi dependency management set up for you. You can find an example of how your project will look like here: https://github.com/pemukl/python-template-instance.git

Why pixi? Because it has a project-oriented dependency management similar to poetry but it adds the power of the conda ecosystem, enabling you to install non-python dependencies. https://pixi.sh/v0.26.1/switching_from/poetry/

## What you need

- pixi installed
  `brew install pixi`
- git installed
  `brew install git`
- pre-commit installed
  `brew install pre-commit`
- cookiecutter installed
  `brew install cookiecutter`
- optionally docker (or [Orbstack](https://orbstack.dev/) 😉) and docker-compose installed

## How you do it

Just run the following command to start a new project in the current directory.

    cookiecutter https://github.com/pemukl/python-template

Credits: Thanks to the team at [at] for showing me cookiecutter via [their template](https://github.com/at-gmbh/at-python-template).
