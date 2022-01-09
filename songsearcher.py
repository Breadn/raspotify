from lxml import html, tostring
import requests

class SongSearcher:

    MAX_RESULTS = 5

    def __init__(self, query_base):
        self.query_base = query_base
        self.response = None
        self.results = []
        self.select_info = {
            "title":None,
            "ytID":None,
            "duration":None,
            "views":None
        }
        print(f"Initialized SongSearcher with base query: {self.query_base}")
    
    def _update_response(self, query):
        url = f"{self.query_base}{query.replace(' ', '+')}"
        print(f"Updating response with url: {url}")
        self.response = requests.get(url)

    def search(self, keywords):
        self._update_response(keywords)
        tree = html.fromstring(self.response.content)

        print(tostring(tree))

        test = tree.xpath(f'//*[@id="video-title"]/@title')
        print(test)

        for i in range(0,self.MAX_RESULTS):
            self.results.append(tree.xpath(f'(//a[@id="video-title"]/@aria-label)[{i}]'))
        print(self.results)






