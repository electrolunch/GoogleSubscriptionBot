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

    def clear_subscriptions(self,user_id):
        pass

    def remove_subscription(self,user_id,subscription):
        pass

class JsonSubsStore(SubsStore):
    def __init__(self, path):
        self.path = path
        self.subscriptions = []
 

    def load_subscriptions(self, user_id)-> list[SearchSubscription]:
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
        # ic(data)
        # ic(user_id)
        if data.get(str(user_id)):
            data[str(user_id)].append(json_string)
        else:
            data[str(user_id)]=[json_string]
        # WRITE TO file
        with open(self.path, 'w',encoding="utf-8") as file:
            json.dump(data, file)

    def save_subscriptions(self, user_id, subscription:list[SearchSubscription]):
        json_list=[]
        for sub in subscription:
            json_list.append(json.dumps(sub.toJSON()))
        # json_string = json.dumps(subscription.toJSON())
        # read json file result.json as dict
        with open(self.path, 'r') as file:
            fileread=file.read()
            if fileread =='':
                data={}
            else:
                data = json.loads(fileread)
        # ic(data)
        # ic(user_id)
        if data.get(str(user_id)):
            for json_string in json_list:
                #check if user already has subs
                if json_string not in data[str(user_id)]:
                    data[str(user_id)].append(json_string)
        else:
            data[str(user_id)]=json_list
        # WRITE TO file
        with open(self.path, 'w',encoding="utf-8") as file:
            json.dump(data, file)
    
    def clear_subscriptions(self, user_id):
        with open(self.path, 'r') as file:
            fileread=file.read()
            if fileread =='':
                data={}
            else:
                data = json.loads(fileread)
                
        if data.get(str(user_id)):
            data[str(user_id)].clear()

        with open(self.path, 'w',encoding="utf-8") as file:
            json.dump(data, file)
    
    def remove_subscription(self, user_id, sub_query):
        subs=self.load_subscriptions(user_id)
        ic(subs)
        # ic(subscription)

        subs=[sub for sub in subs if sub.query!=sub_query]
        ic(subs)
        json_list=[]
        for sub in subs:
            json_list.append(json.dumps(sub.toJSON()))

        data={}
        data[str(user_id)]=json_list

        with open(self.path, 'w',encoding="utf-8") as file:
            json.dump(data, file)