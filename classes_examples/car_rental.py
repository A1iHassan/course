class Car:

    archive = {}

    # Constructor
    def __init__(self, model, serial):
        self.model = model
        self.serial = serial
        self.is_rented = False

    # Instance Methods
    def rent(self):
        if not self.is_rented and Car.archive[self.serial]:
            self.is_rented = True
        else:
            print("Car is already rented.")

    def return_car(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print("Car is not rented.")

    @classmethod
    def set_certificate(cls, car, certificate):
        if not car.is_rented:
            cls.archive[car.serial] = certificate

    @staticmethod
    def is_valid_model(model):
        return isinstance(model, str) and len(model) > 0

# Example Usage:
car = Car("Toyota Camry")
car.rent()
print(car.is_rented)  # Output: True
