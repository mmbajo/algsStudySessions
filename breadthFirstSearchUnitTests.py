import breadthFirstSearch as bfs
import unittest


class TestBFS(unittest.TestCase):
    def test_case1(self):
        answer = ['A', 'B', 'C', 'D']
        tree = bfs.Node('A')
        tree.addChild('B').addChild('C')
        tree.children[0].addChild('D')
        output = tree.breadthFirstSearch([])
        self.assertEqual(answer, output)


if __name__ == '__main__':
    unittest.main()
