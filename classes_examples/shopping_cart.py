class ShoppingCart:
    # Class property
    total_carts = 0
    carts = {}

    # Constructor
    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1
        self.cart_id = ShoppingCart.total_carts
        ShoppingCart.carts[self.cart_id] = self

    # Instance Methods
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def view_cart(self):
        print(f"Cart {self.cart_id}: {self.items}")

    @classmethod
    def get_cart_by_id(cls, cart_id):
        return cls.carts.get(cart_id, None)

    @staticmethod
    def is_valid_item(item):
        return isinstance(item, str) and len(item) > 0
    
    def __str__(self):
        return "{ cart: " + f"{self.cart_id}, items: {self.items}" + " }"

# Example Usage:
cart1 = ShoppingCart()
cart1.add_item("Apple")
cart2 = ShoppingCart.from_list(["Banana", "Orange"])
print(ShoppingCart.carts)  # Output: 2
print(ShoppingCart.get_cart_by_id(1).items)  # Output: ['Apple']
print(ShoppingCart.get_cart_by_id(1))  # Output: { cart: 1, items: ['Apple'] }
