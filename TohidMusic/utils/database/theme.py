# Copyright (C) 2025 by Tohid_Help @ Github, < https://github.com/Tohidkhan6332 >
# Subscribe On YT < Tohidkhan_6332 >. All rights reserved. © Tohid © Mr Tohid.

"""
Tohidkhan6332 is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Tohid <https://github.com/Tohidkhan6332>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

# from typing import Dict, List, Union
# from TohidMusic.core.mongo import mongodb

# themedb = mongodb.notes


# async def _get_theme(chat_id: int) -> Dict[str, int]:
#     _notes = await themedb.find_one({"chat_id": chat_id})
#     if not _notes:
#         return {}
#     return _notes["notes"]


# async def get_theme(chat_id: int, name: str) -> Union[bool, dict]:
#     name = name.lower().strip()
#     _notes = await _get_theme(chat_id)
#     if name in _notes:
#         return _notes[name]
#     else:
#         return False


# async def save_theme(chat_id: int, name: str, note: dict):
#     name = name.lower().strip()
#     _notes = await _get_theme(chat_id)
#     _notes[name] = note
#     await themedb.update_one(
#         {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
#     )
