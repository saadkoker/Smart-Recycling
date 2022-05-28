import pyqrcode


class Product:
    """A class representing a product.

    Private instance variables:
        - _cost: the cost of the product ($)
        - _id: the product's unique identifier
        - _recycle_type: a url to a webpage containing the product's recycle type.
    """
    _cost: float
    _id: int
    _recycle_type: str

    def __init__(self, cost: float, id: int, url: str) -> None:
        self._cost = cost
        self._id = id
        self._recycle_type = url

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
        return self._recycle_type

    def redeem(self, recycle_type) -> int:
        """Redeem the product's qr code and return the product id.
        """
        url = pyqrcode.create(recycle_type)
        url.png('code.png', scale=4)

        return self._id
