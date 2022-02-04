import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "1234567"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
START_MSG = os.environ.get("START_MSG", "")
DB_URL = os.environ.get("DB_URL", "")
