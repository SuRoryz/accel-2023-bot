import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from json import dumps, loads

key = 'help_theme_no_result'

async def commandHelpThemeNoResult(event, answer):
    chat = event.chat_id

    prev = loads(Sql.getCache(chat)[0][3])

    prev['answer'] = prev['answer'][:3]
    results = prev['answer']

    results.append(answer[0])
    
    message = HELP_THEME_NOTHING
    markup = [[Button.inline(f"🔄 Попробовать ещё раз", f'help_theme_no_1'.encode())]]

    results = list(map(int, results))
    print(results)

    if results == [1, 1, 1, 1]:
        message = HELP_THEME_UMNIK
        markup = [[Button.inline(f"🔄 Это не то, что я хочу", f'help_theme_no_1'.encode())], [Button.inline(f"✅ Получить ссылку на заявку", f'help_theme_result:1'.encode())]]
    elif results == [2, 2, 2, 2]:
        message = HELP_THEME_STS
        markup = [[Button.inline(f"🔄 Это не то, что я хочу", f'help_theme_no_1'.encode())], [Button.inline(f"✅ Получить ссылку на заявку", f'help_theme_result:2'.encode())]]
    elif results == [3, 3, 3, 3]:
        message = HELP_THEME_UMNIK_STS
        markup = [[Button.inline(f"🔄 Это не то, что я хочу", f'help_theme_no_1'.encode())], [Button.inline(f"✅ Получить ссылку на заявку", f'help_theme_result:3'.encode())]]
    elif results == [4, 4, 4, 4]:
        message = HELP_THEME_START
        markup = [[Button.inline(f"🔄 Это не то, что я хочу", f'help_theme_no_1'.encode())], [Button.inline(f"✅ Получить ссылку на запись", f'help_theme_result:4'.encode())]]


    return message, markup