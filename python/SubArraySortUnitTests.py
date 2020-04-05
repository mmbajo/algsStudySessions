import SubArraySort as ss
import unittest


class TestSubArraySort(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(ss.subarraySort([1, 2]), [-1, -1])


if __name__ == '__main__':
    unittest.main()
