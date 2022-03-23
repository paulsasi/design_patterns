from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Credentials:
    db: str
    user: str
    password: str
    host: str
    port: str = "5062"


@dataclass
class Database(ABC):

    credentials: Credentials

    @abstractmethod
    def execute_select_query(self, query: str):
        pass


class PostgreSql(Database):

    def __init__(self, credentials: Credentials):
        super().__init__(credentials)

    def execute_select_query(self, query: str):
        return "holaaa" + query


@dataclass
class MariaSql(Database):

    def __init__(self, credentials: Credentials):
        super().__init__(credentials)

    def execute_select_query(self, query: str):
        return "maria" + query
