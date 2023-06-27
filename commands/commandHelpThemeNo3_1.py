import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_3_1'

async def commandHelpThemeNo3_1(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:3]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if int(answer[0]) == 1:
        return "Извините, согласно критерию ФСИ вы не можете подать заявку на грант.", []

    markup = [[Button.inline(f"Да, есть проект", f'help_theme_no_4_1_1:1'.encode()), Button.inline(f"Нет, нет проекта", f'help_theme_no_3_2:0'.encode())]]
    
    return "У вас есть проект, на которую вы бы хотели получить финансирование?", markup