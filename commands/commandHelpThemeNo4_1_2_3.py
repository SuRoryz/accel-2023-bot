import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_1_2_3'

async def commandHelpThemeNo4_1_2_3(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:7]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if int(answer[0]) == 1:
        return 'Ваш проект подходит под программу "СтудСтартап" (https://fasie.ru/studstartup/)', []

    markup = [[Button.inline(f"Да содержит", f'help_theme_no_4_1_2_4:1'.encode())],
              [Button.inline(f"Нет, не содержит", f'help_theme_no_4_1_2_4:2'.encode())]]
    
    return 'Содержит ли проект Ваш интеллектуальный вклад, улучшающий эффективность данного товара/изделия/технологии/услуги?', markup