from typing import List, Dict

'''
The Algorithm takes O(nm*8^s + ws) time and O(nm + ws) space
'''


class BoggleBoardSolution:
    def boggleBoard(self,
                    boggle: List[List[str]],
                    words: List[str]) -> List[str]:
        # Add words on a Trie
        trie = Trie()
        for word in words:
            trie.add(word)
        # Initialize visited 2D Boolean array
        visited = [[False for letter in row] for row in boggle]
        # Initialize Cache for found Words
        inBoggleBoard = {}
        # Explore every BoggleBoard element
        for i in range(len(boggle)):
            for j in range(len(boggle[i])):
                self.explore(i, j, boggle, trie.root, visited, inBoggleBoard)
        return list(inBoggleBoard.keys())

    def explore(self, i: int, j: int,
                boggle: List[List[str]],
                trieNode: Dict,
                visited: List[List[bool]],
                inBoggleBoard: Dict):
        if visited[i][j]:
            return
        currLetter = boggle[i][j]
        if currLetter not in trieNode:
            return
        visited[i][j] = True
        trieNode = trieNode[currLetter]
        if '*' in trieNode:
            inBoggleBoard[trieNode['*']] = True
        neighbors = self.getNeighbors(i, j, boggle)
        for neighbor in neighbors:
            self.explore(neighbor[0], neighbor[1],
                         boggle, trieNode, visited, inBoggleBoard)
        visited[i][j] = False

    def getNeighbors(self, i: int, j: int, boggle: List[List[str]]) -> List[List[int]]:
        maxColIdx = len(boggle[0]) - 1
        maxRowIdx = len(boggle) - 1
        neighbors = []
        if i < maxRowIdx and j < maxColIdx:
            neighbors.append([i + 1, j + 1])
        if i < maxRowIdx and j > 0:
            neighbors.append([i + 1, j - 1])
        if i > 0 and j < maxColIdx:
            neighbors.append([i - 1, j + 1])
        if i > 0 and j > 0:
            neighbors.append([i - 1, j - 1])
        if i > 0:
            neighbors.append([i - 1, j])
        if j > 0:
            neighbors.append([i, j - 1])
        if i < maxRowIdx:
            neighbors.append([i + 1, j])
        if j < maxColIdx:
            neighbors.append([i, j + 1])
        return neighbors


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
