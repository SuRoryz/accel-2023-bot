import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import loads, dumps

key = 'help_theme_no_4_1_2'

async def commandHelpThemeNo4_1_2(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:4]
    prev['answer'].append(answer[0])

    Cache = dumps(prev)
    Sql.updateCache(chat, "c3", Cache)

    markup = [[Button.inline(f"Да", f'help_theme_no_4_1_2_1:1'.encode())], [Button.inline(f"Нет", f'help_theme_no_4_1_2_1:2'.encode())]]
    
    return 'Есть ли у Вас действующий договор с Фондом содействия инноваций (за исключением грантополучателей второго года программы "Умник")?', markup