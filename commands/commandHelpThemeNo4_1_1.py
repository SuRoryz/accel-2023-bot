import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_1_1'

async def commandHelpThemeNo4_1_1(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:4]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if int(answer[0]):
        return "Выберите интересующую тему и приходите попробовать свои силы в одном из наших проектов:\n1. УМНИК\n2. СТУДСТАРАП\n3. ШУСТРИК\n4. СТАРТ\n\nТемы можно найти по ссылке: https://airo61.donland.ru/activity/37782/", []

    markup = [[Button.inline(f"Цифровые технологии", f'help_theme_no_4_1_1_1:1'.encode())], [Button.inline(f"Медицина и технологии здоровьесбережения", f'help_theme_no_4_1_1_1:2'.encode())],
              [Button.inline(f"Новые материалы и химические технологии", f'help_theme_no_4_1_1_1:3'.encode())], [Button.inline(f"Новые приборы и производственыне технологии", f'help_theme_no_4_1_1_1:4'.encode())],
              [Button.inline(f"Биотехнологии", f'help_theme_no_4_1_1_1:5'.encode())], [Button.inline(f"Ресурсосберегающая энергетика", f'help_theme_no_4_1_1_1:6'.encode())]]
    
    return "В каком направлении вы хотите реализовать свою идею?", markup