from lxml import html
import requests

class SongSearcher:

    MAX_RESULTS = 5
    query_base = "https://www.youtube.com/results?search_query="

    def __init__(self):
        self.response
        self.results
        self.select_info = {
            "title":None,
            "ytID":None,
            "duration":None,
            "views":None
        }
    
    def _update_response(self, query):
        self.response = requests.get(f"{self.query_base}{query.replace(' ', '+')}")

    def search(self, keywords):
        self._update_response(keywords)
        tree = html.fromstring(self.response.content)
        self.results = tree.xpath('//*[@id="video-title"]')
        print(self.results)






