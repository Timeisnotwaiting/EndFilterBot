from pyrogram import Client
from pyrogram.types import Message

async def get_filter_info(_, m):
    reply = m.reply_to_message
    l = len(m.command)
    if l == 1:
        return await m.reply("You need to give the filter a name!")
    if l == 2 and not reply:
        return await m.reply("You need to give the filter some content!")
    if l == 2 and (reply.sticker or reply.animation):
        
