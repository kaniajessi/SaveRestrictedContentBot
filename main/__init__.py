#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
from dotenv import load_dotenv
import logging, time, sys

load_dotenv("config.env")

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s - %(asctime)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.WARNING)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.WARNING)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.WARNING)
LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
    ubot_me = userbot.get_me()
    LOGS.info(f"UserBot Started as @{ubot_me.username} [ {ubot_me.id} ]")
except BaseException:
    LOGGER(__name__).info("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)


Bot = Client(
    "SaveRestricted", bot_token=BOT_TOKEN, api_id=int(API_ID), api_hash=API_HASH
)

try:
    Bot.start()
    bot_me = Bot.get_me()
    LOGS.info(f"Bot Started as @{bot_me.username}")
except Exception as e:
    LOGGER(__name__).error(e)
    sys.exit(1)
