import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_2_3'

async def commandHelpThemeNo4_2_3(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:6]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if int(answer[0]) == 2:
        return "Извините, проекты не содержащие элементы научной новизны не допускаются к участию. А если всё-таки у Вашей идеи появилась научная новизна, возвращайтесь назад.", []

    markup = [[Button.inline(f"Да", f'help_theme_no_4_2_4:1'.encode())], [Button.inline(f"Нет", f'help_theme_no_4_2_4:2'.encode())]]
    
    return "Является ли Ваша идея актуальной и технически значимой для решения современных проблем и задач?", markup