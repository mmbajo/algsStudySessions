import unittest
from sort import *


class TestSortingAlgorithms(unittest.TestCase):
    def test_HeapSort(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = HeapSort().sort(array)
        self.assertEqual(sorted(array), out)

    def test_QuickSort(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = QuickSort().sort(array)
        self.assertEqual(out, sorted(array))

    def test_MergeSort1(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = MergeSort1().sort(array)
        self.assertEqual(out, sorted(array))

    def test_MergeSort2(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = MergeSort2().sort(array)
        self.assertEqual(out, sorted(array))

    def test_SelectionSort(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = SelectionSort().sort(array)
        self.assertEqual(out, sorted(array))

    def test_BubbleSort(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = BubbleSort().sort(array)
        self.assertEqual(out, sorted(array))

    def test_InsertionSort(self):
        array = [0, 0, 0, 0, 0, -1, -36, 45, 34, 243, 0, 0, 0]
        out = InsertionSort().sort(array)
        self.assertEqual(out, sorted(array))


if __name__ == '__main__':
    unittest.main()
