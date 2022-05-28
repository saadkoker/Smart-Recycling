class Customer:
    """A class representing a customer.

    Private instance variables:
        - _wallet: the amount of money ($) in this customer's wallet
    """
    _wallet: float

    def __init__(self, initialMoney: float) -> None:
        self._wallet = initialMoney

    def get_balance(self) -> float:
        """Return this customer's current wallet balance.
        """
        return self._wallet

    def add_funds(self, money: float) -> None:
        """Add money to this customer's wallet.
        """
        self._wallet += money

    def remove_funds(self, money: float) -> None:
        """Remove money from this customer's wallet.
        """
        self._wallet -= money
