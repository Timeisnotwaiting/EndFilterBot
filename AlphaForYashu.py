from pyrogram import Client
from pyrogram.types import Message

async def get_filter_info(_, m):
    reply = m.reply_to_message
    l = len(m.command)
    if l == 1:
        return await m.reply("You need to give the filter a name!")
    if l == 2 and not reply:
        return await m.reply("You need to give the filter some content!")
    if l > 1 and (reply.sticker or reply.animation):
        _name = m.text.split()[1].strip()
        file_id = reply.sticker.file_id if reply.sticker else reply.animation.file_id   
        return details = {name=_name, file=file_id, format=("sticker" if reply.sticker else "animation"), caption=None}
    if l > 1 and (reply.photo or reply.video or reply.audio):
        _name = m.text.split(None, 2)[1]
        file_path = await _.download_media(reply, f"
