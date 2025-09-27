class PMeter:
    def __init__(self, mins_buy: int):
        self.mins_buy = mins_buy

    @property
    #Minutes Purchased getter.
    def mins_buy(self) -> int:
        return self._mins_buy

    #Minutes Purchased setter.
    @mins_buy.setter
    def mins_buy(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Minutes bought must be a positive number.")
        self._mins_buy = value




