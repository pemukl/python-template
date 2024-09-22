import logging
import os
from pathlib import Path
from typing import Any, Dict, Union

import yaml
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger('{{cookiecutter.module_name}}')


ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir)


def load_config(config_file: Union[str, Path]) -> Dict[str, Any]:
    """
    Load the config from the specified yaml file

    :param config_file: path of the config file to load
    :return: the parsed config as dictionary
    """
    with open(os.path.join(ROOT_DIR, "config", config_file)) as fp:
        return yaml.safe_load(fp)

config = load_config("config.yaml")


def logging_setup(config: Dict):
    """
    setup logging based on the configuration

    :param config: the parsed config tree
    """

    log_conf = config['logging']
    fmt = log_conf['format']

    class CustomFormatter(logging.Formatter):
        grey = "\x1b[38;20m"
        green = "\x1b[32m"
        yellow = "\x1b[33;20m"
        red = "\x1b[31;20m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"

        FORMATS = {
            logging.DEBUG: grey + fmt + reset,
            logging.INFO: green + fmt + reset,
            logging.WARNING: yellow + fmt + reset,
            logging.ERROR: red + fmt + reset,
            logging.CRITICAL: bold_red + fmt + reset
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            formatter.datefmt = log_conf["datefmt"]
            return formatter.format(record)

    if log_conf['enabled']:
        level = logging._nameToLevel[log_conf['level'].upper()]
    else:
        level = logging.NOTSET

    logger.setLevel(level=level)

    ch = logging.StreamHandler()
    ch.setLevel(level=level)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)


logging_setup(config)
