from decimal import Decimal
from typing import List
import csv

class Stock:
    types = (str, int, float)
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(*[fn(val) for fn, val in zip(cls.types, row)])

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, n: int):
        self.shares -= n


class DStock(Stock):
    types = (str, int, Decimal)


def print_portfolio(path):
    p = read_portfolio(path)
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('-'*10 + ' ' + '-'*10 + ' ' + '-'*10)
    for s in p:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))



