import unittest
from stock import Stock

class TestStock(unittest.TestCase):

    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_with_kwargs(self):
        s = Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock('GOOG', 100, 2.0)
        self.assertEqual(s.cost, 200.0)

    def test_sell(self):
        s = Stock('GOOG', 100, 2.0)
        s.sell(50)
        self.assertEqual(s.shares, 50)
        self.assertEqual(s.cost, 100.0)

    def test_from_row(self):
        row = ['GOOG', 100, 490.1]
        s = Stock.from_row(row)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.__repr__(), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        s1 = Stock('A', 100, 1.0)
        s2 = Stock('A', 100, 1.0)
        self.assertTrue(s1 == s2)

    def test_shares_string_error(self):
        s = Stock('A', 100, 1.0)
        with self.assertRaises(TypeError):
            s.shares = '100'

    def test_shares_negative_error(self):
        s = Stock('A', 100, 1.0)
        with self.assertRaises(ValueError):
            s.shares = -100

    def test_price_string_error(self):
        s = Stock('A', 100, 1.0)
        with self.assertRaises(TypeError):
            s.price = '1.0'

    def test_price_negative_error(self):
        s = Stock('A', 100, 1.0)
        with self.assertRaises(ValueError):
            s.price = -1.0

    def test_invalid_attribute_error(self):
        s = Stock('A', 100, 1.0)
        with self.assertRaises(AttributeError):
            s.share = 1


if __name__ == '__main__':
    unittest.main()

