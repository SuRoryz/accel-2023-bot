import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'help_theme_yes_good'

async def commandHelpThemeYesGood(event, arg):
    chat = event.chat_id
    
    return HELP_THEME_YES_GOOD + arg[0], []