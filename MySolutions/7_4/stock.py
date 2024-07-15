from structure import Structure, typed_structure
from validate import String, PositiveInteger, PositiveFloat


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

stock_dict = {
    'name': String(),
    'shares': PositiveInteger(),
    'price': PositiveFloat(),
    '__eq__': __eq__,
    'cost': cost,
    'sell': sell,
}

Stock = typed_structure('Stock', **stock_dict)

