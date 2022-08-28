from pyrogram import Client, filters
from pyrogram.types import Message
from os import getenv

API_ID = int(getenv["API_ID", None])
API_HASH = getenv["API_HASH", None]
BOT_TOKEN = getenv["BOT_TOKEN", None]

YASHVI = Client(":YashuAlpha:", API_ID, API_HASH, BOT_TOKEN)

@YASHVI.on_message(filters.command("filter"))
async def filter_event(_, m):
