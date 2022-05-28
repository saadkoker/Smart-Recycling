import pyqrcode


class Product:
    """A class representing a product.

    Private instance variables:
        - _cost: the cost of the product ($)
        - _id: the product's unique identifier
        - _recycle_url: a url to a webpage containing the product's recycle type.
        - _bin: the bin that this product should be thrown in

    Preconditions:
        - self._bin in {'recycling', 'compost', 'mixed_paper', 'garbage', 'mixed_containers'}
    """
    _cost: float
    _id: int
    _recycle_url: str
    _bin: str

    def __init__(self, cost: float, id: int, url: str, bin: str) -> None:
        self._cost = cost
        self._id = id
        self._recycle_url = url
        self._bin = bin

    def get_cost(self) -> float:
        """Return the cost of the product.
        """
        return self._cost

    def get_id(self) -> int:
        """Return the id of the product.
        """
        return self._id

    def get_recycle_type(self) -> str:
        """Return the recycle_type of the product.
        """
        return self._recycle_url

    def get_bin(self) -> str:
        return self._bin

    def redeem(self) -> int:
        """Redeem the product's qr code and return the product id.
        """
        url = pyqrcode.create(self._recycle_url)
        url.png('code.png', scale=4)

        return self._id
