import os

from {{cookiecutter.module_name}}.util import logger


def histring():
    return f"Your {{cookiecutter.project_name}} journey starts here :) (on {os.getenv('ENVIRONMENT')})"


def main():
    # TODO your journey starts here
    logger.info(histring())


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
