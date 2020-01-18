'''
3 solutions
1st Solution - O(bns) time | O(n) space
'''


# 1st solution
def multiStringSearch1(bigString, smallStrings):
    def isSmallStringInBigString(bigString, smallString):
        for i in range(len(bigString)):
            if i + len(smallString) > len(bigString):
                break
            if isInBigString(bigString, smallString, i):
                return True
        return False

    def isInBigString(bigString, smallString, startIdx):
        bigStringLeftIdx = startIdx
        bigStringRightIdx = startIdx + len(smallString) - 1
        smallStringLeftIdx = 0
        smallStringRightIdx = len(smallString) - 1

        while bigStringLeftIdx <= bigStringRightIdx:
            if (
                bigString[bigStringLeftIdx] != smallString[smallStringLeftIdx] or
                bigString[bigStringRightIdx] != smallString[smallStringRightIdx]
            ):
                return False

            bigStringLeftIdx += 1
            bigStringRightIdx -= 1
            smallStringLeftIdx += 1
            smallStringRightIdx -= 1

        return True

    return [isSmallStringInBigString(bigString, smallString)
            for smallString in smallStrings]


# 2nd solution
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, startIdx, string):
        currNode = self.root
        for j in range(startIdx, len(string)):
            currLetter = string[j]
            if currLetter not in currNode:
                currNode[currLetter] = {}
            currNode = currNode[currLetter]

    def contains(self, string):
        currNode = self.root
        for j in range(len(string)):
            currLetter = string[j]
            if currLetter not in currNode:
                return False
            currNode = currNode[currLetter]
        return True


def multiStringSearch2(bigString, smallStrings):
    trie = SuffixTrie(bigString)
    return [trie.contains(smallString) for smallString in smallStrings]

# 3rd solution


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def insert(self, string):
        currNode = self.root
        for j in range(len(string)):
            currLetter = string[j]
            if currLetter not in currNode:
                currNode[currLetter] = {}
            currNode = currNode[currLetter]
        currNode[self.endSymbol] = string


def multiStringSearch3(bigString, smallStrings):
    trie = Trie()
    for smallString in smallStrings:
        trie.insert(smallString)
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedStrings)
    return [string in containedStrings for string in smallStrings]


def findSmallStringsIn(bigString, startIdx, trie, containedStrings):
    currNode = trie.root
    for j in range(startIdx, len(bigString)):
        currLetter = bigString[j]
        if currLetter not in currNode:
            break
        currNode = currNode[currLetter]
        if trie.endSymbol in currNode:
            containedStrings[currNode[trie.endSymbol]] = True
