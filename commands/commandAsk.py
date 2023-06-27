import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'задать вопрос'

async def commandAsk(event):
    chat = event.chat_id

    markup = event.client.build_reply_markup(
        [[Button.text("Назад", resize=True)]]
        )
    
    await event.respond(ASK_GPT, buttons=markup)

    return True