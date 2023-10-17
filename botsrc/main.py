from botsrc.bot import BotManager as bm
from aiogram import  executor
import logging
from botsrc.handlers import start_handler,help_handler,search_result_handler,add_subs_handler
logging.basicConfig(level=logging.INFO)






def main():
    logging.info('Start main')
    # token = input('Input token: ')
    token = "6237416859:AAH7RYinJjgOaA1YlVWKOlJlExd9Trbeul8"
    bm.bot_init(str(token))
    start_handler.register_handlers(bm.dp)
    # help_handler.register_handlers(bm.dp)
    search_result_handler.register_handlers(bm.dp)
    add_subs_handler.register_handlers(bm.dp)
    logging.debug('Bot started')
    executor.start_polling(bm.dp, skip_updates=True,timeout=100)

    # BotManager.dp.start_polling(BotManager.dp, skip_updates=True,timeout=100)



if __name__ == '__main__':
    main()