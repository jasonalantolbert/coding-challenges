import unittest

from substringWithConcat.substrconcat import find_substring


class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]

        expected = {0, 9}
        actual = set(find_substring(s, words))
        self.assertEqual(expected, actual)

    def test2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]

        expected = set()
        actual = set(find_substring(s, words))
        self.assertEqual(expected, actual)

    def test3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]

        expected = {6, 9, 12}
        actual = set(find_substring(s, words))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
