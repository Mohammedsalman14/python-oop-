import csv


class Item:

    pay_rate = 0.8
    all = []

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Items('{self.name}',{self.price},{self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get(
                    'price')),
                quantity=int(item.get('quantity')))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: float):
        # Checking validation to the Received Arguments

        assert price >= 0, f"price {price} is not greater than zero"
        assert quantity >= 0, f"qantity {quantity} is not greater than zero"

        # Assigning parms to self
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)


phone1 = Phone("apple", 500, 5)
print(phone1.all)
