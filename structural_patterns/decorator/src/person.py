from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Person:
    name: str
    age: int

    @abstractmethod
    def describe(self) -> str:
        pass



class Primitive(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def describe(self) -> str:
        name = self.name
        age = self.age
        return "PRIMITIVE"


class Decorator(Person):

    _person: Person = None

    def __init__(self, person: Person):
        self._person = person

    @property
    def person(self) -> Person:
        return self._person

    def describe(self) -> str:
        return self._person.describe()



class Industry(Decorator):

    def describe(self) -> str:
        return "INDUSTRY" + self.person.describe()


class Teacher(Decorator):

    def describe(self) -> str:
        return "TEACHER" + self.person.describe()


class Scientist(Decorator):

    def describe(self) -> str:
        return "SCIENTIST" + self.person.describe()