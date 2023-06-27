import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import dumps, loads

key = 'help_theme_result'

async def commandHelpThemeNoResultResult(event, answer):
    chat = event.chat_id

    Cache = dumps({'answer': []})
    Sql.updateCache(chat, "c3", Cache)
    
    return "ссылка #" + answer[0], []