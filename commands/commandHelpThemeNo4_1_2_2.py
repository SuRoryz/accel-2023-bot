import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_1_2_2'

async def commandHelpThemeNo4_1_2_2(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:6]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    markup = [[Button.inline(f"На собственных разработках и исследованиях", f'help_theme_no_4_1_2_3:1'.encode())],
              [Button.inline(f"На ранее известных и общедоступных идеях или технологиях", f'help_theme_no_4_1_2_3:2'.encode())]]
    
    return 'На чем основан Ваш проект?', markup