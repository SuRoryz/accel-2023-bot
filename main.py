from telethon import TelegramClient, events

from sql import Sql
from handleNotCommand import handleNotCommand, handleInlineCommand

from config import *
from Inits import *

from json import loads, dumps

client = TelegramClient(SESSION, APP_ID, APP_HASH)

# - - - - - EVENT HANDLERS - - - - -
@client.on(events.NewMessage)
async def message_handler(event) -> None:
    text: str = event.raw_text.lower()
    is_me: bool = event.message.out
    peer_id: int = event.chat_id

    if not(is_me):
        # Добавляем пользователя в таблицу для кеша, если его там нет
        # И заодно кешируем это в памяти, чтоб не обращаться постоянно к дб
        if peer_id not in CACHED:
            Sql.setUpUser(peer_id)
            CACHED.append(peer_id)

            Cache = dumps({'type': "Меню"})
            Sql.updateCache(peer_id, "c2", Cache)
                
        if text in COMMANDS:
            await COMMANDS[text](event)

            try:
                Cache = dumps({'type': text})
                Sql.updateCache(peer_id, "c2", Cache)

            except Exception as e:
                print(e)
         
        else:
            answer = await handleNotCommand(event, client)

            if (answer and answer.lower() in COMMANDS):

                Cache = dumps({'type': answer.lower()})
                Sql.updateCache(peer_id, "c2", Cache)

                await COMMANDS[answer.lower()](event)

@client.on(events.CallbackQuery)
async def inline(event):
    answer = await handleInlineCommand(event, client, COMMANDS)

    if (answer and answer.lower() in COMMANDS):
        await COMMANDS[answer.lower()](event)

        Cache = dumps({'type': answer.lower()})
        Sql.updateCache(event.chat_id, "c2", Cache)


# - - - - - EVENT HANDLERS - - - - -

if __name__ == "__main__":
    client.start(bot_token=BOT_TOKEN)
    
    initConfig()
    COMMANDS = initCommands()
    
    Sql.setUp()

    client.run_until_disconnected()
