from Product import Product


class Apple(Product):
    """ A class representing an apple.

    Private instance variables:
        - _cost: the cost of the apple ($)
        - _id: the product's unique identifier
        - _recycle_url: a url to a webpage containing the apple's recycle type.
        - _bin: the bin that a coffee cup should be thrown into
    """
    _cost: float
    _id: int
    _recycle_url: str
    _bin: str

    def __init__(self, cost: float, id: int) -> None:
        super().__init__(cost, id, "https://anudevgill.github.io/index.html", "compost")
