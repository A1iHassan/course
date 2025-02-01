class Pet:

    # Constructor
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    # Instance Methods
    def adopt(self):
        if not self.is_adopted:
            self.is_adopted = True
            print(f"{self.name} has been adopted!")
        else:
            print("already adopted")

    def is_puppy(self):
        return self.species == "Dog" and self.age < 2

    @staticmethod
    def is_valid_species(species):
        return species in ["Dog", "Cat", "Bird"]

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and age >= 0

# Example Usage:
pet = Pet("Buddy", "Dog", 1)
print(pet.is_puppy())  # Output: True
print(Pet.is_valid_species("Fish"))  # Output: False