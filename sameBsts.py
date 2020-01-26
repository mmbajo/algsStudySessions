from typing import List

# A variation of problem https://leetcode.com/problems/same-tree/


class Solution1:
    '''
    O(n^2) time | O(n^2) space
    Where n is equal to the length of array
    '''

    def sameBsts(self, arrayOne: List[float], arrayTwo: List[float]) -> bool:
        if len(arrayOne) == 0 and len(arrayTwo) == 0:
            return True

        if len(arrayOne) != len(arrayTwo):
            return False

        if arrayOne[0] != arrayTwo[0]:
            return False

        leftBstOne = self.getLeftBst(arrayOne)
        rightBstOne = self.getRightBst(arrayOne)
        leftBstTwo = self.getLeftBst(arrayTwo)
        rightBstTwo = self.getRightBst(arrayTwo)

        return (self.sameBsts(leftBstOne, leftBstTwo) and
                self.sameBsts(rightBstOne, rightBstTwo))

    def getLeftBst(self, array: List[float]):
        cache = []
        for i in range(1, len(array)):
            if array[i] < array[0]:
                cache.append(array[i])
        return cache

    def getRightBst(self, array: List[float]):
        cache = []
        for i in range(1, len(array)):
            if array[0] <= array[i]:
                cache.append(array[i])
        return cache


class Solution2:
    '''
    O(n^2) time | O(d^2) space
    where n is the length of array and d is depth of tree
    '''

    def sameBsts(self, arrayOne: List[float], arrayTwo: List[float]) -> bool:
        return self.areSameBsts(arrayOne,
                                arrayTwo,
                                0,
                                0,
                                float("-inf"),
                                float("inf"))

    def areSameBsts(self, arrayOne: List[float], arrayTwo: List[float],
                    rootIdxOne: int, rootIdxTwo: int,
                    minVal: float, maxVal: float) -> bool:
        if rootIdxOne == -1 or rootIdxTwo == -1:
            return rootIdxOne == rootIdxTwo

        if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
            return False

        leftRootIdxOne = self.getSmallerIdx(arrayOne, rootIdxOne, minVal)
        rightRootIdxOne = self.getBiggerOrEqualIdx(arrayOne, rootIdxOne, maxVal)
        leftRootIdxTwo = self.getSmallerIdx(arrayTwo, rootIdxTwo, minVal)
        rightRootIdxTwo = self.getBiggerOrEqualIdx(arrayTwo, rootIdxTwo, maxVal)

        # Recursion
        currentVal = arrayOne[rootIdxOne]
        isLeftBst = self.areSameBsts(arrayOne, arrayTwo,
                                     leftRootIdxOne, leftRootIdxTwo,
                                     minVal, currentVal)
        isRightBst = self.areSameBsts(arrayOne, arrayTwo,
                                      rightRootIdxOne, rightRootIdxTwo,
                                      currentVal, maxVal)
        return isLeftBst and isRightBst

    def getSmallerIdx(self, array: List[float], startIdx: int,
                      minVal: float) -> int:
        for i in range(startIdx + 1, len(array)):
            if minVal <= array[i] < array[startIdx]:
                return i
        return -1

    def getBiggerOrEqualIdx(self, array: List[float], startIdx: int,
                            maxVal: float) -> int:
        for i in range(startIdx + 1, len(array)):
            if array[startIdx] <= array[i] < maxVal:
                return i
        return -1
