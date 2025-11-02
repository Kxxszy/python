class Potato:
    price = 5
    def __init__(self, content):
        self.content = content


obj1 = Potato ("gingjiao")
print (obj1. price)
print (Potato.price)
obj1. price = 10
print (obj1.price)
print (Potato.price)