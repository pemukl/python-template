![Python Version](https://img.shields.io/badge/python-3.11-blue)
![GitHub Repo stars](https://img.shields.io/github/stars/pemukl/python-template?style=social)

# Marc's Python Template 🐍

## What you get

A fresh python project nicely set up with git, pre-commit code formatting, a docker config and pixi dependency management set up for you.

Why pixi? Because it has a project-oriented dependency management similar to poetry but it adds the power of the conda ecosystem meaning more powerful environments. https://pixi.sh/v0.26.1/switching_from/poetry/

## What you need

- pixi installed
  `brew install pixi`
- git installed
  `brew install git`
- pre-commit installed
  `brew install git`
- cookiecutter installed
  `brew install cookiecutter`
- optionally docker and docker-compose installed

## How you do it

Just run the following command to start a new project in the current directory.

    cookiecutter https://github.com/pemukl/python-template
