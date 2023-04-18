import csv


class Item:

    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

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
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):

        super().__init__(name, price, quantity)

        # Checking validation to the Received Arguments
        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater than zero"

        # Assigning parms to self

        self.broken_phones = broken_phones
        self.all.append(self)

    def showbroken_phones(self):
        return self.broken_phones


ph = Phone("Samsung", 200, 3)
print(ph.calculate_total_price())
