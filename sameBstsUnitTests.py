import unittest
from sameBsts import Solution1, Solution2


class TestMe(unittest.TestCase):
    def test_case1(self):
        arrayOne = [2, 3, 4, 5, 6, 7, 8]
        arrayTwo = [2, 3, 4, 5, 6, 7, 8]
        sb = Solution1()
        self.assertEqual(sb.sameBsts(arrayOne, arrayTwo), True)

    def test_case2(self):
        arrayOne = [2, 3, 4, 5, 6, 7, 8]
        arrayTwo = [2, 3, 4, 5, 6, 7, 8]
        sb = Solution2()
        self.assertEqual(sb.sameBsts(arrayOne, arrayTwo), True)


if __name__ == '__main__':
    unittest.main()
