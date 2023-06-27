import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_1_2_1'

async def commandHelpThemeNo4_1_2_1(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:5]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if not int(answer[0]):
        return "Извините, в программе СтудСтартапа могут участвовать проекты без действующего договора с Фондом Содействия Инновациям", []

    markup = [[Button.inline(f"Цифровые технологии", f'help_theme_no_4_1_2_2:1'.encode())], [Button.inline(f"Медицина и технологии здоровьесбережения", f'help_theme_no_4_1_2_2:2'.encode())],
              [Button.inline(f"Новые материалы и химические технологии", f'help_theme_no_4_1_2_2:3'.encode())], [Button.inline(f"Новые приборы и производственыне технологии", f'help_theme_no_4_1_2_2:4'.encode())],
              [Button.inline(f"Биотехнологии", f'help_theme_no_4_1_2_2:5'.encode())], [Button.inline(f"Ресурсосберегающая энергетика", f'help_theme_no_4_1_2_2:6'.encode())]]
    
    return 'Выберите интересующую тему:', markup