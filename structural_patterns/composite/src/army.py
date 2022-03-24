from abc import ABC, abstractmethod
from dataclasses import dataclass

class ArmyEntity(ABC):

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Soldier(ArmyEntity):
    def __init__(self, name, age) -> None:
        self.name :str  = name
        self.age: int = age

    def get_age(self):
        return self.age

    def attack(self):
        print(f"Ataaaack {self.name}")


class Batallion(ArmyEntity):
    def __init__(self, children) -> None:
        self.children : tuple[ArmyEntity] = children

    def get_age(self):
        return sum([c.get_age() for c in self.children])

    def attack(self):
        for c in self.children:
            c.attack()