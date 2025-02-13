# Copyright (C) 2025 by Tohid_Help @ Github, < https://github.com/Tohidkhan6332 >
# Subscribe On YT < Tohidkhan_6332 >. All rights reserved. © Tohid © Mr Tohid.

"""
Tohidkhan6332 is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Tohid <https://github.com/Tohidkhan6332>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import asyncio
from pyrogram.enums import ChatType

import config
from TohidMusic import app
from TohidMusic.core.call import Tohid
from TohidMusic.utils.database import (
    get_client,
    is_active_chat,
    get_active_chats,
    is_music_playing,
    get_assistant,
)

autoend = {}


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(config.AUTO_LEAVE_ASSISTANT_TIME):
            from TohidMusic.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                try:
                    async for i in client.get_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001821969607
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(chat_id)
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while True:
        await asyncio.sleep(30)
        for chat_id in list(autoend.keys()):
            if not await is_active_chat(chat_id):
                del autoend[chat_id]
                continue
            userbot = await get_assistant(chat_id)
            members = []
            async for member in userbot.get_call_members(chat_id):
                if member is not None:
                    members.append(member)
            if len(members) <= 1:
                try:
                    await Tohid.stop_stream(chat_id)
                    await app.send_message(
                        chat_id,
                        "ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄʟᴇᴀʀᴇᴅ ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ <b>ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ sᴏɴɢs ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.</b>",
                    )
                except Exception:
                    pass
            del autoend[chat_id]


asyncio.create_task(auto_end())
