import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_2_2'

async def commandHelpThemeNo4_2_2(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:5]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    markup = [[Button.inline(f"Да, содержит", f'help_theme_no_4_2_3:1'.encode())], [Button.inline(f"Нет, не содержит", f'help_theme_no_4_2_3:2'.encode())]]
    
    return "Содержит ли Ваш проект новые и оригинальные идеи, методы или технологии?", markup