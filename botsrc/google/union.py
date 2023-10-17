from googleapiclient.discovery import build
import json
from icecream import ic
class SearchEngine:
    def __init__(self):
        pass

    def search(self, query,num=None, date_restrict=None):
        print(f"Searching: {query}" )

class GoogleSearch(SearchEngine):
    def __init__(self):
        self.service = build('customsearch', 'v1', developerKey='AIzaSyB5mCuEoYZ3BYhfk_hOdSGejEEXjVhnz8E')

    def search(self, query,num=None, date_restrict=None):
        # Perform a Google search
        res = self.service.cse().list(q=query, cx='e4af4deb1e26646f8',num=num,dateRestrict=date_restrict).execute()
        ic(res)
        return res.get('items', [])

#%%
# import schedule

# job1 = schedule.every().day.at("09:00").do(check_new_results)





class SearchSubscription:
    def __init__(self, user_id, query, search_engine:SearchEngine, date_range = 'd7',result_num=10):
        self.user_id = user_id
        self.query = query
        self.date_range = date_range # Default timer value
        self.last_results = []
        self.search_engine = search_engine
        self.result_num=result_num

    def load_last_results(self):
        try:
            with open('results.json', 'r',encoding="utf-8") as file:
                self.last_results = json.load(file)
        except FileNotFoundError:
            self.last_results = []

    def save_results(self,results):
        with open('results.json', 'w',encoding="utf-8") as file:
            json.dump(results, file)

    def update_results(self):
        # Perform a Google search
        results = self.search_engine.search(self.query,num=self.result_num,date_restrict=self.date_range)
        # Identify new links
        self.load_last_results()

       
        new_links = [item['link'] for item in results if item['link'] not in self.last_results]
        if new_links:
            # send_to_user()
            self.last_results.extend(new_links) 

        self.save_results(self.last_results)
        # Return the new links
        return new_links


# from bot import bot

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = {}

    def add_subscription(self, user_id, subscription):
        # Create a new subscription
        self.subscriptions[user_id] = subscription

    def set_timer(self, user_id, timer):
        pass
        # # Set the timer for the subscription
        # self.subscriptions[user_id].timer = timer
    def send_updates(self):
        for user_id, subscription in self.subscriptions.items():
            new_links = subscription.update_results()
            print(f"user_id:{user_id}", f"new_links: {new_links}")
            # if new_links:
            #     await bot.send_message(subscription.user_id, '\n'.join(new_links))
    # async def send_updates(self):
    #     # Send updates for all subscriptions
    #     for subscription in self.subscriptions.values():
    #         new_links = subscription.update_results()
    #         # if new_links:
    #         #     await bot.send_message(subscription.user_id, '\n'.join(new_links))


