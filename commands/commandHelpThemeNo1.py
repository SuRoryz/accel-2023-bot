import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'помочь с программой'

async def commandHelpThemeNo1(event, args=None):
    chat = event.chat_id

    markup = [[Button.inline(f"до 18 лет", f'help_theme_no_2:1'.encode())], [Button.inline(f"от 18 до 30 лет", f'help_theme_no_2:2'.encode())],
              [Button.inline(f"31 и более", f'help_theme_no_2:3'.encode())]]

    if (args):
        return "Укажите ваш возраст", markup
    
    await event.respond("Укажите ваш возраст", buttons=markup)