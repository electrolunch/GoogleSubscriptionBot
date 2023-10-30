from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import logging
from botsrc.bot import BotManager as bm
from aiogram import types,Dispatcher
from aiogram.types import ChatActions
from botsrc.google.google_search import GoogleSearchEngine
from botsrc.google.subscription import SearchSubscription
from botsrc.google.subscription_store import JsonSubsStore
from aiogram.utils.callback_data import CallbackData
from aiogram.types import CallbackQuery
# Define a callback data object
class SubsCommand(StatesGroup):
    quary = State()

async def add_subs_command(message: types.Message):
    userid = message.from_user.id
    if chech_subscription_plan(userid):
        await SubsCommand.quary.set()
    else:
        await message.reply("""Лимит для бесплатной версии не более одной ссылки.
          Оформите подписку для увеличения лимита\n""")
        return
    await message.reply("Введите запрос\n")

async def add_quary_handler(message: types.Message, state: FSMContext):
    quary=parse_quary(message.text)
    # search_engine = GoogleSearch()
    # store=JsonSubsStore(r"D:\PProjects\GoogleSubscribe\results.json")
    sub=SearchSubscription(quary)
    bm.sm.add_subscription(message.from_user.id,sub)
    await message.reply("Подписка добавлена\n")
    await state.finish()

async def clear(message: types.Message):
    bm.sm.clear_subscriptions(message.from_user.id)
    await message.reply("All clear", reply=False)
    

async def show_subscriptions_handler(message: types.Message):
    user_id = message.from_user.id
    subscriptions = bm.sm.get_subscriptions(user_id)
    if not subscriptions:
        await message.reply("You don't have any subscriptions yet.")
        return

    keyboard = types.InlineKeyboardMarkup()
    for sub in subscriptions:
        button = types.InlineKeyboardButton(text=sub.query, callback_data=f"show_sub:{sub.query}")
        button_x = types.InlineKeyboardButton(text="X", callback_data=f"delete_sub:{sub.query}")
        keyboard.add(button, button_x)
        # keyboard.add(button_x)

    await message.reply("Your subscriptions:", reply_markup=keyboard)

async def delete_subscription(query: CallbackQuery):
    user_id = query.from_user.id
    query_data = query.data.split(":")
    sub_query = query_data[1]
    user_id = query.from_user.id
    subscriptions = bm.sm.get_subscriptions(user_id)
    for sub in subscriptions:
        if sub.query == sub_query:
            bm.sm.remove_subscription(user_id, sub)
            await query.answer("Subscription removed.")
            break
    else:
        await query.answer("Subscription not found.")
            
def chech_subscription_plan(userid):
    return True
def parse_quary(quary):
    return quary
def register_handlers(dp:Dispatcher):
    dp.register_message_handler(add_subs_command,commands=['add'])
    dp.register_message_handler(add_quary_handler,state=SubsCommand.quary)
    dp.register_message_handler(show_subscriptions_handler, commands=['show'])
    dp.register_message_handler(clear, commands=['clear'])
    dp.register_callback_query_handler(delete_subscription, lambda c: c.data.startswith("delete_sub:"))