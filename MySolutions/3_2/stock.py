from typing import List
import csv

class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, n: int):
        self.shares -= n


def read_portfolio(path) -> List['Stock']:
    f = open(path)
    f_csv = csv.reader(f)
    headers = next(f_csv)
    stocks = []
    for row in f_csv:
        stocks.append(Stock(row[0], int(row[1]), float(row[2])))

    return stocks


def print_portfolio(path):
    p = read_portfolio(path)
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('-'*10 + ' ' + '-'*10 + ' ' + '-'*10)
    for s in p:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

