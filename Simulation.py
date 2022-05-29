from Customer import Customer
from CoffeeCup import CoffeeCup
from Apple import Apple
from Soda import Soda
from Newspaper import Newspaper
from PlasticBottle import Bottle
from classifier import predict

# cashback amount for this simulation
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
        bottle2 = Bottle(4.00, 502)

        self.ids.extend([101, 502])

        print("user1's current balance (before transaction): $" + str('{:.2f}'.format(user1.get_balance())))

        user1.remove_funds(coffee1.get_cost())  # user1 buys coffee1
        product_id = coffee1.redeem('coffee1')

        print("user1 purchased a $" + str('{:.2f}'.format(coffee1.get_cost())) + " coffee.")

        if product_id in self.ids:
            self.ids.remove(product_id)

            if coffee1.get_bin() == predict('sim_images/garbage.jpg'):
                user1.add_funds(CASHBACK)
                print("user1 correctly disposed of the coffee cup. $" + str('{:.2f}'.format(CASHBACK)) + " cashback rewarded.")

        print("user1's current balance (after disposal): $" + str('{:.2f}'.format(user1.get_balance())))

        print("user2's current balance (before transaction): $" + str('{:.2f}'.format(user2.get_balance())))

        user2.remove_funds(bottle2.get_cost())
        product_id = bottle2.redeem('bottle2')

        print("user2 purchased a $" + str('{:.2f}'.format(bottle2.get_cost())) + " water bottle.")

        if product_id in self.ids:
            self.ids.remove(product_id)

            if bottle2.get_bin() == predict('sim_images/garbage.jpg'):
                user2.add_funds(CASHBACK)
            else:
                print("user2 did not correctly dispose of the coffee cup. No cashback rewarded.")

        print("user2's current balance (after disposal): $" + str('{:.2f}'.format(user2.get_balance())))


if __name__ == '__main__':
    s = Simulation()
    s.run()