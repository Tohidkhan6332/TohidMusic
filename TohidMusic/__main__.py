# Copyright (C) 2025 by Tohid_Help @ Github, < https://github.com/Tohidkhan6332 >
# Subscribe On YT < Tohidkhan_6332 >. All rights reserved. © Tohid © Mr Tohid.

"""
Tohidkhan6332 is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Tohid <https://github.com/Tohidkhan6332>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import importlib
from typing import Any

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall, GroupCallNotFound

import config
from config import BANNED_USERS
from TohidMusic import LOGGER, app, userbot
from TohidMusic.core.call import Tohid
from TohidMusic.misc import sudo
from TohidMusic.plugins import ALL_MODULES
from TohidMusic.utils.database import get_banned_users, get_gbanned


async def init() -> None:
    # Check for at least one valid Pyrogram string session
    if all(not getattr(config, f"STRING{i}") for i in range(1, 6)):
        LOGGER("TohidMusic").error("Add Pyrogram string session and then try...")
        exit()
    await sudo()
    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for module in ALL_MODULES:
        importlib.import_module("TohidMusic.plugins" + module)
    LOGGER("TohidMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Tohid.start()
    try:
        await Tohid.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except (NoActiveGroupCall, GroupCallNotFound):
        LOGGER("TohidMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        exit()
    except:
        pass
    await Tohid.decorators()
    LOGGER("TohidMusic").info("Tohid Music Bot Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("TohidMusic").info("Stopping Tohid Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    LOGGER("TohidMusic").info("Stopping Music Bot")
