import unittest
from sort import HeapSort


class TestSortingAlgorithms(unittest.TestCase):
    def test_HeapSort(self):
        array = [12, 3, 4, 5, 2, 1, 4, 5]
        out = HeapSort().sort(array)
        self.assertEqual(sorted(array), out)


if __name__ == '__main__':
    unittest.main()
