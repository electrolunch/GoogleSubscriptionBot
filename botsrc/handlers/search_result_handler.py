import logging
from botsrc.bot import BotManager as bm
from aiogram import types,Dispatcher
from aiogram.types import ChatActions
from icecream import ic

async def update_command(message: types.Message):
    updates=bm.sm.get_updates(message.from_user.id)
    if not updates:
        await message.reply("Нет новых результатов\n")
        return
    # ic(updates)
    # await message.reply('\n'.join([f"{i+1}) {link}" for i,link in enumerate(updates)]))
    for query in updates.keys():
        links = updates[query]
        if not links:
            # await bm.bot.send_message(message.from_user.id, f"Нет новых результатов по запросу {query}\n")
            continue
        # ic(links)
        # await message.reply(update['query'])
        # send links each on new line with number like 1) 2) 3)
        # await message.reply('\n'.join([f"{i+1}) {link}" for i,link in enumerate(update['new_links'])]))
        message_text = f"Результаты по запросу {query}:\n"
        message_text += '\n'.join([f"{i+1}) {link}" for i,link in enumerate(links)])
        await message.reply(message_text)

        # await message.reply('\n'.join(update['new_links']))
        # await message.reply(update['new_links'])



def register_handlers(dp:Dispatcher):
    dp.register_message_handler(update_command,commands=['update'])