import unittest

from autocompleteSystem.autocomplete import autocomplete


class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "de"
        queries = ["dog", "deer", "deal"]

        expected = {"deer", "deal"}
        actual = set(autocomplete(s, queries))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
