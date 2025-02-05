class items:
    all_items = {}
    
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        items.all_items[name] = quantity

    def __str__(self):
        return f"{self.name}, {self.quantity}"

    @classmethod
    def sell(cls, name, quantity):
        for i in cls.all_items:
            if i == name:
                if cls.all_items[name] >= quantity:
                    cls.all_items[name] -= quantity
                    return 0
                return 1
        return 2
    
    @classmethod
    def stock(cls):
        i = 0
        for item in cls.all_items.values():
            i += item
        return i

    @classmethod
    def inventory(cls):
        return str(cls.all_items)

while True:
    try:
        command = input("How can I help you: ")
        if command == "add item":
            item_name = input("what is the item name: ")
            item_quantity = int(input("what is the quantity you want to add: "))
            new_item = 1
            for i in items.all_items:
                if i == item_name:
                    items.all_items[item_name] += item_quantity
                    new_item = 0
                    print("add quantity to existing item")
            if new_item == 1:
                item = items(item_name, item_quantity)
                print("add new item")
        elif command == "sell item":
            item_name = input("what is the item name: ")
            item_quantity = int(input("what is the quantity you want to sell: "))
            i = items.sell(item_name, item_quantity)
            if i == 0:
                print("item sold successfully")
            elif i == 1:
                print("no sufficient quantity")
            elif i == 2:
                print("item not found")
        elif command == "check stock":
            print(items.stock())
        elif command == "check inventory":
            print(items.inventory())
        elif command == "done":
            break
        else:
            print("command not found")
    except ValueError:
        print("quantity must be a number")