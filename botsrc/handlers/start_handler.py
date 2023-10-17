import logging
from botsrc.bot import BotManager as bm
from aiogram import types,Dispatcher
from aiogram.types import ChatActions


async def start_command(message: types.Message):
    await message.reply("Вас приветсвтует GoogleSearchSubscribeBot!\n")


def register_handlers(dp:Dispatcher):
    dp.register_message_handler(start_command,commands=['start'])