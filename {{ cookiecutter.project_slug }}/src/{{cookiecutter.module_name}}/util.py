import os
import sys
from pathlib import Path
from typing import Any, Dict, Union

import yaml
from dotenv import load_dotenv
from loguru import logger

"""
This module contains utility functions for the project. It exports:

- `ROOT_DIR`: the root directory of the project
- `DATA_DIR`: the data directory of the project
- `logger`: the logger for the project
- `config`: dictionary containing the config for the project. Config is loaded from `config.yaml` in the `config` directory.
"""


load_dotenv()


ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir)

DATA_DIR = os.path.join(ROOT_DIR, "data")

default_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)

custom_format = (
    "<green>{time:HH:mm:ss}</green> <cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)
logger.remove()
logger.add(sys.stderr, format=custom_format)

class Dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = Dotdict(value)

def load_config(config_file: Union[str, Path]) -> Dict[str, Any]:
    """
    Load the config from the specified yaml file

    :param config_file: path of the config file to load
    :return: the parsed config as dictionary
    """
    with open(os.path.join(ROOT_DIR, "config", config_file)) as fp:
        conf = yaml.safe_load(fp)
        return Dotdict(conf)

config = load_config("config.yaml")
