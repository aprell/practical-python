# Exercise 8.1
# Exercise 9.1

from .stock import Stock
import unittest

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertAlmostEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock("GOOG", 100, 490.1)
        self.assertEqual(s.cost, 49010)

    def test_sell(self):
        s = Stock("GOOG", 100, 490.1)
        s.sell(50)
        self.assertEqual(s.shares, 50)
        s.sell(30)
        self.assertEqual(s.shares, 20)
        s.sell(30)
        self.assertEqual(s.shares, 0)

    def test_shares(self):
        s = Stock("GOOG", 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = "100"

if __name__ == "__main__":
    unittest.main()
