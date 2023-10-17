
from abc import ABC, abstractmethod
import json

from botsrc.google.subscription import SearchSubscription

class ResultsStore(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def update_results(self, subscription:SearchSubscription, results):
        pass

class JsonResultsStore(ResultsStore):
    def __init__(self, path):
        self.path = path
        # self.results = {}
    
    def update_results(self, subscription: SearchSubscription, results,user_id):
        data = self.read_data()
        # user_data=data[str(user_id)]
        if data.get(str(user_id)):
            user_data=data[str(user_id)]
        else:
            user_data={}

        new_links = []
        if user_data.get(subscription.query):
            for link in results:
                if link not in user_data[subscription.query]:
                    new_links.append(link)
                    user_data[subscription.query].append(link)
        else:
            user_data[subscription.query] = results
            new_links = results
        
        data[str(user_id)]=user_data
        self.write_data(data)
        return new_links

    def write_data(self, data):
        with open(self.path, 'w',encoding="utf-8") as file:
            json.dump(data, file)

    def read_data(self):
        with open(self.path, 'r',encoding="utf-8") as file:
            fileread=file.read()
            if fileread=='':
                data={}
            else:
                data = json.loads(fileread)
        return data
