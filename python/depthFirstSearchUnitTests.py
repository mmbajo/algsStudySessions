import depthFirstSearch as dfs
import unittest


class TestDFS(unittest.TestCase):
    def test_case1(self):
        answer = ['A', 'B', 'D', 'C']
        tree = dfs.Node('A')
        tree.addChild('B').addChild('C')
        tree.children[0].addChild('D')
        output = tree.depthFirstSearch([])
        self.assertEqual(answer, output)


if __name__ == '__main__':
    unittest.main()
