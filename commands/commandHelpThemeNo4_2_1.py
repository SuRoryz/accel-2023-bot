import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_2_1'

async def commandHelpThemeNo4_2_1(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:4]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    if int(answer[0]) == 2:
        return "Выберите интересующую тему и приходите попробовать свои силы в одном из наших проектов:\n1.\n2.\n3.\n4.\n", []

    markup = [[Button.inline(f"1", f'help_theme_no_4_2_2:1'.encode())], [Button.inline(f"2", f'help_theme_no_4_2_2:2'.encode())],
              [Button.inline(f"3", f'help_theme_no_4_2_2:3'.encode())], [Button.inline(f"4", f'help_theme_no_4_2_2:4'.encode())],
              [Button.inline(f"5", f'help_theme_no_4_2_2:5'.encode())], [Button.inline(f"6", f'help_theme_no_4_2_2:6'.encode())]]
    
    return "В каком направлении вы хотите реализовать свою идею?", markup