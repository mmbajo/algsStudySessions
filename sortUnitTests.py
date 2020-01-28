import unittest
from sort import HeapSort, QuickSort, MergeSort


class TestSortingAlgorithms(unittest.TestCase):
    def test_HeapSort(self):
        array = [12, 3, 4, 5, 2, 1, 4, 5]
        out = HeapSort().sort(array)
        self.assertEqual(sorted(array), out)

    def test_QuickSort(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = QuickSort().sort(array)
        self.assertEqual(out, sorted(array))

    def test_MergeSort(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = MergeSort().sort(array)
        self.assertEqual(out, sorted(array))


if __name__ == '__main__':
    unittest.main()
