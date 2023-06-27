import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'help_theme_yes'

async def commandHelpThemeYes(event, arg=None):
    chat = event.chat_id

    markup = [[Button.inline(f"Тема 1", f'help_theme_yes_good:1'.encode())], [Button.inline(f"Тема 2", f'help_theme_yes_good:2'.encode())],
              [Button.inline(f"Тема 3", f'help_theme_yes_good:3'.encode())], [Button.inline(f"Затрудняюсь ответить", f'help_theme_no_1'.encode())]]
    
    return HELP_THEME_YES, markup