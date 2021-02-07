from Models.Ingredient import Ingredient


# Beverage Class for every beverage and the ingredients
class Beverage:
    def __init__(self, beverage_name):
        self.beverage_name = beverage_name
        self.ingredients = {}

    def add_ingredient(self, name, qty):
        ingredient = Ingredient(name, qty)
        self.ingredients[name] = ingredient

    def get_ingredient_quantity(self, name):
        if name not in self.ingredients:
            raise Exception(name + " ingredient does not exist in beverage : " + self.beverage_name)
        return self.ingredients[name].get_quantity()

    def __str__(self):
        return self.beverage_name + " : " + str(self.ingredients)

    def __repr__(self):
        return self.beverage_name + " : " + str(self.ingredients)
