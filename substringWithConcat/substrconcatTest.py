import unittest

from substringWithConcat.substrconcat import find_substring


class MyTestCase(unittest.TestCase):
    def test_substrconcat(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        actual = find_substring(s, words)
        expected = [6, 9, 12]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
