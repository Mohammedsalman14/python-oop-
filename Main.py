

class Item:

    pay_rate=0.8

    def __init__(self, name: str, price: float, quantity: float):
        # Checking validation to the Received Arguments

        assert price >=0,f"price {price} is not greater than zero"
        assert quantity >=0,f"qantity {quantity} is not greater than zero"

        # Assigning parms to self
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity


item1 = Item("Phone", 100, 5)


print("Item1: ", item1.calculate_total_price())

item2 = Item("Laptop", 1000, 3)

print("Item2: ", item2.calculate_total_price())

print(Item.__dict__) #All the attributes for Class level
print(item1.__dict__) #All the attributes for Instance level

# print(2*"salman")
