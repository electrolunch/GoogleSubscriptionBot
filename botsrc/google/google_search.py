from botsrc.google.subscription import SearchSubscription
from googleapiclient.discovery import build
from botsrc.google.search import SearchEngine
from icecream import ic


class SearchResult:
    def __init__(self,res:dict):
        self.res=res
        self.links = []
        for result in res['items']:
            self.links.append(result['link'])

class GoogleSearchEngine(SearchEngine):
    def __init__(self):
        self.service = build('customsearch', 'v1', developerKey='AIzaSyB5mCuEoYZ3BYhfk_hOdSGejEEXjVhnz8E')

    def search(self, sub:SearchSubscription)->SearchResult:
        # Perform a Google search
        # ic(sub.query)
        # ic(sub)
        res = self.service.cse().list(q=sub.query, cx='e4af4deb1e26646f8',num=sub.num,dateRestrict=sub.date_restrict).execute() #pylint: disable=no-member
        # ic(res)
        return SearchResult(res)
        # return links
    
        

if __name__ == '__main__':
    g = GoogleSearchEngine()
    print(g.search('python'))