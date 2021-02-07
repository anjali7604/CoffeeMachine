# Puts all the beverages to be processed as tasks in the synchronized queue
class CoffeeProcessor:

    def __init__(self, coffee_queue, beverages, inventory):
        self.coffee_queue = coffee_queue
        self.beverages = beverages
        self.inventory = inventory

    # Put every beverage making as a task in the synchronized queue to be picked by the threads running
    def run(self):
        for beverage in self.beverages: 
            self.coffee_queue.put((beverage, self.inventory))
        self.coffee_queue.join()
