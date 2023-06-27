import config
from sql import Sql
from json import loads, dumps
from telethon.tl.custom import Button
from chatGPT import getAnswer
import random

async def handleNotCommand(event, client) -> None:
    user = event.chat_id
    cache_full = Sql.getCache(user)[0]
    cache = loads(cache_full[2])

    word_to_choose = ["⚙ Думаю над ответом...", "⚙ Обрабатываю ваше сообщение...", "⚙ Решаю, что ответить...", "⚙ Пожалуйста, подождите..."]
    
    if event.raw_text.lower() ==  "назад":
        prev_location = cache
        return config.MENU_TREE[prev_location['type'].lower()]

    elif cache["type"] == "задать вопрос":
        if cache_full[4]:
            cache_messages = loads(cache_full[4])
        else:
            cache_messages = []
        
        e = await event.respond(random.choice(word_to_choose))

        if not(cache_messages):
            cache_messages = []

        if len(cache_messages) > 9:
            cache_messages.pop(0)

        #await event.respond('Обрабатываю ваш запрос...')
        
        new_cache = getAnswer(cache_messages, event.raw_text)
        Sql.updateCache(event.chat_id, "c4", dumps(new_cache))

        await e.edit(new_cache[-1]["content"] + "\n\nКонтакты Представительства в Ростовской области Фонда содействия инновациям:\n+7 961 293-46-95\nhttps://taplink.cc/fasie61")

        #text = f'От пользователя: {event.message.sender.username}\n\n"{event.raw_text}"\n\nЧтобы написать в этот диалог, ответьте на это сообщение\n\nUSER_ID:{event.chat_id}'
        #
        #await client.send_message(config.ADMIN, text)
        #await event.respond("Сообщение отправлено!")

    elif event.message.is_reply:
        rpl = await event.message.get_reply_message()
        rpl_text = rpl.message

        admin_id = await client.get_entity(config.ADMIN)
        admin_id = admin_id.id

        print(admin_id, user)

        if "USER_ID:" in rpl_text and admin_id == user:
            user_id = rpl_text.split("USER_ID:")[1]
            text = f"Техническая поддержка ответила на ваш вопрос:\n\n{event.raw_text}"

            await client.send_message(int(user_id), text)
            await event.respond("Сообщение отправлено!")


async def handleInlineCommand(event, client, COMMANDS) -> None:
    answer = event.data.decode("UTF-8")
    peer_id: int = event.chat_id

    args = answer.split(":")[1:]
    answer = answer.split(":")[0]

    print(args, answer)

    cache = loads(Sql.getCache(peer_id)[0][2])
    
    if answer == "back":
        prev_location = cache
        #print(prev_location, loads(Sql.getCache(peer_id)[0][3])['answer'], args)
        print(args[0])
        if args[0] not in ["help_theme_no_2"] and "help_theme_no" in args[0]:
            location = loads(Sql.getCache(peer_id)[0][3])['answer'][-2]
            message, buttons = await COMMANDS[config.MENU_TREE[prev_location['type'].lower()].lower()](event, location)
        else:
            message, buttons = await COMMANDS[config.MENU_TREE[prev_location['type'].lower()].lower()](event, True)

        if (config.MENU_TREE[prev_location['type'].lower()].lower() not in ["меню", "помочь с программой"]):
            buttons.append([Button.inline(f"⬅ Назад", f'back:{config.MENU_TREE[prev_location["type"].lower()].lower()}'.encode()), Button.inline(f"↩ Меню", f'menu'.encode())])

        Cache = dumps({'type': config.MENU_TREE[prev_location['type'].lower()].lower()})
        Sql.updateCache(peer_id, "c2", Cache)
        
        await event.edit(message, buttons=event.client.build_reply_markup(buttons))
    
    if answer == "menu":
        return "Меню"
    
    if answer in COMMANDS:
        try:
            Cache = dumps({'type': answer})
            Sql.updateCache(peer_id, "c2", Cache)

        except Exception as e:
            print(e)
        
        if args:
            message, buttons = await COMMANDS[answer](event, args)
        else:
            message, buttons = await COMMANDS[answer](event)

        buttons.append([Button.inline(f"⬅ Назад", f'back:{answer}'.encode()), Button.inline(f"↩ Меню", f'menu'.encode())])

        print(loads(Sql.getCache(peer_id)[0][3])['answer'])

        await event.edit(message, buttons=event.client.build_reply_markup(buttons))
    




