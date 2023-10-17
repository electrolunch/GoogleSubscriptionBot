from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import logging
from botsrc.bot import BotManager as bm
from aiogram import types,Dispatcher
from aiogram.types import ChatActions
from botsrc.google.google_search import GoogleSearchEngine
from botsrc.google.subscription import SearchSubscription
from botsrc.google.subscription_store import JsonSubsStore

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
    await state.finish()

def chech_subscription_plan(userid):
    return True
def parse_quary(quary):
    return quary
def register_handlers(dp:Dispatcher):
    dp.register_message_handler(add_subs_command,commands=['add'])
    dp.register_message_handler(add_quary_handler,state=SubsCommand.quary)