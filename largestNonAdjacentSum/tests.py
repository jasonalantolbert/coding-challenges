import unittest

from largestNonAdjacentSum.nonadjsum import non_adj_sum


class MyTestCase(unittest.TestCase):
    def test_1(self):
        ints = [2, 4, 6, 2, 5]
        expected = 13
        actual = non_adj_sum(ints)
        self.assertEqual(expected, actual)

    def test_2(self):
        ints = [5, 1, 1, 5]
        expected = 10
        actual = non_adj_sum(ints)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
