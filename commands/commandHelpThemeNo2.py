from json import dumps
import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'help_theme_no_2'

async def commandHelpThemeNo2(event, answer):
    chat = event.chat_id

    Cache = dumps({'answer': [answer[0]]})
    Sql.updateCache(chat, "c3", Cache)

    print('ANSWER: ', answer)

    if int(answer[0]) != 2:
        if int(answer[0]) == 1:
            return 'Согласно возрастному критерию Вам подходит программа грантовой поддержки “ШУСТРИК” (https://shustrik.org/)', []
        else:
            return 'Согласно возрастному критерию Вам подходит программа грантовой поддержки “Старт” (https://fasie.ru/programs/programma-start/)', []

    markup = [[Button.inline(f"РФ", f'help_theme_no_3:1'.encode())], [Button.inline(f"Иное", f'help_theme_no_3:2'.encode())]]
    
    return "Укажите ваше гражданство", markup