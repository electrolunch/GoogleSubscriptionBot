from botsrc.google.google_search import SearchResult
from botsrc.google.search import SearchEngine
from botsrc.google.subscription import SearchSubscription
from botsrc.google.subscription_store import SubsStore
# from bot import bot
from icecream import ic
from services.results_store import ResultsStore
class SubscriptionManager:
    def __init__(self,search_engines:dict[str, SearchEngine],store:SubsStore,results_store:ResultsStore):
        self.search_engines:SearchEngine = search_engines
        self.store:SubsStore = store
        self.results_store:ResultsStore = results_store
        self.subscriptions:SearchSubscription = {}

    def add_subscription(self, user_id, subscription):
        self.store.save_subscription(user_id,subscription)
        # Create a new subscription
        # print(user_id)
        # if self.subscriptions.get(user_id):
        #     self.subscriptions[user_id].append(subscription)
        # else:
        #     self.subscriptions[user_id]=[subscription]
    def get_subscriptions(self, user_id):
        return self.store.load_subscriptions(user_id)
        # return self.subscriptions.get(user_id, [])

    def set_timer(self, user_id, timer):
        pass
        # # Set the timer for the subscription
        # self.subscriptions[user_id].timer = timer
    def get_updates(self,user_id):
        print(user_id)
        # ic(self.store)
        user_subs=self.store.load_subscriptions(user_id)
        # ic(user_subs)
        updates={}

        subscription:SearchSubscription
        for subscription  in user_subs:
            search_engine:SearchEngine=self.search_engines[subscription.search_engine]
            result:SearchResult=search_engine.search(subscription)
            ic(result)
            new_links = self.results_store.update_results(subscription,result.links,user_id)
            updates[subscription.query]=new_links
        return updates
    def clear_subscriptions(self,user_id):
        self.store.clear_subscriptions(user_id)
    def remove_subscription(self,user_id,sub_query):
        self.store.remove_subscription(user_id,sub_query)
        # self.subscriptions[user_id]=[]
    # async def send_updates(self):
    #     # Send updates for all subscriptions
    #     for subscription in self.subscriptions.values():
    #         new_links = subscription.update_results()
    #         # if new_links:
    #         #     await bot.send_message(subscription.user_id, '\n'.join(new_links))
