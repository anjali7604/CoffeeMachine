import threading
from Models.Ingredient import Ingredient



# Refills/Consumes inventory by taking lock on the object to avoid race conditions
class Inventory:
    # class variable LOW -the minimum quantity to indicate ingredient is running low
    LOW = 300

    def __init__(self):
        self.lock = threading.Lock()
        self.ingredients = {}

    def add_ingredient(self, name, qty):
        ingredient = Ingredient(name, qty)
        self.ingredients[name] = ingredient

    # get ingredient quantity of the inventory for given ingredient
    def get_ingredient_quantity(self, name):
        if name not in self.ingredients:
            raise Exception(name + " ingredient is not available ")
        return self.ingredients[name].get_quantity()

    def consume_ingredient(self, ingredient, req_qty):
        self.ingredients[ingredient].consume_qty(req_qty)

    # Lock the Inventory object so that at a time only one thread can access it to avoid race conditions
    def consume_inventory(self, beverage):
        with self.lock:

            # check if all ingredients are available
            for ingredient in beverage.ingredients:

                try:
                    if ingredient not in self.ingredients:
                        print("{} cannot be prepared because item {} is not available"
                              .format(beverage.beverage_name, ingredient))
                        return

                except Exception as e:
                    print(e)
                    return

            # check if all ingredients are available in sufficient amount
            for ingredient in beverage.ingredients:

                try:
                    # check if ingredient quantity in inventory is less than required quantity to prepare beverage
                    if self.get_ingredient_quantity(ingredient) < beverage.get_ingredient_quantity(ingredient):
                        print("{} cannot be prepared because item {} is not sufficient"
                              .format(beverage.beverage_name, ingredient))
                        self.check_inventory()
                        return
                except Exception as e:
                    print(e)
                    return
            # If we reached here means all the ingredients are available in sufficient quantity to make the beverage
            # So update the inventory quantity after consuming required amount
            for ingredient in beverage.ingredients:
                try:
                    req_qty = beverage.get_ingredient_quantity(ingredient)

                    self.consume_ingredient(ingredient, req_qty)

                except Exception as e:
                    print(e)
                    return

            print("{} is prepared".format(beverage.beverage_name))
            self.check_inventory()
            return

    # Check the inventory if it running low
    def check_inventory(self):
        low_ingredients = []

        for ingredient in self.ingredients:
            if self.get_ingredient_quantity(ingredient) <= Inventory.LOW:
                low_ingredients.append(self.ingredients[ingredient])

        if len(low_ingredients) > 0:
            print("ALERT!! Ingredients {} are running low".format([ingrt.name for ingrt in low_ingredients]))
            s = input("Do you want to refill the  Ingredients?:y/n \n".format(ingredient))
            print("Entered input is s: " + s)
            if s.upper() == 'Y':
                self.refill(low_ingredients)

    # Refill the inventory when running low
    def refill(self, low_ingredients):
        for ingredient in low_ingredients:
            s = input("Do you want to refill {}?:y/n \n".format(ingredient.name))
            if s.upper() == 'Y':
                qty = input("Enter quantity to be refilled:\n")
                if int(qty) > 0:
                    self.update_inventory(ingredient.name, int(qty))

    def update_inventory(self, ingredient, quantity):
        self.ingredients[ingredient].refill_quantity(quantity)
