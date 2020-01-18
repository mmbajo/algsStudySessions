import heaps
import unittest

test1 = heaps.MinHeap([2, 3, 1, 45, 31, 3, 2])


class TestHeap(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(test1.heap[0] == min(test1.heap), True)


if __name__ == '__main__':
    unittest.main()
