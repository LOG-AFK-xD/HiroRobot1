import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from HiroRobot.events import register
from HiroRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/ff2fa22dfa6ae838cc6cd.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Hiro Robot.** \n\n"
    TEXT += "💠 **I'm Working Properly** \n\n"
    TEXT += f"💠 **My Master : [Vain](https://t.me/saint_foire)** \n\n"
    TEXT += f"💠 **Library Version :** `{telever}` \n\n"
    TEXT += f"💠 **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"💠 **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("Help", "https://t.me/Hiroxbot?start=help"),
            Button.url("Support", "https://t.me/machinaxsupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
