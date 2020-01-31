from boggleBoard import Trie
import unittest


class TestImplementation(unittest.TestCase):
    def test_Trie(self):
        listOfWords = ['a', 'aab']
        expected = {'a': {'*': 'a', 'a': {'b': {'*': 'aab'}}}}
        trie = Trie()
        for word in listOfWords:
            trie.add(word)
        self.assertEqual(expected, trie.root)


if __name__ == '__main__':
    unittest.main()
