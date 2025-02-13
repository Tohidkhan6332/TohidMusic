# Copyright (C) 2025 by Tohid_Help @ Github, < https://github.com/Tohidkhan6332 >
# Subscribe On YT < Tohidkhan_6332 >. All rights reserved. © Tohid © Mr Tohid.

"""
Tohidkhan6332 is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Tohid <https://github.com/Tohidkhan6332>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄 ᴩᴀᴜsᴇ 🙄",
            description=f"ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://i.imgur.com/RarYnNk.jpeg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 ʀᴇsᴜᴍᴇ 😋",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://i.imgur.com/RarYnNk.jpeg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂 sᴋɪᴩ 🙂",
            description=f"sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ ᴍᴏᴠᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴛʀᴇᴀᴍ.",
            thumb_url="https://i.imgur.com/RarYnNk.jpeg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 ᴇɴᴅ 🥺",
            description="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://i.imgur.com/RarYnNk.jpeg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥴 sʜᴜғғʟᴇ 🥴",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://i.imgur.com/RarYnNk.jpeg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🥱 ʟᴏᴏᴩ 🥱",
            description="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://i.imgur.com/RarYnNk.jpeg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
