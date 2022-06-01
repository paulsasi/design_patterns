from dataclasses import dataclass
import scraper
import json

@dataclass
class Adapter:

    adaptee: scraper.Scraper

    def get_data(self) -> str:
        data = self.adaptee.get_data()
        return json.dumps({key: value for key, value in data})