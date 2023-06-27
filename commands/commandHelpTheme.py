import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'помочь с программой'

async def commandHelpTheme(event, get_only_text=False):
    chat = event.chat_id

    #new_event = await event.respond("Загрузка", buttons=Button.clear())

    if (get_only_text):
        markup = [[Button.inline(f"🟩 Да", f'help_theme_yes'.encode()), Button.inline(f"🟥 Нет", f'help_theme_no_1'.encode())]]

        return HELP_THEME, markup
    
    markup = event.client.build_reply_markup(
        [[Button.inline(f"🟩 Да", f'help_theme_yes'.encode()), Button.inline(f"🟥 Нет", f'help_theme_no_1'.encode())]]
        )
    
    await event.respond(HELP_THEME, buttons=markup)