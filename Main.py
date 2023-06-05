
from Item import Item
from Phone import Phone


ph = Phone("Samsung", 200, 3)

ph.apply_increment(0.2)

print(ph.price)

ph.sendMail()
print(ph.is_integer(123))