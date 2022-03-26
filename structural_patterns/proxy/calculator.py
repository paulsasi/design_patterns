from abc import ABC, abstractmethod
from math import factorial

class CalculatorService(ABC):

    @abstractmethod
    def factorial(self, number: int):
        pass

    @abstractmethod
    def summation(self, number: int):
        pass



class Calculator(CalculatorService):
    
    def factorial(self, number: int):
        factorial = 1
        for i in range(1, number):
            factorial = factorial * i
        return factorial

    def summation(self, number: int):
        return sum([i for i in range(1, number)])


class CalculatorProxy(CalculatorService):

    def __init__(self, service):
        self.service : Calculator = service
        self.factorial_cache : dict = {}
        self.summation_cache : dict = {}

    def factorial(self, number: int):
        if number not in self.factorial_cache:
            result = self.service.factorial(number)
            self.factorial_cache[number] = result
        else:
            result = self.factorial_cache[number]
        return result

    def summation(self, number: int):
        if number not in self.summation_cache:
            result = self.service.summation(number)
            self.summation_cache[number] = result
        else:
            result = self.summation_cache[number]
        return result

    
