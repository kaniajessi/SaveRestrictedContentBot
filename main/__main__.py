import glob
from pathlib import Path

from main.utils import load_plugins

from . import LOGGER, bot

LOGGER("BOT").info("Starting To Load Plugins")
path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

# Don't be a thief
LOGGER("BOT").info("[🔥 BERHASIL DIAKTIFKAN! 🔥]")

if __name__ == "__main__":
    bot.run_until_disconnected()
