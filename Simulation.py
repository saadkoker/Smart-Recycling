from Customer import Customer
from CoffeeCup import CoffeeCup
from Apple import Apple
from Soda import Soda
from Newspaper import Newspaper
from PlasticBottle import Bottle

CASHBACK = 0.05


class Simulation:
    """A class representing a simulation of the program in action.

    Instance variables:
        - ids: a list of all the product ids
    """
    ids: list

    def __init__(self) -> None:
        self.ids = []

    def run(self) -> None:
        # Initialize users
        user1 = Customer(10.00)
        user2 = Customer(15.00)

        # Initialize products
        coffee1 = CoffeeCup(5.00, 101)
        coffee2 = CoffeeCup(5.00, 102)
        coffee3 = CoffeeCup(3.00, 103)




