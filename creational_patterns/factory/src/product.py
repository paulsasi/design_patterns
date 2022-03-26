from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, price):
        self.price :int = price

    def get_price(self):
        return self.price

    @abstractmethod
    def apply_discount(self):
        pass

class Shirt(Product):

    def __init__(self, price):
        self.discount_ratio : float = 0.2
        super().__init__(price)

    def apply_discount(self):
        self.price = (1 - self.discount_ratio) * self.price
        

class Shoe(Product):

    def __init__(self, price):
        self.discount_ratio : float = 0.5
        super().__init__(price)

    def apply_discount(self):
        self.price = (1 - self.discount_ratio) * self.price