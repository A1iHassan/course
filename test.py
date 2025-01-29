class pharmacy_items:
    # class properties
    available = []

    def __init__(self, name, quantity, expiration, price):
        self.name = name
        self.cuantity = quantity
        self.expiration = expiration
        self.price = price
        for i in range(len(pharmacy_items.needed)):
            if name == pharmacy_items.needed[i]:
                pharmacy_items.needed.pop(i)
        pharmacy_items.available.append({"name": name, "quantity": quantity, "price": price})

    @classmethod
    def sell(cls, name):
        pass

