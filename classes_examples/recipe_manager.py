class Recipe:
    # Class property
    all_recipes = []

    # Constructor
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        Recipe.all_recipes.append(self)

    # Instance Methods
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def check_ingredient(self, ingredient):
        return ingredient in self.ingredients

    @classmethod
    def find_recipes_by_ingredient(cls, ingredient):
        all_who_has_it = []
        for i in cls.all_recipes:
            for j in i.ingredients:
                if j == ingredient:
                    all_who_has_it.append(str(i))
        return all_who_has_it

    @staticmethod
    def is_valid_ingredient(ingredient):
        return isinstance(ingredient, str) and len(ingredient) > 0
    
    def __str__(self):
        return "{ " + f"name: {self.name}, ingredients: {self.ingredients}" + " }"

# Example Usage:
recipe1 = Recipe("Pasta")
recipe1.add_ingredient("Tomato")
recipe2 = Recipe("Pizza")
recipe2.add_ingredient("Tomato")
tomato_recipes = Recipe.find_recipes_by_ingredient("Tomato")
print(tomato_recipes)  # Output: ['Pasta', 'Pizza']