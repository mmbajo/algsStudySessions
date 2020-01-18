import multiStringSearch
import unittest


class TestSolutions(unittest.TestCase):
    def test_case1(self):
        bigString = 'I love you'
        smallStrings = ['I', 'love', 'dogs']
        answer = [True, True, False]
        output = multiStringSearch.multiStringSearch1(bigString, smallStrings)
        self.assertEqual(answer, output)

    def test_case2(self):
        bigString = 'I love you'
        smallStrings = ['I', 'love', 'dogs']
        answer = [True, True, False]
        output = multiStringSearch.multiStringSearch2(bigString, smallStrings)
        self.assertEqual(answer, output)


if __name__ == '__main__':
    unittest.main()
