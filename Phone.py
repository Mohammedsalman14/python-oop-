from Item import Item
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