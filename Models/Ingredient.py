
# class for each ingredient with its name and quantity
class Ingredient:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

    def get_quantity(self):
        return self.qty

    def consume_qty(self, req_qty):
        self.qty -= req_qty

    def refill_quantity(self,quantity):
        self.qty += quantity

    def __str__(self):
        return self.name+" : " + str(self.qty)

    def __repr__(self):
        return self.name+" : " + str(self.qty)
