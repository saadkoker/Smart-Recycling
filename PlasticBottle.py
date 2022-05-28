from Product import Product


class Bottle(Product):
    """ A class representing a plastic water bottle.

    Private instance variables:
        - _cost: the cost of the bottle ($)
        - _id: the product's unique identifier
        - _recycle_url: a url to a webpage containing the botle's recycle type.
        - _bin: the bin that a coffee cup should be thrown into
    """
    _cost: float
    _id: int
    _recycle_url: str
    _bin: str

    def __init__(self, cost: float, id: int) -> None:
        super().__init__(cost, id, "http://localhost:63343/Website/Recycling.html?_ijt=e55rpeo04o8p61ghj14v8dquen&_ij_reload=RELOAD_ON_SAVE",
                         "recycling")
