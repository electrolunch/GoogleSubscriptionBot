from botsrc.google.subscription import SearchSubscription
class SearchEngine:
    def __init__(self):
        pass

    def search(self, sub:SearchSubscription):
        print(f"Searching: {sub.query}" )