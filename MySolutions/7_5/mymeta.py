class MyMeta(type):

    def __new__(cls, name, bases, __dict__):
        print(f'Creating class: {name}')
        print(f'Base classes: {bases}')
        print(f'Attributes: {list(__dict__)}')
        return super().__new__(cls, name, bases, __dict__)


class Stock(metaclass=MyMeta):

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


class MyStock(Stock):
    pass


if __name__ == '__main__':
    s = Stock('A', 100, 10.0)
    ms = MyStock('AAPL', 100, 20.0)

