import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_3'

async def commandHelpThemeNo3(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:2]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if int(answer[0]) == 2:
        markup = [[Button.inline(f"Да", f'help_theme_no_3_1:0'.encode()), Button.inline(f"Нет", f'help_theme_no_3_1:1'.encode())]]
        
        return "Вы обучаетесь в университете РФ?", markup

    markup = [[Button.inline(f"Да, получаю высшее образование", f'help_theme_no_4_1:0'.encode())], [Button.inline(f"Да, получаю среднее профессиональное образование", f'help_theme_no_4_2:0'.encode())],
              [Button.inline(f"Нет, не получаю", f'help_theme_no_4_1_0:0'.encode())]]
    
    return "Получаете ли вы образование?", markup