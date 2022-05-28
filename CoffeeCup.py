from Product import Product


class CoffeeCup(Product):
    """ A class representing a coffee cup.

    Private instance variables:
        - _cost: the cost of the coffee cup ($)
        - _id: the product's unique identifier
        - _recycle_type: a url to a webpage containing the product's recycle type.
    """
    _cost: float
    _id: int
    _recycle_type: str

    def __init__(self, cost: float, id: int) -> None:
        super().__init__(cost, id, "http://localhost:63343/Website/Garbage.html?_ijt=kkv7qhumt2npulqpoutloig3el&_ij_reload=RELOAD_ON_SAVE")
