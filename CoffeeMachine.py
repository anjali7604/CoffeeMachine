from Models.Beverage import Beverage
from CoffeeProcessor import CoffeeProcessor
from Models.Inventory import Inventory
from Utility.MakeDrink import MakeDrink
from threading import Thread
from queue import Queue


# Initializes inventory, beverages list and executes threads
class CoffeeMachine:

    def __init__(self, json_obj):
        self.json_obj = json_obj
        self.coffee_queue = Queue(-1)
        self.inventory = Inventory()
        self.outlets_count = 0
        self.beverages = []
        self.initialize_inventory_beverages()
        self.make_coffees()

    # creates threads equals to no. of outlets(N) to be run in parallel in daemon
    def initialize_queue(self):

        for i in range(self.outlets_count):
            t = Thread(target=MakeDrink.get_drink, args=(self.coffee_queue,))
            t.daemon = True
            t.start()
            return self.coffee_queue

    # initialize inventory and beverages to be processed
    def initialize_inventory_beverages(self):
        machine = self.json_obj["machine"]

        self.outlets_count = machine["outlets"]["count_n"]

        items = machine["total_items_quantity"]

        for ingredient in items:
            self.inventory.add_ingredient(ingredient, items[ingredient])

        beverage_list = machine["beverages"]

        beverages = []

        for bev in beverage_list:
            beverage = Beverage(bev)
            ingredient_list = beverage_list[bev]
            for ingredient in ingredient_list:
                beverage.add_ingredient(ingredient, ingredient_list[ingredient])
            beverages.append(beverage)
        self.beverages = beverages

    # create threads and execute them using synchronized queue
    def make_coffees(self):
        self.coffee_queue = self.initialize_queue()
        CoffeeProcessor(self.coffee_queue, self.beverages, self.inventory).run()
