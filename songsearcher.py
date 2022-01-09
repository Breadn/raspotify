from lxml import html
import requests

class SongSearcher:

    MAX_RESULTS = 5

    def __init__(self, query_base):
        self.query_base = query_base
        self.response = None
        self.results = None
        self.select_info = {
            "title":None,
            "ytID":None,
            "duration":None,
            "views":None
        }
        print(f"Initialized SongSearcher with base query: {self.query_base}")
    
    def _update_response(self, query):
        self.response = requests.get(f"{self.query_base}{query.replace(' ', '+')}")

    def search(self, keywords):
        self._update_response(keywords)
        tree = html.fromstring(self.response.content)
        self.results = tree.xpath('//*[@id="video-title"]')
        print(self.results)






