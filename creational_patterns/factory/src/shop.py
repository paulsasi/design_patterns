from abc import ABC, abstractmethod
import product

class Shop:

    @abstractmethod
    def create_product(self, price: int):
        pass


    def display_info(self):
        product = self.create_product(price=100)
        product.apply_discount()
        price = product.get_price()
        print(f"Price: {price}")


class CenterShop(Shop):

    def create_product(self, price: int):
        return product.Shirt(price=price)

class CountryShop(Shop):

    def create_product(self, price: int):
        return product.Shoe(price=price)