import unittest
import LargestRange as lr


class TestLargestRange(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(lr.largestRange([1]), [1, 1])


if __name__ == '__main__':
    unittest.main()
