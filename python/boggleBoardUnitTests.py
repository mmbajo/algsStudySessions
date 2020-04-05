from boggleBoard import Trie, BoggleBoardSolution
import unittest


class TestImplementation(unittest.TestCase):
    def test_Trie(self):
        listOfWords = ['a', 'aab']
        expected = {'a': {'*': 'a', 'a': {'b': {'*': 'aab'}}}}
        trie = Trie()
        for word in listOfWords:
            trie.add(word)
        self.assertEqual(expected, trie.root)

    def test_boggleBoardSolution(self):
        boggleRowWords = ['thisisa', 'simplex', 'bxxxxeb', 'xogglxo',
                          'xxxDTra', 'REPEAdx', 'xxxxxxx', 'NOTRE-P',
                          'xxDETAE']
        words = ['this', 'is', 'not', 'a', 'simple', 'boggle',
                 'board', 'test', 'REPEATED', 'NOTRE-PEATED']
        expected = ['this', 'is', 'a', 'simple', 'boggle', 'board',
                    'NOTRE-PEATED']
        boggle = [list(wordRow) for wordRow in boggleRowWords]
        solution = BoggleBoardSolution()
        out = solution.boggleBoard(boggle, words)
        self.assertEqual(len(out), len(expected))
        for word in out:
            self.assertTrue(word in expected)


if __name__ == '__main__':
    unittest.main()
