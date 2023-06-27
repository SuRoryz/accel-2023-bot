import config
import requests
import os
import importlib
import xml.etree.ElementTree as ET
import sys
import time
from sheets import Sheets

def initCommands() -> dict:
    # Получаем модули комманд из папки commands
    modules: list = os.listdir('commands')
    commands: dict = dict()
    
    # Проходим через все py файлы и импортируем функцию команды
    # А так же её ключ
    for module in modules:
        if module == "__pycache__":
            continue

        module = module.replace('.py', '')
        
        module_module = importlib.import_module(f'commands.{module}')
        module_func = getattr(module_module, module)
        module_key = getattr(module_module, "key")

        if type(module_key) == tuple:
            for key in module_key:
                commands[key] = module_func
        else:
            commands[module_key] = module_func
    
    return commands

# Получаем данные из гугл таблицы
def initConfig() -> None:
    sh = Sheets()
    table = sh.getTable()
    
    wks = table.sheet1

    config.MENU = wks.cell('B2').value

    config.HELP_THEME = wks.cell('C2').value # Примерная тема?

    config.HELP_THEME_YES = wks.cell('D2').value # Да
    config.HELP_THEME_YES_GOOD = wks.cell('N2').value # Выбрал тему

    config.HELP_THEME_NO_1 = wks.cell('E2').value # Нет. Уточняем тему
    config.HELP_THEME_NO_2 = wks.cell('F2').value
    config.HELP_THEME_NO_3 = wks.cell('G2').value
    config.HELP_THEME_NO_4 = wks.cell('H2').value

    config.HELP_THEME_UMNIK = wks.cell('I2').value
    config.HELP_THEME_STS = wks.cell('J2').value
    config.HELP_THEME_UMNIK_STS = wks.cell('K2').value
    config.HELP_THEME_START = wks.cell('L2').value
    config.HELP_THEME_NOTHING = wks.cell('M2').value

    config.ASK = wks.cell('O2').value