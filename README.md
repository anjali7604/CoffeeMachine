Added integration tests in test_integration.py under tests/integration

To run for any Json file, run the Driver class and give input Json file
as argument when prompted for input


SOME CONSIDERATIONS AND ASSUMPTIONS:

1.) Why am I using Threads if I am taking lock on inventory?
--The objective of taking lock on whole inventory is to avoid race conditions
--We could have taken lock on just ingredients sepeartely, but in that case there are 2 scenorios:
  Case 1: Either it leads to deadlocks --Eg. Lets say my hot coffee needs hot water and hot milk
                                and my hot tea also needs hot water and hot milk
                                Now if hot coffeee takes lock on hot water and hot coffee takes lock on hot milk, 
                                This leads to deadlock because my hot coffee is waiting for hot milk which is locked by 
                                hot tea(where hot tea is waiting before releasing this lock for lock on hot water
                                that is currently locked by hot coffee ) --So Deadlock
  Case 2: If I dont wait for other ingredients to release lock , i.e. independent locks on each ingredient,
        in this case, there can e a scenario, where each beverage consumed some ingredients seperately , 
        but couldnt make the whole beverage, because it is consumed by some other beverage 
        which also is not completed due to other insufficient ingredients
        This wpuld lead to waste of ingredients without getting any complete beverage.
        We could optimize it by making atleast one beverage if it can be made rather than making
        many half or incomplete beverages
  
Considering above two scenarios, it would be better to take a lock on whole inventory

Since we take lock on whole inventory, does it mean we dont get faster and optimized benifits of running threads?
    -- Even though one thread runs at a time for inventory(as it takes lock).
     But the remaining work(like mixing and other process after getting all ingredients) can be done parallely,
     thus giving the benefits of threads

2.) Why use LOW(minimum indicator) value common for all ingredients?
-- We could have taken different LOW(minimum indicator) values for each ingredient 
    if the ingredient list has been fixed before, but in our case ingredients are variable 
    and comes as input in the json file






