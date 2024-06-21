from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n


class Date(Structure):
    _fields = ('year', 'month', 'day')

