# Copyright (C) 2025 by Tohid_Help @ Github, < https://github.com/Tohidkhan6332 >
# Subscribe On YT < Tohidkhan_6332 >. All rights reserved. © Tohid © Mr Tohid.

"""
Tohidkhan6332 is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Tohid <https://github.com/Tohidkhan6332>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from pyrogram import filters
from pyrogram.types import Message
from config import BANNED_USERS
from strings import get_command
from TohidMusic import app
from TohidMusic.core.call import Tohid
from TohidMusic.utils.database import set_loop
from TohidMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(filters.command(STOP_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Tohid.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention), disable_web_page_preview=True
    )
