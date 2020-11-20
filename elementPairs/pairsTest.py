import unittest

from elementPairs.pairs import cons, car, cdr


class MyTestCase(unittest.TestCase):
    def test_car(self):
        self.assertEqual(car(cons(3, 4)), "3")

    def test_cdr(self):
        self.assertEqual(cdr(cons(3, 4)), "4")


if __name__ == '__main__':
    unittest.main(exit=False)
