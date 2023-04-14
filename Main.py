import csv342

class Item:

    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: float):
        # Checking validation to the Received Arguments

        assert price >= 0, f"price {price} is not greater than zero"
        assert quantity >= 0, f"qantity {quantity} is not greater than zero"

        # Assigning parms to self
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    def __repr__(self) -> str:
        return f"Items('{self.name}',{self.price},{self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 1000, 1)
item4 = Item("Charger", 100, 2)

print(Item.all)


