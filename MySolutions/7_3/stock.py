from structure import Structure
from validate import String, PositiveInteger, PositiveFloat


class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def __eq__(self, other_stock):
        return (
                self.name == other_stock.name and 
                self.shares == other_stock.shares and 
                self.price == other_stock.price
        )

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, n: PositiveInteger):
        self.shares -= n

