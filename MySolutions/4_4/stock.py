from decimal import Decimal
from typing import List
import csv

class Stock:
    __slots__ = ['name', '_shares', '_price']
    _types = (str, int, float)

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self._shares = shares
        self._price = price

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))
    
    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, v):
        if not isinstance(v, self._types[1]):
            raise TypeError(f'shares must be an {str(self._types[1])}')
        if v < 0:
            raise TypeError('shares must be positive')

        self._shares = v

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, v):
        if not isinstance(v, self._types[2]):
            raise TypeError(f'shares must be an {str(self._types[2])}')
        if v < 0:
            raise TypeError('price must be a positive')
        self._price = v
            

    @classmethod
    def from_row(cls, row):
        return cls(*[fn(val) for fn, val in zip(cls._types, row)])

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, n: int):
        self.shares -= n


class DStock(Stock):
    _types = (str, int, Decimal)


def print_portfolio(path):
    p = read_portfolio(path)
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('-'*10 + ' ' + '-'*10 + ' ' + '-'*10)
    for s in p:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))



