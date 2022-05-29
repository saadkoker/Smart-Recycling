from Product import Product


class Soda(Product):
    """ A class representing a soda.

    Private instance variables:
        - _cost: the cost of the soda ($)
        - _id: the product's unique identifier
        - _recycle_url: a url to a webpage containing the soda's recycle type.
        - _bin: the bin that a soda should be thrown into
    """
    _cost: float
    _id: int
    _recycle_url: str
    _bin: str

    def __init__(self, cost: float, id: int) -> None:
        super().__init__(cost, id, "https://anudevgill.github.io/Containers.html",
                         "mixed_containers")
