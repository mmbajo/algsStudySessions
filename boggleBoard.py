from typing import List


class BoggleBoardSolution:
    pass


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def add(self, word: str):
        currNode = self.root
        for letter in word:
            if letter not in currNode:
                currNode[letter] = {}
            currNode = currNode[letter]
        currNode[self.endSymbol] = word
