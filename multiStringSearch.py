'''
3 solutions
1st Solution - O(bns) time | O(n) space
'''

# 1st solutions


def multiStringSearch1(bigString, smallStrings):
    return [isSmallStringInBigString(bigString, smallString)
            for smallString in smallStrings]


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
