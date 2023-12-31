from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from botsrc.google.google_search import GoogleSearchEngine
from botsrc.google.subscription_manager import SubscriptionManager
from botsrc.google.subscription_store import JsonSubsStore
from botsrc.google.union import GoogleSearch
from services.results_store import JsonResultsStore
import getpass
# tok=getpass.getpass("Введите Telegram bot token: ")
tok="6237416859:AAH7RYinJjgOaA1YlVWKOlJlExd9Trbeul8"
class BotManager:
    bot=None
    dp=None
    sm:SubscriptionManager = None
    storage = MemoryStorage()
    @classmethod
    def bot_init(cls,token):
        tok = token
        cls.bot = Bot(token=tok)
        cls.dp = Dispatcher(cls.bot,storage=cls.storage)
        store=JsonSubsStore(r"user_subs.json")
        results_store=JsonResultsStore(r"user_results.json")
        cls.sm = SubscriptionManager(search_engines={'google':GoogleSearchEngine()},store=store,results_store=results_store)



