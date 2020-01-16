import zigzagTraverse as zz
import unittest


class TestZigzagTraverse(unittest.TestCase):
    def test_case1(self):
        array = [[1, 3], [2, 4]]
        out = [1, 2, 3, 4]
        self.assertEqual(zz.zigzagTraverse(array), out)


if __name__ == '__main__':
    unittest.main()
