
import copy
from typing import List

class Configuration:

    def __init__(self, urls: List[str], hosts: List[List[str]]):
        self.urls = urls
        self.hosts = hosts

    def __copy__(self):
        return Configuration(urls=copy.copy(self.urls), hosts=copy.copy(self.hosts))

    def __deepcopy__(self, memo=None):
        return Configuration(urls=copy.deepcopy(self.urls), hosts=copy.deepcopy(self.hosts))

