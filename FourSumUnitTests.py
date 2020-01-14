from FourSum import fourSum
import unittest


def sortAndStringify(array):
    return ','.join(sorted(list(map(lambda x: str(x), array))))


class TestFourSum(unittest.TestCase):
    def test_case1(self):
        output = fourSum([1, 2, 3, 4, 5, 6, 7], 10)
        output = list(map(sortAndStringify, output))
        quads = [[1, 2, 3, 4]]
        self.assertTrue(len(output) == 1)
        for quad in quads:
            self.assertTrue(sortAndStringify(quad) in output)
