
# Utility class to make coffee/beverage
class MakeDrink:
    #  Picks beverage to be processed from the queue
    @staticmethod
    def get_drink(coffee_queue):

        while True:
            beverage, inventory = coffee_queue.get()

            try:
                inventory.consume_inventory(beverage)

            except Exception as e:
                print("Error occurred in processing {} with error {}".format(beverage.beverage_name, e))

            coffee_queue.task_done()
