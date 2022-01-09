from lxml import html
import requests
import re   # I'm sorry, I've relented and am going to feed my soul to cthulhu

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
        htmlstr = self.response.text
        ytIDs = re.findall(r'watch\?v=(\S{11})', htmlstr)
        ytTitles_raw = re.findall(r'\"title\":{\"runs\":\[{\"text\":\".+?(?=")', htmlstr)
        
        # TODO: limit to max 5 and obtain metadata

        # TODO: encapsulate into select fn
        self.select_info.update("title", re.findall(r'"text":.+', ytTitles_raw[0])[0].split('":"')[1])
        self.select_info.update("ytID", ytIDs[0])






