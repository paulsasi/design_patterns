from abc import ABC, abstractmethod
from dataclasses import dataclass
import database


@dataclass
class Scrapper(ABC):

    variable: str
    db: database.Database

    @abstractmethod
    def scrap_time_period(self, start: int, end: int):
        pass


class WindDir(Scrapper):

    def __init__(self, variable: str, db: database.Database):
        super().__init__(variable, db)

    def scrap_time_period(self, start: int, end: int):
        return "WInDir scraaaaaped:     " + self.variable


class WindSpeed(Scrapper):

    def __init__(self, variable: str, db: database.Database):
        super().__init__(variable, db)

    def scrap_time_period(self, start: int, end: int):
        return "WInSpeed scraaaaaped:     " + self.variable

