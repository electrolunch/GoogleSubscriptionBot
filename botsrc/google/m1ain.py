#%%
import json

with open(r'D:\PProjects\GoogleSubscribe\user_subs.json', 'r') as file:
    data = json.load(file)

# import google_search as gs
# import subscription as sb
# import subscription_manager as sbm
# #%%
# google=gs.GoogleSearchEngine()
# #%%
# subscription=sb.SearchSubscription(
#     user_id=123,
#     query="Australia",
#     search_engine=google,
#     date_range="d1"
#     )

# subscription_manager=sbm.SubscriptionManager()

# subscription_manager.add_subscription(
#     user_id=123,
#     subscription=subscription
#     )

# #%%
# subscription_manager.send_updates()
# results=google.search('maven',num=10,date_restrict='d7')

# with open('results.json', 'w') as file:
#     json.dump(results, file)
# #%%
# for item in results:
#     print(item['title'])
#     print(item['link'])
#     print('---')
# %%
