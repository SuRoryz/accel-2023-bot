import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = ('/start', 'меню')

async def commandStart(event):
    chat = event.chat_id

    markup = event.client.build_reply_markup(
        [[Button.text("Помочь с программой", resize=True), Button.text("Задать вопрос", resize=True)]]
        )
    
    await event.respond(MENU, buttons=markup)

    return True