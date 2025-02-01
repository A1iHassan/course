class Car:

    # Constructor
    def __init__(self, model):
        self.model = model
        self.is_rented = False

    # Instance Methods
    def rent(self):
        if not self.is_rented:
            self.is_rented = True
        else:
            print("Car is already rented.")

    def return_car(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print("Car is not rented.")

    @staticmethod
    def is_valid_model(model):
        return isinstance(model, str) and len(model) > 0

# Example Usage:
car = Car("Toyota Camry")
car.rent()
print(car.is_rented)  # Output: True
