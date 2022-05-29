from Customer import Customer
from CoffeeCup import CoffeeCup
from Apple import Apple
from Soda import Soda
from Newspaper import Newspaper
from PlasticBottle import Bottle
from classifier import predict

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

        apple1 = Apple(2.00, 201)

        soda1 = Soda(3.00, 301)

        newspaper1 = Newspaper(1.00, 401)

        bottle1 = Bottle(2.00, 501)
        bottle2 = Bottle(4.00, 502)

        self.ids.extend([101, 102, 103, 201, 301, 401, 501, 502])

        user1.remove_funds(coffee1.get_cost())  # user1 buys coffee1
        product_id = coffee1.redeem('coffee1')

        if product_id in self.ids:
            self.ids.remove(product_id)

            if coffee1.get_bin() == predict('sim_images/garbage_bin.jpg'):
                user1.add_funds(CASHBACK)

        print(user1.get_balance())
