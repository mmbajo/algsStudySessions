import unittest
import sameBsts as sb


class TestMe(unittest.TestCase):
    def test_case1(self):
        arrayOne = [2, 3, 4, 5, 6, 7, 8]
        arrayTwo = [2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(sb.sameBsts(arrayOne, arrayTwo), True)


if __name__ == '__main__':
    unittest.main()
