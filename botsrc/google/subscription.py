from pydantic import BaseModel


class SearchSubscription(BaseModel):
    # user_id: int
    query: str
    date_restrict: str
    num:int | None
    search_engine: str
    def __init__(self, query,date_restrict='d7',num=None,search_engine = "google"):
        super().__init__(query=query,date_restrict=date_restrict,num=num,search_engine=search_engine)
        # self.user_id = user_id
        self.query = query
        self.date_restrict = date_restrict 
        self.num=num
        self.search_engine = search_engine
        # self.last_results = []
        # self.search_engine = search_engine
        # self.result_num=result_num
        # self.store = store
    def toJSON(self):
        return {
            "query":self.query,
            "date_restrict":self.date_restrict,
            "num":self.num,
            "search_engine":self.search_engine
            
        }
    @staticmethod
    def fromJSON(json_data):
        subscription = SearchSubscription.parse_obj(json_data)
        return subscription
    
    def __str__(self):
        return f"SearchSubscription(\
                    query='{self.query}',\
                    date_restrict='{self.date_restrict}',\
                    num={self.num}, \
                    search_engine='{self.search_engine}')"
    # def load_last_results(self):
    #     try:
    #         self.last_results = self.store.load_last_results(self.query)
    #     except FileNotFoundError:
    #         self.last_results = []

    # def save_results(self,results):
    #     try:
    #         self.store.save_last_results(self.query,results)
    #     except FileNotFoundError:
    #         self.last_results = []

    # def update_results(self):
    #     # Perform a Google search
    #     results = self.search_engine.search(self.query,num=self.result_num,date_restrict=self.date_range)
    #     # Identify new links
    #     self.load_last_results()

       
    #     new_links = [item['link'] for item in results if item['link'] not in self.last_results]
    #     if new_links:
    #         # send_to_user()
    #         self.last_results.extend(new_links) 

    #     self.save_results(self.last_results)
    #     # Return the new links
    #     return new_links
