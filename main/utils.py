import importlib
import logging
import sys
from pathlib import Path

from . import LOGGER


def load_plugins(plugin_name):
    path = Path(f"main/plugins/{plugin_name}.py")
    name = "main.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["main.plugins." + plugin_name] = load
    LOGGER("BOT").info(f"Succesfully Load {plugin_name}")
