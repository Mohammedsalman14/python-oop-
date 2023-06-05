import csv


class Item:

    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price+self.__price*increment_value

    def calculate_total_price(self):
        return self.price*self.quantity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}',{self.price},{self.quantity})"

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

    def __send(self):
        pass
    def __prepare_body(self):
        pass
    def __connect(self):
        pass
    def sendMail(self):
        self.__send()
        self.__prepare_body()
        self.__connect()
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
