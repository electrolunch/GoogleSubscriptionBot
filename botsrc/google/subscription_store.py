from botsrc.google.subscription import SearchSubscription
import json
from icecream import ic
class SubsStore:
    def __init__(self):
        pass
    
    def save_subscription(self, user_id, subscription:SearchSubscription):
        pass

    def load_subscriptions(self, user_id):
        pass



class JsonSubsStore(SubsStore):
    def __init__(self, path):
        self.path = path
        self.subscriptions = []
 

    def load_subscriptions(self, user_id):
        # ic(self.path)
        with open(self.path, 'r') as file:
            text = file.read()
            if text=='':
                return []
            else:
                data = json.loads(text)
        # ic(data)
        subs_str=data[str(user_id)]
        subs=[]
        for sub_str in subs_str:
            sub = json.loads(sub_str)
            # ic(sub)
            subs.append(SearchSubscription.fromJSON(sub))
        # ic(subs)
        return subs

    def save_subscription(self, user_id, subscription:SearchSubscription):
        json_string = json.dumps(subscription.toJSON())
        # read json file result.json as dict
        with open(self.path, 'r') as file:
            fileread=file.read()
            if fileread =='':
                data={}
            else:
                data = json.loads(fileread)
        ic(data)
        ic(user_id)
        if data.get(str(user_id)):
            data[str(user_id)].append(json_string)
        else:
            data[str(user_id)]=[json_string]
        # WRITE TO file
        with open(self.path, 'w',encoding="utf-8") as file:
            json.dump(data, file)

   