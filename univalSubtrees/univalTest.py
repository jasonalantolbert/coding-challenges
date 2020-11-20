import unittest

from univalSubtrees.univals import Node, count_univals


class MyTestCase(unittest.TestCase):
    def test_unival_count(self):
        tree = Node("0", left=Node("1"),
                    right=Node("0", left=Node("1", left=Node("1"), right=Node("1")), right=Node("0")))
        expected = 5
        actual = count_univals(tree)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
