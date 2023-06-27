import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_2_4'

async def commandHelpThemeNo4_2_4(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:7]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if int(answer[0]) == 2:
        return "Извините, но такие идеи не могут принимать участие в программе. Возможно, вам стоит грубже погрузиться в тему и доработать проект.", []
    
    return 'Ваш проект подходит под программу "УМНИК" (https://fasie.ru/programs/programma-umnik/)', []