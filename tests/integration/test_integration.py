import unittest
import json
from CoffeeMachine import CoffeeMachine


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.json_obj = None
        with open("fixtures/sampleJsonInput.json", "r") as read_file:
            self.json_obj = json.load(read_file)
        self.CoffeeMachineTestObj = CoffeeMachine(self.json_obj)
        self.CoffeeMachineTestObj.initialize_inventory_beverages()

    def test_correct_outlet_size(self):
        self.assertEqual(self.CoffeeMachineTestObj.outlets_count, 3)

    def test_correct_inventory_created(self):
        inventory = self.CoffeeMachineTestObj.inventory
        self.assertEqual(len(inventory.ingredients), 5)
        total_ingredient_qty = 0
        for ingredient in inventory.ingredients:
            total_ingredient_qty += inventory.ingredients[ingredient].qty
        self.assertEqual(total_ingredient_qty, 1300)

class Test2(unittest.TestCase):
    def setUp(self):
        self.json_obj = None
        with open("fixtures/sample2.json", "r") as read_file:
            self.json_obj = json.load(read_file)
        self.CoffeeMachineTestObj = CoffeeMachine(self.json_obj)
        self.CoffeeMachineTestObj.initialize_inventory_beverages()

    def test_correct_outlet_size(self):
        self.assertEqual(self.CoffeeMachineTestObj.outlets_count, 5)

    def test_correct_inventory_created(self):
        inventory = self.CoffeeMachineTestObj.inventory
        self.assertEqual(len(inventory.ingredients), 6)
        total_ingredient_qty = 0
        for ingredient in inventory.ingredients:
            total_ingredient_qty += inventory.ingredients[ingredient].qty
        self.assertEqual(total_ingredient_qty, 2000)

class Test3(unittest.TestCase):
    def setUp(self):
        self.json_obj = None
        with open("fixtures/sample3.json", "r") as read_file:
            self.json_obj = json.load(read_file)
        self.CoffeeMachineTestObj = CoffeeMachine(self.json_obj)
        self.CoffeeMachineTestObj.initialize_inventory_beverages()

    def test_correct_outlet_size(self):
        self.assertEqual(self.CoffeeMachineTestObj.outlets_count, 3)

    def test_correct_inventory_created(self):
        inventory = self.CoffeeMachineTestObj.inventory
        self.assertEqual(len(inventory.ingredients), 6)
        total_ingredient_qty = 0
        for ingredient in inventory.ingredients:
            total_ingredient_qty += inventory.ingredients[ingredient].qty
        self.assertEqual(total_ingredient_qty, 1600)

if __name__ == '__main__':
    unittest.main()
